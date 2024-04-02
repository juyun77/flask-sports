# 기본 이미지로 Python 3.9를 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 현재 디렉토리의 모든 파일을 컨테이너의 작업 디렉토리로 복사
COPY . /app

# 필요한 패키지 설치를 위한 requirements.txt 파일 복사
# (Flask 및 그 외 필요한 패키지 목록을 포함해야 함)
COPY requirements.txt /app

# requirements.txt에 명시된 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 컨테이너가 시작될 때 실행될 명령어 설정
# Flask 애플리케이션 실행
CMD ["flask", "run", "--host=0.0.0.0"]
