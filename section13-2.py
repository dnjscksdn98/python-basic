# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 최종 완성

import random
import time
import sqlite3
import winsound
import datetime

# DB 생성 & Auto Commit
conn = sqlite3.connect("C:/python_workspace/resource/records.db", isolation_level=None)

# Cursor 연결
cursor = conn.cursor()

# 테이블 생성
# autoincrement : 직접 삽입을 안해줘도 자동으로 삽입해주고 증가
cursor.execute("create table if not exists records(id integer primary key autoincrement, cor_cnt integer, record text, reg_date text)")


words = []  # 영어 단어 리스트(100개 로드)

n = 1  # 게임 시도 횟수
cor_cnt = 0  # 정답 개수

with open("./resource/word.txt", 'r') as f :
    for c in f :
        words.append(c.strip())  # strip() : 문자열의 양쪽 끝에 존재하는 공백과 \n을 삭제

input("Ready? Press Enter Key!")  # Enter Game!, enter 키를 입력하면 다음으로 실행

start = time.time()  # Start Time

print()

while n <= 5 :  # 총 다섯번 실행
    random.shuffle(words)  # shuffle() : 리스트의 원소들을 랜덤으로 섞어준다
    q = random.choice(words)  # choice() : 리스트의 원소들 중에서 랜덤으로 하나 뽑아오기

    print()

    # 문제 출력
    print("Question #{}".format(n))
    print(q)

    # 타이핑 입력
    x = input()

    print()

    if str(q).strip() == str(x).strip() :  # 입력 확인(공백 제거)
        print("Pass!")

        # 정답 소리 재생
        winsound.PlaySound("./sound/good.wav", winsound.SND_FILENAME)

        cor_cnt += 1
    
    else :
        print("Wrong!")

        # 오답 소리 재생
        winsound.PlaySound("./sound/bad.wav", winsound.SND_FILENAME)

    n += 1  # 다음 문제 전환

end = time.time()  # End Time
et = end - start  # 총 시간
et = format(et, ".3f")  # 소수점 아래 3자리까지 포멧 변경

if cor_cnt >= 3 :
    print("합격!")

else :
    print("불합격!")


# 기록 DB 삽입
cursor.execute("insert into records('cor_cnt', 'record', 'reg_date') values(?, ?, ?)", (cor_cnt, et, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


# 수행 시간 출력
print("게임 시간 : ", et, "초", " 정답 개수 : {}".format(cor_cnt))

# 시작 지점
if __name__ == "__main__" :
    pass