import os
import sys
import math
import jieba
import logging
from bs4 import BeautifulSoup


def argText():
    arguments = sys.argv

    # Verbose mode
    if "-v" not in arguments:
        jieba_logger = logging.getLogger("jieba")
        jieba_logger.setLevel(logging.CRITICAL)

    # Find argument `-t` in the arguments
    if "-t" in arguments:
        # print("Argument -t found")
        text = arguments[arguments.index("-t") + 1]
        # print("Argument -t value: ", text)

    # Find argument `-f` in the arguments
    if "-f" in arguments:
        # print("Argument -f found")
        file = arguments[arguments.index("-f") + 1]
        # print("Argument -f value: ", file)
        with open(file, "r") as f:
            text = f.read()

    return text


def generate_div(word, mode):
    if mode == "b":
        s = '<div class="text black">'
    else:
        s = '<div class="text gray">'
    s = s + word + "</div>"
    soup = BeautifulSoup(s, "html.parser")
    div = soup.find("div")
    if div and div.text.strip() == "":
        return ""
    else:
        return s


def generate(seg_list):
    with open(os.path.join("template", "template.html"), "r") as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    target_div = soup.find("div", id="context")
    # print("target_div: ", target_div)

    div_str = "<div id=\"context\" class=\"container\">"
    for word in seg_list:
        if word in [" ", "\t"]:
            div_str += generate_div(word, "b")
        elif word == "\n":
            div_str += "<div class=\"line-break\"></div>"
        else:
            mid_index = math.ceil(len(word) / 2)
            div_str += generate_div("".join(word[:mid_index]), "b")
            div_str += generate_div("".join(word[mid_index:]), "g")
    div_str += "</div>"


    target_div.replace_with(BeautifulSoup(div_str, "html.parser"))
    neo_content = soup.prettify()
    with open("result.html", "w") as file:
        file.write(neo_content)
    print("Succeeded! Check the `result.html` in the current directory.")


def main():
    text = argText()
    seg_list = jieba.cut(text, cut_all=False)
    generate(seg_list)


if __name__ == "__main__":
    main()
