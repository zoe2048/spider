# -*- coding:utf-8 -*-

"""
中英文名称翻译
"""
import csv


def creat_transtab(transfile, transtype='en-cn'):
    d1 = {}
    with open(transfile, encoding='utf-8-sig') as f:
        csv_f = csv.reader(f)
        headers = next(csv_f)
        if 'country' in transfile:
            d2 = {}
            d3 = {'UK': '英国', 'West Germany': '西德', 'South Korea': '韩国', 'Soviet Union': '苏联'}
            code_id = headers.index('code')
            en_id = headers.index('name_en')
            cn_id = headers.index('name_cn')
            if transtype == 'en-cn':
                for line in csv_f:
                    en = line[en_id]
                    code = line[code_id]
                    cn = line[cn_id]
                    if en not in d1:
                        d1[en] = cn
                    if code not in d2:
                        d2[code] = cn
            elif transtype == 'cn-en':
                for line in csv_f:
                    en = line[en_id]
                    code = line[code_id]
                    cn = line[cn_id]
                    if cn not in d1:
                        d1[cn] = en
                    if cn not in d2:
                        d2[cn] = code
            return d1, d2, d3
        else:
            en_id = headers.index('name_en')
            cn_id = headers.index('name_cn')
            if transtype == 'en-cn':
                for line in csv_f:
                    en = line[en_id]
                    cn = line[cn_id]
                    if en not in d1:
                        d1[en] = cn
            elif transtype == 'cn-en':
                for line in csv_f:
                    en = line[en_id]
                    cn = line[cn_id]
                    if cn not in d1:
                        d1[cn] = en
            return d1,


# 参照翻译对照表，中英文转换
def translate_data(intab, transfile):
    newintab = {}
    transtabs = creat_transtab(transfile)
    for ele in intab:
        for transtab in transtabs:
            if ele in transtab:
                ele_transed = transtab.get(ele)
                newintab[ele_transed] = intab[ele]
                break
            else:
                continue
    return newintab


# 统一名称
def union_data(data):
    for key in data:
        if key in ['香港', '台湾', '澳门']:
            keyn = '中国' + key
            data[keyn] = data.pop(key)
        elif key in ['Hong Kong', 'Tai Wan', 'Macao']:
            keyn = key + '(China)'
            data[keyn] = data.pop(key)
    return data





