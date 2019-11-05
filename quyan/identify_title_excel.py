#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymysql
import pdfplumber
import re
import time
import  xlrd
from comm.basetools_excel import  BasTls,find_sheet_value,get_sheet_value
from comm.log import my_logger
from setting import *
from decimal import Decimal
from contr.identify_process import check_company
from comm.get_head_end import get_head,get_end
"""modification 2019/4/14 修改了相对位置不准的问题，用key_word和key_word_next来定位取数据."""
# pd.set_option('display.max_columns', 100)


ROW_DIS = 5 #最小行距
COL_DIS = 5 #最小列距离
##参数
def compare_str(str1,str_list):
    #比较两个字符包含关系，返回被包含字符
    if isinstance(str_list,list):
        for elem in str_list:
            if len(str1) <= len(elem) and str1 in elem:
                return True
            elif len(str1) > len(elem) and elem in str1:
                return True
        else:
            return False
    else: #str_list是一个字符串
        if len(str1)<=len(str_list) and str1 in str_list:
            return True
        elif len(str1)> len(str_list) and str_list in str1:
            return True
        else:
            return  False
def max_str(str1,str2): #比较两个字符串返回最长的
    if not str1:
        return  str2
    if not str2:
        return  str1
    if len(str1)<=len(str2):
        return  str2
    else:
        return  str1

def compare_list(list1,list2):
    #对相同长度的两个list进行最大数的合并
    if not list1 or len(list1)<len(list2):
        return list2
    if not list2 or len(list2)<len(list1):
        return list1
    res_list =[]
    for i in range(len(list1)):
        res_out = compare_str(list1[i],list2[i])
        res_list.append(res_out)
    return  res_list

def mix_list(list1,list2):
    #对相同长度的两个list进行最大数的合并
    if not list1:
        return list2
    if not list2:
        return list1
    if len(list1)<=len(list2):
        res_list = list2
        for i in range(len(list1)):
            res_list[i] = max_str(list1[i],list2[i])
    else:
        res_list = list1
        for i in range(len(list2)):
            res_list[i] = max_str(list1[i], list2[i])
    return  res_list

def add_list(list1,list2):
    if not list1:
        return  list2
    if not list2:
        return  list1
    if len(list1) != len(list2):
        return compare_list(list1,list2)
    res_list = []
    for i in range(len(list1)):
        tm_str =list1[i]+list2[i]
        res_list.append(tm_str)
    return  res_list

def select_list(list1):
    res_str = ''  # 最终字符串,同一个字段，多个规则提取原则,包括去掉‘’
    max_l = 0  # 取最长的字符
    for elem in list1:
        if len(elem) > max_l:  # 取字符最长的
            max_l = len(elem)
            res_str = elem
    return  res_str

def regu_extract_sub(regu_rule,sub_str,extract_str):
    if regu_rule and regu_rule != 'None' and (sub_str == 'None' or not sub_str):
        # 正则提取
        patten = re.compile(regu_rule, re.M)
        res = patten.findall(extract_str)
        print(patten)
        print(res)
        print('extract string:', extract_str)
        res_out = ""
        if not res:
            my_logger.error('extract null with the regular rule: %s, all string:%s' % (regu_rule, extract_str))
        else:
            res_out = res[0]
    elif regu_rule and regu_rule != 'None' and sub_str != 'None' and sub_str:
        # 正则匹配到则替换，否则为""字符不操作，将正则作为判断条件而已
        patten = re.compile(regu_rule, re.M)
        res = patten.findall(extract_str)
        # print(patten)
        # print(res)
        # print('extract sub string:', extract_str)
        res_out = ""
        if not res:
            my_logger.info('extract null with the regular rule: %s, all string:%s' % (regu_rule, extract_str))
            res_out = extract_str
        else:
            res_out = sub_str
    else:
        res_out = extract_str
    return  res_out

def find_key(pdfcontent,key_word,is_list =0):
    iskey = 0  # 关键词是否配置到
    flag = 0  # 文档类型是否找到
    #is_list是否要重复查找关键词，列表词
    l_k_f, t_k_f, r_k_f, b_k_f = 0,0,0,0
    kw_list =[] #对于连续多个字符与key word字符的位置
    # print(pdfcontent)
    for item in pdfcontent:
        if not item['text']:
            continue
        if len(key_word.split()) == 1:  # key word没有空格情况
            if key_word in item['text']:
                iskey += 1
                # print('yeseyes')
                # print (item)
            else:
                iskey = 0
        else:  # key word 含有空格情况
            if compare_str(item['text'], key_word.split()):  # 关键词含有空格，关键词无空格，其他字符是关键词一部分时
                # pdf中key_word的位置
                 # print('okokok')
                iskey += 1
            else:
                iskey = 0
        if iskey == 1:
            l_k_f, t_k_f = float(item['x0']), float(item['top'])  # 在关键词有空格
        if iskey == len(re.split('\s+', key_word.strip())):
            # print(item)
            # print('kw kw yes')
            # real_x0 = item['x0'],real_x1= item['x1'],real_top= item['top']
            r_k_f, b_k_f = float(item['x1']), float(item['bottom'])  # 实际关键词位置
            # print(r_k_f,b_k_f)
            flag = 1
            if is_list==0:
                break  # 找到关键词
            else:
                iskey = 0 #清空后继续查找
                kw_list.append((l_k_f,t_k_f,r_k_f,b_k_f,flag))

    print(key_word,l_k_f,t_k_f,r_k_f,b_k_f,flag)
    print (kw_list)
    if is_list==0:
        return  l_k_f,t_k_f,r_k_f,b_k_f,flag
    else:
        return  kw_list

class identify_title_item(BasTls):
    def __init__(self, company, document_type):
        self.company = company
        self.document_type = document_type
        # 读取规则，将pdf信息提取出来
    def pathTodata(self, filePath):
        '''
        [{'id': 126, 'document_type': '发货通知单', 'company': '阿克苏诺贝尔化学品（博兴）有限公司', 'classify_word': 'customer_order',\
         'classify_word1': 'None', 'key_word': '销售订单编号', 'position_feature_context': '318.720,116.285,412.552,124.237', 'feature_position_start': '595.200,0', \
         'feature_position_end': '595.200,0', 'labelid': 34, 'sequence_no': '1', 'column_numerical': 'None', 'unit_length': '0', 'empty_count': 0,\
         'insert_time': datetime.datetime(2019, 4, 19, 14, 6, 7), 'update_time': datetime.datetime(2019, 4, 19, 14, 6, 7), 'key_word_next': None}, ]
        每一个classify提取后，再设置正则规则提取局部内容
        classify_word1 作为一级提取词，当有多条用一个规则是，通过正则后只有一条合格不为空，再多条中取不为空结果，如果多个不为空任意取最新的，否则是正则没过滤作用
        classify_word是在一级提取词基础上有多个classify_word1拼接,
        即同一个规则classify_word,classify_word1 如order_remark，order_remark_1 对应多条相同，从这多条规则中结果选取一个条结果；如果'order_remark一个，order_remark_1，order_remark_2多条，\
        合并为将order_remark_1，order_remark_2连接为一条规则
        '''
        my_logger.info(filePath)
        workbook = xlrd.open_workbook(filePath)
        # sheet = workbook.sheet_by_index(0)
        sheet_index_list =[]
        i = 0
        for sheet in workbook.sheets():
            rflag, cflag = find_sheet_value(sheet, self.document_type)
            if rflag!=None :
                sheet_index_list.append(i)
                #break
            i +=1 #返回关键词所在的sheet页面
        if rflag==None and cflag==None and not sheet_index_list:
            my_logger.error('the document type is wrong: %s' %self.document_type)
            return {}

        ruleList_item = self.getRule_item_list(self.company, self.document_type,0)
        ruleList_list = self.getRule_item_list(self.company, self.document_type,1)
        if not ruleList_item:
            return {}

        # 这个字典用来装提取的所有字段结果
        out_res = [] #最终结果是按照[{},{}]输出
        for sheet_index in sheet_index_list:
            ac_docu_type = 0  # 对找不到关键词的计算，如果找到关键词大于门限值，说明文档类型也不正确
            sheet = workbook.sheet_by_index(sheet_index)
            resultDict_title = {}  # 最终classify word
            resultDict_item = {}  # 最终classify word
            resDict = {}  # 正常classify word
            resDict_1 = {}  # classify word_1
            for ruleDict in ruleList_item:  # 没有条规则进行识别
                classify_word = ruleDict['classify_word']
                key_word = ruleDict['key_word']
                classify_word_1 = ruleDict['classify_word1']  # 初级提取
                sub_str = ruleDict['sub_str']  # 初级提取
                regu_rule = ruleDict['regu_rule']  # 初级提取的正则表达
                is_list = ruleDict['is_list']  # 是否存在重复的产品列表
                if is_list == 0:
                    is_list = None
                if not ruleDict['suffix'] or ruleDict['suffix'] == 'None':
                    suffix_str = ''
                else:
                    suffix_str = ruleDict['suffix']
                key_word_loc = eval(ruleDict['position_feature_context'])  # (2, 0)
                start = eval(ruleDict['feature_position_start'])  # (2, 1)

                # extract用来装单个特征提取出来的信息。
                extract = []
                # extract_all =[]

                ##如果存在key_word，先判断key_word位置是否变化，有变化的话，提取范围根据key_word 变化而变化;如果key word不存在直接根据物理坐标提取
                product_list = []
                txt = ''
                if not key_word or key_word == 'None' or (not key_word_loc[0] and not key_word_loc[1]):
                    my_logger.warn('the key word is null,ruleid: %d' % ruleDict['id'])
                    if len(start) == 2:
                        if start[0]> sheet.nrows or start[1] > sheet.ncols:
                            my_logger.error('the document type may be is not right')
                            ac_docu_type += 1
                            txt = ''
                        else:
                            txt = get_sheet_value(sheet, start[0], start[1])
                    else:
                        my_logger.error('the real pick word is null with the loc ' + str(start))
                    if not txt:
                        my_logger.error('the real pick word is null with the cell %d,%d' % (start[0],  start[1]))
                elif key_word :
                    real_row,real_col = find_sheet_value(sheet,key_word)
                    if real_row==None or real_col==None:
                        my_logger.error('the key word do not find %s' %key_word)
                        ac_docu_type +=1
                        txt =''
                    else:
                        diff_row,diff_col = real_row-key_word_loc[0],real_col-key_word_loc[1]
                        pick_row,pick_col = diff_row+start[0],diff_col+start[1]
                        #print(pick_row,pick_col)
                        txt = get_sheet_value(sheet,pick_row,pick_col)
                        if not real_row and not real_col:
                            my_logger.error("the real key word is not found in the document: %s" % key_word)
                else:  # kw ,kw_next 都有值情况
                    txt = ''

                res_out = regu_extract_sub(regu_rule, sub_str, txt) + suffix_str #为空字符情况也会增加连接符号
                if classify_word_1 and classify_word_1 != 'None':
                    if classify_word_1 in resDict_1.keys():
                        if len(resDict_1[classify_word_1]) < len(res_out):  #有相同的规则，取字符串长的
                            resDict_1[classify_word_1] = res_out
                    else:
                        resDict_1[classify_word_1] = res_out
                    tmp_list = []
                    if classify_word in resDict.keys():
                        tmp_list = resDict[classify_word]
                        if {classify_word_1: ""} not in tmp_list:
                            tmp_list.append({classify_word_1: ""})
                    else:
                        tmp_list.append({classify_word_1: ""})
                    resDict[classify_word] = tmp_list
                else:
                    if classify_word in resDict.keys():
                        if len(resDict[classify_word]) < len(res_out):  # 一级分类词,取长度大的值
                            resDict[classify_word] = res_out
                    else:
                        resDict[classify_word] = res_out
                # 仅仅classify_word_1加入字典，最终值是在resDict_1保留，与resDict的内容无关，因此为‘’
                # resDict[classify_word] 为[{'classify_word_1':''},{'classify_word_2':''},]
                #  #resDict_1 为{'classify_word_1':'','classify_word_2':""}
            key_index = 0  # 主键
            product_list_len = 0
            for ruleDict in ruleList_list:  #产品列表
                classify_word = ruleDict['classify_word']
                key_word = ruleDict['key_word']
                classify_word_1 = ruleDict['classify_word1']  # 初级提取
                sub_str = ruleDict['sub_str']  # 初级提取
                regu_rule = ruleDict['regu_rule']  # 初级提取的正则表达
                if not ruleDict['key_word_next'] or ruleDict['key_word_next'] == 'None':  #对于主键的列表的停止字符，默认为''停止
                    kw_next = ''
                else:
                    kw_next = ruleDict['key_word_next']
                if not ruleDict['suffix'] or ruleDict['suffix'] == 'None':
                    suffix_str = ''
                else:
                    suffix_str = ruleDict['suffix']
                key_word_loc = eval(ruleDict['position_feature_context'])  # (2, 0)
                start = eval(ruleDict['feature_position_start'])  # (2, 1)
                ##如果存在key_word，先判断key_word位置是否变化，有变化的话，提取范围根据key_word 变化而变化;如果key word不存在直接根据物理坐标提取
                product_list = []
                txt = ''
                if not key_word or key_word == 'None' or (not key_word_loc[0] and not key_word_loc[1]):
                    my_logger.warn('the key word is null,ruleid: %d' % ruleDict['id'])
                    if len(start) == 2:
                        if start[0]> sheet.nrows or start[1] > sheet.ncols:
                            my_logger.error('the document type may be is not right')
                            ac_docu_type += 1
                            txt = ''
                        else:
                            txt = get_sheet_value(sheet, start[0], start[1])
                        if key_index ==0:   #item的主键
                            i=0
                            while txt != kw_next:
                                i +=1
                                product_list.append(txt)
                                txt = get_sheet_value(sheet, start[0]+i, start[1])
                            product_list_len = len(product_list)
                            if not product_list : #没有列表
                                my_logger.error( 'the  real key_index pick word is null with the cell %d,%d' % (start[0], start[1]))
                        else: #非主键列表
                            for i in range(product_list_len):
                                txt = get_sheet_value(sheet, start[0] + i, start[1])
                                product_list.append(txt)
                    else:
                        my_logger.error('the real pick word is null with the loc ' + str(start))
                elif key_word:
                    real_row, real_col = find_sheet_value(sheet, key_word)
                    if real_row==None or real_col==None:
                        my_logger.error('the key word do not find %s' %key_word)
                        ac_docu_type +=1
                        txt =''
                    else:
                        diff_row, diff_col = real_row - key_word_loc[0], real_col - key_word_loc[1]
                        pick_row, pick_col = diff_row + start[0], diff_col + start[1]
                        txt = get_sheet_value(sheet, pick_row, pick_col)
                        if not real_row and not real_col:
                            my_logger.error("the real key word is not found in the document: %s" % key_word)
                    if key_index == 0:
                        i = 0
                        while txt != kw_next:
                            i += 1
                            product_list.append(txt)
                            txt = get_sheet_value(sheet, start[0] + i, start[1]) #产品列表按照列不变，行依次增加模式
                        product_list_len = len(product_list)
                        if not product_list:
                            my_logger.error('the  real key_index pick word is null with the cell %d,%d' % (start[0], start[1]))
                    else:  # 非主键列表
                        for i in range(product_list_len):
                            if start[0] + i >= sheet.nrows:
                                break
                            txt = get_sheet_value(sheet, start[0] + i, start[1])
                            product_list.append(txt)
                #结果处理
                res_out_list = []
                tmp_list =[]
                for elem in product_list:
                    res_tmp =regu_extract_sub(regu_rule, sub_str, elem)
                    if res_tmp:
                        res_out_list.append(regu_extract_sub(regu_rule, sub_str, elem) + suffix_str)
                    else: #为空
                        res_out_list.append(regu_extract_sub(regu_rule, sub_str, elem) )  ##为空字符情况就不需要连接符号
                if classify_word_1 and classify_word_1 != 'None':
                    if classify_word_1 in resDict_1.keys():
                        tmp_list = mix_list(resDict_1[classify_word_1], res_out_list)
                        resDict_1[classify_word_1] = tmp_list
                    else:
                        resDict_1[classify_word_1] = res_out_list
                    tmp_list = []
                    if classify_word in resDict.keys():
                        tmp_list = resDict[classify_word]
                        if {classify_word_1: []} not in tmp_list:
                            tmp_list.append({classify_word_1: []})
                    else:
                        tmp_list.append({classify_word_1: []})
                    resDict[classify_word] = tmp_list
                else:
                    print(classify_word, res_out_list)
                    if classify_word in resDict.keys():
                        tmp_list = mix_list(resDict[classify_word], res_out_list)
                        resDict[classify_word] = tmp_list
                    else:
                        resDict[classify_word] = res_out_list
                    print(resDict[classify_word],tmp_list)
                key_index += 1

                    # resDict[classify_word] 为[{'classify_word_1':[]},{'classify_word_2':[]},]
                    #  #resDict_1 为{'classify_word_1':['',''],'classify_word_2':['','']}
            print('word_1 list:', resDict_1)
            print('word list:', resDict)
            '''
            word_1 list: {'gw2': ['67.500', '0.000'], 'gw1': ['2,958.000+', '6,928.000+']}
            word list: {'client': 'BASF Chemicals Co. Ltd.', 'dest_port': 'KOBE', 'dod': '18.05.2019', 'cbm': '22.432', 'gw': [{'gw2': []}, 
            {'gw1': []}], 'dg_class': [], 'customer_order': 'No:2.009228441', 'container_type': ["20' 8'6"], 'num': ['12', '32'], 'nw': ['2,760.000', '6,400.000'], 
            'tue': '1', 'total_gw': '15,176.000', 'product_name': ['10 Basonat HI 100 ap 230KG', '10 Basonat HB 175 MP/X CN'], 'package': ['Steel drums', 'Steel drums'],
             'carrier': 'Golden Fortune Shipping Co. Ltd'}
            '''
            # for elem in list(resDict_1.keys()): #对resDict_1 格式{'classify_word':['',' ']}变为{'classify_word': ' '}
            #     resDict_2[elem]=select_list(resDict_1[elem])#取同一个classify word的最长字符
            # 对classify_word下的classify_word_1的classify_word_2进行合并
            for keys in list(resDict.keys()):
                res_str = ''  # 最终字符串
                if not resDict[keys]:
                    my_logger.error("error in pick word is null")
                    resultDict_title[keys] = resDict[keys]
                else:
                    if isinstance(resDict[keys][0], dict):  # 有classify_word_1的情况
                        tm_dict = {}
                        for elem in resDict[keys]:
                            tm_dict.update(elem)
                        tmp_list = []
                        for elem in sorted(tm_dict.keys()):  # 对classify_word_1，classify_word_2按照顺序进行排序，按序做累加
                            if isinstance(resDict_1[elem], list):
                                print(tmp_list)
                                print(resDict_1[elem])
                                tmp_list = add_list(tmp_list, resDict_1[elem])
                            else:
                                res_str += resDict_1[elem]
                        if res_str:
                            resultDict_title[keys] = res_str
                        else:
                            resultDict_item[keys] = tmp_list
                        # resultDict_title[keys] = res_str
                        # resultDict_item[keys] = tmp_list
                    else:  # 为字符串时
                        if isinstance(resDict[keys], list):
                            resultDict_item[keys] = resDict[keys]  # 取同一个classify word的最长字符
                        else:
                            resultDict_title[keys] = resDict[keys]
            print(resDict)
            for elem in resultDict_item:
                resultDict_item[elem] = del_last_null(resultDict_item[elem])
            print(resultDict_item, resultDict_title)
            if ac_docu_type /(len(ruleList_item) + len(ruleList_list)) >0.5: #有大于50%个关键词找不到 或 超出边框的excel的sheet表的次数门限，直接丢弃该sheet页的提取
                my_logger.error('the num of finding without key word %d,maybe document type is wrong'%ac_docu_type)
            else:
                tmp = self.custom_normal_encap(resultDict_title,resultDict_item, self.document_type)
                out_res.append(tmp)
        return out_res

    def custom_normal_encap(self,input_title,input_item,doc_type):
        title = input_title
        item = input_item
        out_res ={}
        total_nw = 0
        total_num = 0
        total_gw = 0
        declPrice = [] #单价 ammount/nw
        if 'num' in item :
            for elem in item['num']:
                if elem:
                    total_num += int(elem)
        if 'nw' in item:
            i = 0
            for elem in item['nw']:
                if elem =='':
                    elem = title['total_num'] #数量为空，就去title的总数量
                    item['nw'][i] = title['total_num']
                total_nw += float(elem)
                ava = float(item['amount'][i])/float(elem)
                declPrice.append(str(Decimal('%.4f'%ava)))
        if 'gw' in item:
            for elem in item['gw']:
                total_gw += float(elem)
        if 'total_num' in title:
            if total_num !=  int(title['total_num']):
                my_logger.error('total num is not equal file:%d, cacu:%d' %(int(title['total_num']),total_num))
        else:
            title['total_num'] = total_num
        if 'total_nw' in title:
            if total_nw !=  float(title['total_nw']):
                my_logger.error('total nw is not equal file:%d, cacu:%d' %(float(title['total_nw']),total_nw))
        else:
            title['total_num'] = total_nw
        if 'total_gw' in title:
            if total_gw !=  float(title['total_gw']):
                my_logger.error('total gw is not equal file:%d, cacu:%d' %(float(title['total_gw']),total_gw))
        else:
            title['total_gw'] = total_gw
        if 'declPrice' not in item:
            item['declPrice'] = declPrice
        out_res = {'title': title, 'item': item, 'type': doc_type}
        return out_res

    def request_encap(self,input_title,input_item): #fms录入封装
        out_res ={}
        out_title = input_title
        out_item_tmp = input_item
        #print ('out item tmp',out_item_tmp)
        for i in range( len(input_item['Goods_EN'])-len(out_item_tmp['Class'])) :
            out_item_tmp['Class'].extend([''])  #对于在1页有多个危险品，其关键词在页中不存在是，只能这样补齐
        if not input_title or not input_item:
            my_logger.error('the error extract is null')
            return out_res
        # print(out_item_tmp)
        l = len( input_item[sorted(input_item.keys())[0]])  #取第一个元素长度
        list_cbm =[]
        for elem in  input_item.keys():  #检查所有产品长度相等
            if l != len(input_item[elem]):
                my_logger.error('get product list error:'+ str( input_item ) )
            list_cbm.append("")
        list_cbm[0] =  input_title['CBM'] #"Dan_Cbm":["10000"], #只填一个总的
        out_item_tmp["Dan_Cbm"] =list_cbm
        list_tmp =[]
        for elem in out_item_tmp["Dan_Gw"]: #['7,912.800+324.000']
            list_tmp.append(eval(elem.replace(",","")))
        out_item_tmp["Dan_Gw"] = list_tmp
        dg = 'N'
        for elem in input_item['Class']:
            if elem:
                dg ="Y"
        out_title['B_Danger'] = dg
        out_title['ETD'] = time_format(out_title['ETD'])
        out_title['ETA'] = time_format(out_title['ETA'])
        package = input_item['package'][0]
        for elem in input_item['package']:
            if elem != package:
                package = 'Package'
        out_title['Pkgs_Unit'] = package
        out_title['Booking_Month'] = booking_month(out_title['ETD'])
        #'Container_Quantity': '1+' 标注是最多两个箱子 ,'container_t': '20+','Container_Type': ['20', '20', '20']
        con_tt = input_title['container_t'].strip("+").split("+")
        reslist = []
        print(con_tt,out_item_tmp)
        for i in range(len(con_tt)):
            out_item ={}
            if not con_tt[i]: #当为空停止
                break
            out_item['Container_Type'] = con_tt[i]
            out_item['Container_Quantity'] = input_title['Container_Quantity'].split("+")[i]
            out_item['Goods'] = input_item_res(con_tt[i],out_item_tmp) #含有该箱型的商品列表
            reslist.append(out_item)
        out_res = {'title':out_title,'item':reslist,'type':'BOOKING REQUEST'}
        print(out_res)
        return out_res

    def shipping_encap(self,input_title,input_item): #fms录入封装
        out_title = input_title
        #print ('out item tmp',out_item_tmp)
        if not input_title or not input_item:
            my_logger.error('the error extract is null')
            return out_title
        out_title['Notify'] = list_to_str(input_item['Notify'])
        out_title['Notify_P'] = del_null_list(input_item['Notify_P'])[-1]
        out_title['Notify_Addr'] = del_null_list(input_item['Notify_Addr'])[-1]
        out_title['Product_En'] = list_to_str(input_item['Product_En']).replace('®','')
        out_title['Marking'] = list_to_str(input_item['Marking']).replace('....','China')  #basf shipping特殊处理
        out_title['Consignee'] = del_null_list(input_item['Consignee'])[-1]
        out_title['Consignee_P'] = del_null_list(input_item['Consignee_P'])[-1].replace("TO THE ORDER OF ",'')
        out_title['Consignee_Addr'] = del_null_list(input_item['Consignee_Addr'])[-1]
        out_title['Remark'] = input_title['Docu_Type'] + '\n'+ del_null_list(input_item['Remark'])[-1]
        out_res ={'title':out_title,'item':[],'type':'SHIPPING INSTRUCTIONS'}
        if len(out_title['Consignee'].split("\n"))>=2:
            out_title['Consignee_P2'] = out_title['Consignee'].split("\n")[1]
        else:
            out_title['Consignee_P2'] =''
        return out_res

def list_to_str(list_1):
    #对于list不同元素相加为字符串
    if len(list_1)<1:
        my_logger.warning('list is null')
        return  ''
    elif len(list_1)==1:
        return  list_1[0]
    else:
        res =''
        for elem in list_1:
            if not elem:
                continue
            if elem not in res:
                res = res + elem+ '\n'
        return res
def del_null_list(list_1): #去掉list中的空字符
    list_2 = ['']
    for elem in list_1:
        if not elem:
            continue
        else:
            list_2.append(elem)
    return  list_2
def del_last_null(list_1): #去掉结尾的list中结尾为"" 元素
    list_2 =list_1
    str = list_2.pop()
    while str ==''and list_2:
        str = list_2.pop()
    list_2.append(str)
    return  list_2

def input_item_res(con_t,input_item):
    #con—t箱号类型，返回箱号类型的产品列表的字典
    res_dict = {}
    for elem in input_item.keys():
        res_dict[elem] =[]  #初始化
    for i in range(len(input_item[sorted(input_item.keys())[0]])):
        if con_t == input_item['Container_Type'][i]:
            for elem in input_item.keys():
                res_dict[elem].append(input_item[elem][i])
    return  res_dict
def time_format(time1,type=1):
    #15.06.2019 type =1
    #06.15.2019 type =2
    #输出2019-06-15
    if '.' in time1:
        tlist = time1.split('.')
        if type ==1:
            if len(tlist[2])==4:
                out_time = tlist[2]+"-" +tlist[1]+"-"+tlist[0]
        elif type ==2:
            if len(tlist[2])==4:
                out_time = tlist[2]+"-" +tlist[0]+"-"+tlist[1]
        else:
            out_time = time1.replace('.','-') #2019.06.15
    else:
        out_time = time1
    return out_time

def booking_month(datetime):
    #2019 - 06 - 15；2019-7-25
    #out：201906，201908
    time_list = datetime.split('-')
    if time_list[2] >= '25':
        mon = int(time_list[1])+1
    else:
        mon = int(time_list[1])
    if mon < 10:
        mon_str = '0'+str(mon)
    else:
        mon_str = str(mon)
    return  time_list[0]+mon_str



def tmp():
    #处理basf的映射关系
    pathfile='../set_rules/pdf_files/basf/com.pdf'
    pdf = pdfplumber.open(pathfile)
    pgs = pdf.pages
    res =pgs[0].extract_table()
    list_a = []
    for elem_list in res:
        list1 =[]
        for elem in elem_list:
            list1.append(elem.replace('\xa0',' ').replace(',',''))
        list_a.append(list1)

    print (list_a)

def main_title_item(company,path):
    sql = """select * from config where company = '{}' and type='fms'""".format(company)
    bt = BasTls()
    cnn = bt.conn()
    rows, columns = bt.query(cnn, sql)
    for row in rows:
        document_type = row[2]
        idf = identify_title_item(company, document_type)
        title, item = idf.pathTodata(path)
        if not title:
            continue
        if document_type =='BOOKING REQUEST':
            res = idf.request_encap(title, item)
            res = check_company(res)
        elif document_type =='SHIPPING INSTRUCTIONS':
            res = idf.shipping_encap(title, item)

        if res:
            return  res



if __name__ == '__main__':
    from contr.identify_process import check_company
    from contr.save_result import save_xls_res,save_xls_custom_res
    # path = './pdf_files/model0.pdf'
    # document_type = '送货单'
    # company = '罗门哈斯国际贸易（上海）有限公司'
    # company = '阿克苏诺贝尔化学品（博兴）有限公司'
    # path = '../set_rules/pdf_files/aks/aks_boxin.pdf'
    # document_type = '发货通知单'
    # company = '宣伟(上海)涂料有限公司'
    # path = '../set_rules/pdf_files/dm/shhai.pdf'
    # document_type = '出货单'
    # company = '宣伟(上海)涂料有限公司'
    # document_type = 'Delivery Note'
    # path = '../set_rules/pdf_files/dm/shhai.pdf'
    # company = '罗门哈斯国际贸易（上海）有限公司'
    # document_type = '送货单'
    # path = '../set_rules/pdf_files/lmhs/data30.pdf'
    company = '巴斯夫(中国)'
    document_type = '出货单'
    path = '../set_rules/pdf_files/basf/data05.pdf'
    # path = '../set_rules/pdf_files/basf/basf.pdf'
    # company = 'PPG 天津涂料'
    # document_type = 'Delivery Docket'
    # path = '../set_rules/pdf_files/ppg/tj.pdf'
    # company = 'basf'
    document_type = 'BOOKING REQUEST'
    path = '../set_rules/pdf_files/basf_ex/request4.pdf'
    company = 'basf'
    # document_type = 'SHIPPING INSTRUCTIONS'
    # path = '../set_rules/pdf_files/basf_ex/shipping5.pdf'
    # path = '../set_rules/pdf_files/basf_ex/booking2.pdf'
    # # idf = identify_title(company, document_type)
    # company = '巴斯夫（中国）有限公司'
    # document_type = '备 货 单'
    # path = '../set_rules/pdf_files/basf/basf2.pdf'
    # # company = '宣伟'
    # document_type = '出货单'
    # path = '../set_rules/pdf_files/dm/shhai.pdf'
    #
    # company = '伟迪捷（上海）标识技术有限公司'
    # document_type = '提货单'
    # path = '../set_rules/pdf_files/wdj/wdj4.pdf'
    # company = '伟迪捷（上海）标识技术有限公司'
    # document_type = '提货单'
    # path = '../set_rules/pdf_files/wdj/linx.pdf'
    # document_type = '进口货物报关单'
    # path = '../set_rules/pdf_files/custom/mw.xlsx'
    company = 'china'
    document_type = '出口货物报关单'
    path = '../set_rules/pdf_files/custom/bgd_1.xlsx'
    path = '../set_rules/pdf_files/custom/201900762.xlsx'
    # company = 'china'
    # document_type = '出口货物报关单'
    # company = 'china_q'
    # path = '../set_rules/pdf_files/custom/bgd2.xlsx'
    document_type = 'INVOICE'
    company = 'yongyu'
    path = '../set_rules/pdf_files/custom/bgd2_invoice.xlsx'

    # document_type = 'BOOKING ADVICE'
    # path = '../set_rules/pdf_files/森璞/sp.xls'
    # company = '安吉森璞'
    # document_type = '外仓进库单'
    # path = '../set_rules/pdf_files/pp/PP进仓.xlsx'
    # company = 'ppg_in'
    # idf = identify_title(company, document_type)
    # res=  idf.pathTodata(path)
    # print(res)
    # document_type = '进口货物报关单'
    # company = '艾仕得_in'
    # path = '../set_rules/pdf_files/custom/mw1.xlsx'

    # document_type = '进口货物报关单'
    # company = 'mw_in'
    # path = '../set_rules/pdf_files/custom/mw2.xlsx'
    idf = identify_title_item(company, document_type)
    res = idf.pathTodata(path)
    # print(title,item)
    # res = idf.shipping_encap(title,item)
    # res = idf.request_encap(title,item) #海运需要的
    # res_new = check_company(res)  #海运需要的
    # res = idf.custom_normal_encap(title,item,document_type)
    print(res)
    i =0
    for elem in res:
        save_xls_res(elem,os.path.dirname(path),os.path.basename(path).split('.')[0]+str(i))
        i +=1
    # save_xls_custom_res(res, os.path.dirname(path), os.path.basename(path).split('.')[0])

    # tmp()
    #print(data2)

