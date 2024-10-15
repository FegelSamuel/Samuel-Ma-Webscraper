# C Documentation Crawler
```bash
cd CDocumentationCrawlers/CDocumentationCrawlers/spiders
```
Geeks For Geeks
```bash
scrapy runspider g4g.py
```
w3schools
```bash
scrapy runspider w3.py
```
cppreference
```bash
scrapy runspider ref.py
```
Three Crawlers going through GeeksForGeeks, W3Schools, and cppreference and storing C/C++ Article's `title` and `url` in a generated `articles.json` file. 
# Disclaimer
I was not able to get GeeksForGeeks to show me C Documentation only, so it will show C++ documentation.