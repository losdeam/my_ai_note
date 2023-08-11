# [笔记目录](目录.md)
# c++部分

&emsp;&emsp;本文档基于本人在使用[C++ Primer Plus(第6版)](https://detail.tmall.com/item.htm?ali_refid=a3_430673_1006:1110169018:N:1SEYC6BrFkWyec2+BRr6qNLV2e79Xy+FuLmx4IOJ/U4=:a4b7eae6733d3abccb1e46986f247992&ali_trackid=162_a4b7eae6733d3abccb1e46986f247992&id=40346852306&spm=a2e0b.20350158.31919782.1)中的学习总结而出。内容大都为书中的内容的。
* c++简单实例


```c++
#include <iostream>
int main()
{
    using namespace std;
    cout << "hello world"<< endl;
    return 0 ;
}
```

&emsp;&emsp;以上实例中可能会出现窗口迅速关闭无法观察到实际效果的情况，故在使用时通常在末尾加上`cin.get();`。即

```c++
#include <iostream>
int main()
{
    using namespace std;
    cout << "hello world"<< endl;
    cin.get();
    return 0 ;
}
```

## C++的规范
______

### C++的推荐代码规范
* 每条语句各占一行
* 每个函数都有一个开始花括号和一个结束花括号，这两个花括号各占一行
* 函数中的语句都相对于花括号进行缩进
* 与函数名称相关的圆括号周围没有空白
______

### C++的语句规范
* 在变量使用前必须进行说明（==防止在运行过程中由于错误拼写导致的结果错误==）
* 面向分号(==以分号为行的分割==,语句的结尾必须添加分号)
* 允许在程序的任何位置声明新的变量
* 允许在创建变量时对其进行赋值


``` c++
int a = 5 ;
```

______
### C++的函数规范
* 在定义时需要对函数的输出类型进行定义
* 在定义时需要对函数的输入参数类型进行定义

```c++
double sqrt(double);
```

* 在使用前必须保证
  * 在源代码文件中输入函数原型(声明函数)
  * 包含的头文件中定义了原型
* 通常将自定义函数防止在`main函数`之后进行定义，但在`main函数`前输入其函数原型


______

### C++的变量命名规范
> * 在名称中只能使用字母字符、数字和下划线(_)
> * 名称的第一个字符不能是数字
> * 区分大小写
> * 不能将C++关键字用作名称
______
## C++的数据类型

### 整型
* 赋值
```c++
int n_int = INT_MAX; //将int形式下的最大值赋值给n_int
int emus{7};         //将7赋值给emus
int rheads = {12}    //将12赋值给rheads
int rocs ={};        //将空值(0)赋值给rocs
int psychics{};      //将空值(0)赋值给psychics
```
* 知识
```c++
int  a= 'M';
    cout << a << endl; // 77
```
&emsp;&emsp;如果将字符直接赋值给整型的变量，整型变量中将会保存其ASCII编码值。

### 无符号类型
&emsp;&emsp;整型通过声明可以转换为其**无法储存负数值**的无符号变体，其优势在于可以增大变量能够存储的最大值。
```c++
unsigned short change_1;// unsigned short type
unsigned int change_2;  // unsigned int type
unsigned change_3;      // unsigned int type
unsigned long change_4; // unsigned long type
```
&emsp;&emsp;`unsigned`本身便是`unsigned int`的缩写

### 进制问题
&emsp;&emsp; C++采用前一（两）位来表示数字常量的基数
```c++
    cout << 42 << "(42 表示十进制的42)\n";      //42(42 表示十进制的42)    
    cout << 0x42 << "(0x42 表示十六进制的42)\n";  //66(0x42 表示十六进制的42)
    cout << 042 << "(042 表示八进制的42)\n";     //34(042 表示八进制的42) 
```
&emsp;&emsp;在默认情况下，cout以十进制的格式显示整数，不论整数在程序中是几进制的。
&emsp;&emsp;当然如果想显示不同进制的整数也是可以的。
```c++
    cout << dec << "(42 的十进制)"<< 42 << endl;          //(42 的十进制)42
    cout << hex  << "(42 的十六进制)"<< 42 << endl; //(42 的十六进制)2a  
    cout << 42 << endl ;                           //2a
    cout <<  oct  << "(42 的八进制)" << 42 << endl; //   
```
> `dec` : 将cout中整型显示形式改为十进制
> `hex` : 将cout中整型显示形式改为十六进制
> `oct` : 将cout中整型显示形式改为八进制
> 在下一次声明前将永久保留声明的显示形式

### char类型
* 赋值
```C++
char ch ;
```
#### 转义符

|字符名称    | 换行符   |水平制表符  |垂直制表符 |退格       |回车      |振铃    |反斜杠    |问号       |单引号   |双引号    |
|:------:   | :------: | :------:   |  :------:| :------:  | :------:| :------:| :------:|  :------:| ------:| :------:| 
|**c++代码**|`\n`        |  `\t`     |`\v`     |    ` \b `  |`\r`     |`\a`    |`\\ `    |`\?`    |`\'`      |`\"`     |
&emsp;&emsp; 转义符用于输入无法直接用键盘输入程序中的字符

### const限定符
&emsp;&emsp;就像c语言中的`#define`,`const限定符`用于声明无法在程序执行过程中被更改的常量
```c++
const int a= 10;
```

### 浮点数
______
## C++的语句

### cout
&emsp;&emsp;`cout`是c++中常见的**输出方式**,与`printf`不同的是,`cout`利用了重载的方式使得其能自由的输出数据而不需要用户自行对输出数据的类型进行定义。

```c++
//使用cout不需要知道输出数据的类型
    cout << "hello world"<< endl;  
    cout << 25 <<;
//使用printf需要知道输出数据的类型并自行进行定义
    printf("%s"," hello world");
    printf("%d",25);
```

______

### cin
&emsp;&emsp;`cin`是c++中常见的**输入方式**,与`cout`相同，`cin`也是智能对象，能自由的输出数据而不需要用户自行对输出数据的类型进行定义。

```c++
int a ;
char b ;
//使用cin不需要知道输入数据的类型
    cin >> a;  
    cin >> b;
//使用scanf需要知道输入数据的类型并自行进行定义
    scanf("%d",&a);
    scanf("%c",&b);
```

&emsp;&emsp;需要注意的是`>>`与`<<`同样也是数据流的流向，`>>` 表示输入由`cin`(输入流)流向已定义的变量`<<` 表示输出由已定义变量流向`cout`(输出流)
___
### sizeof
&emsp;&emsp;`sizeof`常用于获取对应数据类型所占的数据长度(单位为**字节**)

```c++
cout << "int is " << sizeof(int) << "bytes" <<endl; // int is 4 bytes
```
