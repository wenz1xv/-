写的一些简单的爬虫

### 1、pubmed 关键词搜索及链接爬取
[get_pubmed.py](https://raw.githubusercontent.com/wenz1xv/easy_crawler/main/get_pubmed.py)

依赖库：requests beautifulsoup4

输入：搜索关键词（同目录下list.txt读入）

输出：搜索结果链接与文章名

*我也不知道这有什么用，同学需要这个就顺便写了

### 2、 简单爬取淘宝商品链接

[get_taobao](https://raw.githubusercontent.com/wenz1xv/easy_crawler/main/get_taobao.py)

依赖库：requests re xlwt

输入：console 输入商品名和cookies

输出：excel 或直接打印在console

详见[简书链接](https://www.jianshu.com/p/c6a986861e8c)

*19年写的了，当时不太会，可能写的有点糟，尽量修改好看点

### 3、 简单爬取1688商品数据

[get_1688](https://raw.githubusercontent.com/wenz1xv/easy_crawler/main/get_1688.py)

依赖库: urllib xlwt beautifulsoup4 requests

输入：console 输入商品名

输出：excel 或直接打印在console

详见[简书链接](https://www.jianshu.com/p/b4fb9cf18f7f)

*同上

### 4、简单爬取book118文档，图片形式保存

[get_book118](https://raw.githubusercontent.com/wenz1xv/easy_crawler/main/get_book118.py)

详见[简书链接](https://www.jianshu.com/p/8012edb46153)

依赖库： requests json re sys beautifulsoup4 time os

输入：文档链接

输出：一个文件夹的图片

*这个可能bug有点多，太久远了啊
