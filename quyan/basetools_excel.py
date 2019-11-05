import pymysql
import json
import pdfplumber
import  xlrd
import  re
import datetime
from comm.log import  my_logger
from setting import *
"""modified 2019/4/11 为巴斯夫修改了按照库位WH水平分割元素，硬编码"""

ROW_DIS = 5 #最小行距
COL_DIS = 5 #最小列距离

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

class BasTls(object):
    def conn(self,type='rule'):
        # if type=='rule':
        #     cnn = pymysql.connect('10.2.16.46', 'root', 'Mwclg_2018', 'RPA',charset='utf8')
        # else:
        #     cnn = pymysql.connect('10.2.11.188', 'root', '123456', 'AMMS')
        cnn = pymysql.connect(host=SQL_HOST, port =SQL_PORT,user= SQL_USER,password= SQL_PWD, database ='RPA', charset='utf8')
        print(SQL_HOST)
        return cnn
    def LinkSql(self, host=SQL_HOST, user=SQL_USER, password=SQL_PWD, database='RPA', port=3306):
        conn = pymysql.connect(host=SQL_HOST,port=SQL_PORT, user=SQL_USER, password=SQL_PWD, database='RPA', charset='utf8')
        # conn = pymysql.connect(host=host, user=user, password=password, database=database, port=port)
        cursor = conn.cursor()
        return conn, cursor
    def query(self, cnn, sql):
        cur = cnn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        columns = [column[0] for column in cur.description]
        return rows,columns
    def execute(self,cnn,sql):
        cur = cnn.cursor()
        try:
            cur.execute(sql)
            cnn.commit()
        except Exception as e:
            my_logger.error("insert mysql error %s" %e)
            cnn.rollback()
    # 执行sql语句

    def executeSql(self, cursor, sql):
        cursor.execute(sql)

    # 提交和关闭数据库
    def commitAndCloseSql(self, conn, cursor):
        conn.commit()
        conn.close()
        cursor.close()

        # 根据公司和订单类型 获取对应规则库数据， way默认为1，调取表头规则数据，不为1时调取产品表格信息

    def getRule(self, company, document_type):
        # sequence_no 按照序号排列，第一个list序号就默认为主键
        ruleList = []
        conn, cursor = self.LinkSql()
        self.executeSql(cursor,
                        "select * from ai_identify_rule where company = '{}' and document_type = '{}' and  ORDER BY sequence_no".format(
                            company, document_type))

        columns = [col[0] for col in cursor.description]
        for row in cursor.fetchall():
            ruleDict = dict(zip(columns, row))
            ruleList.append(ruleDict)
        self.commitAndCloseSql(conn, cursor)
        # print(ruleList)
        return ruleList

    def getRule_item_list(self, company, document_type, is_list=0):
        # sequence_no 按照序号排列，第一个list序号就默认为主键
        ruleList = []
        conn, cursor = self.LinkSql()
        exe_sql = "select * from ai_identify_rule where company = '{}' and document_type = '{}' and is_list={}  ORDER BY sequence_no".format(
            company, document_type, is_list)
        print(exe_sql)
        self.executeSql(cursor, exe_sql)

        columns = [col[0] for col in cursor.description]
        for row in cursor.fetchall():
            ruleDict = dict(zip(columns, row))
            ruleList.append(ruleDict)
        self.commitAndCloseSql(conn, cursor)
        # print(ruleList)
        return ruleList

    def lttodic(self,lt):
        l0 = lt[0]
        l1 = lt[1:]
        l = list(zip(*l1))
        return dict(zip(l0, l))
    def to_json(self,dic):
        return json.dumps(dic)
    def pdf_read(self,filePath):
        pdf = pdfplumber.open(filePath)
        return pdf
    def read(selfself,filePath,index =0):
        workbook = xlrd.open_workbook(filePath)
        sheet = workbook.sheet_by_index(index)
        return  sheet

    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            pass
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        return False
    def is_chinese(self,check_str):
        """判断一个unicode是否是汉字"""
        for uchar in check_str:
            if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
                return True
        return False

    def coded_decoding(self,hor,ver,no_empty):
        dct_hor = {}
        result = []
        for key,value in enumerate(hor[0]):
            dct_hor[key] = value
        for id in sorted(dct_hor):
            h = []
            h_l = dct_hor[id].split()
            for hh in h_l:
                hhh = hh.split('WH')
                if len(hhh)>1:
                    hhh[1] = 'WH'+hhh[1]
                h.extend(hhh)
            r = []
            dct_ver = {}
            i = 0
            while i < len(ver):
                l = {}
                abs_l = []
                for key,value in enumerate(ver[i]):
                    dct_ver[key] = value
                for j in sorted(dct_ver):
                    k = 0
                    if len(dct_ver[j].strip()) == 0:
                        continue
                    v_l = dct_ver[j].split()
                    for ll in v_l:
                        if ll in h:
                            k += 1
                    if k == len(v_l):
                        l[j] = dct_ver[j].replace('_', '').strip()
                if len(l.keys()) > 0:
                    kk = list(l.keys())
                    for k_l in kk:
                        abs_l.append(abs(id - k_l))
                    mi = min(abs_l)
                    mi_index = abs_l.index(mi)
                    r.append(l[kk[mi_index]])
                    # print(l[kk[mi_index]])
                i += 1
                dct_ver.clear()
                if len(r) < i:
                    r.append(' ')
            # print(r)
            if len([rr for rr in r if rr.strip() != '']) >= no_empty:
                result.append(r)
            else:
                r = []
        a = 0
        b = 0
        while a < len(result):
            while b < len(result[a]) - 1:
                if result[a][b] == ' ':
                    result[a][b] = result[a - 1][b]
                b += 1
            b = 0
            a += 1
        return (result)

    def loc_coordinate(self, filePath, key_word, document_type):
        flag = 0
        sheet = self.read(filePath)
        nrow = sheet.nrows
        ncol = sheet.ncols
        print(sheet.nrows,sheet.ncols)
        row_j = None  # 行数，用于辨别相对行数
        col_j = None  # 列数，用于区别列数
        if not key_word:
            my_logger.warn('key word is null')
            return row_j,col_j
        if not document_type:
            my_logger.error("document type is null")
            return row_j,col_j
        for row in  range(nrow):
            # print( sheet.row_values(j))
            for col in range(ncol):
                if compare_sheet_value(sheet,row,col,document_type):
                    flag =1
                    break
            if flag==1:
                break
        if flag==0:
            my_logger.error("document type is not contained %s" % document_type)
            print('error in document type')
            return row_j, col_j
        flag = 0
        for row in range(nrow):
            for col in range(ncol):
                if compare_sheet_value(sheet, row, col, key_word):
                    flag = 1
                    row_j = row
                    col_j = col
                    break
            if flag == 1:
                break
        print('key word loc',row_j,col_j)
        return row_j, col_j



    def loc_pick_word(self, filePath, key_word_rela,pick_word,relative):
        #key_word_rela 是关键词所在文档行与列
        #key_word是pick word，要返回截止到一个字符起始位,这里仅仅是pick word在一行的情况适用
        #pick word 不是整个文档去搜索，而是查找相对key word的范围 row:1 pick word在key word之后一行，col:1 在key word之后一个空格， 代表空格数
        flag = 0 #是否找到
        sheet = self.read(filePath)
        nrow = sheet.nrows
        ncol = sheet.ncols
        row_j = 0  # 行数，用于辨别相对行数
        col_j = 0  # 列数，用于区别列数
        # if not pick_word:
        #     my_logger.warn('pick word is null')
        #     return row_j,col_j
        # if not pick_word:
        #     return row_j,col_j
        re_row, re_col = 0, 0
        if relative:
            if 'row' in relative:  # 两种模式行位置
                re_row = int(relative.split(',')[0].split(':')[1] ) # relative格式row:2,col:3
            if 'col' in relative and 'row' not in relative:
                re_col = int( relative.split(',')[0].split(':')[1] )  # relative格式col:3
            elif 'col' in relative and 'row' in relative:
                re_col = int(relative.split(',')[1].split(':')[1] ) ##relative格式row:2,col:3

        if not key_word_rela[0]  and not key_word_rela[1] and pick_word: #key_word_rela[1]==0
            for row_j in range(nrow):
                col_j = 0
                for col_j in range(ncol):
                    if compare_sheet_value(sheet,row_j,col_j,pick_word):
                        flag =1
                        break
                if flag ==1:
                    break
            return row_j, col_j
        elif not key_word_rela[0]  and not key_word_rela[1] and  not pick_word: #key_word_rela[1]==0    都为空情况取去rela为绝对位置
            return re_row, re_col
        else:
            row = key_word_rela[0] + int(re_row)
            col = key_word_rela[1] + int(re_col)
            if row >=sheet.nrows:
                row = sheet.nrows-1
            if row <0:
                row =0
            if col >= sheet.ncols:
                col = sheet.ncols-1
            if col <0:
                col =0
            print ('kw rela,pick word,re row,re col',key_word_rela,pick_word,re_row,re_col)
            print(row,col)
            if compare_sheet_value(sheet,row,col,pick_word):
                flag =1
            if flag ==0:
                my_logger.warning('''the pick word is not in the document: %s''' % pick_word)
            return row, col


def get_sheet_value(she, row, col):
    # #cell_type ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
    # she是sheet，row，col,是被比较字符串 sheet的单元格值与字符串比较
    if row==None or col==None:
        return  ''
    if row > she.nrows or col>she.ncols:
        return ''
    pick_type = she.cell_type(row, col)
    pick_value = she.cell_value(row, col)

    flag = 0
    if pick_type == 3:
        pick_value = xlrd.xldate.xldate_as_datetime(she.cell(row, col).value, 0).strftime("%Y/%m/%d %H:%M")
    elif pick_type == 1:
        if not pick_value:
            pick_value = ''
        else:
            pick_value= pick_value.strip()
    elif pick_type == 2:
        if re.findall('\\.0$',str(pick_value)): #excel取出来就当成了.0浮点数
            pick_value = str(int(pick_value))
        else:
            pick_value = str(pick_value)
    elif pick_type == 0:
        pick_value =''
    else:
        my_logger.warning('error in type: %d' % pick_type)
    return  pick_value

def find_sheet_value(sheet,key_word):
    #查找kw 是否在sheet中
    nrow = sheet.nrows
    ncol = sheet.ncols
    flag =0
    row_j, col_j= None,None
    if not key_word:
        my_logger.warn('key word is null')
        return row_j,col_j
    for row in  range(nrow):
        # print( sheet.row_values(j))
        for col in range(ncol):
            if equal_sheet_value(sheet,row,col,key_word):
                flag = 1
                row_j, col_j = row, col
                #break #取最后面新的
        if flag==1:
            break
    if flag==0:
        for row in range(nrow):
            # print( sheet.row_values(j))
            for col in range(ncol):
                if compare_sheet_value(sheet,row,col,key_word):
                    flag =1
                    row_j, col_j = row,col
                    break  #取最新
            if flag==1:
                break
    if flag==0:
        my_logger.warning('not find the key word %s' %key_word)
    return row_j, col_j

def compare_sheet_value(she,row,col,pick_word):
    # #cell_type ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
    #she是sheet，row，col,是被比较字符串 sheet的单元格值与字符串比较
    if not pick_word:
        return False
    pick_type =she.cell_type(row,col)
    pick_value = she.cell_value(row, col)
    # print('element:',row,col,pick_word,pick_value,pick_type)
    if not pick_value:
        return  False
    flag =0
    if pick_type == 3:
        pick_value = xlrd.xldate.xldate_as_datetime(she.cell(row, col).value, 0)
        if compare_date(pick_value, pick_word):
            flag = 1
    elif pick_type == 1:
        # print(pick_value)
        if pick_word in pick_value:  # pick_value 为空情况也可以返回
            flag = 1
    elif pick_type == 2:
        if pick_word in str(pick_value):
            flag = 1
    elif pick_type ==0:
        flag =0
    else:
        my_logger.warning('error in type: %d' %pick_type)
    if flag ==1:
        #print('compare value',pick_value, pick_word)
        return True
    else:
        return False

def equal_sheet_value(she,row,col,pick_word):
    # #cell_type ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
    #she是sheet，row，col,是被比较字符串 sheet的单元格值与字符串比较
    if not pick_word:
        return False
    pick_type =she.cell_type(row,col)
    pick_value = she.cell_value(row, col)
    if not pick_value:
        return  False
    flag =0
    if pick_type == 3:
        pick_value = xlrd.xldate.xldate_as_datetime(she.cell(row, col).value, 0)
        if compare_date(pick_value, pick_word):
            flag = 1
    elif pick_type == 1:
        # print(pick_value)
        if pick_word == pick_value:  # pick_value 为空情况也可以返回
            flag = 1
    elif pick_type == 2:
        if pick_word == str(pick_value):
            flag = 1
    elif pick_type ==0:
        flag =0
    else:
        my_logger.warning('error in type: %d' %pick_type)
    if flag ==1:
        #print('equal value',pick_value, pick_word)
        return True
    else:
        return False

def compare_date(date_1,str1):
    #date_1是datetime格式，str是字符串，进行比较
    flag = 0
    if re.findall('\d+/\d+/\d+', str1) and ':' not in str1:
        date_2 = datetime.datetime.strptime(str1, "%Y/%m/%d")
        # date_2 = date_1.strftime("%Y/%m/%d")
        # print (date_1,date_2)
        if date_2 == date_1:
            flag = 1
    elif re.findall('\d+/\d+/\d+\s+\d+:\d+:\d+', str1):
        date_2 = datetime.datetime.strptime(str1, "%Y/%m/%d %H:%M:%S")
        if date_2 == date_1:
            flag = 1
    elif re.findall('\d+-\d+-\d+', str1) and ':' not in str1:
        date_2 = datetime.datetime.strptime(str1, "%Y-%m-%d")
        if date_2 == date_1:
            flag = 1
    elif re.findall('\d+-\d+-\d+\s+\d+:\d+:\d+', str1):
        date_2 = datetime.datetime.strptime(str1, "%Y-%m-%d %H:%M:%S")
        if date_2 == date_1:
            flag = 1
    # else:
    #     my_logger.error('the time formate is not match %s'%str1)
    #     print(date_1,date_1.strftime("%Y/%m/%d"))
    if flag ==1:
        return True
    else:
        return  False


if __name__ == '__main__':
    company = '启钥国际贸易（上海）有限公司'
    document_type = '备 货 单'
    filePath='D:/weiy/pdf/test/SH007717.xls'
    key_word = '备 货 单'
    st = BasTls()
    st.retrive_cargo(company,'产品编号')

    p

