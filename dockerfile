# 베이스 이미지로 Python 3 사용
FROM python:3.10

# 작업 디렉토리 설정
WORKDIR /usr/src

# 시스템 패키지 업데이트 및 필요한 패키지 설치
RUN apt-get update && \
    apt-get install -y wget unzip cur && \
    apt-get install -y chromium

# Chrome 설치
RUN wget -O /tmp/chrome-linux64.zip https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/linux64/chrome-linux64.zip && \
    unzip /tmp/chrome-linux64.zip -d /usr/local/share/ && \
    ln -s /usr/local/share/chrome-linux64/chrome /usr/local/bin/google-chrome && \
    rm /tmp/chrome-linux64.zip

# ChromeDriver 설치
RUN wget -O /tmp/chromedriver-linux64.zip https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/linux64/chromedriver-linux64.zip && \
    unzip /tmp/chromedriver-linux64.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver-linux64.zip

# 필요한 Python 패키지 설치
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

# 환경 변수 설정 파일 복사
COPY .env .env

# 컨테이너 시작 명령어 설정
CMD ["python", "main.py"]
