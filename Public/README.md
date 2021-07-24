# 개발 기록

## 1월 27일 

### totalmenu에 링크 달기 (15:37)
- templates/totalmenu.py - 코드수정
- templates/context_processor.py - 파일생성
- EricaPlace/settings.py - 코드수정
### 페이지 css 수정
- 모든 페이지 margin 제거
- Main.html 메인에 미들사진 두장 추가
  #### Userguide.html 
    1) 창 좁아지면 메인컨테이너 밑으로 가는거 수정
    2) 캠퍼스맵 고화질사진 새탭열기 -> 다운로드로 변경
    3) 캠퍼스맵, 오시는길 컨테이너 top위치 수정, 네이버지도에 border 추가 
    4) 버튼 호버시 마우스포인터로 수정
  #### Buildings.html , Mainplace.html
    1) 사진에 border추가
    2) height 270px로 고정

- Mainplace.html, Buildings.html 반응형 추가


## 1월 28일

### 예약 신청 데이터 모델 수정 및 처리
- rsv/models.py - 코드 수정
- rsv/views.py - 코드 수정
### 페이지 css 수정
- 모든 페이지에서의 nav-search, nav-recommend 어떠한 창 크기에도 상관없이 완벽하게 고정
  #### Userguide.html 
    1) nav에서 추천기능 탭 생성 : nav-recommend --> search 둘 중 하나만 뜨도록 nav.js 수정

## 1월 30일

### index.css 수정
- form 안으로 submit 버튼을 가져오면서 발생한 타임테이블이 깨지는 현상 수정

### form.html 수정
- 사용 인원, 사용 목적 부분 drop-down 형식으로 변경(input -> select)
- 행사 내용 부분 기존 입력 방식 input에서 textarea로 변경

### form.css 수정
- 기존 css 안 입힌 대관 신청 작성란 틀에 css 추가

### nav-search.html,css 수정
- 사람 수 선택 시 애니메이션 추가
- 사람 수에 따른 컨테이너 띄우기
- 10명에 더보기 추가
- nav-s-img 컨테이너 디자인 변경

### UseGuide.html,js 수정 중 (from totalmenu)
- 백에서 url */1 , */2 로 주면 js 에서 window.onload 써서 페이지 로드 시에 해당 탭에 맞게 
- 해당함수
### UseGuide.html,js 완료
- totalmenu에서 userguide로 갈 때 새로고침 거치고 이동

### 예약 신청, 신청 현황 확인
- 예약 신청시 DB에 신청 내용 저장
- 신청 현황에 이름, 휴대폰 번호 입력시 확인 가능
- 신청 시간 선택 안하고 신청할 시 alert 팝업(근데 다음 화면으로 넘어가짐)

## 1월 31일

### alert 추가
- 대관신청 페이지(reservation, form) alert 추가 및 수정
- 다음 화면으로 넘어가지지 않도록 변경
- 학생/관계자/외부인에 따라 열리는 칸도 alert 가능하도록 수정

### date 관련 수정
- input=date가 정상적으로 넘어가지도록 수정
- 입력을 위해 클릭해도 달력이 안 보이던 현상 수정

## 2월 1일

### main.html 링크 달기
- 사진속 버튼 누르면 바로 신청페이지로 넘어가기
- Campus Map 누르면 캠퍼스맵 페이지로 넘어가기
- 이건 뭐하지 --> PORTAL HANYANG으로 변경하고 a 태그 포털로 연결 해놓음 

### nav_search 백엔드 적용
- 좌석수 선택시 결과 화면 뜨기
- 장소 추천 메뉴

### nav_recommend 사진 변경
- 이름 사진과 맞게 사진 바꿈

## 2월 4일
### nav-left 디자인 변경
### status.html, css 완성


## 2월 5일
### 장소 추천 페이지 완성
### reservation_js.html 에 예약된 날짜 정보 보내주기

## 2월 5일
### 좌측 nav 각 탭으로 연결 시에 따른 css 수정  
### recommend.html 연결된 mainplace.css 떼고 새로 recommend.css 추가
- 제목은 대관장소추천으로 고정하고 타이틀바 밑에 목적띄우기로 변경
- 장소 이름 반대편으로 대여회수:n 으로 표현
### status.css 신청상태 애니메이션추가   

## 2월 7일
### favicon 적용

## 2월 8일
### reservation 페이지 수정
- nav.css z-index 수정(input이 nav보다 위로 가는 현상 수정)
- calender 하위 요소 수정
- js 불러오기 위한 수정

### reservation 페이지 이미 예약된 곳 데이터 받아와서 누를 수 없도록 수정
- 날짜를 변경할 때 마다 초기화
- 예약된 곳이 사이에 있는 경우 더 큰 범위를 잡으면 예약이 가능한 경우 => 수정 및 alert
- 예약이 불가능한 구역 배경 색 추가
- 날짜를 누르지 않았을 때(오늘) 예약한 데이터가 있을 경우, 페이지가 로드될 때 확인하여 disabled
- reset 버튼을 눌렀을 때 disabled한 시간들도 초기화하도록 수정

### form.html alert 상세화 및 css 수정
- 입력되지 않은 부분 alert 해줌
- 정렬 통일

## 2월 11일
### 예약 승인 및 승인 취소
- 관리자 페이지에서 아직 승인 안된 예약은 '신청승인' 버튼 표시
- 승인된 예약은 '승인취소' 버튼 표시
- 누르면 현황이 바뀜

## 2월 16일
### 야외시설, 복지관 추가
### /director/status Pagination 오류 수정
- 페이지 3 띄워놓고 First나 Previous 누르면 페이지 1로 바뀌는 오류 수정
### 관리자 페이지 신청현황 검색기능
- 일단 대충 폼 만들어놓긴 했는데 제대로 작동은 안됨

## 2월 18일
### 관리자 환경설정 메뉴 추가
- 건물, 방, FAQ 추가, 수정, 삭제 기능

## 2월 21일
### 관리자 신청 현황 조회 방법 수정
- 단대, 승인여부, 날짜 중 하나만 선택해도 조회 가능
### create_bulding.html 수정
- 건물명, 영문건물명, 건물번호, 사진 중 하나라도 정보가 빠져있을 시 alert 및 데이터 넘어가지 않도록 수정

## 2월 23일
### timetable 오류 수정
- 날짜를 잘못 받아와 초기 화면에서 예약되지 않은 시간임에도 예약 되었다고 alert하던 오류 수정
### reservation, form 페이지 수정
- nav가 다른 페이지와 다르게 깨지던 현상 수정

## 2월 27일
### 대관신청 페이지 수정
- timetable 직접 입력 금지
- form 페이지 여러번 반복해도 해당 신분에 맞는 것만 체크하도록 수정

## 3월 3일
### 폼 작성 오류 수정 및 정규표현식
- 학생, 관계자, 외부인 선택 바꿨을 시 발생하는 오류 수정
- 폼 양식에 맞게 정규표현식 적용 (프론드, 백 둘다)

## 3월 5일
### 빈 폼 제출 막기
- Javascript Console 이용해서 강제 제출 또한 막음
### 신청 취소 부분적으로 막기
- 아직 처리중인 신청에 대해서만 본인이 직접 취소 가능
### 장소추천 조건 수정
- 신청 승인이 된 데이터만 이용해서 장소 추천

## 3월 6일
### 대관 신청 페이지 수정
- 디자인 전체 수정
- bootstrap datetimepicker 적용 (type = text)
- 날짜 및 시간 선택하는 부분 js 수정
- 적용하기 버튼 삭제(수정 전에는 안 눌러도 제출이 가능했음)

## 3월 8일
### 대관 신청 페이지 버그 픽스
- 시작 시간과 끝 시간(2번 클릭)만 선택할 수 있도록 수정
- 폼 작성으로 넘어간 뒤 뒤로가기를 누르면 데이터가 남아있는 현상 수정(초기화됨)
- 달력 초기화 버그 수정

## 3월 9일
### 대관 신청 페이지, 폼 작성 페이지 디자인 수정
- 디자인 수정
