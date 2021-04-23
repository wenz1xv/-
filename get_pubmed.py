# -*- coding: utf-8 -*
# 请先在命令行运行：pip install requests beautifulsoup4
# 输入文件请在同目录下新建list.txt
# 多个关键词请用+连接(例如 ISG15+mRNA+metabolite)
# 输出文件为同目录下的output.txt
import requests
from bs4 import BeautifulSoup

def get_pubmed(keyword, page, file):
    """
    参数:
        keyword - 搜索的关键词
        page - 搜索的页数
        file - 输出文件
    """
    url = 'https://pubmed.ncbi.nlm.nih.gov'
    rep = requests.get(f'{url}/?term={keyword}&page={page}')
    html = BeautifulSoup(rep.text, features='html.parser')
    li = html.find_all(class_='docsum-title')
    if len(li):
        for index, item in enumerate(li):
            file.write(f"{index+1+(page-1)*10}\t{url}{item['href']}\t{item.text.strip()}\n")
        print(f'get {keyword} page {page} success')
        return True
    return False

def main(inp_file, out_file, pages, mode):
    """
    参数:
        inp_file - 输入文件
        out_file - 输出文件
        pages - 搜索页数
        mode - 输出模式 a/w 追加/覆写
    """
    print(f'read file {inp_file}, save result in {out_file}')
    outfile = open(out_file, mode)
    with open(inp_file, 'r') as file:
        keyword= file.readline().strip()
        while keyword:
            outfile.write(f'search word: {keyword}\n')
            for page in range(pages):
                if not get_pubmed(keyword, page+1, outfile):
                    if page==0:
                        outfile.write(f'\t{keyword} has no result find')
                        print(f'\t{keyword} has no result find')
                    break
            keyword = file.readline().strip()
    outfile.close()
    print('done')

main('list.txt', 'output.txt', 5, 'w')
