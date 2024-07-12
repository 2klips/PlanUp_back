from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging
import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import controllers.scraper as scraper  # scraper 모듈 임포트

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://10.0.2.2:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLRequest(BaseModel):
    url: str

def clear_webdriver_cache():
    cache_dirs = [
        os.path.expanduser("~/.wdm"),
        os.path.expanduser("~/.cache/selenium"),
        os.path.expanduser("~/webdriver_manager")
    ]
    for cache_dir in cache_dirs:
        if os.path.exists(cache_dir):
            for root, dirs, files in os.walk(cache_dir, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(cache_dir)

def initialize_driver():
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.headless = True
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    except json.decoder.JSONDecodeError:
        logger.error("Failed to initialize driver, clearing cache and retrying...")
        clear_webdriver_cache()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

@app.post("/scrape")
async def scrape_job_details(request: URLRequest):
    url = request.url
    logger.info(f"Received URL: {url}")
    try:
        if "saramin" in url:
            job_details = scraper.get_saramin_job_details(url)
        elif "work" in url:
            if "detail" in url:
                job_details = scraper.get_worknet_job_details(url)
            else:
                job_details = scraper.get_worknet_job_details_v2(url)
        elif "wanted" in url:
            job_details = scraper.get_wanted_job_details(url)
        elif "jobkorea" in url:
            job_details = scraper.get_jobkorea_job_details(url)
        elif "jobplanet" in url:
            job_details = scraper.get_jobplanet_job_details(url)
        else:
            job_details = {"error": "지원되지 않는 URL입니다."}
            logger.warning(f"Unsupported URL: {url}")
        return job_details
    except Exception as e:
        logger.error(f"Error scraping job details: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="서버 오류가 발생했습니다.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
