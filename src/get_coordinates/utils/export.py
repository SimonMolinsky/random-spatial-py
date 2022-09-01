from typing import List
import json


def export_txt(fname: str, points: List):
    with open(fname, 'w') as fout:
        fout.write('Lon,Lat\n')
        for pt in points:
            line = str(pt[0]) + ',' + str(pt[1]) + '\n'
            fout.write(line)
    print('Points saved successfully to txt file!')


def export_json(fname: str, points: List):
    d = {'Lon/Lat': points}
    with open(fname, 'w') as fout:
        json.dump(d, fout)
    print('Points saved successfully to json file!')


if __name__ == '__main__':
    from src.points import random_from_point

    tpoint = [50.45, 30.523333]  # lat , lon
    rpoints = random_from_point(tpoint[1], tpoint[0])
    export_json('p.json', rpoints)
    export_txt('p.txt', rpoints)
