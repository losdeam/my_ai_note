#include<graphics.h> 
#include<conio.h>
#include <conio.h>
#include <stdlib.h>
#include <time.h>
#include <ctime>

#define SNAKE_NUM 500 
struct Snake
{
	int size;
	int dir;
	int speed;
	POINT coor[SNAKE_NUM];
}snake;

struct food
{
	int x;
	int y;
	bool flag;
	int r;
	DWORD color;  //存放地址或指针	 
}food;


enum DIR
{
	UP,
	DOWN,
	LEFT,
	RIGHT,
};

void gameinit()
{
	srand((unsigned int)time(NULL)); //使用无符号类型的ing来保存更大的time
	initgraph(640, 480);
	snake.size = 6;
	snake.speed = 8;
	snake.dir = RIGHT;
	for (int i = 0; i < snake.size; i++)
	{
		snake.coor[i].x = 40 - 10 * i;
		snake.coor[i].y = 10;
	}

	food.x = rand() % 640;
	food.y = rand() % 480;
	food.color = RGB(255, 0, 0);

	food.r = 10;
	food.flag = true;
}

void gamedraw()
{
	BeginBatchDraw();
	setbkcolor(RGB(31, 29, 66));
	cleardevice();

	//
	setfillcolor(RED);
	for (int i = 0; i < snake.size; i++)
	{
		solidcircle(snake.coor[i].x, snake.coor[i].y, 5); // 5为所画圆的半径
	}
	setfillcolor(food.color);
	if (food.flag)
	{
		solidcircle(food.x, food.y, food.r);
	}
	EndBatchDraw();
}

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
		case 's':
		case 'S':
		case 80:
			if (snake.dir != UP)
			{
				snake.dir = DOWN;
			}
			break;
		case 'a':
		case 'A':
		case 75:
			if (snake.dir != RIGHT)
			{
				snake.dir = LEFT;
			}
			break;
		case 'd':
		case 'D':
		case 77:
			if (snake.dir != LEFT)
			{
				snake.dir = RIGHT;
			}
			break;
		case ' ':
			while (1)
			{
				if (_getch() == ' ')
					break;
				else if (_getch() == 27)
					return 1;
			}
			break;
		}
	}
	return 0;
}

void eatfood()//吃食物
{
	if (food.flag && snake.coor[0].x >= food.x - food.r && snake.coor[0].x <= food.x + food.r && snake.coor[0].y >= food.y - food.r && snake.coor[0].y <= food.y + food.r)
	{
		food.flag = false;
		snake.size++;


	}
	if (!food.flag)//食物消失重新生成一个
	{
		food.x = rand() % 640;
		food.y = rand() % 480;
		food.color = RGB(255, 0,0);
		food.r = 10;
		food.flag = true;
	}
}

void snakemove() 
{
	for (int i = snake.size - 1; i > 0; i--)
	{
		snake.coor[i] = snake.coor[i - 1];
	}   // 每个关节均移动到下一关节上，头部独立判断
	switch (snake.dir)
	{
	case RIGHT:
		snake.coor[0].x += snake.speed;
		if (snake.coor[0].x > 640)
		{
			snake.coor[0].x = 0;
		}
		break;
	case UP:
		snake.coor[0].y -= snake.speed;
		if (snake.coor[0].y < 0)
		{
			snake.coor[0].y = 480;
		}
		break;
	case DOWN:
		snake.coor[0].y += snake.speed;
		if (snake.coor[0].y > 480)
		{
			snake.coor[0].y = 0;
		}
		break;
	case LEFT:
		snake.coor[0].x -= snake.speed;
		if (snake.coor[0].x < 0)
		{
			snake.coor[0].x = 640;
		}
		break;
	}
}

int main() {
	gameinit();
	gamedraw();

	while (true)
	{
		gamedraw();
		if (keycontrol()) break;
		snakemove();
		eatfood();
		Sleep(20);
		

	}
	return 0;
}