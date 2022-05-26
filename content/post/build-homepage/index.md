---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Steps to Build A Website with Hugo Academic and GitHub"
subtitle: ""
summary: ""
authors: 
  - admin
tags: 
  - 教程
date: 2022-05-26T12:38:39+08:00
lastmod: 2022-05-26T12:38:39+08:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

categories: []


# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

**写在前言**：今天花了一天的时间将个人学术主页初步搭建好了，趁着还有印象，赶紧整理一波，以便之后查阅。我使用的是HUGO的[Academic](https://github.com/wowchemy/starter-hugo-academic)主题，部署在GitHub上。当然，也可以根据这个主题里的官方文档，使用[Netlify](https://app.netlify.com/)快速部署站点（[保姆级使用教程](https://wowchemy.com/docs/getting-started/hugo-github-quickstart/)）,不过部署的站点后缀都是.netlify.app，我花了半天的时间看了通过[教程](https://www.bilibili.com/video/BV1Gz4y1f7Qj?share_source=copy_web)尝试了这个方案，并搭建了一个初步的[demo](https://cjerry.netlify.app/)，跟着里面的一步步来就成功搭建好了，还是比较顺利的。但在这之后个人还是想直接部署在GitHub上，就开始进行HUGO-Academic+GiuHub的部署，没承想，这其中一波三折，花了我大半天的时间，现在将基本流程和主要的坑整理出来。

# 环境配置

**需要在电脑上配置的环境是：**

1. [Git](https://blog.csdn.net/mukes/article/details/115693833)，安装后可以通过`git --version`在命令提示符/终端应用程序中运行来检查
2. [hugo_extended_0.95.0_Windows-64bit]()，特别注意：一定要选对版本！使用`hugo mod graph`来看版本是否安装对，不要出现Warn提示版本不匹配就行，不然之后都会有影响，我在这里卡了就好久orz

3. 官网文档中的[先决条件](https://wowchemy.com/docs/getting-started/install-hugo-extended/)步骤参考

# 操作

按照[官方文档](https://wowchemy.com/docs/hugo-tutorials/deployment/#github-pages)配置Giuhub页面操作

1. Github创建新的存储库

​	在个人的Github中创建一个新的存储库（通常缩写为*repos*），建议库的名称与GitHub账户同名，为：<USERNAME>.github.io，之后个人网站部署在https://<USERNAME>.github.io/上

2. 下载Hugo Academic模板至本地

```
git clone https://github.com/wowchemy/starter-hugo-academic.git My_Website
cd My_Website
git submodule update --init --recursive
```

3. 配置文件

​	在`config/_default/config.yaml`文件中，设置 Github 用户名`baseURL: 'https://<USERNAME>.github.io/'`部署到个人的github仓库中。`<USERNAME>`如果 Hugo 正在运行，则停止它，`public`如果目录存在，则删除该目录（通过键入`rm -r public/`）。

​	添加*<USERNAME>.github.io*存储库到名为*public*的文件夹中的子模块中，替换使用个人的 Github 用户名：

```
git submodule add -f -b master https://github.com/<USERNAME>/<USERNAME>.github.io.git public
```

4. 打包上传

​	将所有内容添加到本地 git 存储库并将其推送到 GitHub 上的远程存储库：

```
git add .
git commit -m "Initial commit"
git pull --rebase origin main
git push -u origin main
```

​	在运行上述命令时，系统可能会提示输入 Github 用户名和密码。

​	5. 上传发布网站代码

​	接下来，通过运行 Hugo 并将*公共*子模块上传到 GitHub 来**重新生成网站的 HTML 代码：**

```
hugo
cd public
git add .
git commit -m "Build website"
git push origin main
cd ..
```

​	Git 完成将打包好的网站上传到 Github 后，可以`https://<USERNAME>.github.io`在浏览器中打开所生成的新网站。

​	**Postscript**：上面这五步是官方给的，我按照这些一步步做之后总是出错，部署到GitHub上时总是显示时报错，搞了半天在各种错误快要让我放弃时，发现了一个-->[视频 ](https://www.bilibili.com/video/BV1k54y187nv)，加上改到最后报错为

```
Conversion error: Jekyll::Converters::Scss encountered an error while converting 'assets/css/style.scss':No such file or directory @ dir_chdir - /github/workspace/docs
```

​	我才知道原来是第五步这里少了一个命令，应该加一行命令语句：

```go
hugo --destination ./docs --buildDrafts --cleanDestinationDir
```

​	*我在之后又build有错，问题是* :

```
Error: fatal: remote error: upload-pack: not our ref 68d3700db3a223b3810db7e33635e99e9608143b
Error: fatal: Fetched in submodule path 'public', but it did not contain 68d3700db3a223b3810db7e33635e99e9608143b. Direct fetching of that commit failed.
Error: The process '/usr/bin/git' failed with exit code 128`
```

​	*后来清了一下`public`的缓存，命令`git rm -r --cached public/`然后再上传一遍就好了*

将项目文件生成静态网页至`./docs`，在对个人仓库<USERNAME>.github.io下进行Pages设置在`./docs`下

{{< figure src="1.png" id="wowchemy" >}}

​	网页便成功搭建好，并且可运行了！

{{< figure src="2.png" id="wowchemy" >}}

​	于是到了这里，利用Hugo Academic + GitHub 的个人学术主页配置就已经大功告成了，下面就是往里面增加内容了，具体的创作内容还是可以参考[官方文档](https://wowchemy.com/docs/content/)，不过我目前还没开始beautify我的主页，之后逐步推进丰富完善，如果有机会的话可能也会尝试用Vue来直接写而不基于Hugo框架了~

