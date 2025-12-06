# Python 3.10 버전을 기본 이미지로 사용합니다.
FROM python:3.10-slim

# 작업 디렉토리를 /usr/src/app으로 설정합니다.
WORKDIR /usr/src/app

# 호스트의 requirements.txt 파일을 컨테이너로 복사합니다.
# (requirements.txt 파일이 있다고 가정합니다. 없다면 Django와 기타 라이브러리를 직접 명시해야 합니다.)
COPY requirements.txt .

# 필요한 Python 패키지를 설치합니다.
RUN pip install --no-cache-dir -r requirements.txt

# 현재 프로젝트의 모든 파일을 컨테이너의 작업 디렉토리로 복사합니다.
COPY . .

# Django 애플리케이션의 포트(기본 8000)를 노출합니다.
EXPOSE 8000

# 컨테이너가 시작될 때 실행할 명령어입니다.
# (나중에 docker-compose에서 migrate와 runserver를 실행할 것입니다.)
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
