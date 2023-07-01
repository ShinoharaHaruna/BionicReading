# BionicReading

使用Python生成仿生阅读结果的HTML文件。

[English README](./README.md)

## 描述

BionicReading是一个Python工具，可以生成展示仿生阅读结果的HTML文件。仿生阅读是一种利用眼睛的自然运动来提高阅读速度和理解力的技术。该工具利用Python提供简单的命令行界面，根据输入的文本或文本文件生成具有仿生阅读结果的HTML文件。

程序支持中文。

## 截图

![仿生阅读截图](https://cloud.icooper.cc/apps/sharingpath/PicSvr/PicMain/bionic-reading-screenshot.png)

## 基本用法

使用BionicReading，您可以按照以下命令操作：

```bash
python main.py -t "这是一个示例句子。"
```

该命令将为提供的句子生成一个仿生阅读结果的HTML文件。

```bash
python main.py -f ../test.txt
```

该命令从`test.txt`文件中读取内容，并生成一个仿生阅读结果的HTML文件。

```bash
python main.py -v -t "包含此参数将输出jieba库的详细信息。"
```

在文本后面添加`-v`参数将使工具输出`jieba`库的详细信息。

在所有情况下，生成的HTML文件名为`result.html`，将生成在当前目录。

## 安装

要使用BionicReading，请按照以下步骤操作：

1. 克隆GitHub仓库：

```bash
git clone https://github.com/your-username/BionicReading.git
```

2. 切换到项目目录：

```bash
cd BionicReading
```

3. 使用conda安装所需依赖：

```bash
conda create --name <myenv> --file package-list.txt
```

使用此命令创建一个conda环境以安装所需依赖。

如果您更喜欢使用`pip`，只需安装`jieba`和`BeautifulSoup`即可。

4. 使用上面提到的基本用法命令运行工具。

## 要求

BionicReading需要以下依赖项：

- Python 3.x
- `jieba`
- `BeautifulSoup`

## 贡献

欢迎为BionicReading做出贡献！如果您有任何bug报告、功能请求或建议，请在GitHub仓库上提出问题。如果您想贡献代码，请随时提交拉取请求。

## 许可证

本项目采用[MIT许可证](LICENSE)。