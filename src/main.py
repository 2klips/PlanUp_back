from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import controllers.scraper as scraper  # scraper 모듈 임포트

app = FastAPI()

# CORS 설정 추가
origins = [
    "http://localhost:3000",  # 프론트엔드 주소
    "http://127.0.0.1:3000",  # 프론트엔드 주소
    "http://10.0.2.2:3000",  # Android 에뮬레이터용
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

@app.post("/scrape")
async def scrape_job_details(request: URLRequest):
    url = request.url
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
        return job_details
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
