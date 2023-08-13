# [笔记目录](目录.md)
# Linux部分
在b站上跟随[【小白入门 通俗易懂】2021韩顺平 一周学会Linux](https://www.bilibili.com/video/BV1Sv411r7vd/?spm_id_from=333.337.search-card.all.click&vd_source=3b0e33a626cf5e45835cac5d91093908)开始进行Linux的学习

## 常见问题
* vmware在使用一段时间后就卡死
    * 可能是虚拟机的内存给小了或者处理器给少了
    * 可能是虚拟机在下载的时候出现损坏？
    * 直接换VirtualBox，问题基本都能解决
* 换VirtualBox没法用vmtools
    * 安装VirtualBox的增强功能，效果一样的
* 视频里远程连接的软件没法下
    * 用MobaXterm也能行，还能直接传本地文件
* 为什么我远程连接不上我的虚拟机
  *  可能是虚拟机ip地址无效(建议ping通了再试)
  *  ping通了还不行？还出现下面这样的报错？
    ![Alt text](data/Linux/error_1.png)
        * 你确定你的虚拟机开机了？

## 远程连接
1. 在虚拟机中连接上网
2. 通过`ifconfig`指令获取虚拟机的ip地址(不联网的话是拿不到ip地址的)
   ![Alt text](data/Linux/ifconfig.png)
3. 在本机中通过`ping`指令来确认ip地址的有效性![Alt text](data/Linux/ping.png)
4. 确认ip地址的有效性后通过MobaXterm的Session选项来实现SSH显示的远程连接。
 ![Alt text](data/Linux/MobaXterm_1.png)
5. 将获取到的虚拟机ip地址填入Remote host中即可实现
![Alt text](data/Linux/login.png)
6. 在登录后就可以正常使用虚拟机了(当然,只有命令行没有桌面)

## Vim
___
### 简介
&emsp; Vi是Linux和Unix系统上最基本的文本编辑器,而Vim可以看做是Vi的增强版本，可以主动以字体颜色辨别语法的正确性

### 使用指南
&emsp; Vim有三种常见的模式
1. 正常模式
&emsp;  打开文档后的默认模式，可以通过移动光标来实现定位，并通过指令进行复制与删除操作
2. 插入模式
&emsp;  通过输入任意一个字母进入，只有在插入模式下才能对文档输入字符。
3. 命令行模式
&emsp;  在插入模式下通过输入esc返回正常模式后再输入:进入，在此模式下可以通过指令来实现文档的保存与退出

### 常见指令
正常模式下
> * `yy` :拷贝当前行
> * `nyy`:拷贝当前行向下的`n`行 
> * `p` :在光标行的下一行进行粘贴拷贝内容
> * `dd` :删除当前行
> * `ndd`:删除当前行向下的`n`行 
> * 输入数字`n`后按下`shift+g`:跳转到当前文件的第`n`行
> * `G` :跳转到文档最末行
> * `gg`:跳转到文档最首行
> * `u` :撤销上一次输入
>
命令行模式下
>`:set nu`/`:set nonu`:设置/取消文件的行号
>`:wq` :保存文档并退出
>`:q` :正常退出(未修改文档时)
>`:q!` :不保存退出(不保存已有更改)

____
## shell指令大全

### 关机&重启命令
* `shutdown -h now` : 立刻关机
* `shutdown -h 1`   : 一分钟后执行关机
* `shutdown -r now` : 立刻重启
* `shutdown -c` : 取消预设的关机/重启指令
* `halt`  : 立刻关机
* `reboot` :  立刻重启
* `sync` : 把内存的数据同步到磁盘
___
### 用户登录登出
* `logout` : 注销当前用户
* `su - 用户名` : 尝试切换至另一用户，有密码则需输入密码
___
### 用户管理
* `useradd 用户名` : 添加一个用户
* `passwd 用户名` : 给用户指定密码
注：当密码过于简单时会出现这样的报错信息，但是可以不用管，在第二次确认后一样能用!
![Alt text](data/Linux/error_2.png)
* `userdel 用户名` : 删除用户但保留其家目录
* `userdel -r 用户名` : 删除用户及其家目录
* `id 用户名` : 查询用户的信息
* `whoami/who am i` : 查看当前用户
___
### 用户组
&emsp;  将用户进行分类,并对同组用户进行统一的管理
* `groupadd 组名` : 新增组
* `groupdel 组名` : 删除组
* `useradd -g 用户组 用户名` : 在新增用户时直接加入组
* `usermod -g 用户组 用户名` : 修改用户的组
___
#### 相关文件

* `/etc/passwd` : 用户的配置文件，记录用户的信息
  ![Alt text](data/Linux/userconfig_1.png)

内容含义 : `用户名:口令:用户标识号:组标识号:注释性描述:主目录:登录Shell`
______
* `/etc/shadow` : 用户口令的配置文件
  ![Alt text](data/Linux/userconfig_2.png)

内容含义 : `登录名:加密口令:最后一次修改时间:最小时间间隔:最大时间间隔:警告时间:不活动时间:失效时间:标识`
______
* `/etc/group` : 组的配置文件,记录Linux包含的组的信息
![Alt text](data/Linux/userconfig_3.png)

内容含义 :`组名:口令:组标识号:组内用户列表`
___
### 指定运行级别
&emsp; Linux中有着7个运行级别分别是
* `0` : 关机
*  `1` : 单用户[找回丢失密码]
![Alt text](data/Linux/init_1.png)
* `2` : 多用户状态没有网络服务
![Alt text](data/Linux/init_2.png)
* `3` : 多用户状态有网络服务
![Alt text](data/Linux/init_3.png)
* `4` : 安全模式
* `5` : 图形界面
![Alt text](data/Linux/init_5.png)
* `6` : 系统重启
  
使用`init`命令可以实现不同运行级别的切换(仅root用户可以)
______

### [root用户找回密码](https://blog.csdn.net/shenzhi0518/article/details/124091254?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522169173440016800215012329%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=169173440016800215012329&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-2-124091254-null-null.142^v92^chatsearchT3_1&utm_term=centos%208%20%E5%A6%82%E4%BD%95%E6%89%BE%E5%9B%9Eroot%E5%AF%86%E7%A0%81&spm=1018.2226.3001.4187)
(centos7和centos8的方式不太一样，下文是另一教程的总结与实践，原文请点击标题处)
1. 重启虚拟机，在出现以下页面时快速移动光标，防止自动登录
![Alt text](data/Linux/rootpw_1.png)

2. 界面保持后按下键盘`e`键进入以下界面
![Alt text](data/Linux/rootpw_2.png)

3. 找到`linux`开头`quiet`结尾的行尾输入`空格+rd.break`,然后键盘按`ctrl+x` 进入紧急救援模式
![Alt text](data/Linux/rootpw_3.png)
![Alt text](data/Linux/rootpw_4.png)

> * 输入`mount`将光标移动到末尾处可以看见`sysroot`是以只读模式挂载的，需要将其转换为读写模式重新挂载
  
4. 输入 `mount -o remount,rw /sysroot`重新挂载sysroot为读写模式
5. 输入 `chroot /sysroot/`将目录切换至`sysroot`中
> 由于中文语言在后续操作中会产生乱码，故要先改成英语模式。若已经是英语模式了，可以跳过
6. 输入 `LANG=en`
7. 输入 `touch /.autorelabel`来更新系统信息,否则可能会出现`passwd`更改并重启后依然无法登陆的情况
8. 输入`passwd`以进行新密码的设置
9. 输入`exit` 以退出sysroot 再输入`reboot`进行重启(重启时间可能会有点久)
____
### 帮助指令
* `man [命令或配置文件]` : 查看命令的帮助信息
* `help` : 获得shell内置命令的帮助信息
______
### 文件目录类
* `pwd` : 显示当前工作目录的绝对路径
* `ls [选项] [目录]`
  > 常用选项
  > * `-a` : 显示当前目录所有的文件和目录，包括隐藏的
  > * `-l` : 以列表的方式显示信息
* `cd [参数]` : 切换到指定目录
  > * `cd ~/cd` ： 回到当前用户的家目录
  > * `cd..`    : 回到当前目录的上一级目录
* `mkdir [选项] 要创建的目录` : 创建目录
  > * `-p` :  创建多级目录

* `rmdir [选项] 要删除的空目录` : 删除指定的空目录
* `touch 文件名称` :  在指定位置创建一个空文件
* `cp [选项] [文件/文件夹的目录]` : 拷贝文件到指定目录
  >* `-r` : 递归复制整个文件夹
* `rm [选项] 要删除的文件或目录` : 移除文件或目录
    > * `-r` : 递归删除整个文件夹
    > * `-f` : 强制删除不提示
> &emsp;在Linux中所有选项都可以一起使用,例如`-rf`便是递归删除所有文件夹并且不提示。巧的是Linux中万物皆文件，所以万恶的 `rm -rf /*` 的意思便是递归删除根目录下的所有文件。
&emsp;如果实在想试试的话建议先使用虚拟机的快照功能弄个备份，备份完了再开始大胆整花活
* `mv [文件1] [文件名2]` : 将文件1的文件名修改为文件名2
* `mv [目录1] [目录2]` : 将目录1中文件移动到目录2中
### 查看类
* `cat [选项] 要查看的文件` : 查看指定文件内容
  > * `-n` : 显示行号
* `more` : 按全屏幕的方式按页显示文本文件的内容，其中内置了若干快捷键
&emsp;

  *  快捷键大全
  
|  操作 | 功能说明 |
| :-------: | :------: |
| 空格键 | 下翻一页 |
| Enter | 下翻一行 |
| q | 退出 |
| Ctrl + F | 向下滚动一屏(效果==空格) |
| Ctrl + B | 返回上一页 |
| = | 输出当前行的行号 |
|  :f   | 输出文件名和当前行的行号 | 

![Alt text](data/Linux/more.png)
* `less` : 按分屏的方式按页显示文本文件的内容，其中内置了若干快捷键
&emsp;

  *  快捷键大全
  
|  操作 | 功能说明 |
| :-------: | :------: |
| 空格键 | 下翻一页 |
| [pagedown] | 下翻一页 |
| [pageup] | 返回上一页 |
| /字串 | 向下查询字串 |
| Ctrl + B | 返回上一页 |
| = | 输出当前行的行号 |
|  :f   | 输出文件名和当前行的行号 | 

![Alt text](data/Linux/less.png)

#### 分屏和全屏的区别
&emsp;&emsp;全屏查看是将**文件全部读取完成后再进行显示**而分屏查看是**根据显示的需要逐步加载内容**。分屏查看在显示大型文件方面具有较高的效率。

* `echo [选项] [输出内容]` : 输出内容到控制台
* 