# [笔记目录](目录.md)
# markdown部分
____
## 1.软件使用

本人是使用vscode进行文档的编写的，总体体验还不错
### 1.1 在vscode中使用markdown
![Alt text](data/markdown/vscode_1.png)
* 首先下载vscode中的扩展
    * ![Alt text](data/markdown/vscode_2.png)
    * ![Alt text](data/markdown/vscode_3.png)
* 然后创建一个.md后缀的文件
* 点击这玩意开始.md文件的预览
* ![Alt text](data/markdown/vscode_4.png)
* 齐活，开始markdown的学习吧
___
## 2.标题
`#` 在markdown中是标题的意思
`#` 越多表示标题的级别越高(==级别越低越接近主目录==)
![Alt text](data/markdown/title.png)
建议自己试试，多试试就懂了
> 注意`#`后需要填入一个空格才能使得`#`生效
____


## 3.页内文字跳转([参考博客](https://blog.csdn.net/qq_43660925/article/details/120731625?ops_request_misc=&request_id=&biz_id=102&utm_term=markdown%E5%AE%9E%E7%8E%B0%E6%96%87%E6%9C%AC%E5%86%85%E9%83%A8%E8%B7%B3%E8%BD%AC&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0-120731625.nonecase&spm=1018.2226.3001.4187))

### 3.1目录跳转法
```markdown
    [TOC]
```
[TOC]

### 3.2 铆钉法
使用万能的html来实现
[点击此处跳转至文档尾部](#1)
<h5 id="2"> 文档尾部回来</h5>
```html
 [点击此处跳转至文档尾部](#1)
 <h5 id="2"> 文档尾部回来</h5>
```
此处h`n`为字体大小。具体跳转是跟着id走的。当然id可以随意设置。
&emsp; &emsp;当然markdown的标题也是能当id用的
[点击此处去看看目录跳转法](#31目录跳转法)
```markdown
    [点击此处去看看目录跳转法](#31目录跳转法)
```


### 3.3 超链接
&emsp; &emsp;本质上其实与铆钉法相同。只是把id改为了文档目录或者网页的网址。
[点击此处回到主目录](目录.md)
[点击此处打开csdn](https://www.csdn.net/)
```html
[点击此处回到主目录](目录.md)
[点击此处打开csdn](https://www.csdn.net/)
```
___
## 4.字体
### 4.1 字体大小的修改
```html
<font size="1">1号字体</font>
<font size="2">2号字体</font>
<font size="3">3号字体</font>
<font size="4">4号字体</font>
<font size="5">5号字体</font>
```
<font size="1">1号字体</font>
<font size="2">2号字体</font>
<font size="3">3号字体</font>
<font size="4">4号字体</font>
<font size="5">5号字体</font>

___

### 4.2 字体颜色修改

____
### 4.3缩进
&nbsp;使用`&nbsp;`，可以缩进约1/4个汉字的大小
&ensp; 使用`&ensp;`，可以缩进约1/2个汉字的大小
&emsp; 使用`&emsp;`，可以缩进约1个汉字的大小
汉
_____
## 5.分隔
&emsp;使用`___`就可以产生以下效果
_____
当然多输一点效果也是一样的，不管是
`_____________`
还是
`__________________________________________`
都只会产生和上面一样的分隔线

____
## 6.表格
### 6.1 代码样式
```markdown
|  参数名   | 参数类型 | 
| :-------: | :------: | 
| a________ |   int    | 
```
### 6.2 展示情况
|  参数名   | 参数类型 | 
| :-------: | :------: |  
| a________        |   int    | 

&emsp;&emsp;表格的核心在于`| :------: | `,`| :------: | `的个数决定了表格的最大长度。`| :------: | `之上一行为标题，以`|`作为单元格间的分界线

_____

### 6.3 实现单元格的合并
&emsp; &emsp; markdown本身并不支持这样的操作，但是markdown支持HTML语言，而HTML可以实现这样的操作
```  html
<table>
    <tr>
        <td>第一列</td> 
        <td>第二列</td> 
   </tr>
    <tr>
        <td rowspan="2">这里是合并列</td>    
        <td >行二列二</td>  
    </tr>
    <tr>
        <td >行三列二</td>  
    </tr>
</table>
```
<table>
    <tr>
        <td>第一列</td> 
        <td>第二列</td> 
   </tr>
    <tr>
        <td rowspan="2">这里是合并列</td>    
        <td >行二列二</td>  
    </tr>
    <tr>
        <td >行三列二</td>  
    </tr>
</table>

&emsp; &emsp; 当然列的合并便可以实现标题的功能了

```  html
<table>
    <tr  align = "center">
        <td colspan="2">这里是合并列</td> 
   </tr>
    <tr>
        <td >行二列一</td>    
        <td >行二列二</td>  
    </tr>
    <tr>
        <td >行三列一</td>  
        <td >行三列二</td>  
    </tr>
</table>
```
<table>
    <tr  align = "center">
        <td colspan="2">这里是合并列</td> 
   </tr>
    <tr>
        <td >行二列一</td>    
        <td >行二列二</td>  
    </tr>
    <tr>
        <td >行三列一</td>  
        <td >行三列二</td>  
    </tr>
</table>


&emsp; &emsp; 记得加上`align`,`align`可以实现文本的`靠右`，`靠左`，`居中`,三种模式的切换。~~怎么变成Html学习笔记了~~
____

<h5 id="1">文档尾部</h5>

[返回](#2)