# xhsCrawler
## 环境安装

<kbd>Step1:</kbd> 安装谷歌浏览器并下载ChromeDriver

```
https://googlechromelabs.github.io/chrome-for-testing/
```

<kbd>Step2:</kbd> 安装依赖库
```bash
pip install -r requirements.txt
```
## 使用方法

1. 首先需要运行`login.py`文件进行扫码登录
- 请注意，登录后需要手动扫码确认登录，登录成功后程序会自动退出。
- 登录成功后，程序会成功用于保存登录状态。

```bash
python login.py
```


2. 然后运行`main.py`文件进行关键词帖子文章检索和收集

```bash
python main.py
```

## 提示：运行过程中不要打开Chrome和Excel，否则出现如下报错：
![Uploading image.png…]()
