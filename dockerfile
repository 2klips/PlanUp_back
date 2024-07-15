# Python 3.10을 베이스 이미지로 사용합니다
FROM python:3.10

# 작업 디렉토리를 /app으로 설정합니다
WORKDIR /app

# 시스템 패키지를 업데이트하고 필요한 패키지를 설치합니다
RUN apt-get update && \
    apt-get install -y wget unzip curl

# Chrome을 설치합니다
RUN wget -O /tmp/chrome-linux64.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y /tmp/chrome-linux64.deb && \
    rm /tmp/chrome-linux64.deb

# webdriver-manager와 관련된 Python 패키지를 설치합니다
RUN pip install webdriver-manager

# 소스 코드를 복사합니다
COPY . .

# 환경 변수 설정 파일을 복사합니다
COPY .env .env

# Docker 컨테이너가 시작될 때 실행할 명령어를 설정합니다
CMD ["python", "main.py"]
