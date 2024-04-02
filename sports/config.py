
import os

BASE_DIR = os.path.dirname(__file__)

# MySQL 연결 설정 예시
# 포맷: mysql+pymysql://<사용자명>:<비밀번호>@<호스트>/<데이터베이스명>?charset=utf8mb4
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1111@localhost/sports?charset=utf8mb4'

SQLALCHEMY_TRACK_MODIFICATIONS = False


# import os

# BASE_DIR = os.path.dirname(__file__)

# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'sports.db'))
# SQLALCHEMY_TRACK_MODIFICATIONS = False
