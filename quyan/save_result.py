import os
import shutil
import pandas as pd
import time
import json
import xlwt
import re

def makf(d):
    if os.path.exists(d):
        pass
    else:
        os.makedirs(d)
def remf(f):
    if os.path.exists(f):
        os.remove(f)
def save_csv(title,item):
    print(111)
    dcsv = './save_csv/'
    dt = dcsv + 'title.csv'
    di = dcsv + 'item.csv'
    dr = dcsv + 'result.csv'
    makf(dcsv), remf(dt), remf(di)
    name = ['委托客户', '客户订单号',  '订单备注']
    pf_title = pd.DataFrame(title, columns=name, index=[1])
    pf_title.to_csv(dt, encoding='utf-8')
    pf_item = pd.DataFrame(item, columns=['物料号', '批次', '件数'])
    pf_item.to_csv(di, encoding='utf-8')
    # 判断result文件是否存在,在->删除
    remf(dr)
    fr = open(di, 'r', encoding='utf-8').read()
    fd = open(dt, 'r', encoding='utf-8').read()
    with open(dr, 'a', encoding='utf-8') as f:
        f.write(fd)
        f.write(fr)  # 合并写入同一个文件夹下
    now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
    dir = './results/shengl_results/'
    dira = './results/shenglall_results/'
    # 保存实时更新得文件夹,保存所有记录得文件夹
    makf(dir), makf(dira)
    shutil.copyfile(dr, dir + now + 'result.csv')  # 复制文件到指定目录,顺便重命名
    shutil.copyfile(dr, dira + now + 'result.csv')  # 保存所有识别记录

def save_csv_res(dct_data,path):
    #path 单个文件识别结果保存路径,只是保存结果
    dcsv = './save_csv/'
    dt = dcsv + 'title.csv'
    di = dcsv + 'item.csv'
    makf(dcsv)
    remf(dt), remf(di)
    time.sleep(1)
    now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
    #dir =  path
    makf(path)
    dira = path+'all/'
    try:
        cus_num = dct_data['title']['customer_order']
    except:
        cus_num = dct_data['title']['Customer_No']
    # 保存实时更新得文件夹,保存所有记录得文件夹
    makf(dira)
    order_str = cus_num.replace("/", "-")  # 有些客户订单号有/的
    dr = dira +now+'_'+ order_str + 'result.csv'
    pf_title = pd.DataFrame(pd.Series(dct_data['title']),columns=['title'])
    # pf_title = pf_title.reset_index().rename(columns ={"option","value"})
    pf_title.to_csv(dt, encoding='utf-8')
    pf_item = pd.DataFrame(pd.Series(dct_data['item']),columns=['item'])
    # pf_item = pf_item.reset_index().rename(columns ={"item","value"})
    pf_item.to_csv(di, encoding='utf-8')
    # 判断result文件是否存在,在->删除
    try:
        fr = open(di, 'r').read()
    except:
        fr = open(di, 'r', encoding='utf-8').read()
    try:
        fd = open(dt, 'r').read()
    except:
        fd =open(dt, 'r',encoding='utf-8').read()
    #print(dr)
    with open(dr, 'a', encoding='utf-8') as f:
        f.write(fd)
        f.write(fr)  # 合并写入同一个文件夹下
    return  True
    #shutil.copyfile(dr, dir + now + 'result.csv')  # 复制文件到指定目录,顺便重命名
    #shutil.copyfile(dr, dira + now + 'result.csv')  # 保存所有识别记录

'''
{'title':{'client': '宣伟（南通）涂料有限公司', 'customer_order': '611-1888-6496730', 'order_remark': '杭州昊邦汽车用品有限公司,广东省佛山市南海区里水镇道道通汽配城A7栋13号',
        'transport_remark': '', 'PONO': '', 'DONO': '', 'total_num':'164','total_net_weight':'',}, 
'item': {'matirial': ['SW909-LN', 'SW909-3020-LI'], 'batch': ['TN0789121037', 'TN0919121970'], 'num': ['64', '100'], 'net_weight': []},'result':{'res':0,'info':'物料号不存在'}}
'''
def save_txt_res(dct_data,path,name=''):
    #path 单个文件识别结果保存路径
    makf(path)
    now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
    try:
        cus_num = dct_data['title']['customer_order']
    except:
        cus_num = dct_data['title']['Customer_No']
    if not name:
        name = cus_num.replace("/","-")
    res_file = path +now+ '_'+name + "res.txt"
    if not dct_data['title'] and dct_data['item']:
        print('error in result',dct_data)
        return False
    with open(res_file,'w',encoding='utf-8') as f:
        #json_data1=json.dumps(json_data,ensure_ascii=False) 入参字典
        #json.load()可以解码
        json.dump(dct_data,f)  #这里保存为编码格式 入参文件
        #f.write(str(dct_data)) #这里保存为可视化
        f.close()
    dira = os.path.dirname(os.path.dirname(path))+'/all/'
    # 保存实时更新得文件夹,保存所有记录得文件夹
    print(res_file)
    makf(dira)
    #time.sleep(1)
    #order_str =cus_num.replace("/","-") #有些客户订单号有/的
    shutil.copyfile(res_file, dira+now+'_'+name+"res.txt")  # 复制文件到指定目录
    return True

def save_xls_res(dct_data, path, name= None):
    now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
    # dir =  path
    makf(path)
    if not name:
        dira = path + 'all/'
        try:
            cus_num = dct_data['title']['customer_order']
        except:
            cus_num = dct_data['title']['Customer_No']
        makf(dira)
        order_str = cus_num.replace("/", "-")  # 有些客户订单号有/的
    else:
        dira = path + '/res/'
        makf(dira)
        order_str =name
    res_file = dira + now + '_' + order_str + 'result.xls'

    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('Sheet1')
    i = 0
    for elem in dct_data['title'].keys():
        worksheet.write(i, 0, elem)
        worksheet.write(i, 1, dct_data['title'][elem])
        i +=1
    col = 0
    for elem in dct_data['item'].keys():
        row = i
        worksheet.write(row, col, elem)
        for el in dct_data['item'][elem]:
            row +=1
            worksheet.write(row, col, el)
        col +=1
    workbook.save(res_file)
    print(res_file)
    return  True

def save_xls_check(dct_data, path, name= None):
    now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
    # dir =  path
    makf(path)
    if not name:
        dira = path + 'all/'
        makf(dira)
        order_str =''
    else:
        dira = path + '/res/'
        makf(dira)
        order_str =name
    res_file = dira + now + '_' + order_str + 'result.xls'

    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('Sheet1')
    i = 0
    for elem in dct_data['title'].keys():
        worksheet.write(i, 0, dct_data['title'][elem]['no'])
        worksheet.write(i, 1, elem)
        worksheet.write(i, 2, dct_data['title'][elem]['text'])
        worksheet.write(i, 3, dct_data['title'][elem]['check'])
        worksheet.write(i, 4, dct_data['title'][elem]['info'])
        i +=1
    col = 0
    for elem in dct_data['item'].keys():
        row = i
        worksheet.write(row, col, elem)
        for el in dct_data['item'][elem]:
            row +=1
            worksheet.write(row, col, el['text'])
        col +=1
    workbook.save(res_file)
    print(res_file)
    return  True

def save_xls_custom_res(dct_data, path, name= None):
    now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
    # dir =  path
    str_name = '序号  电子帐册  备案序号  料件号  海关编码  品名	申报要素	成交数量	成交单位	第一数量	第一单位	第二数量	第二单位	币制	单价	总价\
    	征免方式	原产国	目的国	件数	包装种类	净重/KGS	毛重/KGS	境内货源(目的)地	最终目的地/原产地'

    keyword_mapping = {'product_name': '品名', 'nw': '第一数量', 'product_unit': '第一单位', 'num':'成交数量', 'first_unit':'成交单位' , 'amount': '总价',\
     'currency': '币制', 's_country': '原产国', 'd_country': '目的国', 'source_city': '境内货源(目的)地', 'tax_collect': '征免方式','record_no':'备案序号',\
    'material_no':'料件号','hscode':'海关编码','declear_elem':'申报要素','ser_no':'序号','acount':'电子帐册','average':'单价','package':'包装种类',\
                       'net_weight':'净重/KGS','second_num':'第二数量','second_unit':'第二单位'}

    item_name_list = re.split('\s+',str_name)
    makf(path)
    dira = path + '/result/'
    makf(dira)
    if name:
        order_str =name
    else:
        order_str = ''
    res_file = dira + now + '_' + order_str + '.xls'

    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('Sheet1')
    i = 0
    for elem in item_name_list:
        worksheet.write(1, i, elem)
        i +=1
    col = item_name_list.index('件数')
    worksheet.write(2,col,dct_data['title']['total_num'])
    col = item_name_list.index('毛重/KGS')
    worksheet.write(2, col, dct_data['title']['total_gw'])
    # col = item_name_list.index('包装种类')
    # worksheet.write(2, col, dct_data['title']['package'])

    for elem in  keyword_mapping.keys():
        col = item_name_list.index(keyword_mapping[elem])
        j =2
        for va in dct_data['item'][elem]:
            worksheet.write(j, col, va)
            j +=1
    j = len(dct_data['item']['product_name'])
    col = item_name_list.index('电子帐册')
    worksheet.write(j+2, col, '汇总')
    workbook.save(res_file)
    return  True

if __name__ == '__main__':
    jpg = './Hpdata/识别正确/rotation/2019-06-14jpg/M10.jpg'
    dir='./Hpdata'
    res=save_xls_res =(jpg,dir)
    print(res)