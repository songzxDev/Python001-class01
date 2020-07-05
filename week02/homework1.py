# -*- coding:utf-8 -*-
import requests
import pandas as pd
from bs4 import BeautifulSoup

# 安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中
myheader = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'Host': 'maoyan.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cookie': 'uuid_n_v=v1; uuid=535F9DC0B7AA11EA974289B279A7041D3C7E135915E641ADB5E8E2AF73F37CC4; _csrf=0c1e2e11b6f009db94cff327d90f20fd4b47d55fb959867465d197fafd8c0ed1; mojo-uuid=177e9a686c4a85cf1977e4cfdfe86c4d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593175277; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593175277; _lxsdk_cuid=172f0a57f46c8-0b1b4b0eb6bce8-f7d1d38-144000-172f0a57f46c8; _lxsdk=535F9DC0B7AA11EA974289B279A7041D3C7E135915E641ADB5E8E2AF73F37CC4; mojo-session-id={"id":"3418d251ff09b9a2ebdf3d65668c62ea","time":1593175277397}; mojo-trace-id=1; __mta=45462939.1593175277442.1593175277442.1593175277442.1; _lxsdk_s=172f0a57f47-cc5-a1c-fa8%7C%7C2'

}

resp = requests.get('https://maoyan.com/films?showType=3', headers=myheader)

soup = BeautifulSoup(resp.content, 'html.parser')
result = [['电影名称', '电影类型', '电影主演', '上映时间']]
for dd in soup.select('dl.movie-list dd', limit=10):
    divs = []
    for child in dd.find_all("div", class_="movie-hover-info")[0].children:
        if not isinstance(child, str):
            divs.append(str(child.text).strip())
    mvname, mvtype, starring, playdate = (divs[0].split('\n')[0], divs[1].split('\n')[1].strip(),
                                          divs[2].split('\n')[1].strip(), divs[3].split('\n')[1].strip())
    result.append([mvname, mvtype, starring, playdate])
data = pd.DataFrame(result)
data.to_csv('./maoyan1.csv', index=False, header=False, encoding="utf_8_sig")
