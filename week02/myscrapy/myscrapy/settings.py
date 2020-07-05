# Scrapy settings for myscrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'myscrapy'

SPIDER_MODULES = ['myscrapy.spiders']
NEWSPIDER_MODULE = 'myscrapy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'myscrapy (+http://www.yourdomain.com)'
USER_AGENT = 'myscrapy (+https://maoyan.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'Host': 'maoyan.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cookie': '__mta=212246443.1593139147051.1593139170518.1593139177936.3; uuid_n_v=v1; uuid=339DC6F0B75611EA842AD7B3BE0152F24442D90C88D24A6B8C49236F422F0058; mojo-uuid=177e9a686c4a85cf1977e4cfdfe86c4d; _lxsdk_cuid=172ee7e2f73c8-0fd3491e049683-f7d1d38-144000-172ee7e2f73c8; _lxsdk=339DC6F0B75611EA842AD7B3BE0152F24442D90C88D24A6B8C49236F422F0058; _csrf=ab09867a9699a1909e20266af023f1b71647a844894a0da9f4eb6a4c35a30b00; mojo-session-id={"id":"30b9ea5b90ba61290f271d6126e57bd4","time":1593916402015}; mojo-trace-id=1; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593174115,1593174145,1593217105,1593916402; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593916402; __mta=212246443.1593139147051.1593139177936.1593916402206.4; _lxsdk_s=1731cd229db-91e-f85-461%7C%7C2'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'myscrapy.middlewares.MyscrapySpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'myscrapy.middlewares.MyscrapyDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'myscrapy.pipelines.MyscrapyPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
