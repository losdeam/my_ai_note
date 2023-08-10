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
## shell指令大全![Alt text](image.png)

### 关机&重启命令
* `shutdown -h now` : 立刻关机
* `shutdown -h 1`   : 一分钟后执行关机
* `shutdown -r now` : 立刻重启
* `shutdown -c` : 取消预设的关机/重启指令
* `halt`  : 立刻关机
* `reboot` :  立刻重启
* `sync` : 把内存的数据同步到磁盘
  
### 用户登录登出
* `logout` : 注销当前用户
* `su - 用户名` : 尝试切换至另一用户，有密码则需输入密码

### 用户管理
* `useradd 用户名` : 添加一个用户
* `passwd 用户名` : 给用户指定密码
注：当密码过于简单时会出现这样的报错信息，但是可以不用管，在第二次确认后一样能用!
![Alt text](data/Linux/error_2.png)
* `userdel 用户名` : 删除用户但保留其家目录
* `userdel -r 用户名` : 删除用户及其家目录
* `id 用户名` : 查询用户的信息
* `whoami/who am i` : 查看当前用户

### 用户组
&emsp;  将用户进行分类,并对同组用户进行统一的管理
* `groupadd 组名` : 新增组
* `groupdel 组名` : 删除组
* `useradd -g 用户组 用户名` : 在新增用户时直接加入组
* `usermod -g 用户组 用户名` : 修改用户的组

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
