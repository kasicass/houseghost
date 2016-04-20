del /S /Q house.json
cd hspider
del /S /Q xiaoqu_urls.json
"C:\Python27\Scripts\scrapy.exe" crawl xiaoqu_spider -o house_urls.json
"C:\Python27\Scripts\scrapy.exe" crawl house_spider -o ..\house.json
pause
