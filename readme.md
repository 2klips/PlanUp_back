# 프로젝트 소개

### 플랜업( PLAN UP )

**취업준비를 위한 여러분들을 위해, 캘린더를 통한 일정관리 서비스를 제공합니다!**

* **취업 공고 추가**
구직 사이트에서 원하시는공고의 url를 입력하셔서, 해당 공고의 정보와 자세한 일정을 캘린더에 바로 추가하실 수 있습니다!

   * 해당 공고에 대한 간단한 정보 및 기업정보를 같이 저장하며, 잊어버리지 않도록 취업공고 마감일정과, 추가적인 체크리스트 추가를 통해 취업을 위한 플래너를 관리해보세요!

* **자격증 시험 일정 추가**
    * 준비하시는 자격증이 있다면, 자격증 검색 기능을 통해,원하시는 자격증 시험 일정을 선택하셔서, 나의 캘린더 일정에 추가할 수 있습니다!

**플랜 업과 함께 목표를 이루시도록 도와드릴게요!**

# 포트폴리오

<details>
  <summary>펼치기/접기</summary>
 
![PLAN_UP 기획서_page-0001](https://github.com/user-attachments/assets/31f7e8e5-9f11-48ad-84b4-2d75cfc57c8d)
![PLAN_UP 기획서_page-0002](https://github.com/user-attachments/assets/ff59fad1-362a-4d70-88a9-5dded9682f5f)
![PLAN_UP 기획서_page-0003](https://github.com/user-attachments/assets/e1c54730-5bca-4f9d-aa36-a7176a3f5648)
![PLAN_UP 기획서_page-0004](https://github.com/user-attachments/assets/e58e3242-ff2c-41dc-af1d-1cfe494e19a3)
![PLAN_UP 기획서_page-0005](https://github.com/user-attachments/assets/885521d3-3fb3-4552-a014-73f9dfca706b)
![PLAN_UP 기획서_page-0006](https://github.com/user-attachments/assets/b98bc8da-ed3a-4bdd-8f13-b27dc6fe7493)
![PLAN_UP 기획서_page-0007](https://github.com/user-attachments/assets/dbb87149-45a5-45c4-992e-2f40b0a888dc)
![PLAN_UP 기획서_page-0008](https://github.com/user-attachments/assets/eddbb1c9-9da3-4b36-9a41-e0f23aae1f3e)
![PLAN_UP 기획서_page-0009](https://github.com/user-attachments/assets/492e5b6d-f071-4209-91ec-bdc02f9a55c9)
![PLAN_UP 기획서_page-0010](https://github.com/user-attachments/assets/e1b5aeef-cec4-43b2-ac68-27e88ca62a85)
 
 </details>

 <hr/>

### 기능

* 캘린더를 통해 일정을 한눈에 확인

* 일정 리스트를 통해 내가 추가한 일정 확인

* 일정에 대한 체크리스트로 해당 일정에 할 일, 준비물 등을 확인

* 자격증 일정 검색 및 일정 추가

* 채용 공고 URL을 통한 기업 정보, 채용 공고를 일정에 저장

# 실제 어플 구동 화면
<details>
  <summary>시연 보기/접기</summary>
  

  <br/>

 <center><img src="구동화면.gif" alt="Demo GIF" width="360" height="640"></center>

 
 
</details>



### 프로젝트 폴더 구조

```
Backend/
├── src/
│   ├── config/                 # 설정 파일
│   ├── controllers/            # 컨트롤러
│   ├── middleware/             # 미들웨어
│   ├── models/                 # 데이터베이스 모델
│   ├── routes/                 # 라우트
│   ├── services/               # API 호출 등 비즈니스 로직
│   ├── app.js                  # Express 애플리케이션 설정
├── .env                        # 환경 변수 설정 파일
├── package.json                # npm 패키지 설정 파일
├── requirements.txt            # 종속성 설치 파일
├── main.py                     # 크롤링 서버 파일
└── README.md                   # 프로젝트 설명 파일

```


# 실행
1. 리포지토리 복제
```bash
git clone https://github.com/Songysp/PlanUP_frontend

```

2. 패키지 설치
  * node.js, react-native-cli, android stuid 필요
```bash
npm install
```
  * 백엔드 종속성 설치
```bash
# 백엔드 루트 폴더에서 아래 코드 실행
pip install -r requirements.txt
```

3. 앱 실행

  * 백엔드 서버 실행
```bash
npm start
```
  * FastAPI 크롤링 서버 실행
```bash
python main.py
```
  * 프론트 엔드
```bash
npx react-native run-android
```

# 플레이 스토어

### [스토어 링크](https://play.google.com/store/apps/details?id=com.PlanUP&pli=1)
![플레이스토어](https://github.com/user-attachments/assets/77b51f29-cd09-49e8-a971-87710aa3204f)


### 기술 스택

* **프론트엔드**
  * JavaScript
  * React-Native
  * AndroidStudio
* **백엔드**
  * Node.js
  * Python
  * FastAPI
* **데이터베이스**
  * MongoDB
* **배포**
  * Docker
  * CloudType
* **협업툴**
  * Figma
  * GitHub


# 협업 방식
1. **Figma 활용**
    * 기획안을 스토리보드로 작성
    * 화면 구성을 참고하여 개발

2. **GIT**
    * GIT-FLOW 전략을 차용
    <img src="https://techblog.woowahan.com/wp-content/uploads/img/2017-10-30/git-flow_overall_graph.png" alt="git-flow" width="600" height="600">
    
    * master: 배포를 위한 브랜치. 특별한 경우가 아니면 따로 관여하지 않으며 pull request 기능을 사용
    * develop: 개발, 테스트를 위한 브랜치
    * 모든 개발은 develop 브랜치에서 이루어지고, 추가 기능 개발은 따로 브랜치를 분리해 develop과 병합. 이후 충분한 테스트를 거친 후 master 브랜치에 병합하여 배포 버전을 업데이트

# 작성자의 기여
* 리액트 네이티브 및 안드로이드 개발

  * 리액트 네이티브를 사용한 모바일 애플리케이션 개발.
  * 안드로이드 플랫폼에 대한 개발 환경 세팅 및 폴더 구조 구축.

* 백엔드 서버 구조 구축

  * 서버 아키텍처 설계 및 구현.
  * 백엔드 서버 개발 및 유지보수.


* GitHub 버전 관리 구조 구축

  * GitHub를 활용한 버전 관리 시스템 설정 및 관리.
  * 협업을 위한 브랜치 전략 수립.

* 메인 페이지 구성

* 사용자 인증 및 로그인, 회원가입 세션 개발

* 로그인 및 회원가입 기능 구현.

* 프론트엔드 및 백엔드 환경 변수 관리

* 개발 환경에서 필요한 환경 변수 설정 및 관리.

* 캘린더, 일정, 체크리스트 기능 개발

  * 캘린더와 일정 관리 기능 구현.
  * 체크리스트 기능 개발 및 통합.

* 전체적인 문제 해결 및 유지보수

  * 프로젝트에서 발생한 문제 및 오류 해결.
  * 전체적인 코드 유지보수 및 개선 작업.

* Dockerfile 이미지 생성
  * Dockerfile을 사용하여 컨테이너 이미지를 생성 및 관리.

* APK 빌드 및 배포

  * Android 애플리케이션의 APK 파일 생성 및 배포.
  * 빌드 프로세스 자동화 및 최적화.


* 백엔드 서버 및 크롤링 서버 배포

  * 백엔드 서버와 크롤링 서버의 배포 및 운영.
  * 서버 모니터링 및 유지보수.

* 플레이스토어 배포
* 
  * 애플리케이션을 Google Play Store에 배포.
  * 앱의 업데이트 및 관리.

# 팀 기여
* 현우 팀장:
    * 기획, 디자인
    * 크롤링 코드 보완
    * 화면 구성 디테일 수정
    * CSS 유지보수
    * 취업 공고 검색기능 개발
    * 플레이스토어 배포
* 임희선:
    * 캘린더, 일정 리스트, 체크리스트의 프론트엔드 및 백엔드, DB  초안 개발
    * 자격증 OpenAPI 연결
    * 자격증 검색 일정 추가 기능 개발
    * 회원 관련 백엔드, DB 초반 구성
* 박성주:
    * 파이썬 채용 공고 크롤링 코드 작성
    * FastAPI 크롤링 서버 구축
    * 채용 공고 페이지, 채용 공고 일정 추가 기능, 관련 DB 개발
* 송윤섭:
    * 리액트 네이티브, 안드로이드, 개발 환경 세팅, 폴더 구조 구축
    * 백엔드 서버 구조 구축
    * GitHub 버전 관리 구조 구축
    * 메인 페이지 구성
    * 사용자 인증 및 로그인, 회원가입 세션 개발
    * 프론트, 백엔드 환경 변수 관리
    * 캘린더, 일정, 체크리스트 기능 개발
    * 전체적인 문제, 오류 해결 유지보수
    * Dockerfile 이미지 생성
    * APK 빌드 배포
    * 백엔드 서버, 크롤링 서버 배포
    * 플레이스토어 배포
