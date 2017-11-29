import json
import re
#kadai20 extract document
def doc_extr(doc_dest):
    file = open(doc_dest)
    doc_lines = file.readlines()
    doc_article = ''

    for line in doc_lines:
        article_extr = json.loads(line)
        if (re.search('イギリス', article_extr['text'])):
            doc_article += article_extr['text']

    file.close()
    return doc_article

#kadai21 extract category line
def categ_extr_line(doc_artical):
    lines=doc_artical.split("\n")
    categ_line = []
    for line in lines:
        if ("Category" in line) or ("カテゴリ名" in line):
            categ_line.append(line)
    return categ_line

#kadai22 extract category name
def categ_extr_name(doc_artical):
    import re
    categ_name = []
    categ_line = categ_extr_line(doc_artical)
    for line in categ_line:
        categ_line = re.search('\[\[Category:(.*?)\]\]', line)
        if categ_line:
            categ_name.append(categ_line.group(1))
            print(categ_line.group(1))
    return categ_name

#kadai23 section level
def sect_level(doc_artical):
    import re
    sect = {}
    lines = doc_artical.split('\n')
    for line in lines:
        sect_line = re.search('^(=+)(.*?)(=+)', line)
        if sect_line:
            sect[sect_line.group(2)] = len(sect_line.group(1))-1
            print(sect_line.group(),' ',len(sect_line.group(1))-1)
    return sect

#kadai24 media files extract
def file_dir(doc_artical):
    import re
    sect = {}
    lines = doc_artical.split('\n')
    for line in lines:
        sect_line = re.search('(File|ファイル):(.*?)\|', line)
        if sect_line:
            print(sect_line.group())
    return sect

#kadai25 template
def temp_extr(doc_artical):
    temp_dict = {}
    lines = re.split("\n[\|}]", doc_artical)

    for line in lines:
        temp_line = re.search("^(.*?)\s=\s(.*)", line, re.S)
        if temp_line:
            temp_dict[temp_line.group(1)] = temp_line.group(2)

    for k, v in sorted(temp_dict.items(), key=lambda x: x[1]):
        print(k,v)

#kadai26
def emph_markup_remov(doc_artical):
    temp_dict = {}
    lines = re.split("\n[\|}]", doc_artical)

    for line in lines:
        temp_line = re.search("^(.*?)\s=\s(.*)", line, re.S)
        if temp_line:
            temp_dict[temp_line.group(1)] = re.sub("'{2,5}", "",temp_line.group(2))

    for k, v in sorted(temp_dict.items(), key=lambda x: x[1]):
        print(k,v)

#kadai27
def remov_markup(str):
    str = re.sub("'{2,5}", "", str)
    str = re.sub("\[{2}([^|\]]+?\|)*(.+?)\]{2}", "\2", str)
    return str
def link_markup_remov(doc_artical):
    temp_dict = {}
    lines = doc_artical.split("\n")

    for line in lines:
        cate_line = re.search("^\|(.*?)\s=\s(.*)", line)
        if cate_line:
            temp_dict[cate_line.group(1)] = remov_markup(cate_line.group(2))

    for k, v in sorted(temp_dict.items(), key=lambda x: x[0]):
        print(k, v)

#kadai28
def remove_markup(str):
    str = re.sub("'{2,5}", "", str)
    str = re.sub("\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2", str)
    str = re.sub("\{{2}.+?\|.+?\|(.+?)\}{2}", r"\1 ", str)
    str = re.sub("<.*?>","", str)
    str = re.sub("\[.*?\]", "", str)
    return str
def temp_markup_remov(doc_artical):
    temp_dict = {}
    lines = doc_artical.split("\n")

    for line in lines:
        cate_line = re.search("^\|(.*?)\s=\s(.*)", line)
        if cate_line:
            temp_dict[cate_line.group(1)] = remove_markup(cate_line.group(2))

    for k, v in sorted(temp_dict.items(), key=lambda x: x[0]):
        print(k, v)

#kadai29
import requests
def json_search(json_data):
    ret_dict = {}
    for k, v in json_data.items():
        if isinstance(v, list):
            for e in v:
                ret_dict.update(json_search(e))
        elif isinstance(v, dict):
            ret_dict.update(json_search(v))
        else:
            ret_dict[k] = v
    return ret_dict

def kadai29(doc_artical):
    temp_dict = {}
    lines = doc_artical.split("\n")

    for line in lines:
        temp_line = re.search("^\|(.*?)\s=\s(.*)", line)
        if temp_line is not None:
            temp_dict[temp_line.group(1)] = remove_markup(temp_line.group(2))

    url = "https://en.wikipedia.org/w/api.php"
    payload = {"action": "query",
               "titles": "File:{}".format(temp_dict["国旗画像"]),
               "prop": "imageinfo",
               "format": "json",
               "iiprop": "url"}

    json_data = requests.get(url, params=payload).json()
    print(json_search(json_data)["url"])


def main():
    doc_dest = '/home/viet/Documents/jawiki-country.json'
    doc_artical = doc_extr(doc_dest)
    kadai29(doc_artical)

if __name__ == '__main__':
    main()

