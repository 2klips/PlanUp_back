# 베이스 이미지로 Python 3 사용
FROM python:3.10

# 작업 디렉토리 설정
WORKDIR /usr/src

# 시스템 패키지 업데이트 및 필요한 패키지 설치
RUN apt-get update && \
    apt-get install -y wget unzip curl

# 크롬 설치
RUN wget -O /tmp/chrome-linux64.zip https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/linux64/chrome-linux64.zip && \
    mkdir -p /usr/local/chrome && \
    unzip /tmp/chrome-linux64.zip -d /usr/local/chrome && \
    ln -s /usr/local/chrome/chrome-linux64/chrome /usr/local/bin/chrome && \
    rm /tmp/chrome-linux64.zip

# 크롬드라이버 설치
RUN wget -O /tmp/chromedriver-linux64.zip https://storage.googleapis.com/chrome-for-testing-public/126.0.6478.126/linux64/chromedriver-linux64.zip && \
    mkdir -p /usr/local/bin && \
    unzip /tmp/chromedriver-linux64.zip -d /usr/local/bin && \
    mv /usr/local/bin/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
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
