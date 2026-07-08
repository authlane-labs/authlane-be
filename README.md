# AuthLane BE

![Python](https://img.shields.io/badge/Python-3.12-3776ab?logo=python)
![Flask](https://img.shields.io/badge/Flask-REST-000000?logo=flask)
![MariaDB](https://img.shields.io/badge/MariaDB-SQLAlchemy_Async-003545?logo=mariadb)

React 인증 화면과 레거시 로그인 폼이 함께 사용하는 Flask REST API입니다. 로그인, 토큰 갱신, 세션 dashboard 데이터를 제공합니다.

## 기능

- `POST /api/auth/login`
- `POST /api/auth/refresh`
- `GET /api/dashboard`
- `PATCH /api/events/{event_id}/status`
- OpenAPI 명세 제공
- k6 smoke script 제공

## 아키텍처

- 구조: MVC
- Framework: Flask
- ORM: SQLAlchemy 2.0 Async Mode
- Database: MariaDB
- Runtime: Gunicorn / Waitress

## 실행

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Docker

```bash
docker compose up --build
```

## 환경 변수

```bash
DATABASE_URL=mysql://app:app@localhost:3306/app
```

## 설계 메모

controller, service, repository를 분리해 인증 요청 처리, 토큰 발급, 저장소 접근 책임이 섞이지 않도록 구성했습니다.
