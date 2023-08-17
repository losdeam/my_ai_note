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
___
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
___
### const限定符
&emsp;&emsp;就像c语言中的`#define`,`const限定符`用于声明无法在程序执行过程中被更改的常量
```c++
const int a= 10;
```
___
### 浮点数
&emsp;&emsp;c++可以用两种不同的方式来书写浮点数
1. 小数点表示法
```
12.34
0.00023
8.0
```
2. E表示法

```
2.52e+4  // 25200 = 2.52 * 10^4
8.33E-4  //0.000833 = 8.33 * 10^-4
7E5      // 700000 = 7* 10^ 5
```
#### 浮点类型
1. `float`       
2. `double`         
3. `long double`
   
&emsp;&emsp;当我们使用`cout`函数进行输出时过于智能的`cout`会删除结尾的零,如果我们想要保留结尾的零或者想将显示的形式转换为`E表示法`时我们可以使用`cout.setf()`。`.`表示`setf`是`cout`对象的成员函数,只有通过对象才能进行调用。

#### setf()函数
&emsp;&emsp;通过对于参数的设置来调节cout函数的显示模式
```c++
cout.setf(ios_base::oct,ios_base::basefield); //将后续cout中整型的默认显示方式修改为8进制
cout << 8 << endl; //10
```
<table>
    <tr>
        <td>第二个参数</td> 
        <td>第一个参数</td> 
        <td> 含义 </td>
   </tr>
    <tr>
        <td rowspan="3">ios_base::basefield</td>    
        <td >ios_base::dec</td>  
        <td >使用10进制</td>  
    </tr>
    <tr>
        <td >ios_base::oct</td>  
        <td >使用8进制</td> 
    </tr>
    <tr>
        <td >ios_base::hex</td>  
        <td >使用16进制</td> 
    </tr>
     <tr>
        <td rowspan="2">ios_base::floatfield</td>    
        <td >ios_base::fixed</td>  
        <td >使用定点计数法(即一般计数法)</td>  
    </tr>
    <tr>
        <td >ios_base::scientific</td>  
        <td >使用科学计数法</td> 
    </tr>
     <tr>
        <td rowspan="3">ios_base::adjustfield</td>    
        <td >ios_base::left</td>  
        <td >左对齐</td>  
    </tr>
    <tr>
        <td >ios_base::right</td>  
        <td >右对齐</td> 
    </tr>
    <tr>
        <td >ios_base::internal</td>  
        <td >符合或前缀左对齐，值右对齐</td> 
    </tr>
</table>

____

### C++的类型转换
&emsp;&emsp; **C++** 会自动执行很多类型转换：

* 将一种算数类型的值赋给另一种算数类型的变量时，c++将对值进行转换
* 表达式中包含不同的类型时，C++将对值进行转换
* 将参数传递给函数时，C++将对值进行转换
  
  <table>
    <tr  align = "center">
        <td colspan="2">潜在的数值转换问题</td> 
   </tr>
    <tr>
        <td >转换</td>    
        <td >潜在的问题</td>  
    </tr>
    <tr>
        <td >将较大的浮点类型转换为较小的浮点类型</td>  
        <td >有效位数降低,值可能超出目标类型的取值范围,在这种情况下，结果是不确定的</td>  
    </tr>
        <tr>
        <td >将浮点类型转换为整型</td>  
        <td >小数部分丢失，原来的值可能超出目标类型的取值范围，在这种下，结果是不确定的</td>  
    </tr>
        <tr>
        <td >将较大的整数转换为较小的整数</td>  
        <td >原来的值可能超出目标类型的取值范围,通常只复制右边的字节</td>  
    </tr>
</table>

> `0`赋值给`bool`变量时，将被转换为`false`；而非零值将被转换为`true`

* 强制类型转换 
  * （类型） 变量
  *  类型   (变量)

______
## C++运算符
* `+` : 加法运算
* `-` : 减法运算
* `*` : 乘法运算
* `/` : 除法运算，除数与被除数均为整数时将会返回商的整数部分，小数部分将被忽略
* `%` ：取模运算，获取除后余数，用于浮点数时会出现报错
![Alt text](data/C++/%.png)
___
## 复合类型

### 数组
#### 声明
&emsp;&emsp;声明**数组**时应满足以下三点：
    1. 存储在每个元素中的值的类型；
    2.  数组名；
    3.  数组中的元素名
```c++
    typename arrayName[arrySize] ; 
```
#### 说明
- c++的数组从0开始编号
- c++的数组可以通过下标来直接获取数组中的对于值
- 当出现下标越界的情况时，c++将会出现报错

#### 初始化
&emsp;&emsp;有且仅有定义数组的时候可以对数组进行初始化
```c++
    int cards[4] = {3,6,8,10};
    int hand[4];
```
&emsp;&emsp;但是可以在运行过程中通过下标来对数组中的元素进行赋值
```c++
    cards[3] = 5;
```
&emsp;&emsp;在初始化数组时还可以留空，即提供少于元组的元素数目的值。未赋值部分将默认为0(字符情况下为空值)
```c++
    int cards[4] = {3,6};
```
&emsp;&emsp;也可以不设置元素数目，让c++编译器自动计算提供的元素的个数以作为元组的元素数目
```c++
    int cards[] = {3,6,8,10};
```
> 1. 初始化数组时，可省略等号
```c++
    int cards[4]{3,6,8,10};
```
> 2. 可不在大括号中包含任何东西，将所有元素设置为空值
```c++
    int cards[4]{};
```
> 3. 列表初始化禁止缩窄转换(内存占用多的类型转换为内存占用少的类型)
```c++
    long plifs[] = {25,92,3.0};   // 报错
```
____
### 字符串
&emsp;&emsp;存储在内存的连续字节中的一系列字符。

#### 初始化
1. **c-风格字符串**
   
&emsp;&emsp;必须以空字符`\0`结尾。
```c++
    char dog[8] = {'b','y','e','y','e','y','e','\0'};
```
2. **使用引号**
```c++
    char bird[11] = "Mr. Cheeps";
    char fish[] = "Bubbles";
```
&emsp;&emsp;使用键盘进行字符串的输入或者是使用引号进行定义时结尾的空字符将会被**自动添加**。同时需要注意的是空**字符同样也会占据数组的一个位置**，在确认最小数组时请确保不会产生越界现象。
#### 拼接字符串
&emsp;&emsp;任何两个由**空白**(**空格**、**制表符**和**换行符**)分隔的字符串常量都将自动拼接成一个。所以以下代码有着相同的输出
```c++
    cout << "aaaaaa" "bbbb\n";
    cout << "aaaaaabbbb\n";
    cout <<"aaaa"
    "aabbbb\n";
```
#### 相关函数
##### strlen()
&emsp;&emsp;保存于头文件`<cstring>`中,功能为返回存储在数组中的字符串的长度，而不是数组本身的长度且计算长度时不计算空字符。
```c++
    char lis[] = {'a','b','\0','a','b','c','\0'};
    cout << strlen(lis)<<endl;  // 2 
    cout << sizeof(lis)<<endl;  // 7
```

##### cin的缺陷
&emsp;&emsp;在输入字符串时`cin`函数以**空白**(**空格**、**制表符**和**换行符**)来确认字符串的结束位置。所以在输入的过程中无法输入空格(输入空格后会将后续内容存储至下一次输入中或者丢弃)。

```c++
    cin >> num ;  //输入abc def
    cout << num;  //输出abc
```

##### getline()
&emsp;&emsp;保存于头文件`<iostream>`中,通过回车键输入的换行符来确认输入结尾。该函数有两个参数，第一个参数用于存储输入行的数组的名称，第二个参数是要读取的字符数。超过读取数或是遇到换行符时停止读取。

```c++
    cin.getline(name,20); //将该行的输入读取入name数组中，最大字符获取量为20
```
##### get()
&emsp;&emsp;保存于头文件`<iostream>`中,与`getline`相似但是不再读取并丢弃换行符，而是将其留在输入队列中。
```c++
    cin.get(name,20); //将该行的输入读取入name数组中，最大字符获取量为20
```
&emsp;&emsp;但是有个问题就是当遇到换行符时，get函数依然不会跳出。幸运的是get有个好用的变体get()。它可以获得下一行字符(即使是换行符)
```c++
    cin.get(name,20);
    cin.get();
```
&emsp;&emsp;还有一种好用的方法就是把两者直接进行结合
```c++
    cin.get(name,20).get();
```

____

### String 
&emsp;&emsp;C++添加了`String`类使得对字符串的操作能够更加容易。要使用`String`类时，必须先声明头文件`<string>`,并且使用名称空间std。其特点在于可以**声明为简单变量而非数组**。
```c++
    string str1 ;
    string str2 = "test";
```
___
### 结构
&emsp;&emsp;类似于`python`中的类，其中关键字`struct`声明了后续为一个名字为`test`的结构。`test`结构拥有`name`和`num`两个结构成员.
```c++
    struct test{
        char name[20];
        int num ;
    };
    test name {"losdeam",10}; 
    test name_1 {};
```
> 注：不允许缩窄转换
___
### 共用体
&emsp;&emsp;共用体在声明时会**按照最大的成员进行内存的分配**，而在使用时可以自由的使用所有成员类型，但是**同时仅能使用一种**(使用**同一物理地址**)。
```c++
    union one4all
    {
        int int_val;
        long long_val;
        double double_val;
    };
    one4all pail;
    pail.int_val = 15; //pail中保存int_val
    pail.double_val = 1.38; //pail.int_val被pail.double_val覆盖

```
___
### 枚举
```c++
    enum spectrum {red,orange,yellow,green,blue};
```
这条语句完成以下两项工作:
* `spectrum`被称为枚举
* `red`,`orange`,`yellow`等作为符号常量,对应整数值为0~4。这些常量叫做`枚举量`
  
当后续使用red,orange,yellow等时将会直接被转换为整数值。当然直接赋值也是可以的。
```c++
    enum spectrum {red=1,orange=8,yellow=5,green=7,blue=3};
    enum spectrum {red=1,orange,yellow,green=7,blue=3};
```
____
## 指针
&emsp;&emsp;指针是c++中极为重要(~~折磨~~)的一种变量类型。由于储存值的地址而非值本身。其中&用于直接获取变量的地址，*应用于指针以获取指针处保存的值
```c++
    int num = 6;
    int * address ;
    address = &num; // address中保存num的地址值
    cout << *address ; //输出num值(6)
```

____
## C++的语句

### cout
&emsp;&emsp;保存于头文件`<iostream>`中,`cout`是c++中常见的**输出方式**,与`printf`不同的是,`cout`利用了重载的方式使得其能自由的输出数据而不需要用户自行对输出数据的类型进行定义。

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
&emsp;&emsp;保存于头文件`<iostream>`中,`cin`是c++中常见的**输入方式**,与`cout`相同，`cin`也是智能对象，能自由的输出数据而不需要用户自行对输出数据的类型进行定义。

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
&emsp;&emsp;保存于头文件`<iostream>`中,`sizeof`常用于获取对应数据类型所占的数据长度(单位为**字节**)

```c++
cout << "int is " << sizeof(int) << "bytes" <<endl; // int is 4 bytes
```
