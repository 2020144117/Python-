# Git原理及基本使用   

## 一.  Git原理

#### 1. Git 分布式版本系统的原理

***Git分布式版本控制系统***（Distributed Version Control System)原理：客户端并不只提取最新版本的文件快照，而是把原始的代码仓库完整地镜像下来。这样，任何一处协同工作用的服务器发生故障，事后都可以用任何一个镜像出来的本地仓库恢复。每一次的提取操作，实际上都是一次对代码仓库的完整备份。  

#### 2. Git的分层结构

 git的工作总共分**四层**，其中三层是在自己本地也就是前面说的git仓库，包括了**工作目录**，**暂存区**和**本地仓库**，工作目录就是我们执行命令git init时所在的地方，也就是我们执行一切文件操作的地方，暂存区和本地仓库都是在.git目录，因为它们只是用来存数据的。**远程仓库在中心服务器**，也就是我们做好工作之后推送到远程仓库，或者从远程仓库更新下来最新代码到我们的git仓库。git所存储的都是一系列的文件快照

![](C:\Users\admin\Desktop\Git原理图片\图4.jpg)  

#### 3. Git基本底层原理

Git的核心是它的对象数据库，其中保存着git的对象，其中最重要的是<u>***blob***</u>、<u>***tree***</u>和<u>***commit***</u>对象，blob对象实现了对文件内容的记录，tree对象实现了对文件名、文件目录结构的记录，commit对象实现了对版本提交时间、版本作者、版本序列、版本说明等附加信息的记录。这三类对象，完美实现了git的基础功能：对版本状态的记录。

> ***blob数据对象记录内容，tree对象记录文件名和文件目录结构，commit对象记录版本的信息***              

#### 4. Git提交流程原理

***git add***添加文件到暂存区，并且创建数据对象添加到tree对象中且记录到git数据库      

Git根据某一时刻暂存区所表示的状态创建并记录一个对应的数对象（**一个暂存区对应一个tree对象**）       

**git commit **（作用）

> 把以上的tree对象添加到commit 对象中记录到git 数据库中。

 blob(文件)>tree(目录)>commit(汇总提交和提交信息)>Git数据库

运行 git add 和 git commit 命令时， Git 所做的实质工作是**将被改写的文件保存为数据对象，更新暂存区，记录树对象，最后创建一个指明了顶层树对象和父提交的提交对象**。 这三种主要的 Git 对象——数据对象、树对象、提交对象——最初均以单独文件的形式保存在 对象数据库。      

#### 5. Git的引用(分支)

git的引用类似于一个指针，它指向的是某一个***hash***键值。创建一个引用只需要把一个git对象的hash键值保存在以引用的名字命名的文件中。    

> 我们创建的新分支是一个独立的单元，**分支指针**和***commit***集是**一对一**的关系，只是commit集根据时间序列排列，分支的指针会自动指向最新的commit对象。     

#### 6. Git log原理        

列出所有分支log及所有父节点commit,查找**HEAD指针**对应的分支

​     

## 二. Git基本使用

![](C:\Users\admin\Desktop\Git原理图片\图5.png)

#### 1. 基本命令行指令

(1)名字和email地址

```java
git config --global user.name "Your Name"
git config --global user.email "481794113@qq.com"
```

(2)初始化仓库

```java
git init
```

(3)添加文件到仓库

步骤一：创建一个普通的文本文件

<img src="C:\Users\admin\Desktop\Git原理图片\.git.png" style="zoom:200%;" />

步骤二：使用git命令行将文本添加到版本库中

>第一步：用命令 告诉Git，把文件提交给本地仓库：

```java
git add .
```

> 第二步：用命令告诉Git 把文件提交到本地仓库

```java
git commit -m "备注"
```

(4)查看版本状态

```java
git status
```

(5)查看日志

```java
git log  
```

(6)查看差异

```java
git diff // 查看不同版本之间的文件差异
```

(7)版本回退

> 把当前版本回退到上一个版本，就可以使用`git reset`命令：

```java
git reset --hard HEAD^  # ^:上个版本  ^^：上上个版本 ^^^:上上上个版本
```

(8)管理修改

```java
第一次修改 -> git add -> 第二次修改 -> git commit
```

![](C:\Users\admin\Desktop\Git原理图片\图片.png)



**操作方式2：**

```java
第一次修改 -> git add -> 第二次修改 -> git add -> git commit
```

(9) 撤销修改

```
git checkout -- filename 

git checkout -- readme.txt
```

> 命令 `git checkout -- readme.txt` 意思就是，把 `readme.txt` 文件在工作区的修改全部撤销，这里有两种情况：

**一：`readme.txt` 自修改后还没有被放到暂存区(`git add`)，现在，撤销修改就回到和版本库一模一样的状态；**

**二：`readme.txt` 已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。**

(10)删除文件

```
git rm text.txt
```

> 删除完成后需要 `commit`

> 如果删除了想恢复,可以使用 `reset` 版本恢复

<img src="C:\Users\admin\Desktop\Git原理图片\图片2.png" style="zoom:150%;" />

(11)分支管理

**查看分支：**

```
git branch
```

**创建分支：**

```
git branch <name>
```

**切换分支**

```
git checkout <name>
```

**创建 + 切换分支**

```
git checkout -b <name>
```

**删除分支**

```
git branch -d <name>
```









