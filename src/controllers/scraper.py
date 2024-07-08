import json
import requests
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def save_image(image_url, file_name):
    try:
        img_data = requests.get(image_url).content
        with open(file_name, 'wb') as handler:
            handler.write(img_data)
        return f"Image saved as {file_name}"
    except Exception as e:
        return f"Failed to save image from {image_url}: {e}"

def get_saramin_job_details(url):
    driver = initialize_driver()
    driver.get(url)
    wait = WebDriverWait(driver, 30)
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
        closing_date = driver.find_element(By.XPATH, "//dt[text()='마감일']/following-sibling::dd").text.strip()
        job_details['마감일'] = closing_date
    except:
        job_details['마감일'] = ""

    try:
        start_date = driver.find_element(By.XPATH, "//dt[text()='시작일']/following-sibling::dd").text.strip()
        job_details['접수시작일'] = start_date
    except:
        job_details['접수시작일'] = ""

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
        employee_count = driver.find_element(By.XPATH, "//dt[normalize-space(text())='사원수']/following-sibling::dd").text.strip()
        job_details['사원수'] = employee_count
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
        image_save_message = save_image(logo_image_url, 'saramin_company_logo.png')
        job_details['로고저장결과'] = image_save_message
    except:
        job_details['로고이미지'] = ""

    driver.quit()
    return job_details

def get_worknet_job_details(url):
    driver = initialize_driver()
    driver.get(url)
    wait = WebDriverWait(driver, 30)
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
        image_save_message = save_image(logo_image_url, 'worknet_company_logo.png')
        job_details['로고저장결과'] = image_save_message
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
    return job_details

def get_worknet_job_details_v2(url):
    driver = initialize_driver()
    driver.get(url)
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'careers-area')))
    job_details = {"URL": url}

    try:
        time.sleep(5)  # Extra waiting time
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # careers-area crawling
        careers_area = soup.find('div', class_='careers-area')
        if careers_area:
            try:
                company_name_elem = careers_area.find('p', class_='tit_corp')
                job_details['회사이름'] = company_name_elem.get_text(strip=True) if company_name_elem else 'N/A'
            except:
                job_details['회사이름'] = 'N/A'

            try:
                recruitment_title_elem = careers_area.find('p', class_='tit')
                job_details['채용제목'] = recruitment_title_elem.get_text(strip=True) if recruitment_title_elem else 'N/A'
            except:
                job_details['채용제목'] = 'N/A'

            try:
                application_period_elem = careers_area.find('p', class_='txt')
                application_period_text = application_period_elem.get_text(separator=' ', strip=True) if application_period_elem else 'N/A'
                job_details['접수기간'] = " ".join(application_period_text.split())
            except:
                job_details['접수기간'] = 'N/A'

            try:
                d_day_elem = careers_area.find('span', class_='b-circle sky')
                job_details['D-Day'] = d_day_elem.get_text(strip=True) if d_day_elem else 'N/A'
            except:
                job_details['D-Day'] = 'N/A'
        else:
            job_details['회사이름'] = 'N/A'
            job_details['채용제목'] = 'N/A'
            job_details['접수기간'] = 'N/A'
            job_details['D-Day'] = 'N/A'

        # corp-info crawling
        corp_info = soup.find('div', class_='corp-info')
        if corp_info:
            table_rows = corp_info.find_all('tr')
            for row in table_rows:
                elements = row.find_all(['th', 'td'])
                for i in range(0, len(elements), 2):
                    key = elements[i].get_text(strip=True)
                    value = elements[i+1].get_text(strip=True) if len(elements) > i+1 else 'N/A'
                    if key == '회사명':
                        job_details['회사이름'] = value
                    elif key == '업종':
                        job_details['업종'] = value
                    elif key == '홈페이지':
                        job_details['홈페이지'] = elements[i+1].find('a').get('href', 'N/A')
                    elif key == '회사주소':
                        job_details['회사주소'] = value
        else:
            job_details['회사이름'] = 'N/A'
            job_details['업종'] = 'N/A'
            job_details['홈페이지'] = 'N/A'
            job_details['회사주소'] = 'N/A'

        # Company logo crawling
        logo_div = soup.find('div', class_='logo')
        if logo_div:
            logo_img = logo_div.find('img')
            if logo_img:
                logo_url = urljoin(url, logo_img['src'])
                job_details['회사로고'] = logo_url
                save_image(logo_url, 'company_logo.png')
            else:
                job_details['회사로고'] = 'N/A'
        else:
            job_details['회사로고'] = 'N/A'

        # careers-dtl crawling
        careers_dtl = soup.find('div', class_='careers-dtl')
        if careers_dtl:
            try:
                recruitment_section_elem = careers_dtl.find('h3', class_='cir-tit')
                job_details['모집부문및자격요건'] = recruitment_section_elem.get_text(strip=True) if recruitment_section_elem else 'N/A'
                
                employment_type_elem = careers_dtl.find('h4', class_='sub-tit', text='고용형태')
                if employment_type_elem:
                    employment_type_texts = []
                    sibling = employment_type_elem.find_next_sibling()
                    while sibling and sibling.name == 'div' and 'pre-wrp' in sibling.get('class', []):
                        employment_type_texts.append(sibling.get_text(strip=True))
                        sibling = sibling.find_next_sibling()
                    job_details['고용형태'] = " ".join(employment_type_texts) if employment_type_texts else 'N/A'
                else:
                    job_details['고용형태'] = 'N/A'

                common_section_elem = careers_dtl.find('h4', class_='sub-tit', text='공통사항')
                if common_section_elem:
                    common_section_pre = common_section_elem.find_next('pre', class_='pre-wrp')
                    job_details['공통사항'] = common_section_pre.get_text(strip=True) if common_section_pre else 'N/A'
                else:
                    job_details['공통사항'] = 'N/A'
            except Exception as e:
                job_details['error'] = str(e)
                if '모집부문및자격요건' not in job_details:
                    job_details['모집부문및자격요건'] = 'N/A'
                if '고용형태' not in job_details:
                    job_details['고용형태'] = 'N/A'
                if '공통사항' not in job_details:
                    job_details['공통사항'] = 'N/A'
        else:
            job_details['모집부문및자격요건'] = 'N/A'
            job_details['고용형태'] = 'N/A'
            job_details['공통사항'] = 'N/A'

    finally:    
        driver.quit()

    return job_details

def get_wanted_job_details(url):
    driver = initialize_driver()
    driver.get(url)
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'JobHeader_JobHeader__Tools__80TiC')))
    job_details = {"URL": url}

    try:
        job_header = driver.find_element(By.CLASS_NAME, 'JobHeader_JobHeader__Tools__80TiC')
        company_elem = job_header.find_element(By.CLASS_NAME, 'JobHeader_JobHeader__Tools__Company__Link__zAvYv')
        job_details['회사이름'] = company_elem.get_attribute('data-company-name') if company_elem else 'N/A'

        info_spans = job_header.find_elements(By.CLASS_NAME, 'Typography_Typography__root__RdAI1.Typography_Typography__label1__hNiv5.Typography_Typography__weightMedium__GXnOM.JobHeader_JobHeader__Tools__Company__Info__yT4OD')
        job_details['지역'] = info_spans[0].text.strip() if len(info_spans) >= 1 else 'N/A'
        job_details['경력'] = info_spans[1].text.strip() if len(info_spans) >= 2 else 'N/A'
    except:
        job_details['회사이름'] = 'N/A'
        job_details['지역'] = 'N/A'
        job_details['경력'] = 'N/A'

    try:
        position_title_elem = driver.find_element(By.CLASS_NAME, 'JobHeader_JobHeader__InX6I').find_element(By.CLASS_NAME, 'Typography_Typography__root__RdAI1.Typography_Typography__title3__J1fCl.Typography_Typography__title3__weightBold__xwZk7.Typography_Typography__weightBold__KkJEY.JobHeader_JobHeader__PositionName__kfauc')
        job_details['직무'] = position_title_elem.text.strip() if position_title_elem else 'N/A'
    except:
        job_details['직무'] = 'N/A'

    try:
        description_article = driver.find_element(By.CLASS_NAME, 'JobDescription_JobDescription__dq8G5')
        description_div = description_article.find_element(By.CLASS_NAME, 'JobDescription_JobDescription__paragraph__wrapper__G4CNd')
        main_position = description_div.text.split('자격요건')[-1].strip().split('\n')
        main_position = [item for item in main_position if item and item != '상세 정보 더 보기']
        job_details['자격요건'] = main_position if '[제출서류]' not in main_position else main_position[:main_position.index('[제출서류]')]
    except:
        job_details['자격요건'] = 'N/A'

    try:
        closing_date_elem = driver.find_element(By.CLASS_NAME, 'JobDueTime_JobDueTime__3yzxa').find_element(By.CLASS_NAME, 'Typography_Typography__root__RdAI1.Typography_Typography__body1-reading__3pEGb.Typography_Typography__weightRegular__jzmck')
        job_details['마감일'] = closing_date_elem.text.strip() if closing_date_elem else 'N/A'
    except:
        job_details['마감일'] = 'N/A'

    try:
        location_elem = driver.find_element(By.CLASS_NAME, 'JobWorkPlace_JobWorkPlace__map__location____MvP').find_element(By.CLASS_NAME, 'Typography_Typography__root__RdAI1.Typography_Typography__body2__5Mmhi.Typography_Typography__weightMedium__GXnOM')
        job_details['주소'] = location_elem.text.strip() if location_elem else 'N/A'
    except:
        job_details['주소'] = 'N/A'

    try:
        logo_elem = driver.find_element(By.CLASS_NAME, 'CompanyInfo_CompanyInfo__logo__2E3od').find_element(By.TAG_NAME, 'img')
        logo_url = logo_elem.get_attribute('src') if logo_elem else 'N/A'
        job_details['로고'] = logo_url
        if logo_url != 'N/A':
            image_save_message = save_image(logo_url, 'wanted_company_logo.png')
            job_details['로고저장결과'] = image_save_message
    except:
        job_details['로고'] = 'N/A'

    driver.quit()
    return job_details

def get_jobkorea_job_details(url):
    driver = initialize_driver()
    driver.get(url)
    
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'artReadJobSum')))
    
    job_details = {"URL": url}

    def get_element_text(xpath, key):
        try:
            element = driver.find_element(By.XPATH, xpath)
            job_details[key] = element.text.strip()
        except Exception as e:
            print(f"Error getting {key}: {e}")
            job_details[key] = ""

    def get_date(date_type):
        xpath = f"//div[@class='divReadBx']//dl[@class='date']//dt[text()='{date_type}']/following-sibling::dd/span[@class='tahoma']"
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element.text.strip()
        except Exception as e:
            print(f"Error getting {date_type}: {e}")
            return ''

    try:
        company_name = driver.find_element(By.CSS_SELECTOR, 'span.coName').text.strip()
        job_details['회사명'] = company_name
    except:
        job_details['회사명'] = ""

    try:
        job_title = driver.find_element(By.CSS_SELECTOR, 'h3.hd_3').text.strip().split('\n')[-1].strip()
        job_details['제목'] = job_title
    except:
        job_details['제목'] = ""
    
    try:
        date_elements = driver.find_elements(By.CSS_SELECTOR, "dl.date dt, dl.date dd")
        for i in range(0, len(date_elements), 2):
            date_type = date_elements[i].text.strip()
            date_value = date_elements[i+1].find_element(By.CSS_SELECTOR, "span.tahoma").text.strip()
            
            if '시작일' in date_type:
                job_details['접수시작일'] = date_value
            elif '마감일' in date_type:
                job_details['접수마감일'] = date_value
    except Exception as e:
        print(f"Error in date crawling: {e}")
        job_details['접수시작일'] = ''
        job_details['접수마감일'] = ''

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
        job_details['지역'] = location.replace('\n지도', '') if '\n지도' in location else location
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
        logo_element = driver.find_element(By.CSS_SELECTOR, 'div.tbLogo img')
        logo_url = logo_element.get_attribute('src').strip()
        job_details['회사로고'] = logo_url
        image_save_message = save_image(logo_url, 'jobkorea_company_logo.png')
        job_details['로고저장결과'] = image_save_message
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
    return job_details

def get_jobplanet_job_details(url):
    driver = initialize_driver()
    driver.get(url)
    
    wait = WebDriverWait(driver, 30)
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
            image_save_message = save_image(company_logo, 'jobplanet_company_logo.png')
            job_details['로고저장결과'] = image_save_message
    except:
        job_details['회사로고'] = ""

    driver.quit()
    return job_details

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')  # 한글 출력을 위해 인코딩 설정
    url = sys.argv[1]
    if "saramin" in url:
        job_details = get_saramin_job_details(url)
    elif "work" in url:
        if "detail" in url:
            job_details = get_worknet_job_details(url)
        else:
            job_details = get_worknet_job_details_v2(url)
    elif "wanted" in url:
        job_details = get_wanted_job_details(url)
    elif "jobkorea" in url:
        job_details = get_jobkorea_job_details(url)
    elif "jobplanet" in url:
        job_details = get_jobplanet_job_details(url)
    else:
        job_details = {"error": "지원되지 않는 URL입니다."}

    print(json.dumps(job_details, ensure_ascii=False, indent=4))
