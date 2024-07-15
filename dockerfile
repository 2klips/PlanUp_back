# 베이스 이미지로 Python 3 사용
FROM python:3.10

# 작업 디렉토리 설정
WORKDIR /usr/src

# 시스템 패키지 업데이트 및 필요한 패키지 설치
RUN apt-get update && \
    apt-get install -y wget unzip curl

# 크롬 설치
RUN wget https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_114.0.5735.110-1_amd64.deb && \
    apt-get -y install ./google-chrome-stable_114.0.5735.110-1_amd64.deb

# 크롬드라이버 설치
RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip && \
    mkdir -p /usr/local/bin && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin && \
    rm /tmp/chromedriver.zip

# 필요한 Python 패키지 설치
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

# 환경 변수 설정 파일 복사
COPY .env .env

# 컨테이너 시작 명령어 설정
CMD ["python", "main.py"]
