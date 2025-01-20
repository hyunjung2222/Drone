import time, cv2
from threading import Thread
from djitellopy import Tello

tello = Tello()

tello.connect()

keepRecording = True
tello.streamon()
frame_read = tello.get_frame_read()

def videoRecorder():
    # 비디오 녹화를 위한 VideoWriter 객체 생성
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        try:
            # 프레임이 유효한지 확인
            if frame_read.frame is not None:
                video.write(frame_read.frame)
            time.sleep(1 / 30)
        except Exception as e:
            print(f"비디오 녹화 중 오류 발생: {str(e)}")
            break

    # 비디오 파일 정상 종료를 위해 release() 호출
    video.release()

# 별도 스레드에서 비디오 녹화 실행
recorder = Thread(target=videoRecorder)
recorder.start()

try:
    tello.takeoff()
    time.sleep(2)  # 이륙 후 안정화를 위한 대기
    tello.move_up(100)
    time.sleep(2)  # 상승 후 안정화를 위한 대기 
    tello.rotate_counter_clockwise(360)
    time.sleep(2)  # 회전 후 안정화를 위한 대기
    tello.land()
except Exception as e:
    print(f"드론 제어 중 오류 발생: {str(e)}")
    tello.land()  # 오류 발생시 안전하게 착륙

# 녹화 종료
keepRecording = False
recorder.join()
