del /S /Q house.json

cd hspider
del /S /Q house_urls.json
"C:\Python27\Scripts\scrapy.exe" crawl xiaoqu_spider -o house_urls.json
"C:\Python27\Scripts\scrapy.exe" crawl house_spider -o ..\house.json

cd ..
python json2html.py house.json view.html
pause
