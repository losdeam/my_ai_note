# [笔记目录](目录.md)
# cv部分
____
## 1.经典库

### 1.1 opencv
#### 1.1.1 简介
#### 1.1.2 常用函数
##### 1.1.2.1 读取
* `imread`是opencv中最为常见的`图像读取`方式
```python 
    img = cv2.imread("image_path/test.jpg")
```
此时img中保存的为`nparray `多维数组。这意味着可以对其进行常见的矩阵操作。同时图片的格式也不止局限于`.jpg`,还支持`.tif`,`.bmp`,`.png`等多种格式(当输入四通道图片时则数组的通道数也是4)

* `VideoCapture`是opencv中最为常见的`视频读取`方式