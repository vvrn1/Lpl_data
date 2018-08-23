import requests
import json
import csv


def parse_one_team(data):
    for item in data:
        yield{
            '队名': item['sTeamName'],
            '队伍id': item['iTeamId'],
            '平均大龙': item['sAveragingBigDragon'],
            '平均插眼': item['sAveragingWardPlaced'],
            '平均': item['sAveragingKillNeutral'],
            '总击杀': item['iKill'],
            '胜率': item['sAveragingWin'],
            '平均每场击杀': item['sAveragingKill'],
            '总死亡': item['iDeath'],
            '总胜场': item['iWin'],
            '平均排眼': item['sAveragingWardKilled'],
            '总场次': item['iAppearancesFrequency'],
            '平均每场金钱': item['sAveragingGold'],
            '平均小龙': item['sAveragingSmallDragon'],
            '平均每场死亡': item['sAveragingDeath'],
            '总负场': item['iLoss']
        }


url = 'http://apps.game.qq.com/lol/act/a20160519Match/Match.php?_a=teamsearch&iGameId=95&iType=6&sGameType=7,8&iPage=1&sRet=TEAMRANKLIST&r=0.9861627663199555&_=1534944828050'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
data = {'sGet':'TEAMRANKLIST'}
response = requests.post(url,headers=headers, data=data)
response.encoding = 'utf-8'
response = response.text.split('=')[1]
response = json.loads(response)
print(len(response['msg']['data']))
data = response['msg']['data']
# 数据预处理

with open('Data.csv', 'a', newline='') as f:
    fieldnames = ['队名', '队伍id', '平均大龙', '平均插眼', '平均', '总击杀', '胜率', '平均每场击杀', '总死亡', '总胜场', '平均排眼',
                '总场次', '平均每场金钱', '平均小龙', '平均每场死亡', '总负场']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for item in parse_one_team(data):
        writer.writerow(item)
        print(item)

