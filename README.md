## Palm2Bot

## 설치

``` bash
pip install -r requirements.txt
```

## 사용법

### 1. GOOGLE 크리덴셜 등록 

`GOOGLE_APPLICATION_CREDENTIALS` 환경변수에 credentials.json 파일 위치 등록

#### Windows 

``` batch
set GOOGLE_APPLICATION_CREDENTIALS=<credentials.json 파일 경로>
```

#### Linux or OS X

``` bash
export GOOGLE_APPLICATION_CREDENTIALS="<credentials.json 파일 경로>"
```


### 2. API Key 등록

#### Windows

`cmd.exe`를 실행한 후 아래의 명령어로 API 키 등록

``` batch
set API_KEY=<API 키 입력>
```

#### Linux or OS X

터미널에서 아래와 같은 명령어로 API 키 등록

``` bash
export API_KEY="<API 키 입력>"
```


### 3. app.py 실행

아래와 같이 app.py를 실행하게 되면, `http://127.0.0.1:8080`에서 챗봇을 테스트 할 수 있습니다.

``` bash
python app.py
```


