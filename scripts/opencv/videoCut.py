import cv2 as cv
import numpy as np
import os


def get_video_from_current_folder(video_path, video_type='.mp4'):
    video_list = os.listdir(video_path)
    ls = []
    for video in video_list:
        if video.lower().endswith(video_type):
            # print(img)
            ls.append(video)
    return ls if ls else None


def to_second(time):
    print(time, type(time))
    t = [int(n) for n in time.split(':')]
    return t[0]*3600 + t[1]*60 + t[2] if len(t)==3 else t[0]*60 + t[1]


def check_time_validity(time):      # time is a list with [start, end] represent a time interval
    for period in time:
        if not period[0] < period[1]:
            return False
    return True


def laplace_enhance(img, kernel=None):
    if not kernel:
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])  # 定义卷积核
    image_enhance = cv.filter2D(img, -1, kernel)  # 进行卷积运算
    return image_enhance


'''
多用在图像整体偏暗，扩展灰度级。另外一种情况是，图像有“冲淡”的外观（很亮白）需要压缩中高以下的大部分的灰度级。伽马变换对于图像对
比度偏低，并且整体亮度值偏高（对于于相机过曝）情况下的图像增强效果明显。
'''
def gamma_enhance(img):
    def gamma(image, c, v):
        lut = np.zeros(256, dtype=np.float32)
        for i in range(256):
            lut[i] = c * i ** v
        output_img = cv.LUT(image, lut)
        output_img = np.uint8(output_img + 0.5)  # 这句一定要加上
        return output_img

    out2 = gamma(img, 0.00000005, 4.0)
    return out2

'''
对数变换可以拉伸范围较窄的低灰度值，同时压缩范围较宽的高灰度值。可以用来扩展图像中的暗像素值，同时压缩亮像素值。
其中c为常数，r加1可以使函数向左移一个单位，得到的s均大于0。
'''
def log_enhance(img):
    def log(c, image):
        output_img = c * np.log(1.0 + image)
        output_img = np.uint8(output_img + 0.5)
        return output_img

    out2 = log(20, img)
    return out2

'''
直方图均衡化是通过调整图像的灰阶分布，使得在0~255灰阶上的分布更加均衡，提高了图像的对比度，达到改善图像主观视觉效果的目的。对比度较低的图像适合使用直方图均衡化方法来增强图像细节。、
opencv自带的函数只能进行一个通道的增强，下面是彩色图像的直方图增强：
'''
def equalize_hist_enhance(img):
    result = img.copy()
    for j in range(3):
        result[:, :, j] = cv.equalizeHist(img[:, :, j])
    return result

'''
自适应直方图均衡化首先将图像划分为不重叠的区域块，然后对每一个块分别进行直方图均衡化。显然，在没有噪声影响的情况下，每一个小区域
的灰度直方图会被限制在一个小的灰度级范围内；但是如果有噪声，每一个分割的区域块执行直方图均衡化后，噪声会被放大。为了避免出现
噪声这种情况，提出了“限制对比度”(Contrast Limiting)，如果直方图的bin超过了提前预设好的“限制对比度”，那么会被裁剪，然后将裁剪的部
分均匀分布到其他的bin，这样就重构了直方图。
'''
def clahe_enhance(img):
    # 创建CLAHE对象
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    # 限制对比度的自适应阈值均衡化
    b, g, r = cv.split(img)

    b = clahe.apply(b)
    g = clahe.apply(g)
    r = clahe.apply(r)

    enhanced = cv.merge([b, g, r])
    return enhanced

def frame_valid(time, intervals):
    for interval in intervals:
        if interval[0] <= time <= interval[1]:
            return True
    return False


def cut_video(video_path, output_path, start, end):
    a = [to_second(i) for i in start]
    b = [to_second(j) for j in end]

    interval = list(zip(a, b))
    if not check_time_validity(interval):
        print('Time interval illegal! Try to correct and proceed!')
        return
    videols = get_video_from_current_folder(video_path)
    for video in videols:
        cap = cv.VideoCapture(os.path.join(video_path, video))
        fourcc = cv.VideoWriter_fourcc(*'mp4v')  # *'XVID' is .avi format

        success, frame = cap.read()
        writer = cv.VideoWriter(os.path.join(output_path, video), fourcc, int(1.25*cap.get(5)), (frame.shape[1], frame.shape[0]))

        while success:
            time = cap.get(cv.CAP_PROP_POS_MSEC) // 1000
            print(time)
            if frame_valid(int(time), interval):
                success, frame = cap.retrieve()
                # TODO: frame augmentation, denoise
                frame = laplace_enhance(frame)
                # end TODO
                # print(len(frame), type(frame[0]))
                writer.write(frame)
                # continue

            success = cap.grab()

        writer.release()
        cap.release()




if __name__ == "__main__":
    vp = 'C:\\Users\\Administrator\\Desktop\\test'
    op = 'C:\\Users\\Administrator\\Desktop\\test\\wer'
    cut_video(vp, op, ['0:12'], ['0:33'])
    # print(to_second('0:12'), to_second('0:34'))
