# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()

nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")
print("nowDateTime : ", nowDateTime)

# SQLite 버전 확인
print("sqlite3.version", sqlite3.version)
print("sqlite3.sqite_version", sqlite3.sqlite_version)


# DB 생성 & Auto Commit(Rollback)
# isolation_level = None : Auto Commit 설정
conn = sqlite3.connect("C:/python_workspace/resource/database.db", isolation_level=None)

# Cursor
c = conn.cursor()
print("Cursor Type : ", type(c))

# 테이블 생성(Data Type : TEXT, NUMERIC INTEGER, REAL, BLOB)
c.execute("create table if not exists users(id integer primary key, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입

# ? : 두번째 인자의 튜플형태를 받음
c.execute("insert into users values(1, 'Won', 'Won@gmail.com', '010-0000-0000', 'Won.com', ?)", (nowDateTime, ))
c.execute("insert into users(id, username, email, phone, website, regdate) values(?,?,?,?,?,?)", (2, "Park", "Park@gmail.com", "010-1111-1111", "Park.com", nowDateTime))


# Many 삽입(튜플, 리스트), 선호
# 튜플 안에 튜플 형태
userList = (
    (3, "Lee", "Lee@naver.com", "010-2222-2222", "Lee.com", nowDateTime),
    (4, "Kim", "Kim@naver.com", "010-3333-3333", "Kim.com", nowDateTime),
    (5, "Jo", "Jo@gmail.com", "010-4444-4444", "Jo.net", nowDateTime)
)

c.executemany("insert into users(id, username, email, phone, website, regdate) values(?, ?, ?, ?, ?, ?)", userList)


# 테이블 데이터 삭제
# conn.execute("delete from users")

# 삭제한 행수 출력 
# print("users db deleted : ", conn.execute("delete from users").rowcount)


# 커밋 : isolation_level = None 일 경우 자동 반영
# 수동 : conn.commit()

# 롤백
# conn.rollback()

# 접속 해제
# conn.close()