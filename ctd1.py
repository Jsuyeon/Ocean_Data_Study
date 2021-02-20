import csv
import pandas as pd
from pandas import DataFrame, Series
import numpy as np
from datetime import datetime
import io

# data from : https://www.data.go.kr/data/15059974/openapi.do
# 부산 지역의 해양 데이터로 다양한 자료 만들어보기
korea_strat = []
with open('C:\\Users\\soy19\\Downloads\\해양환경공단_해양환경측정망(CTD)_항만_20191231.csv', 'r') as data:
    # f=data.readlines()
    f = csv.reader(data, delimiter=',')
    for row in f:
        if row[0] == '대한해협' and row[1][0:2] == '부산':
            korea_strat.append(row)

df = DataFrame(korea_strat)


"""지정된 csvfile 의 줄을 이터레이트 하는 판독기(reader) 객체를 반환합니다. 
csvfile은 이터레이터 프로토콜을 지원하고 __next__가 호출될 때마다 문자열은 반환하는
객체여야한다

csv.DictReader()
일반 판독기처럼 작동하지만 각행의 정보를 키가 전택적 filename 매개변수
dict 로 매핑하는 객체를 만든다
fieldnames 매개 변수는 시퀀스입니다. fieldnames를 생략하면,
파일 f의 첫 번째 행에 있는 값들을 fieldnames로 사용합니다. 
필드 이름이 어떻게 결정되는지와 관계없이, 딕셔너리는 원래 순서를 유지
"""

"""
csv.Dialect
어트리뷰트에 주로 의존하는 컨데이터 클래스인데,특정 reader나 wirter 
인스턴스에 대한 파라미터를 정의하는데 사용 

csv.Sniffer().sniff:
지정된 smaple을 분석하고 발견된 파라미터를 반영하는 Dialect 서브 클래스를 반환
선택적인 delimiters 매개변수를 주면 가능한 유효한 구분 문자를 포함하는 문자열 반환
"""
date, station, depth, temp, sal, n, p = [], [], [], [], [], [], []

import copy
import gsw

#관측한 위도와 경도를 알 수 없어 google에서 나온 부산의 위도와 경도를 사용
lat,lon=35.1796,129.0756
def derive_csv(data):
    density = gsw.z_from_p(cast[6].values,lat)
    absolute_sal=gsw.SA_from_SP(cast[10].values,density,lon,lat)
    reference_sal=gsw.SR_from_SP(absolute_sal)
    conservative_temp=gsw.CT_from_t(absolute_sal,cast[8],density)
    potential_density=gsw.sigma0(absolute_sal,conservative_temp)

    return density,absolute_sal,reference_sal,conservative_temp,potential_density

z,sa,sr,ct,,sigma0=derive_csv(df)
