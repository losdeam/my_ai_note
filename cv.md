# [笔记目录](目录.md)
# cv部分
____
## 1.经典库

### 1.1 opencv
#### 1.1.1 简介
#### 1.1.2 常用函数
##### 1.1.2.1 读取

###### 1.1.2.1.1 imread
* `imread`是opencv中最为常见的`图像读取`方式
```python 
    img = cv2.imread("image_path/test.jpg")
```
此时img中保存的为`nparray `多维数组。这意味着可以对其进行常见的矩阵操作。同时图片的格式也不止局限于`.jpg`,还支持`.tif`,`.bmp`,`.png`等多种格式(当输入四通道图片时则数组的通道数也是4)
###### 1.1.2.1.2 VideoCapture
* `VideoCapture`是opencv中最为常见的`视频读取`方式
```python
    video = cv2.VideoCapture("video_path/test.mp4")
```
此时video是一种特殊的类型，我们可以使用isOpened()函数来确认视频流是否能够被打开
```python
    flag = video.isOpened()
```
此时flag中保存的是video能否被打开的布尔值。

要获取视频流中具体的图像数据需要使用read函数
```python
    ret,frame = video.read()
```
其中`ret`是`video`获取的成功与否，`frame`则是该帧的图像数据，与`imread`中所获取的相同。

`VideoCapture`还有一种有趣的也是最为常用的用法
```python
    video = cv2.VideoCapture(0)
```
此时`VideoCapture`将会自动获取本机的摄像头进行拍摄。当然可以是1，2，3等等(前提是你有这么多的摄像头)。
需要注意的是，opencv中所有的函数都或多或少的存在大小写，而当格式不正确时，python便无法识别对应的函数
____
##### 1.1.2.2 输出
###### 1.1.2.2.1 imwrite
* `imwrite`是`opencv`中最为常见的`图像保存`方式
```python
    flag = cv2.imwrite("test.jpg",img,paras)
```    
> * `img`        : 需要保存的图像数组
> * `"test.jpg"` : 保存后的图像名称与格式
> * `flag`(选填) : 返回是否保存成功
> * `paras`(选填) : 不同的编码格式参数
>   - cv2.CV_IMWRITE_JPEG_QUALITY：设置 .jpeg/.jpg 格式的图片质量，取值为 0-100（默认值 95），数值越大则图片质量越高；
>   - cv2.CV_IMWRITE_WEBP_QUALITY：设置 .webp 格式的图片质量，取值为 0-100；
>   - cv2.CV_IMWRITE_PNG_COMPRESSION：设置 .png 格式图片的压缩比，取值为 0-9（默认值 3），数值越大则压缩比越大。

需要注意的是opencv并不支持在输出中使用中文(会出现乱码)，如果真的想使用中文可以使用`imencode`函数
___
###### 1.1.2.2.2 VideoWriter
* `VideoWriter`是`opencv`中最为常见的`视频保存`方式
```python
    VideoWriter(filename, fourcc, fps, frameSize[, isColor])
```
> filename : 保存的文件路径
> fourcc : 所选择的编码器
> fps   : 要保存视频的帧率
> frameSize : 待保存视频的画面尺寸
> isColor : 指示画面是否为彩色图像
注意此时**VideoWriter并不是一个能够返回值的函数**，而是一个**类**。需要**在声明类后，使用成员函数write来保存对应的帧**
```python
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('testwrite.avi',fourcc, 20.0, (1920,1080),True)
    ...
    out.write(frame)
    ...
    out.release()
```
此时`testwrite.avi`中保存的就是对应的视频了

###### 1.1.2.2.3 imshow
* `imshow`是`opencv`中最为常见的`图像显示`方式
```python
    cv2.imshow('img_name',img)
```
![Alt text](data/cv/imshow_1.png)
`img_name` 为显示窗口的标题， `img`为待显示的图像数据。
需要注意的是，如果出现同名的显示框，那么会出现覆盖的现象，当然，我们也可以使用通过这样的特性来显示视频。

##### 1.1.2.3 等待
* `waitKey` : 是`opencv`中最为常见的`等待`方式,常用于保存`imshow`函数所产生的显示窗口.
``` python
    cv2.imshow('img_name',img)
    cv2.waitKey(5)
```
以上操作会使得`img_name`显示窗口在`5毫秒后关闭`(当然，不用函数的情况下会马上关闭)。本质上是在插入了5毫秒的延时(所有窗口会在程序结束后默认关闭)。
还有一种特殊的用法
``` python
    cv2.imshow('img_name',img)
    cv2.waitKey(0)
```
此时`img_name`显示窗口将不会自动关闭，需要手动关闭

##### 1.1.2.4 销毁
* `destoryallwindows`: 是`opencv`中用于销毁显示窗口的函数。当调用该函数时将会销毁目前产生的所有显示窗口。
  
##### 1.1.2.5 

#### 1.2 实例
如果想快速实现某种操作可以在此处进行寻找
#### 1.2.1 显示一张图片(完整流程)
```python
import cv2
img  = cv2.imread("test.jpg") # 读取
cv2.imshow("img_name",img)  # 显示
cv2.waitKey(0)  # 等待
```

#### 1.2.2 显示摄像头获取的视频 (完整流程)
```python
import cv2
img  = cv2.VideoCapture(0)

while True :
    _,frame = img.read()
    print(frame)
    cv2.imshow("img_name",frame)
    if cv2.waitKey(1) &  0xff == ord("q"): # 在英文状态下，按下按s键 q 会关闭显示窗口    
        break
cv2.destoryallwindows()
```
当然直接写成`cv2.waitKey(1) == ord("q")`同样也是可以跑的,`waitKey`中的值决定了帧数的上限
#### 1.2.3 