<p id= "head"></p>
[TOC]

# C++ 实战
## 1. 游戏
### 1.1 贪吃蛇
跟随csdn上的[【c语言】贪吃蛇](https://blog.csdn.net/yyqzjw/article/details/133136748)进行学习
#### 1.1.1 环境配置
使用到了graphics.h库，需要在[easyx官网](https://easyx.cn/)进行下载。
但是折磨的是easyx在下载后仅会自动为visual studio 进行配置而vscode不会，即需要手动进行配置。~~想python的第n天~~
考虑到时间关系，所以先转而使用visual studio 进行开发
#### 1.1.2 代码分析([源码](game/snake_1.cpp))
##### 1.1.2.1 角色的构造
```c++
struct Snake
{
    int size;
    int dir;
    int speed;
    POINT coor[SNAKE_NUM];
}snake;
```
使用结构体将角色的所有属性均锁定在自己身上，方便进行寻找和修改
##### 1.1.2.2 获取键盘输入
```c++

int  keycontrol()
{
    if (_kbhit()) //非阻塞地响应键盘输入时间
    {
        switch (_getch())
        {
        case 'w':
        case 'W':
        case 72:
            if (snake.dir != DOWN)
            {
                snake.dir = UP;
            }
            break;
        ...
        }
    }
    return 0;
}
```
`_kbhit()` : 用于检查当前是否有键盘输入，若有则返回一个非0值，否则返回0。
`_getch()` : 用于获取当前输入的具体值

教程其实非常简单，但是可以拓展一下试试手。
snake_2.cpp是本人添加了炸弹的新版本，碰到炸弹就会自动退出游戏
<hr>

[返回头部](#head)
[返回c++基础部分](../../c++.md/#head)