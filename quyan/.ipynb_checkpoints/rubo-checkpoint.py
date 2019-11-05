{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 468,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from pandas import Series,DataFrame"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# RUBO2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 读取RUBO2(1).xlsx中Packlist-sheetname"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 469,
   "metadata": {},
   "outputs": [],
   "source": [
    "rubo2 = pd.read_excel('RUBO2(1).xlsx',sheet_name='Packlist',index_col=None,header=0,skiprows=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 470,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Packlist', 'LOG_TRAILER',\n",
       "       'CARRIER CODE', 'SAP HUB', 'Unnamed: 7', 'WMS SHIP DATE', 'CTNS',\n",
       "       'Unit', 'Window', 'SHIP TO', 'CRD date', 'PH date', 'PSST', 'ST NAME',\n",
       "       'SHIP_TO_PHONE_NBR ', 'Address1', 'Address2', 'Address3', 'Address4',\n",
       "       'Address5', 'Address6'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 470,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rubo2.columns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## rubo2_Packlist中筛选出需要的字段信息"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 471,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "rubo2.rename(columns={'Unnamed: 0':'产品代码',  'Packlist':'客户运单号','Unnamed: 7':'目的省份',\\\n",
    "                            'WMS SHIP DATE':'发货时间','CARRIER CODE':'运输类型','CTNS':'预计箱数',\\\n",
    "                            'Unit':'预计发货','SHIP TO':'客户代码'},inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 472,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>客户运单号</th>\n",
       "      <th>产品代码</th>\n",
       "      <th>目的省份</th>\n",
       "      <th>ST NAME</th>\n",
       "      <th>发货时间</th>\n",
       "      <th>预计箱数</th>\n",
       "      <th>客户代码</th>\n",
       "      <th>Window</th>\n",
       "      <th>Address1</th>\n",
       "      <th>Address2</th>\n",
       "      <th>Address3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10006325</td>\n",
       "      <td>FW</td>\n",
       "      <td>辽宁</td>\n",
       "      <td>陈秀琴 13644099578</td>\n",
       "      <td>19/10/17</td>\n",
       "      <td>1</td>\n",
       "      <td>5088269</td>\n",
       "      <td>W3</td>\n",
       "      <td>NaN</td>\n",
       "      <td>大连市甘井子区</td>\n",
       "      <td>橄榄季哲林北园39-2-7-1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10005878</td>\n",
       "      <td>FW</td>\n",
       "      <td>辽宁</td>\n",
       "      <td>滔搏企业发展(上海)有限</td>\n",
       "      <td>19/10/17</td>\n",
       "      <td>5</td>\n",
       "      <td>5074496</td>\n",
       "      <td>W3</td>\n",
       "      <td>公司东北沈阳自营NON-CLC</td>\n",
       "      <td>沈阳市东陵区兰台路19号百丽仓库</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10006164</td>\n",
       "      <td>FW</td>\n",
       "      <td>辽宁</td>\n",
       "      <td>滔搏沈阳沈河区恒隆JOR</td>\n",
       "      <td>19/10/17</td>\n",
       "      <td>41</td>\n",
       "      <td>5084128</td>\n",
       "      <td>W3</td>\n",
       "      <td>DAN-L1_A0276</td>\n",
       "      <td>沈阳市东陵区兰台路19号百丽仓库</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      客户运单号 产品代码 目的省份          ST NAME      发货时间  预计箱数     客户代码 Window  \\\n",
       "0  10006325   FW   辽宁  陈秀琴 13644099578  19/10/17     1  5088269     W3   \n",
       "1  10005878   FW   辽宁     滔搏企业发展(上海)有限  19/10/17     5  5074496     W3   \n",
       "2  10006164   FW   辽宁     滔搏沈阳沈河区恒隆JOR  19/10/17    41  5084128     W3   \n",
       "\n",
       "          Address1          Address2         Address3  \n",
       "0              NaN           大连市甘井子区  橄榄季哲林北园39-2-7-1  \n",
       "1  公司东北沈阳自营NON-CLC  沈阳市东陵区兰台路19号百丽仓库              NaN  \n",
       "2     DAN-L1_A0276  沈阳市东陵区兰台路19号百丽仓库              NaN  "
      ]
     },
     "execution_count": 472,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rubo2_col_list = ['客户运单号','产品代码','目的省份','ST NAME','发货时间','预计箱数','客户代码','Window','Address1','Address2','Address3']\n",
    "\n",
    "rubo2.loc[:2,rubo2_col_list]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# basedata.xlsx中的Sheet'CLC预报'和'客户信息表'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 读取Sheet'CLC预报"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 473,
   "metadata": {},
   "outputs": [],
   "source": [
    "basedata_CLC = pd.read_excel('basedata.xlsx',sheet_name='CLC预报',index_col=None,header=0,skiprows=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 474,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['总单号', 'BU', '发货单号', '发货时间', '出发城市', '目的城市', '客户代码', '卸货地址', '箱数', '件数',\n",
       "       '陆运/铁运/空运', '在途时间', '预计到达时间', '状态', '承运商(包括干线商和终端运输商)', '实际签收时间',\n",
       "       '跟踪备注', '托运单备注', '第1天', '第2天', '第3天', '第4天', '第5天', '第6天', '第7天', '第8天',\n",
       "       '第9天', '第10天', '第11天', '第12天', '第13天', '第14天', '第15天',\n",
       "       'Abnormal Issue 异常信息', '客户简称', '客户名称', '收货人', '联系方式', '联系人手机', '是否预报',\n",
       "       '预报人', '客户类型', 'Unnamed: 42', 'Unnamed: 43'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 474,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "basedata_CLC.columns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Sheet'CLC预报'中筛选出所需字段"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 475,
   "metadata": {},
   "outputs": [],
   "source": [
    "basedata_CLC.rename(columns={'发货单号':'客户运单号'},inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 476,
   "metadata": {},
   "outputs": [],
   "source": [
    "# '客户运单号'=‘发货单号’。‘BU’代表‘产品代码’，rubo2表中有这里没有提取\n",
    "basedata_CLC_col_list = ['总单号','客户运单号','出发城市','目的城市',\\\n",
    "                         '卸货地址','箱数','件数','陆运/铁运/空运','在途时间',\\\n",
    "                         '预计到达时间','客户简称','客户名称','收货人','联系方式','联系人手机']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 477,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>总单号</th>\n",
       "      <th>客户运单号</th>\n",
       "      <th>出发城市</th>\n",
       "      <th>目的城市</th>\n",
       "      <th>卸货地址</th>\n",
       "      <th>箱数</th>\n",
       "      <th>件数</th>\n",
       "      <th>陆运/铁运/空运</th>\n",
       "      <th>在途时间</th>\n",
       "      <th>预计到达时间</th>\n",
       "      <th>客户简称</th>\n",
       "      <th>客户名称</th>\n",
       "      <th>收货人</th>\n",
       "      <th>联系方式</th>\n",
       "      <th>联系人手机</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2019-10-16</td>\n",
       "      <td>10002166</td>\n",
       "      <td>太仓CLC</td>\n",
       "      <td>西安</td>\n",
       "      <td>西安市未央区谭家乡赵村工业园1号</td>\n",
       "      <td>3</td>\n",
       "      <td>62</td>\n",
       "      <td>公路</td>\n",
       "      <td>4</td>\n",
       "      <td>2019-10-21</td>\n",
       "      <td>西安好孩子</td>\n",
       "      <td>好孩子(中国)商贸有限公司</td>\n",
       "      <td>乔爱凤</td>\n",
       "      <td>13572482329/乔爱凤 13572482329/13572482329</td>\n",
       "      <td>13572482329</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2019-10-16</td>\n",
       "      <td>10002742</td>\n",
       "      <td>太仓CLC</td>\n",
       "      <td>西安</td>\n",
       "      <td>西安市长安区引镇现代物流园百丽物流中心C2库</td>\n",
       "      <td>2</td>\n",
       "      <td>40</td>\n",
       "      <td>公路</td>\n",
       "      <td>4</td>\n",
       "      <td>2019-10-21</td>\n",
       "      <td>西安滔搏</td>\n",
       "      <td>滔搏企业发展(上海)有限公司</td>\n",
       "      <td>周利飞</td>\n",
       "      <td>029-84350067/15891776079//029-84350067</td>\n",
       "      <td>15891776079</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2019-10-16</td>\n",
       "      <td>10002680</td>\n",
       "      <td>太仓CLC</td>\n",
       "      <td>沈阳</td>\n",
       "      <td>沈阳市东陵区兰台路19号百丽仓库</td>\n",
       "      <td>37</td>\n",
       "      <td>413</td>\n",
       "      <td>公路</td>\n",
       "      <td>4</td>\n",
       "      <td>2019-10-21</td>\n",
       "      <td>沈阳滔搏</td>\n",
       "      <td>滔搏企业发展(上海)有限公司</td>\n",
       "      <td>倪继航</td>\n",
       "      <td>倪继航13998326980/024-31808509(仓库数据)娄先生/152040543...</td>\n",
       "      <td>15204054378</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         总单号     客户运单号   出发城市 目的城市                    卸货地址  箱数   件数 陆运/铁运/空运  \\\n",
       "0 2019-10-16  10002166  太仓CLC   西安        西安市未央区谭家乡赵村工业园1号   3   62       公路   \n",
       "1 2019-10-16  10002742  太仓CLC   西安  西安市长安区引镇现代物流园百丽物流中心C2库   2   40       公路   \n",
       "2 2019-10-16  10002680  太仓CLC   沈阳        沈阳市东陵区兰台路19号百丽仓库  37  413       公路   \n",
       "\n",
       "  在途时间     预计到达时间   客户简称            客户名称  收货人  \\\n",
       "0    4 2019-10-21  西安好孩子   好孩子(中国)商贸有限公司  乔爱凤   \n",
       "1    4 2019-10-21   西安滔搏  滔搏企业发展(上海)有限公司  周利飞   \n",
       "2    4 2019-10-21   沈阳滔搏  滔搏企业发展(上海)有限公司  倪继航   \n",
       "\n",
       "                                                联系方式        联系人手机  \n",
       "0            13572482329/乔爱凤 13572482329/13572482329  13572482329  \n",
       "1             029-84350067/15891776079//029-84350067  15891776079  \n",
       "2  倪继航13998326980/024-31808509(仓库数据)娄先生/152040543...  15204054378  "
      ]
     },
     "execution_count": 477,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "basedata_CLC.loc[:2,basedata_CLC_col_list]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 读取Sheet'客户信息表'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 478,
   "metadata": {},
   "outputs": [],
   "source": [
    "basedata_Customersinfo = pd.read_excel('basedata.xlsx',sheet_name='客户信息表',index_col=None,header=0,skiprows=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 479,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['-', '客户名称', '客户简称', '客户英文名称', '客户类型', '备注', '详细地址', '城市', '省份', '电话1',\n",
       "       '手机预报', '电话2', '电话-2011', '联系人'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 479,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "basedata_Customersinfo.columns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Sheet'客户信息表'中筛选出所需字段"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 480,
   "metadata": {},
   "outputs": [],
   "source": [
    "basedata_Customersinfo.rename(columns={'-':'客户代码'},inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 481,
   "metadata": {},
   "outputs": [],
   "source": [
    "basedata_Customersinfo_col_list = ['客户代码','详细地址','城市','省份','电话1','手机预报','电话2','电话-2011','联系人']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 482,
   "metadata": {},
   "outputs": [],
   "source": [
    "basedata_Customersinfo.客户代码=basedata_Customersinfo.客户代码.astype(str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 483,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>客户代码</th>\n",
       "      <th>详细地址</th>\n",
       "      <th>城市</th>\n",
       "      <th>省份</th>\n",
       "      <th>电话1</th>\n",
       "      <th>手机预报</th>\n",
       "      <th>电话2</th>\n",
       "      <th>电话-2011</th>\n",
       "      <th>联系人</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>5027246</td>\n",
       "      <td>浙江省湖州市德清县新安镇勾里村金恒路10-20号B1区</td>\n",
       "      <td>湖州</td>\n",
       "      <td>NaN</td>\n",
       "      <td>15868139680</td>\n",
       "      <td>15868139680</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>丁龙龙</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5034719</td>\n",
       "      <td>浙江省湖州市德清县新安镇勾里村金恒路10-20号B1区</td>\n",
       "      <td>湖州</td>\n",
       "      <td>NaN</td>\n",
       "      <td>15868139680</td>\n",
       "      <td>15868139680</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>丁龙龙</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5038771</td>\n",
       "      <td>浙江省湖州市德清县新安镇勾里村金恒路10-20号B1区</td>\n",
       "      <td>湖州</td>\n",
       "      <td>NaN</td>\n",
       "      <td>15868139680</td>\n",
       "      <td>15868139680</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>丁龙龙</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      客户代码                         详细地址  城市   省份          电话1         手机预报  \\\n",
       "0  5027246  浙江省湖州市德清县新安镇勾里村金恒路10-20号B1区  湖州  NaN  15868139680  15868139680   \n",
       "1  5034719  浙江省湖州市德清县新安镇勾里村金恒路10-20号B1区  湖州  NaN  15868139680  15868139680   \n",
       "2  5038771  浙江省湖州市德清县新安镇勾里村金恒路10-20号B1区  湖州  NaN  15868139680  15868139680   \n",
       "\n",
       "   电话2 电话-2011  联系人  \n",
       "0  NaN     NaN  丁龙龙  \n",
       "1  NaN     NaN  丁龙龙  \n",
       "2  NaN     NaN  丁龙龙  "
      ]
     },
     "execution_count": 483,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "basedata_Customersinfo.loc[:2,basedata_Customersinfo_col_list]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 根据字段'客户运单号'合并表RUBO2_Packlist和表basedata_CLC预报"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 484,
   "metadata": {},
   "outputs": [],
   "source": [
    "rubo2.客户运单号 = rubo2.客户运单号.astype(str)\n",
    "basedata_CLC.客户运单号 = basedata_CLC.客户运单号.astype(str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 485,
   "metadata": {},
   "outputs": [],
   "source": [
    "merged_packlist_CLC = pd.merge(rubo2.loc[:,rubo2_col_list],basedata_CLC.loc[:,basedata_CLC_col_list],on='客户运单号')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 486,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "25"
      ]
     },
     "execution_count": 486,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 将merged_packlist_CLC_col_list的所有字段名保存到列表\n",
    "merged_packlist_CLC_col_list = merged_packlist_CLC.columns.tolist()\n",
    "len(merged_packlist_CLC_col_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 487,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['客户运单号',\n",
       " '产品代码',\n",
       " '目的省份',\n",
       " 'ST NAME',\n",
       " '发货时间',\n",
       " '预计箱数',\n",
       " '客户代码',\n",
       " 'Window',\n",
       " 'Address1',\n",
       " 'Address2',\n",
       " 'Address3',\n",
       " '总单号',\n",
       " '出发城市',\n",
       " '目的城市',\n",
       " '卸货地址',\n",
       " '箱数',\n",
       " '件数',\n",
       " '陆运/铁运/空运',\n",
       " '在途时间',\n",
       " '预计到达时间',\n",
       " '客户简称',\n",
       " '客户名称',\n",
       " '收货人',\n",
       " '联系方式',\n",
       " '联系人手机']"
      ]
     },
     "execution_count": 487,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merged_packlist_CLC_col_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 488,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 转换字段‘客户代码’数据的数据类型为str\n",
    "merged_packlist_CLC.客户代码=merged_packlist_CLC.客户代码.astype(str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 489,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>客户运单号</th>\n",
       "      <th>产品代码</th>\n",
       "      <th>目的省份</th>\n",
       "      <th>ST NAME</th>\n",
       "      <th>发货时间</th>\n",
       "      <th>预计箱数</th>\n",
       "      <th>客户代码</th>\n",
       "      <th>Window</th>\n",
       "      <th>Address1</th>\n",
       "      <th>Address2</th>\n",
       "      <th>...</th>\n",
       "      <th>箱数</th>\n",
       "      <th>件数</th>\n",
       "      <th>陆运/铁运/空运</th>\n",
       "      <th>在途时间</th>\n",
       "      <th>预计到达时间</th>\n",
       "      <th>客户简称</th>\n",
       "      <th>客户名称</th>\n",
       "      <th>收货人</th>\n",
       "      <th>联系方式</th>\n",
       "      <th>联系人手机</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10006325</td>\n",
       "      <td>FW</td>\n",
       "      <td>辽宁</td>\n",
       "      <td>陈秀琴 13644099578</td>\n",
       "      <td>19/10/17</td>\n",
       "      <td>1</td>\n",
       "      <td>5088269</td>\n",
       "      <td>W3</td>\n",
       "      <td>NaN</td>\n",
       "      <td>大连市甘井子区</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>公路</td>\n",
       "      <td>4</td>\n",
       "      <td>2019-10-21</td>\n",
       "      <td>大连个人客户</td>\n",
       "      <td>个人客户</td>\n",
       "      <td>陈秀琴 13644099578/</td>\n",
       "      <td>13644099578</td>\n",
       "      <td>13644099578</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10005878</td>\n",
       "      <td>FW</td>\n",
       "      <td>辽宁</td>\n",
       "      <td>滔搏企业发展(上海)有限</td>\n",
       "      <td>19/10/17</td>\n",
       "      <td>5</td>\n",
       "      <td>5074496</td>\n",
       "      <td>W3</td>\n",
       "      <td>公司东北沈阳自营NON-CLC</td>\n",
       "      <td>沈阳市东陵区兰台路19号百丽仓库</td>\n",
       "      <td>...</td>\n",
       "      <td>5</td>\n",
       "      <td>24</td>\n",
       "      <td>公路</td>\n",
       "      <td>4</td>\n",
       "      <td>2019-10-21</td>\n",
       "      <td>沈阳滔搏</td>\n",
       "      <td>滔搏企业发展(上海)有限公司</td>\n",
       "      <td>倪继航</td>\n",
       "      <td>倪继航13998326980/024-31808509(仓库数据)娄先生/152040543...</td>\n",
       "      <td>15204054378</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10006164</td>\n",
       "      <td>FW</td>\n",
       "      <td>辽宁</td>\n",
       "      <td>滔搏沈阳沈河区恒隆JOR</td>\n",
       "      <td>19/10/17</td>\n",
       "      <td>41</td>\n",
       "      <td>5084128</td>\n",
       "      <td>W3</td>\n",
       "      <td>DAN-L1_A0276</td>\n",
       "      <td>沈阳市东陵区兰台路19号百丽仓库</td>\n",
       "      <td>...</td>\n",
       "      <td>41</td>\n",
       "      <td>318</td>\n",
       "      <td>公路</td>\n",
       "      <td>4</td>\n",
       "      <td>2019-10-21</td>\n",
       "      <td>沈阳滔搏</td>\n",
       "      <td>滔搏企业发展(上海)有限公司</td>\n",
       "      <td>倪继航</td>\n",
       "      <td>倪继航13998326980/024-31808509(仓库数据)娄先生/152040543...</td>\n",
       "      <td>15204054378</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3 rows × 25 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      客户运单号 产品代码 目的省份          ST NAME      发货时间  预计箱数     客户代码 Window  \\\n",
       "0  10006325   FW   辽宁  陈秀琴 13644099578  19/10/17     1  5088269     W3   \n",
       "1  10005878   FW   辽宁     滔搏企业发展(上海)有限  19/10/17     5  5074496     W3   \n",
       "2  10006164   FW   辽宁     滔搏沈阳沈河区恒隆JOR  19/10/17    41  5084128     W3   \n",
       "\n",
       "          Address1          Address2  ...  箱数   件数 陆运/铁运/空运 在途时间     预计到达时间  \\\n",
       "0              NaN           大连市甘井子区  ...   1    3       公路    4 2019-10-21   \n",
       "1  公司东北沈阳自营NON-CLC  沈阳市东陵区兰台路19号百丽仓库  ...   5   24       公路    4 2019-10-21   \n",
       "2     DAN-L1_A0276  沈阳市东陵区兰台路19号百丽仓库  ...  41  318       公路    4 2019-10-21   \n",
       "\n",
       "     客户简称            客户名称               收货人  \\\n",
       "0  大连个人客户            个人客户  陈秀琴 13644099578/   \n",
       "1    沈阳滔搏  滔搏企业发展(上海)有限公司               倪继航   \n",
       "2    沈阳滔搏  滔搏企业发展(上海)有限公司               倪继航   \n",
       "\n",
       "                                                联系方式        联系人手机  \n",
       "0                                        13644099578  13644099578  \n",
       "1  倪继航13998326980/024-31808509(仓库数据)娄先生/152040543...  15204054378  \n",
       "2  倪继航13998326980/024-31808509(仓库数据)娄先生/152040543...  15204054378  \n",
       "\n",
       "[3 rows x 25 columns]"
      ]
     },
     "execution_count": 489,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merged_packlist_CLC.loc[:2,merged_packlist_CLC_col_list]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 根据字段'客户代码'合并表merged_packlist_CLC和表basedata_客户信息表"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 490,
   "metadata": {},
   "outputs": [],
   "source": [
    "merged_allinfo = pd.merge(merged_packlist_CLC.loc[:,merged_packlist_CLC_col_list],basedata_Customersinfo.loc[:,basedata_Customersinfo_col_list],on='客户代码')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 调整字段数据的格式和表中字段的排列顺序"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 491,
   "metadata": {},
   "outputs": [],
   "source": [
    "merged_allinfo['发货时间'] = Series(map(lambda x:'{}'.format('20'+str(x)),merged_allinfo['发货时间']))\n",
    "\n",
    "merged_allinfo['客户运单号'] = Series(map(lambda x:'{:09}'.format(int(x)),merged_allinfo['客户运单号']))\n",
    "\n",
    "merged_allinfo['产品代码'] = Series(map(lambda x:'APP' if x=='AP' else x,merged_allinfo['产品代码']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 492,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>发货时间</th>\n",
       "      <th>客户运单号</th>\n",
       "      <th>陆运/铁运/空运</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2019/10/17</td>\n",
       "      <td>010005878</td>\n",
       "      <td>公路</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2019/10/17</td>\n",
       "      <td>010006164</td>\n",
       "      <td>公路</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2019/10/17</td>\n",
       "      <td>010006135</td>\n",
       "      <td>公路</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         发货时间      客户运单号 陆运/铁运/空运\n",
       "0  2019/10/17  010005878       公路\n",
       "1  2019/10/17  010006164       公路\n",
       "2  2019/10/17  010006135       公路"
      ]
     },
     "execution_count": 492,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merged_allinfo.loc[:2,['发货时间','客户运单号','陆运/铁运/空运']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 493,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 256 entries, 0 to 255\n",
      "Data columns (total 33 columns):\n",
      "客户运单号       256 non-null object\n",
      "产品代码        256 non-null object\n",
      "目的省份        256 non-null object\n",
      "ST NAME     256 non-null object\n",
      "发货时间        256 non-null object\n",
      "预计箱数        256 non-null int64\n",
      "客户代码        256 non-null object\n",
      "Window      256 non-null object\n",
      "Address1    222 non-null object\n",
      "Address2    256 non-null object\n",
      "Address3    196 non-null object\n",
      "总单号         256 non-null datetime64[ns]\n",
      "出发城市        256 non-null object\n",
      "目的城市        256 non-null object\n",
      "卸货地址        256 non-null object\n",
      "箱数          256 non-null int64\n",
      "件数          256 non-null int64\n",
      "陆运/铁运/空运    256 non-null object\n",
      "在途时间        256 non-null object\n",
      "预计到达时间      256 non-null datetime64[ns]\n",
      "客户简称        256 non-null object\n",
      "客户名称        256 non-null object\n",
      "收货人         256 non-null object\n",
      "联系方式        256 non-null object\n",
      "联系人手机       256 non-null object\n",
      "详细地址        256 non-null object\n",
      "城市          256 non-null object\n",
      "省份          228 non-null object\n",
      "电话1         250 non-null object\n",
      "手机预报        255 non-null object\n",
      "电话2         128 non-null object\n",
      "电话-2011     137 non-null object\n",
      "联系人         249 non-null object\n",
      "dtypes: datetime64[ns](2), int64(3), object(28)\n",
      "memory usage: 78.0+ KB\n"
     ]
    }
   ],
   "source": [
    "merged_allinfo.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 494,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['客户运单号', '产品代码', '目的省份', 'ST NAME', '发货时间', '预计箱数', '客户代码', 'Window',\n",
       "       'Address1', 'Address2', 'Address3', '总单号', '出发城市', '目的城市', '卸货地址', '箱数',\n",
       "       '件数', '陆运/铁运/空运', '在途时间', '预计到达时间', '客户简称', '客户名称', '收货人', '联系方式',\n",
       "       '联系人手机', '详细地址', '城市', '省份', '电话1', '手机预报', '电话2', '电话-2011', '联系人'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 494,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merged_allinfo.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 495,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "merged_allinfo = merged_allinfo.loc[:,['客户运单号','客户代码','客户简称', '客户名称', '收货人', '联系方式', '联系人手机',\\\n",
    "                      '卸货地址', '箱数', '件数', '在途时间', 'ST NAME','发货时间','预计到达时间','陆运/铁运/空运',\\\n",
    "                      '城市', '省份','出发城市', '目的城市','目的省份','产品代码','总单号']]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 写到Excel文件"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 496,
   "metadata": {},
   "outputs": [],
   "source": [
    "merged_allinfo.to_excel('mergedallinfo.xlsx')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "# 读取target模板.xlsx"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "target=pd.read_excel('target模板.xlsx',sheet_name='Sheet1',index_col=None,header=0,skiprows=1)"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "target_col_list=target.columns.tolist()\n",
    "# target_col_list"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "# 读取basedata.xlsx中sheet_name='CLC预报'"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "basedata_CLC = pd.read_excel('basedata.xlsx',sheet_name='CLC预报',index_col=None,header=0,skiprows=0)"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "basedata_CLC.columns"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "basedata_CLC.loc[:2,'总单号': '客户代码']"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "basedata_CLC.rename(columns={'发货单号':'客户运单号'},inplace=True)"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "basedata_CLC.loc[:2,'总单号': '客户代码']"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "# 设置basedata_CLC的'发货单号'列为basedata_CLC行索引 便于去basedata_CLC中的任意数据存储到rubo2中的运单号信息纪录对应的字段\n",
    "basedata_CLC = basedata_CLC.set_index('发货单号',drop=False)"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "basedata_CLC.loc[10002166:10002680,'总单号': '客户代码']"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "# 读取basedata.xlsx中sheet_name='客户信息表'"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "basedata_Customersinfo = pd.read_excel('basedata.xlsx',sheet_name='客户信息表',index_col=None,header=0,skiprows=0)"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "# 删除不需要的字段"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "rubo2.drop(['Unnamed: 1','Unnamed: 2'],axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "# 修改rubo2字段"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "rubo2 = pd.read_excel('RUBO2(1).xlsx',sheet_name='Packlist',index_col=None,header=0,skiprows=0)\n",
    "rubo2=rubo2.rename(columns={'Unnamed: 0':'产品代码',  'Packlist':'客户运单号','Unnamed: 7':'目的省份',\\\n",
    "                            'WMS SHIP DATE':'发货日期','CARRIER CODE':'运输类型','CTNS':'预计箱数',\\\n",
    "                            'Unit':'预计发货','SHIP TO':'客户代码'})\n",
    "# source_rubo2说明unit对应的应该是箱数，占用了'预计发货'的字段位置"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "# 合并，最后再调整数据格式\n",
    "packlist = Series(map(lambda x:'{:09}'.format(x),rubo2['客户运单号']))\n",
    "\n",
    "rubo2['客户运单号']=packlist\n",
    "\n",
    "rubo2['发货日期'] = Series(map(lambda x:'{}'.format('20'+str(x)),rubo2['发货日期']))\n",
    "\n",
    "rubo2['运输类型'] = Series(map(lambda x:'公路' if x=='RUBO' else '空运',rubo2['运输类型']))\n",
    "\n",
    "rubo2.head(2)"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "# 筛选出需要的字段信息"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "basedata_Customerinfo_col_list = ['客户代码','详细地址','城市','省份','电话1','手机预报','电话2','电话-2011','联系人']"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "rubo2=rubo2.loc[:2,]"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "# 根据外键‘客户运单号’合并rubo2和basedata_CLC"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "pd.merge(rubo2[:,rubo2_col_list],basedata_CLC[:,basedata_CLC_col_list])"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "rubo2"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "pd.merge(rubo2,basedata_CLC,on='客户运单号')"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "rubo2.loc[:2,'发货日期':'客户代码']"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "df1 = DataFrame({'a':range(5),'b':range(6,11)})\n",
    "df2 = DataFrame({'a':[0,1,2,4,3],'B':range(6,11)})"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "target = pd.read_excel('target模板.xlsx',sheet_name='Sheet1',index_col=None,header=0,skiprows=1)"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "target.insert(0,'packlist',packlist)"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "target.drop('客户代码',axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "target.head()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {
    "height": "708.182px",
    "left": "167px",
    "top": "258.293px",
    "width": "349.091px"
   },
   "toc_section_display": true,
   "toc_window_display": true
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
