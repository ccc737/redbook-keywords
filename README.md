# 小红书关键词帖子文章检索和收集爬虫程序


## 程序介绍
本程序使用`selenium`自动化测试框架结合`ChromeDriver`浏览器驱动，模拟用户登录小红书网站，根据关键词搜索帖子，并收集帖子中的文章链接，保存到本地文件中。
主要用于自动化数据抓取、解析和管理，通过模块化的日志系统跟踪项目的执行流程。
此项目采用了多个流行的Python库，使得项目在数据抓取和自动化任务中表现出色，适用于爬虫、数据处理和自动化任务场景。

## 项目优点
- 高效自动化：通过selenium和requests实现自动化的网页登录、数据抓取及解析，大大提升了操作的效率。
- 模块化设计：各功能模块独立，如LOGGER.py管理日志、login.py负责登录，模块之间松耦合，便于后续维护和扩展。
- 易于配置：依赖文件requirements.txt包含了所有需要的库，且支持国内源安装，用户只需一条命令即可完成环境搭建。
- 本地化日志管理：LOGGER.py模块提供丰富的日志记录，便于在不同环境中调试和跟踪项目运行状态。

## 程序功能
1. 模拟用户登录小红书网站
2. 根据关键词搜索帖子
3. 收集帖子中的文章数据
4. 保存文章信息到本地文件中

## 程序模块
```
├── LOGGER.py            # 日志模块
├── login.py             # 登录相关模块
├── main.py              # 主程序入口
├── README.md            # 项目文档
├── requirements.txt     # 依赖库
```

## 环境安装

<kbd>Step1:</kbd> 安装谷歌浏览器并下载ChromeDriver

```
https://googlechromelabs.github.io/chrome-for-testing/
```

<kbd>Step2:</kbd> 安装依赖库
```bash
pip install -r requirements.txt
```

<kbd>Tips</kbd> 推荐使用Python3.10版本

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

# 提示：软件运行过程中实时向目标Excel中写入数据，请不要打开Excel防止无法写入
