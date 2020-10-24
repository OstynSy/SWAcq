import json
from datetime import datetime
from pprint import pprint

#FILENAME = 'Sygnia-20377306.json'
FILENAME = 'Zlidyh5-8577826.json'
MONSTERFILE = 'monsters.json'


def monster_name(id):
    with open(MONSTERFILE, encoding="utf8") as f:
        data = json.load(f)
        for line in data['names']:
            for att in data['attributes']:
                family = id[0:3]
                awakened = id[3]
                element = id[4]
                if awakened != "0" or family == "100":
                    name = '\033[95m' + '\033[1m' + line[id] + '\033[0m'
                else:
                    name = att[element] + " " + line[family]
            f.close()
    return name


def get_monster():
    monster_dict = {}
    with open(FILENAME, encoding="utf8") as f:
        data = json.load(f)
        for line in data['unit_list']:
            ID = str(line['unit_master_id'])
            date = line['create_time']
            monster_dict[monster_name(ID)] = date
        f.close()
    return monster_dict


with open('Monster_acq_date.txt', 'a') as dataFile:
    monst_dict = get_monster()
    sort_dict = sorted(monst_dict.items(), key=lambda x: x[1], reverse=False)

    for i in sort_dict:
        dataFile.write(i[0] + i[1] + '\n')
        print(i[0], i[1])

#pprint(monst_dict)


