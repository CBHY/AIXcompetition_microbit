# AIXcompetition_microbit



## 0. intro

이 repository는 2022-01-14에 열린 광주 AIX 코딩 기초역량 강화 경진대회에서 micro:bit + X 부문에 출전하기 위해 만든 코드를 저장하기 위해 만들었습니다.

참가 상세 부문은 mirco:bit + mobility 입니다.

 주제는 **'micro:bit로 구현한 자동차 안전성 향상을 위한 아이디어'** 입니다.



## 1. 아이디어 소개

자동차를 운행함에 있어 안전성 향상을 위한 3가지 아이디어를 구현했습니다.

1가지 아이디어는 주,정차 시 안전성 향상을 위한 아이디어,

2가지 아이디어는 주행 시 안전성 향상을 위한 아이디어 입니다.



### I. 주,정차 시 안전성 향상을 위한 아이디어

#### i. 초음파 센서를 이용한 하차 보조

![doorcok](..\AIXcompetition_microbit\images\doorcok.png)



추가적인 하드웨어 추가 없이, 주차보조시스템으로 이용되는 초음파 센서를 이용하여 구현하고자 하였습니다.

 ![](D:..\AIXcompetition_microbit\images\6.png)

초음파 센서가 측정한 거리가 지정된 거리보다 가까워지면, 모터 제어로 문을 살짝 잡아주면서 급격한 문 열림을 방지하고 경고하는 기능입니다.

###### 구현 동영상

<video src="..\AIXcompetition_microbit\images\doorcok.mp4"></video>

(microbit 경연대회지만, gpio 핀 자리가 부족하여 주최측 양해를 구하고 라즈베리파이로 구현)









### II. 주행 시 안전성 향상을 위한 아이디어

주행 시 안전성 향상을 위한 아이디어 2가지의 핵심은 

**차량 - 차량 신호 공유**

**차량 - 시스템 신호 공유** 입니다.

모든 객체들이 유기적으로 연결되어 신호를 공유하여 위험 상황에 대처능력을 향상시킵니다.

#### i. 사각지대 물체 인식 신호 공유

사각지대에서 갑자기 튀어나오는 물체나 사람 등을 인식하기 위해서 주행중인 해당 차량만으로는 부족합니다.

카메라, 라이더, 레이더 등, 모든 센서가 인식하기 힘든 사각지대에서 찰나의 순간 차량을 제어해야 합니다.

그래서 저는 주차되어있는 다른 차량의 센서들을 이용하여 물체을 인식하고, 신호를 공유하는 방식의 아이디어를 구현해보았습니다.

###### 구현 영상(Ex 스쿨존 사각지대에서의 주차 차량의 초음파 센서 이용)

<video src="..\AIXcompetition_microbit\images\schoolzone.mp4"></video>



###### 측면 영상

<video src="..\AIXcompetition_microbit\images\20220112_194357_2.mp4"></video>



#### ii. 도로 상황 신호 공유

<video src="..\AIXcompetition_microbit\images\blackicetrafickaccident.mp4"></video>



위 영상에서처럼, 블랙아이스 등 도로 상황 악화 시 신호 공유의 수단이 전무하다는 것을 알 수있습니다.

현제 자동차의 신호 공유 수단으로 좌우 깜빡이, 양보 깜빡이, 브레이크등을 사용하고 있지만 이것들 만으로는 역부족입니다. 그래서 자동차끼리 라디오 통신 등을 이용한 유기적 연결을 통해 이를 극복하고자 하였습니다.

![7](..\AIXcompetition_microbit\images\7.png)



###### 구현 영상(빙판 발견 후 주변 차량에 신호 공유)

<video src="..\AIXcompetition_microbit\images\ice.mp4"></video>







