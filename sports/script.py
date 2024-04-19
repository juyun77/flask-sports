# script.py
from flask import Flask
from sports import create_app, db
from sports.models import plan  # 올바른 임포트 경로
from datetime import datetime

app = create_app()

with app.app_context():
    plans = [
        plan(id=1, date2=datetime.strptime('2024-04-17', '%Y-%m-%d'), time='18:30', kind='잠실', name='LG VS 롯데', player='롯대 : 5, LG : 6'),
        # 추가 데이터 삽입
    ]

    for plan in plans:
        db.session.add(plan)

    db.session.commit()
