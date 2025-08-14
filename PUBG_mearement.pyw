import pyttsx3
from pynput.mouse import Listener


# print("程序将在2秒后开始记录鼠标点击...")
# time.sleep(2)


clicks = []


def on_click(x, y, button, pressed):
    if pressed and button == button.left:
        clicks.append((x, y))
        # print(f"已记录点击 {len(clicks)}: X={x}, Y={y}")
        return len(clicks) < 4

# 开始监听鼠标点击
with Listener(on_click=on_click) as listener:
    listener.join()


'''
for i, (x, y) in enumerate(clicks):
    print(f"点击 {i+1}: X={x}, Y={y}")
'''

# 计算前两次点击的距离
if len(clicks) >= 2:
    x1, y1 = clicks[0]
    x2, y2 = clicks[1]
    distance1 = ((x2 - x1)**2 + (y2 - y1)** 2)**0.5
    # print(f"\n前两次点击之间的像素距离: {distance1:.1f} 像素")

# 计算后两次点击的距离
if len(clicks) >= 4:
    x3, y3 = clicks[2]
    x4, y4 = clicks[3]
    distance2 = ((x4 - x3)**2 + (y4 - y3)** 2)**0.5
    #print(f"后两次点击之间的像素距离: {distance2:.2f} 像素")

# 获得输出值
distance=100/distance1*distance2

'''
# 保存坐标和距离到文件
print("坐标和距离信息已保存到 mouse_clicks.txt 文件中。")
with open('C:/Users/YiboLi/OneDrive/Desktop/mouse_clicks.txt', 'w') as f:

    for x, y in clicks:
        f.write(f"{x},{y}\n")
    # 保存距离信息
    if len(clicks) >= 2:
        f.write(f"前两次点击距离: {distance1:.2f} 像素\n")
    if len(clicks) >= 4:
        f.write(f"后两次点击距离: {distance2:.2f} 像素\n")

    f.write(f"最终结果: {distance:.2f} m\n")
'''

# 初始化语音引擎
engine = pyttsx3.init()
# 设置语速
rate = engine.getProperty('rate')
engine.setProperty('rate', 165)
# 语音输出结果
# 获取可用语音列表
voices = engine.getProperty('voices')
# 选择第一个语音（通常是男性声音，更符合军事化风格）
if len(voices) > 0:
    engine.setProperty('voice', voices[0].id)
# 语音输出
engine.say(f"{distance:.1f}")
engine.runAndWait()