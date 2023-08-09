# [笔记目录](目录.md)
# c++部分

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
以上实例中可能会出现窗口迅速关闭无法观察到实际效果的情况，故在使用时通常在末尾加上`cin.get();`。即
```c++
#include <iostream>
int main()
{
    using namespace std;
    cout << "hello world"<< endl;
    cin.get();
    cin.get();
    return 0 ;
}
```
