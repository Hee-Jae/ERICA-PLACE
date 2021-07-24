# 한양대에리카 2021 컴퓨터캡스톤디자인

### 주제 : 교내 시설물 대관 시스템
### 기간 : 2020. 07 ~ 2021. 05

---
### 디렉토리 구조
```
Public
│   README.md               # 개발 기록
│
└───EricaPlace
    │   db.sqlite3          # 데이터베이스 파일
    │   manage.py           # 실행 파일
    │   requirements.txt    # 패키지 버전
    │
    └───EricaPlace
    │       settings.py     # 환경 세팅
    │       urls.py         # URL 등록
    │
    └───director            # 관리자 페이지
    └───faq                 # 자주 묻는 질문
    └───main                # 메인 페이지
    └───media               # 미디어 리소스
    └───rsv                 # 대관 신청 페이지
    └───static              # 스태틱 리소스
    └───status              # 신청 현황 페이지
    └───templates           # 범용 템플릿
```

### 서버 실행
`/Public/EricaPlace/python3 manage.py runserver`

### 이메일 알림 서비스
- `/Public/EricaPlace/EricaPlace/settings.py` 파일의 `EMAIL_HOST_USER` 에 Gmail 계정 이메일 등록
- `/Public/EricaPlace/EricaPlace/settings.py` 파일의 `EMAIL_HOST_PASSWORD` 에 Gmail 계정 패스워드 등록
- Gmail 계정 로그인 -> Google Account -> Security 메뉴 -> Allow less secure apps 를 'ON' 설정
- 배포 시 Gmail 계정의 패스워드가 노출되지 않도록 주의 해야하며, 임시 계정을 생성해 등록하기를 권장함

### 주의 사항
서버 배포 시 `/Public/EricaPlace/EricaPlace/settings.py` 파일의 `SECRET_KEY` 를 절대 노출 시키면 안된다.

---
### 개발팀 구성원

<table>
    <tr align="center">
        <td style="min-width: 100px;">
            <a href="https://github.com/Hee-Jae">
              <img src="https://github.com/Hee-Jae.png" width="100">
              <br />
              <b> 정희재 </b>
            </a>
            <p> Leader </p>
        </td>
        <td style="min-width: 100px;">
            <a href="https://github.com/wogns0197">
              <img src="https://github.com/wogns0197.png" width="100">
              <br />
              <b> 권재훈 </b>
            </a>
            <p> Member </p>
        </td>
        <td style="min-width: 100px;">
            <a href="https://github.com/sue991">
              <img src="https://github.com/sue991.png" width="100">
              <br />
              <b> 이수아 </b>
            </a>
            <p> Member </p>
        </td>
        <td style="min-width: 100px;">
            <a href="https://github.com/bsyun0571">
              <img src="https://github.com/bsyun0571.png" width="100">
              <br />
              <b> 윤병서 </b>
            </a>
            <p> Member </p>
        </td>
    </tr>
    <tr align="center">
        <td>
            BackEnd
        </td>
        <td>
            FrontEnd
        </td>
        <td>
            BackEnd
        </td>
        <td>
            FrontEnd
        </td>
    </tr>
</table>
