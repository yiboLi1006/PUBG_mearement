import pyttsx3
from pynput.mouse import Listener

# 初始化语音引擎
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)

clicks = []


def on_click(x, y, button, pressed):
    if pressed and button == button.left:
        clicks.append((x, y))
        return len(clicks) < 4

# 开始监听鼠标点击
with Listener(on_click=on_click) as listener:
    listener.join()


# 计算前两次点击的距离
if len(clicks) >= 2:
    x1, y1 = clicks[0]
    x2, y2 = clicks[1]
    distance1 = ((x2 - x1)**2 + (y2 - y1)** 2)**0.5

# 计算后两次点击的距离
if len(clicks) >= 4:
    x3, y3 = clicks[2]
    x4, y4 = clicks[3]
    distance2 = ((x4 - x3)**2 + (y4 - y3)** 2)**0.5

# 获得输出值
distance=100/distance1*distance2

# 语音输出结果
# 语音输出
engine.say(f"{distance:.1f}")
engine.runAndWait()
