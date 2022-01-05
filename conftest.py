import json
import random

import pytest
import requests


# 获取token令牌
@pytest.fixture()
def fp_token():
    token_url='http://pre.passport.suuyuu.cn/oauth/token'
    token_data={'grant_type':'client_credentials',
                'client_id':'10000249',
                'client_secret':'ccd2db898bad47a886f3ed99927a4268'}
    token_head={'Content-Type':'application/x-www-form-urlencoded'}
    datas=requests.post(token_url,data=token_data,headers=token_head)
    print('查看请求：{}'.format(datas.text))
    return datas.json()['access_token']

# 获取浏览器令牌
@pytest.fixture()
def get_date():
    token_url='http://pre.passport.suuyuu.cn/oauth/token'
    token_params={'grant_type':'password',
                  'client_id':'10000169',
                  'client_secret':'39a0feca6d3b4f739d733797e33179e4',
                  'username':'17802711551',
                  'password':'ts123456'}
    token_headers={'Content-Type':'application/x-www-form-urlencoded'}
    token=requests.post(token_url,data=token_params,headers=token_headers)
    print(token.json())
    return token.json()['access_token']

# 获取平台商品数据
@pytest.fixture()
def fp_prodlist(get_date):
    get_product_url='http://pre-console-fp-admin.suuyuu.cn/api/ProductSecretPrice/GetMemberSecretPriceDetailList'
    get_product_data={'pageIndex':'1',
                      'pageSize':'30',
                      'productSpGroupId':'null',
                      'memberCode':'9079788',
                      'memberName':'木易-pre商户测试',
                      'memberId':'f240ef35-bed2-446a-ba50-b55fffd5a4f4',
                      'saleStatus':'2',
                      'clientId':'10000079',
                      'appName':'充值API'}
    get_product_head={'MerchantId':'64cf60f0-d5d3-449b-95a2-03db1c640ace',
                      'Content-Type':'application/json; charset=utf-8',
                      'authorization': 'Bearer {}'.format(get_date)}
    get_prods=requests.post(get_product_url,data=json.dumps(get_product_data),headers=get_product_head)
    print('查看获取的平台商品数据{}'.format(get_prods.json()['data']['list'][(int(random.randint(1,25)))]['productId']))
    return get_prods.json()['data']['list'][(int(random.randint(1,25)))]['productId']