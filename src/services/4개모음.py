import json
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import sys

def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def save_image(image_url, file_name):
    try:
        img_data = requests.get(image_url).content
        with open(file_name, 'wb') as handler:
            handler.write(img_data)
        print(f"Image saved as {file_name}")
    except Exception as e:
        print(f"Failed to save image from {image_url}: {e}")

def get_saramin_job_details(url):
    driver = initialize_driver()
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'col')))
    job_details = {"URL": url}

    try:
        company_name = driver.find_element(By.CSS_SELECTOR, 'div.jv_header a[class="company"]').text.strip()
        job_details['회사명'] = company_name
    except:
        job_details['회사명'] = ""

    try:
        job_title = driver.find_element(By.CSS_SELECTOR, 'h1[class="tit_job"]').text.strip()
        job_details['직무'] = job_title
    except:
        job_details['직무'] = ""

    try:
        experience = driver.find_element(By.XPATH, "//dt[text()='경력']/following-sibling::dd/strong").text.strip()
        job_details['경력'] = experience
    except:
        job_details['경력'] = ""

    try:
        education = driver.find_element(By.XPATH, "//dt[text()='학력']/following-sibling::dd/strong").text.strip()
        job_details['학력'] = education
    except:
        job_details['학력'] = ""

    try:
        salary = driver.find_element(By.XPATH, "//dt[text()='급여']/following-sibling::dd").text.strip()
        job_details['급여'] = salary
    except:
        job_details['급여'] = ""

    try:
        working_hours = driver.find_element(By.XPATH, "//dt[text()='출퇴근 시간']/following-sibling::dd").text.strip()
        job_details['근무시간'] = working_hours
    except:
        job_details['근무시간'] = ""

    try:
        location = driver.find_element(By.XPATH, "//dt[text()='근무지역']/following-sibling::dd").text.strip()
        job_details['근무지역'] = location
    except:
        job_details['근무지역'] = ""

    try:
        employment_type = driver.find_element(By.XPATH, "//dt[text()='근무형태']/following-sibling::dd").text.strip()
        job_details['근무형태'] = employment_type
    except:
        job_details['근무형태'] = ""

    try:
        working_days = driver.find_element(By.XPATH, "//dt[text()='근무일시']/following-sibling::dd").text.strip()
        job_details['근무일시'] = working_days
    except:
        job_details['근무일시'] = ""

    try:
        closing_date = driver.find_element(By.CSS_SELECTOR, 'span.dday').text.strip()
        job_details['마감일'] = closing_date
    except:
        job_details['마감일'] = ""

    try:
        company_info = driver.find_element(By.CSS_SELECTOR, 'h2.jv_title_heading').text.strip()
        job_details['기업정보'] = company_info
    except:
        job_details['기업정보'] = ""

    try:
        company_name_additional = driver.find_element(By.CSS_SELECTOR, 'div.basic_info a.company_name').get_attribute('title').strip()
        job_details['추가_회사명'] = company_name_additional
    except:
        job_details['추가_회사명'] = ""

    try:
        ceo_name = driver.find_element(By.XPATH, "//dt[text()='대표자명']/following-sibling::dd").get_attribute('title').strip()
        job_details['대표자명'] = ceo_name
    except:
        job_details['대표자명'] = ""

    try:
        company_type = driver.find_element(By.XPATH, "//dt[text()='기업형태']/following-sibling::dd").get_attribute('title').strip()
        job_details['기업형태'] = company_type
    except:
        job_details['기업형태'] = ""

    try:
        business_category = driver.find_element(By.XPATH, "//dt[text()='업종']/following-sibling::dd").get_attribute('title').strip()
        job_details['업종'] = business_category
    except:
        job_details['업종'] = ""

    try:
        employee_count = driver.find_element(By.XPATH, "//dt[text()='사원수']/following-sibling::dd").text.strip()
        job_details['사원수'] = employee_count.split('\n')[0].strip()
    except:
        job_details['사원수'] = ""

    try:
        establishment_date = driver.find_element(By.XPATH, "//dt[text()='설립일']/following-sibling::dd").get_attribute('title').strip()
        job_details['설립일'] = establishment_date
    except:
        job_details['설립일'] = ""

    try:
        revenue = driver.find_element(By.XPATH, "//dt[text()='매출액']/following-sibling::dd").get_attribute('title').strip()
        job_details['매출액'] = revenue
    except:
        job_details['매출액'] = ""

    try:
        website = driver.find_element(By.XPATH, "//dt[text()='홈페이지']/following-sibling::dd").get_attribute('title').strip()
        job_details['홈페이지'] = website
    except:
        job_details['홈페이지'] = ""

    try:
        company_address = driver.find_element(By.XPATH, "//dt[text()='기업주소']/following-sibling::dd").get_attribute('title').strip()
        job_details['기업주소'] = company_address
    except:
        job_details['기업주소'] = ""

    try:
        logo_image_url = driver.find_element(By.CSS_SELECTOR, 'div.logo img').get_attribute('src').strip()
        job_details['로고이미지'] = logo_image_url
        save_image(logo_image_url, 'saramin.company_logo.png')
    except:
        job_details['로고이미지'] = ""

    driver.quit()
    filename = 'saramin_job_details.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(job_details, f, ensure_ascii=False, indent=4)
    
    return job_details

def get_worknet_job_details(url):
    driver = initialize_driver()
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'left')))
    job_details = {"URL": url}

    try:
        company_name = driver.find_element(By.CSS_SELECTOR, 'div.tit-area p.tit').text.strip()
        job_details['회사명'] = company_name
    except:
        job_details['회사명'] = ""

    try:
        job_title = driver.find_element(By.CSS_SELECTOR, 'div.tit-area p.tit').text.strip()
        job_details['직무'] = job_title
    except:
        job_details['직무'] = ""

    try:
        closing_date = driver.find_element(By.CSS_SELECTOR, 'span.d-day').text.strip()
        job_details['마감일'] = closing_date
    except:
        job_details['마감일'] = ""

    try:
        experience = driver.find_element(By.XPATH, "//strong[text()='경력']/following-sibling::span").text.strip()
        job_details['경력'] = experience
    except:
        job_details['경력'] = ""

    try:
        education = driver.find_element(By.XPATH, "//strong[text()='학력']/following-sibling::span").text.strip()
        job_details['학력'] = education
    except:
        job_details['학력'] = ""

    try:
        location = driver.find_element(By.XPATH, "//strong[text()='지역']/following-sibling::span").text.strip()
        job_details['지역'] = location
    except:
        job_details['지역'] = ""

    try:
        salary = driver.find_element(By.XPATH, "//strong[text()='임금']/following-sibling::span").text.strip()
        job_details['임금'] = salary
    except:
        job_details['임금'] = ""

    try:
        employment_type = driver.find_element(By.XPATH, "//strong[text()='고용형태']/following-sibling::span").text.strip()
        job_details['고용형태'] = employment_type
    except:
        job_details['고용형태'] = ""

    try:
        working_type = driver.find_element(By.XPATH, "//strong[text()='근무형태']/following-sibling::span").text.strip()
        job_details['근무형태'] = working_type
    except:
        job_details['근무형태'] = ""

    try:
        welfare = driver.find_element(By.XPATH, "//p[@class='tit' and text()='복리후생']/following-sibling::div//li").text.strip()
        job_details['복리후생'] = welfare
    except:
        job_details['복리후생'] = ""

    try:
        logo_image_url = driver.find_element(By.CSS_SELECTOR, 'div.logo-company div.img img').get_attribute('src').strip()
        job_details['로고이미지'] = logo_image_url
        save_image(logo_image_url, 'worknet.company_logo.png')
    except:
        job_details['로고이미지'] = ""

    try:
        company_name_additional = driver.find_element(By.XPATH, "//strong[text()='기업명']/following-sibling::div").text.strip()
        job_details['추가_회사명'] = company_name_additional
    except:
        job_details['추가_회사명'] = ""

    try:
        industry_type = driver.find_element(By.XPATH, "//strong[text()='업종']/following-sibling::div").text.strip()
        job_details['업종'] = industry_type
    except:
        job_details['업종'] = ""

    try:
        company_size = driver.find_element(By.XPATH, "//strong[text()='기업규모']/following-sibling::div").text.strip()
        job_details['기업규모'] = company_size
    except:
        job_details['기업규모'] = ""

    try:
        foundation_year = driver.find_element(By.XPATH, "//strong[text()='설립년도']/following-sibling::div").text.strip()
        job_details['설립년도'] = foundation_year
    except:
        job_details['설립년도'] = ""

    try:
        annual_revenue = driver.find_element(By.XPATH, "//strong[text()='연매출액']/following-sibling::div").text.strip()
        job_details['연매출액'] = annual_revenue
    except:
        job_details['연매출액'] = ""

    try:
        website = driver.find_element(By.XPATH, "//strong[text()='홈페이지']/following-sibling::div/a").get_attribute('href').strip()
        job_details['홈페이지'] = website
    except:
        job_details['홈페이지'] = ""

    try:
        employee_count = driver.find_element(By.XPATH, "//strong[text()='근로자수']/following-sibling::div").text.strip()
        job_details['근로자수'] = employee_count
    except:
        job_details['근로자수'] = ""

    driver.quit()
    filename = 'worknet_job_details.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(job_details, f, ensure_ascii=False, indent=4)
    
    return job_details

def get_jobkorea_job_details(url):
    driver = initialize_driver()
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'artReadJobSum')))
    job_details = {"URL": url}

    try:
        company_name = driver.find_element(By.CSS_SELECTOR, 'span.coName').text.strip()
        job_details['회사명'] = company_name
    except:
        job_details['회사명'] = ""

    try:
        job_title = driver.find_element(By.CSS_SELECTOR, 'h3.hd_3').text.strip()
        job_details['직무'] = job_title
    except:
        job_details['직무'] = ""

    try:
        experience = driver.find_element(By.XPATH, "//dt[text()='경력']/following-sibling::dd").text.strip()
        job_details['경력'] = experience
    except:
        job_details['경력'] = ""

    try:
        education = driver.find_element(By.XPATH, "//dt[text()='학력']/following-sibling::dd").text.strip()
        job_details['학력'] = education
    except:
        job_details['학력'] = ""

    try:
        preferred = driver.find_element(By.XPATH, "//dt[text()='우대']/following-sibling::dd").text.strip()
        job_details['우대사항'] = preferred
    except:
        job_details['우대사항'] = ""

    try:
        employment_type = driver.find_element(By.XPATH, "//dt[text()='고용형태']/following-sibling::dd").text.strip()
        job_details['고용형태'] = employment_type
    except:
        job_details['고용형태'] = ""

    try:
        salary = driver.find_element(By.XPATH, "//dt[text()='급여']/following-sibling::dd").text.strip()
        job_details['급여'] = salary
    except:
        job_details['급여'] = ""

    try:
        location = driver.find_element(By.XPATH, "//dt[text()='지역']/following-sibling::dd").text.strip()
        if '\n지도' in location:
            location = location.replace('\n지도', '')
        job_details['지역'] = location
    except:
        job_details['지역'] = ""

    try:
        time_details = driver.find_element(By.XPATH, "//dt[text()='시간']/following-sibling::dd").text.strip()
        job_details['시간'] = time_details
    except:
        job_details['시간'] = ""

    try:
        position = driver.find_element(By.XPATH, "//dt[text()='직책']/following-sibling::dd").text.strip()
        job_details['직책'] = position
    except:
        job_details['직책'] = ""

    try:
        core_skills = driver.find_element(By.XPATH, "//dt[text()='핵심역량']/following-sibling::dd").text.strip()
        job_details['핵심역량'] = core_skills
    except:
        job_details['핵심역량'] = ""

    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.tbLogo img')))
        logo_element = driver.find_element(By.CSS_SELECTOR, 'div.tbLogo img')
        logo_url = logo_element.get_attribute('src').strip()
        job_details['회사로고'] = logo_url
        save_image(logo_url, 'company_logo.png')
    except:
        job_details['회사로고'] = ""

    try:
        industry = driver.find_element(By.XPATH, "//dt[text()='산업(업종)']/following-sibling::dd").text.strip()
        job_details['산업(업종)'] = industry
    except:
        job_details['산업(업종)'] = ""

    try:
        employee_count = driver.find_element(By.XPATH, "//dt[text()='사원수']/following-sibling::dd/span").text.strip()
        job_details['사원수'] = employee_count
    except:
        job_details['사원수'] = ""

    try:
        establishment_year = driver.find_element(By.XPATH, "//dt[text()='설립년도']/following-sibling::dd//span[1]").text.strip()
        additional_info = driver.find_element(By.XPATH, "//dt[text()='설립년도']/following-sibling::dd//span[2]").text.strip()
        job_details['설립년도'] = f"{establishment_year}년 ({additional_info}년차)"
    except:
        job_details['설립년도'] = ""

    try:
        company_type = driver.find_element(By.XPATH, "//dt[text()='기업형태']/following-sibling::dd").text.strip()
        job_details['기업형태'] = company_type
    except:
        job_details['기업형태'] = ""

    try:
        homepage_url = driver.find_element(By.XPATH, "//dt[text()='홈페이지']/following-sibling::dd/span/a").get_attribute('href').strip()
        job_details['홈페이지'] = homepage_url
    except:
        job_details['홈페이지'] = ""

    driver.quit()
    filename = 'jobkorea_job_details.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(job_details, f, ensure_ascii=False, indent=4)
    
    return job_details

def get_jobplanet_job_details(url):
    driver = initialize_driver()
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'apply_section')))
    job_details = {"URL": url}

    try:
        company_name = driver.find_element(By.CSS_SELECTOR, 'span.company_name').text.strip()
        job_details['회사명'] = company_name
    except:
        job_details['회사명'] = ""

    try:
        job_title = driver.find_element(By.CSS_SELECTOR, 'h1.ttl').text.strip()
        job_details['직무'] = job_title
    except:
        job_details['직무'] = ""

    try:
        job_location = driver.find_element(By.CSS_SELECTOR, 'span.job_location span.item').text.strip()
        job_details['근무지역'] = job_location
    except:
        job_details['근무지역'] = ""

    try:
        closing_date = driver.find_element(By.CSS_SELECTOR, 'span.recruitment-summary__end').text.strip()
        job_details['마감일'] = closing_date
    except:
        job_details['마감일'] = ""

    try:
        d_day = driver.find_element(By.CSS_SELECTOR, 'span.recruitment-summary__dday').text.strip()
        job_details['D-Day'] = d_day
    except:
        job_details['D-Day'] = ""

    try:
        job_position = driver.find_element(By.XPATH, "//dt[text()='직무']/following-sibling::dd").text.strip()
        job_details['직위'] = job_position
    except:
        job_details['직위'] = ""

    try:
        experience = driver.find_element(By.XPATH, "//dt[contains(@class, 'recruitment-summary__dt')]/span[text()='경력']/../following-sibling::dd").text.strip()
        job_details['경력'] = experience
    except:
        job_details['경력'] = ""

    try:
        employment_type = driver.find_element(By.XPATH, "//dt[text()='고용형태']/following-sibling::dd").text.strip()
        job_details['고용형태'] = employment_type
    except:
        job_details['고용형태'] = ""

    try:
        skills = driver.find_element(By.XPATH, "//dt[text()='스킬']/following-sibling::dd").text.strip()
        job_details['기술'] = skills
    except:
        job_details['기술'] = ""

    try:
        company_description = driver.find_element(By.CSS_SELECTOR, 'p.recruitment-detail__txt').text.strip().split('\n')[0]
        job_details['기업소개'] = company_description
    except:
        job_details['기업소개'] = ""

    try:
        company_location = driver.find_element(By.XPATH, "//h3[text()='회사위치']/following-sibling::p").text.strip()
        job_details['회사위치'] = company_location
    except:
        job_details['회사위치'] = ""

    try:
        company_logo = driver.find_element(By.CSS_SELECTOR, 'div.logo img').get_attribute('src')
        job_details['회사로고'] = company_logo
        
        if company_logo:
            image_save_path = os.path.join('images', f"{company_name}_logo.jpg")
            os.makedirs(os.path.dirname(image_save_path), exist_ok=True)
            save_image(driver, company_logo, image_save_path)
            job_details['회사로고파일'] = image_save_path
    except:
        job_details['회사로고'] = ""

    driver.quit()
    
    filename = 'jobplanet_job_details.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(job_details, f, ensure_ascii=False, indent=4)
    
    return job_details

def get_job_details(url):
    if "saramin" in url:
        return get_saramin_job_details(url)
    elif "work.go.kr" in url:
        return get_worknet_job_details(url)
    elif "jobkorea" in url:
        return get_jobkorea_job_details(url)
    elif "jobplanet" in url:
        return get_jobplanet_job_details(url)
    else:
        raise ValueError("지원되지 않는 URL입니다.")

def main():
    if len(sys.argv) < 2:
        print("URL을 입력하세요")
        return

    url = sys.argv[1]
    job_details = get_job_details(url)
    print(json.dumps(job_details, ensure_ascii=False, indent=4))

if __name__ == "__main__":
    main()
