#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ChineseAccounting:
    # 只支持到千亿
    def num2chi(self,digital):
        digital = float(digital)
        digichai = []
        numb = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
        unizheng = ['亿', '万', '元']
        unifen = ['', '拾', '佰', '仟']
        unid = ['分', '角', '整']
        # 分拆到亿
        yi = int(digital / 1_0000_0000)
        digichai.append(yi)
        # 分拆万到亿
        wan = int(digital / 1_0000)
        digichai.append(wan - yi * 1_0000)
        # 分拆万以下
        yuan = int(digital - wan * 1_0000)
        digichai.append(yuan)
        # 分拆分角
        fen = round((digital - int(digital)) * 100)
        # 循环赋值
        RMB = ''
        # 整数部分
        for index, val in enumerate(digichai):
            if val > 0:
                for innerdex in range(3, -1, -1):
                    flag = True
                    willchose = int(val / (10 ** innerdex))  # 除几次方取整
                    if willchose > 0:
                        if willchose >= 10:
                            willchose = willchose % 10
                            if willchose > 0:
                                flag = True
                            else:
                                flag = False
                    else:
                        flag = False
                    if flag:
                        RMB = RMB + numb[willchose] + unifen[innerdex]
                    else:
                        RMB += numb[willchose]
                # 没有错，本语句执行2次
                RMB = RMB.replace('零零', '零')
                RMB = RMB.replace('零零', '零')
                if RMB[0] == numb[0]:
                    RMB = RMB[1:]
                if RMB[-1] == numb[0]:
                    RMB = RMB[:-2]
                RMB += unizheng[index]
        if fen > 0:
            if fen >= 10:
                ling = int(fen % 10)
                if ling > 0:
                    RMB = RMB + numb[int(fen / 10)] + unid[1] + numb[ling] + unid[0]
                else:
                    RMB = RMB + numb[int(fen / 10)] + unid[1]
            else:
                RMB = RMB + numb[0] + numb[fen] + unid[0]
        else:
            RMB += unid[2]
        return RMB
