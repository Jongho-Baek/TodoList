# 📋 Django TodoList 프로젝트

## 📝 프로젝트 개요

이 프로젝트는 Python의 웹 프레임워크인 **Django**와 **Docker**를 사용하여 개발된 간단한 할 일 관리 애플리케이션입니다. 사용자 인증(회원가입, 로그인, 로그아웃) 기능을 제공하며, 로그인한 사용자는 개인적인 할 일 목록을 생성, 조회, 수정 및 삭제할 수 있습니다.

**모든 페이지(인증 및 Todo 폼/목록)는 별도의 CSS 파일을 사용하여 일관되고 깔끔한 디자인이 적용되어 있습니다.**

### 주요 기능

* **사용자 인증:** 회원가입, 로그인, 로그아웃 (보안을 위해 POST 요청 사용)
* **할 일 관리:** CRUD (Create, Read, Update, Delete) 기능
* **데이터베이스:** SQLite3 (기본 설정)
* **환경:** Docker를 이용한 간편한 환경 구축

---

## 💻 사용 기술 스택

| 구분 | 기술/도구 | 버전 |
| :--- | :--- | :--- |
| **백엔드** | Python | 3.10+ |
| **웹 프레임워크** | Django | 5.2.x |
| **데이터베이스**| SQLite3 | - |
| **개발 환경** | Docker, Docker Compose | - |
| **프론트엔드** | HTML5, CSS3 | - |

---

## 🚀 설치 및 실행 방법 (Docker 사용 권장)

이 프로젝트는 Docker Compose를 사용하여 필요한 환경(Python, Django)을 한 번에 설정할 수 있도록 구성되어 있습니다.

## 우분투에서 Docker Compose 설치

### 1. 전제 조건

* **Git:** 소스 코드를 다운로드하기 위해 필요합니다.
* **Docker 및 Docker Compose:** 애플리케이션 실행 환경을 구축하기 위해 필요합니다.

## 우분투에서 Docker Compose 설치
```bash
# Docker Engine 및 Docker Compose 패키지를 한 번에 설치합니다.
sudo apt update
sudo apt install docker.io docker-compose -y

# Docker 서비스가 자동으로 시작되도록 설정
sudo systemctl start docker
sudo systemctl enable docker

### 2. 프로젝트 클론 및 이동

터미널에서 다음 명령어를 실행하여 GitHub 저장소에서 프로젝트를 로컬로 복사합니다.

# 깃허브 저장소에서 클론
git clone https://github.com/Jongho-Baek/TodoList.git

# 프로젝트 디렉토리로 이동
cd TodoList/todolist/

```bash
# Docker 이미지 빌드 및 컨테이너 실행 명령어
docker compose up --build

# 접속 주소
http://127.0.0.1:8000
