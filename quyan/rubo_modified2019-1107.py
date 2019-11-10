import pandas as pd
import re
import datetime
from pandas import Series,DataFrame

# RUBO2

## 读取RUBO2(1).xlsx中Packlist-sheetname

rubo2 = pd.read_excel('RUBO2(1).xlsx',sheet_name='Packlist',index_col=None,header=0,skiprows=0)

# rubo2.columns

## rubo2_Packlist中筛选出需要的字段信息

rubo2.rename(columns={'Unnamed: 0':'产品代码',  'Packlist':'客户运单号','Unnamed: 7':'目的省份',\
                            'WMS SHIP DATE':'发货时间','CARRIER CODE':'运输类型','CTNS':'预计箱数',\
                            'Unit':'预计发货','SHIP TO':'客户代码','CRD date':'CRD_date'},inplace=True)

rubo2_col_list = ['客户运单号','产品代码','目的省份','ST NAME','发货时间','预计箱数','客户代码','CRD_date','PSST','Window','Address1','Address2','Address3']

# rubo2.loc[:2,rubo2_col_list]

# basedata.xlsx中的Sheet'CLC预报'和'客户信息表'

## 读取Sheet'CLC预报

basedata_CLC = pd.read_excel('basedata.xlsx',sheet_name='CLC预报',index_col=None,header=0,skiprows=0)

# basedata_CLC.columns

### Sheet'CLC预报'中筛选出所需字段

basedata_CLC.rename(columns={'发货单号':'客户运单号','在途时间':'在途3', '件数':'预计件数','发货时间':'发货日期',\
                             '预计到达时间':'预计达到日期','陆运/铁运/空运':'运输类型','卸货地址':'卸货地点'},inplace=True)

# '客户运单号'=‘发货单号’。‘BU’代表‘产品代码’，rubo2表中有这里没有提取
basedata_CLC_col_list = ['总单号','客户运单号','出发城市','目的城市',\
                         '卸货地点','箱数','预计件数','运输类型','在途3','发货日期',\
                         '预计达到日期','客户简称','客户名称','联系方式','联系人手机']

# basedata_CLC.loc[:2,basedata_CLC_col_list]

## 读取Sheet'客户信息表'

basedata_Customersinfo = pd.read_excel('basedata.xlsx',sheet_name='客户信息表',index_col=None,header=0,skiprows=0)

# basedata_Customersinfo.columns

### Sheet'客户信息表'中筛选出所需字段

basedata_Customersinfo.rename(columns={'-':'客户代码'},inplace=True) 
# ,'城市':'起运城市','省份':'起运省份'

basedata_Customersinfo_col_list = ['客户代码','详细地址','城市','省份','电话1','电话2','电话-2011','联系人']
# ,'起运城市','起运省份','手机预报'

basedata_Customersinfo.客户代码=basedata_Customersinfo.客户代码.astype(str)

basedata_Customersinfo['联系人电话'] = list(map(lambda x,y,z:str(x)+str(y)+str(z),\
                                           basedata_Customersinfo['电话1'],\
                                           basedata_Customersinfo['电话2'],\
                                           basedata_Customersinfo['电话-2011'] ))

# basedata_Customersinfo['联系人手机'] = basedata_Customersinfo['手机预报']
# basedata_Customersinfo有手机预报和basedata_CLC有联系人手机，所以这里取得是basedata_CLC有联系人手机
#,'联系人手机'
basedata_Customersinfo_col_list = ['客户代码','详细地址','城市','省份','联系人','联系人电话']

# basedata_Customersinfo.loc[:2,basedata_Customersinfo_col_list]

basedata_Customersinfo.fillna('',inplace=True)

# 根据字段'客户运单号'合并表RUBO2_Packlist和表basedata_CLC预报

rubo2.客户运单号 = rubo2.客户运单号.astype(str)
basedata_CLC.客户运单号 = basedata_CLC.客户运单号.astype(str)

merged_packlist_CLC = pd.merge(rubo2.loc[:,rubo2_col_list],basedata_CLC.loc[:,basedata_CLC_col_list],on='客户运单号')

# 将merged_packlist_CLC_col_list的所有字段名保存到列表
merged_packlist_CLC_col_list = merged_packlist_CLC.columns.tolist()
len(merged_packlist_CLC_col_list)

# merged_packlist_CLC_col_list

# 转换字段‘客户代码’数据的数据类型为str
merged_packlist_CLC.客户代码=merged_packlist_CLC.客户代码.astype(str)
basedata_Customersinfo.客户代码= basedata_Customersinfo.客户代码.astype(str)

# 查看merged_packlist_CLC中的选中区域
# merged_packlist_CLC.loc[:2,merged_packlist_CLC_col_list]

# 根据字段'客户代码'合并表merged_packlist_CLC和表basedata_客户信息表

merged_allinfo = pd.merge(merged_packlist_CLC.loc[:,merged_packlist_CLC_col_list],basedata_Customersinfo.loc[:,basedata_Customersinfo_col_list],on='客户代码')

# 计算rubo2_packlist中每一个重复客户代码的个数
# customercode_count = merged_packlist_CLC.groupby('客户代码').count().sort_values('客户运单号',ascending=False)
# customercode_count[customercode_count['客户运单号']>1]
# customercode_count[customercode_count['客户运单号']>1].index


# 添加rubo2_packlist.客户代码不在basedata_Customersinfo.客户代码中的字段rubo2_packlist.客户代码信息到merged_allinfo

# rubo2_packlist.客户代码在basedata_Customersinfo.客户代码中记为lm
lm = []
lb = []
for m in merged_packlist_CLC.客户代码:
    for b in basedata_Customersinfo.客户代码:
        if m == b:
            lm.append(m)
        else:
            lb.append(b)

# rubo2_packlist.客户代码不在database_customerinfo.客户代码中
list(set(merged_packlist_CLC.客户代码)^set(lm))
# 载rubo2_packlist.客户代码中提取不在basedata_Customersinfo.客户代码中的每条记录
for e in list(set(merged_packlist_CLC.客户代码)^set(lm)):
    merged_packlist_CLC[merged_packlist_CLC['客户代码']== e]
    merged_allinfo = pd.concat([pd.DataFrame(merged_allinfo),merged_packlist_CLC[merged_packlist_CLC['客户代码']== e]],sort=True,ignore_index=True)

# 调整字段数据的格式和表中字段的排列顺序

merged_allinfo.fillna('',inplace=True)

merged_allinfo['客户'] = 'NIKE'

# 读取basedata_lead中字段‘城市’和‘省份’确定‘城市等级’
basedata_lead = pd.read_excel('basedata.xlsx',sheet_name='lead',index_col=None,header=0,skiprows=0)

basedata_lead_CP = basedata_lead['City'] + basedata_lead['Province']

basedata_lead['basedata_lead_CP'] =basedata_lead_CP

merged_allinfo_CP = merged_allinfo['目的城市'] + merged_allinfo['目的省份'] 

city_tier = []
for mcp in merged_allinfo_CP:
    for bcp in basedata_lead_CP:
        if mcp == bcp:
            city_tier.append(int(basedata_lead[basedata_lead['basedata_lead_CP']==bcp]['City Tier']))

merged_allinfo['城市等级'] = city_tier


# 字段添加默认值
merged_allinfo['运单类型'] = '大仓出货'
merged_allinfo['整车/零担'] = 'LTL'
merged_allinfo['箱数'] = ''
merged_allinfo['件数'] = ''
merged_allinfo['起运客户代码'] = 'NIKE-TC'
merged_allinfo['起运客户名称'] = '太仓CLC'
# merged_allinfo.起运客户名称 = merged_allinfo.起运客户名称.astype(str)
merged_allinfo['总单号'] = ''
merged_allinfo['客户开票抬头'] = '耐克（体育）有限公司'
merged_allinfo['项目名称'] = '太仓-耐克-运输'
merged_allinfo['体积(立方)'] =''

# ‘起运客户名称’列的值含有"CLC"时，为江苏省太仓市广州西路88号
# ‘起运客户名称’列的值含有"CRWP"时，为江苏昆山巴城工业园长江S北路与立基路交口东北侧
# ‘起运客户名称’列的值含有"BZBJ"时，为河北省廊坊市安次区东环路55号普洛斯物流园A3库

def start_address_re(x):
    if re.findall('CLC',x)[0] == 'CLC':
        x = '江苏省太仓市广州西路88号'
    elif re.findall('CRWP',x)[0] == 'CRWP':
        x = '江苏昆山巴城工业园长江S北路与立基路交口东北侧'
    elif re.findall('BZBJ',x)[0] == 'BZBJ':
        x = '河北省廊坊市安次区东环路55号普洛斯物流园A3库'
    else:
        x = x
    return x

merged_allinfo['起运地址'] = list(map(start_address_re,merged_allinfo['起运客户名称']))

# 起运省份为‘起运地址’的列获取省份
# 起运城市为‘起运地址’的列获取城市

def start_province(strat_address):
    return re.findall('(.+省)',strat_address)[0]
def start_city(strat_address):
    re.findall('省(.+市)',strat_address)
    return re.findall('省(.+市)',strat_address)[0]

merged_allinfo['起运省份'] = list(map(start_province,merged_allinfo['起运地址']))

merged_allinfo['起运城市'] = list(map(start_city,merged_allinfo['起运地址']))

# 1）当该表的‘CRD要求日期’不为空时，取该值
# 2）当原始表的“PSST”列为“Y”时，如果1）有值就加“/PSST”,如果没有1）就为“PSST”
def shipping_note(crd,psst):
    if crd and psst == 'Y':
        return crd + '/PSST'
    elif not crd and psst == 'N':
        return 'PSST'
    else:
        return 'PSST'

merged_allinfo['托运单备注'] = list(map(shipping_note,merged_allinfo['CRD_date'],merged_allinfo['PSST']))

# 修改字段格式
merged_allinfo['发货时间'] = Series(map(lambda x:'{}'.format('20'+str(x)),merged_allinfo['发货时间']))

merged_allinfo['客户运单号'] = Series(map(lambda x:'{:09}'.format(int(x)),merged_allinfo['客户运单号']))

merged_allinfo['产品代码'] = Series(map(lambda x:'APP' if x=='AP' else x,merged_allinfo['产品代码']))



# 修改字段日期格式
datetime.datetime.now().strftime("%Y%m")
merged_allinfo['结算月份'] = datetime.datetime.now().strftime("%Y%m")

merged_allinfo['预计达到日期'] = merged_allinfo['预计达到日期'].dt.strftime('%Y/%m/%d')

merged_allinfo['发货日期'] = merged_allinfo['发货日期'].dt.strftime('%Y/%m/%d')

# 当原始表的“CRD date”列不为空时，该表的"预计达到日期" 与原始表的“CRD date”取最晚时间
def crd_request_date(expected_arrival_date,crd_date):
    if not crd_date:
        return max(expected_arrival_date,crd_date)
    else:
        return ''

# merged_allinfo['CRD_date'] = '2019-10-21'
# merged_allinfo.CRD_date = merged_allinfo.CRD_date.astype('datetime64[ns]')

import datetime
from datetime import datetime

merged_allinfo.CRD_date = merged_allinfo.CRD_date.astype('datetime64[ns]')

merged_allinfo['CRD要求日期'] = list(map(crd_request_date,merged_allinfo['预计达到日期'],merged_allinfo['CRD_date']))
# merged_allinfo['CRD要求日期'] = merged_allinfo['CRD要求日期'].dt.strftime('%Y/%m/%d')



# 联系人（个人客户直接ST NAME,为公司：取客户信息的配置表)
merged_allinfo.loc[merged_allinfo[merged_allinfo['客户名称'] =='个人客户'].index.tolist(),['联系人']]=\
merged_allinfo[merged_allinfo['客户名称'] =='个人客户']['ST NAME']

# 联系人手机（为公司：配置表的预留手机，为个人用户时：ST NAME或SHIP_TO_PHONE_NBR)
merged_allinfo.loc[merged_allinfo[merged_allinfo['客户名称'] =='个人客户'].index.tolist(),['联系人手机']]=\
merged_allinfo[merged_allinfo['客户名称'] =='个人客户']['ST NAME']
# 左对齐
merged_allinfo['联系人手机']=list(map(lambda x:'{:<}'.format(x),merged_allinfo['联系人手机']))
# merged_allinfo.columns

# 卸货地点：公司客户取客户信息表的详细地址，个人客户或为空运时：Address2+Address3+Address1
merged_allinfo.loc[merged_allinfo[merged_allinfo['客户名称'] =='个人客户'].index.tolist(),['卸货地点']]=\
 list(map(lambda x,y,z:str(x)+'/'+str(y)+'/'+str(z),\
                                           merged_allinfo[merged_allinfo['客户名称'] =='个人客户']['Address2'],\
                                           merged_allinfo[merged_allinfo['客户名称'] =='个人客户']['Address3'],\
                                           merged_allinfo[merged_allinfo['客户名称'] =='个人客户']['Address1'] ))

basedata_Customersinfo['联系人电话'] = list(map(lambda x,y,z:str(x)+str(y)+str(z),\
                                           basedata_Customersinfo['电话1'],\
                                           basedata_Customersinfo['电话2'],\
                                           basedata_Customersinfo['电话-2011'] ))



# merged_allinfo.loc[:2,['发货时间','客户运单号','运输类型']]

# merged_allinfo.columns

merged_allinfo = merged_allinfo.loc[:,['客户运单号','客户代码','客户','目的城市','目的省份','城市等级','运单类型','整车/零担',\
                                       '客户名称','客户简称', '联系人','联系人电话','联系人手机','卸货地点', '预计箱数','箱数',\
                                        '预计件数', '件数', '在途3', '发货日期','预计达到日期','运输类型','起运城市','起运省份', \
                                       '起运客户代码','起运客户名称','起运地址','托运单备注','产品代码','总单号','客户开票抬头',\
                                       '项目名称','CRD要求日期','结算月份','体积(立方)']]


# 写到Excel文件

merged_allinfo.to_excel('mergedallinfo.xlsx')