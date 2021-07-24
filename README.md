# 한양대에리카 2021 컴퓨터캡스톤디자인

### 주제 : 교내 시설물 대관 시스템
### 기간 : 2020. 07 ~ 2021. 05
### 기술 스택
<span>
<img src=https://user-images.githubusercontent.com/22339356/125117830-bf0ad900-e129-11eb-9474-69e392a7098d.png width="300">
<img width="40">
<img src=https://user-images.githubusercontent.com/22339356/126877520-8cf3518e-1bd1-4a65-be07-9e710aef2836.png width="230">
</span> <br><br>
<span>
<img src=https://user-images.githubusercontent.com/22339356/126877516-850cb4eb-9580-40a5-8b09-d489bee1d311.png width="230">
<img width="40">
<img src=https://user-images.githubusercontent.com/22339356/126877522-8c54c678-b146-4e9d-ac57-9f402f9372ed.png width="350">
</span>

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
### 둘러보기
<details>
    <summary> 메인 페이지 </summary>
    <img src=https://user-images.githubusercontent.com/22339356/126877840-b8c111df-8518-49b9-a3e4-63bbd0dc2f3b.png width="1000">
</details>


<details>
    <summary> 이용 안내 </summary>
    <img src=https://user-images.githubusercontent.com/22339356/126877919-72647e69-2baa-46e3-bb2e-93488479ac12.png width="1000">
</details>


<details>
    <summary> 주요 연락처 </summary>
    <img src=https://user-images.githubusercontent.com/22339356/126877941-5e934af5-a738-46d4-98e1-a69a04e64454.png width="1000">
</details>


<details>
    <summary> 캠퍼스 지도 </summary>
    <img src=https://user-images.githubusercontent.com/22339356/126877946-6abb979e-2c16-4ed3-81fe-a958d2c4a90e.png width="1000">
</details>


<details>
    <summary> 캠퍼스 실사 이미지 </summary>
    <img src=https://user-images.githubusercontent.com/22339356/126877942-9965739f-1d64-4b41-bd34-ec5f6e3709dc.png width="1000">
</details>


<details>
    <summary> 오시는 길 </summary>
    <img src=https://user-images.githubusercontent.com/22339356/126877937-83ce28a6-eb97-466f-ba28-0320ac28c19b.png width="1000">
</details>

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
