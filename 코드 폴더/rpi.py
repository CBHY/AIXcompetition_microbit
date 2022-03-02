# 이 코드는 라즈베리 파이에서 구동하는 코드입니다.

# lib import
from turtle import distance
import RPi.GPIO as GPIO
import time

# pin setting
GPIO.setmode(GPIO, BCM) # pin number를 BCM 모드로 읽음
GPIO.setup(17, GPIO.OUT)# ultrasonic out
GPIO.setup(27, GPIO.IN) # ultrasoinc in
GPIO.setup(18, GPIO.OUT)# servo moter out
P = GPIO.PWM(18, 50) # 아날로그 핀 제어

# 실행
while True:
    GPIO.output(17, True) # ultrasonic out on
    time.sleep(0.1) 
    GPIO.output(17, False) # ultrasonic out off
    # 시간 변수 초기화
    startTime = time.time()
    stopTime = time.time()

    # 시간 변수 설정
    while GPIO.input(27) == 0:
        Starttime = time.time()
    while GPIO.input(27) == 1:
        stopTime = time.time()
    # 거리 계산
    TimeElapsed = stopTime - startTime
    distence = (TimeElapsed*34000) / 2
    time.sleep(1)
    # 거리 표시
    print(distence, 'Cm')
    
    # 조건부 servo moter 제어
    if distence < 10 :
        p.start(0) # 각도 초기화
        p.ChangeDutyCycle(12) # 설정된 각도로 고정(문 기준 살짝 잡아줌)
        time.sleep(3) # 3초동안 유지
        break
