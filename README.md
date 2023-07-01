# BionicReading

Generate HTML files of bionic reading results using Python.

[中文说明](./README_CN.md)

## Description

BionicReading is a Python tool that allows you to generate HTML files presenting bionic reading results. Bionic reading is a technique that aims to increase reading speed and comprehension by utilizing the natural motion of the eyes. This tool leverages Python and provides a simple command-line interface to generate HTML files with bionic reading results based on the input text or a text file.

Chinese is supported in this program.

## Screenshot

![bionic-reading-screenshot](https://cloud.icooper.cc/apps/sharingpath/PicSvr/PicMain/bionic-reading-screenshot.png)

## Basic Usage

To use BionicReading, you can follow these commands:

```bash
python main.py -t "This is an example sentence."
```

This command will generate a bionic reading result HTML file for the provided sentence.

```bash
python main.py -f ../test.txt
```

This command reads the content from the `test.txt` file and generates a bionic reading result HTML file.

```bash
python main.py -v -t "Including this parameter will output jieba's information."
```

Adding the `-v` parameter along with the text will enable the tool to output detailed information from the `jieba` library.

In all cases, the resulting HTML file, named `result.html`, will be generated in the current directory.

## Installation

To use BionicReading, follow these steps:

1. Clone the GitHub repository:

```bash
git clone https://github.com/your-username/BionicReading.git
```

2. Change into the project directory:

```bash
cd BionicReading
```

3. Install the required dependencies using conda:

```bash
conda create --name <myenv> --file package-list.txt
```

Use this command to create a conda environment to install the dependency.

If you prefer `pip`, just install `jieba` and `BeautifulSoup`.

4. Run the tool using the basic usage commands mentioned above.

## Requirements

BionicReading requires the following dependencies:

- Python 3.x
- `jieba`
- `BeautifulSoup`

## Contributing

Contributions to BionicReading are welcome! If you have any bug reports, feature requests, or suggestions, please open an issue on the GitHub repository. If you would like to contribute code, feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).