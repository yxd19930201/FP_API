import pytest
import requests
import time
import json

class Test_Order():
    def setup(self):
        pass
    def teardown(self):
        pass

    # 获取自有商品的基本信息，包括：商品基本信息、商品销售策略显示情况、密价
    def test_get_product(self,fp_token,fp_prodlist):
        get_product_url='http://pre-sup-fp-order-interface-api.suuyuu.cn/api/OrderCommon/GetValidateProductInfo'
        get_product_data ={
          "productId": fp_prodlist,
          "memberId": "f240ef35-bed2-446a-ba50-b55fffd5a4f4",
          "clientId": "10000079",
          "fromCache": "true"
        }
        get_product_head={'authorization':'Bearer {}'.format(fp_token),
                          'Content-Type':'application/json; charset=utf-8'}
        get_productlist=requests.post(get_product_url,data=json.dumps(get_product_data),headers=get_product_head)
        print(get_productlist.text)
        print(get_productlist.json()['data']['id'])
        print(get_productlist.headers)
        productid=get_productlist.json()['data']['id']
        assert productid

    # 匹配平台话费商品
    @pytest.mark.parametrize('chargePhone',[('1371499115')])
    def test_Phone_Product(self,fp_token,chargePhone):
        phone_url='http://pre-sup-fp-order-interface-api.suuyuu.cn/api/OrderCommon/GetMatchPhoneProduct'
        phone_data={'virtualOperator':'移动',
                    'operatorName':'中国移动',
                    'area':'广东',
                    'chargeValue':'100',
                    'chargePhone':chargePhone,
                    'memberId':'b72aaf46-70c7-4dfa-820d-429582a0b58e',
                    'clientId':'10000079',
                    'fromCache':'true'}
        phone_head={'authorization':'Bearer {}'.format(fp_token),
                    'Content-Type':'application/json; charset=utf-8'}
        getphone_data=requests.post(phone_url,data=json.dumps(phone_data),headers=phone_head)
        print(getphone_data.json()['data']['id'])
        phoneid=getphone_data.json()['data']['id']
        assert phoneid


    # 匹配平台流量商品
    @pytest.mark.parametrize('chargePhone',[('13714199115')])
    def test_Traffic_product(self,fp_token,chargePhone):
        Traffic_url='http://pre-sup-fp-order-interface-api.suuyuu.cn/api/OrderCommon/GetMatchTrafficProduct'
        Traffic_data={'operatorName':'中国移动',
                      'area':'广东',
                      'chargeValue':'1024',
                      'chargePhone':chargePhone,
                      'packetKind':'4',
                      'memberId':'b72aaf46-70c7-4dfa-820d-429582a0b58e',
                      'clientId':'10000079',
                      'fromCache':'true'}
        Traffic_head={'authorization':'Bearer {}'.format(fp_token),
                    'Content-Type':'application/json; charset=utf-8'}
        Traffic_datas=requests.post(Traffic_url,data=json.dumps(Traffic_data),headers=Traffic_head)
        print(Traffic_datas.json()['data']['id'])
        Traffic_product=Traffic_datas.json()['data']['id']
        assert Traffic_product


    # 获取推广大使和合作伙伴价格
    @pytest.mark.parametrize('OrderId',[('22010415086611931519')])
    def test_AndStrategy_Price(self,fp_token,OrderId):
        AndStrategy_Price_url='http://pre-sup-fp-order-interface-api.suuyuu.cn/api/Product/GetPromoterAndStrategyFellowPrice'
        AndStrategy_Price_data={'DealerMemberId':'f240ef35-bed2-446a-ba50-b55fffd5a4f4',
                                'FpMemberId':'64cf60f0-d5d3-449b-95a2-03db1c640ace',
                                'ProductId':'17033310',
                                'SupProductId':'500001925',
                                'FpIsStrategyFellow':'false',
                                'OrderId':OrderId}
        AndStrategy_Price_head={'authorization':'Bearer {}'.format(fp_token),
                                'Content-Type':'application/json; charset=utf-8'}
        get_AndStrategy_data=requests.get(AndStrategy_Price_url,params=AndStrategy_Price_data,headers=AndStrategy_Price_head)
        print(get_AndStrategy_data.json()['data']['barginPrice'])
        barginPrice=get_AndStrategy_data.json()['data']['barginPrice']
        assert barginPrice



    # 获取商品池商品
    def test_fp_Product(self,fp_prodlist,fp_token):
        fp_Product_url='http://pre-sup-fp-order-interface-api.suuyuu.cn/api/Product/GetProduct'
        fp_Product_data={'id':fp_prodlist,
                         'fromCache':'true'}
        fp_Product_head={'authorization':'Bearer {}'.format(fp_token),
                        'Content-Type':'application/json; charset=utf-8'}
        fp_Product_data=requests.post(fp_Product_url,data=json.dumps(fp_Product_data),headers=fp_Product_head)
        print(fp_Product_data.text)
        fp_Productid=fp_Product_data.json()['data']['id']
        assert fp_Productid


    # 获取平台商品信息
    def test_ProductPool_List(self,fp_token):
        ProductPool_List_url='http://pre-sup-fp-order-interface-api.suuyuu.cn/api/Product/GetProductPoolList'
        ProductPool_List_data={'productType':'4',
                               'appointSupProductId':'500002184',
                               'memberId':'f240ef35-bed2-446a-ba50-b55fffd5a4f4',
                               'fpMemberId':'64cf60f0-d5d3-449b-95a2-03db1c640ace',
                               'productId':'10056598',
                               'faceValue':'0',
                               'groupId':'44327b38-c6bf-48ef-8fef-7b8503b4c2d6',
                               'orderId':'',
                               'invoiceType':'0'}
        ProductPool_List_head={'authorization':'Bearer {}'.format(fp_token),
                                'Content-Type':'application/json; charset=utf-8'}
        get_ProductPool_List=requests.post(ProductPool_List_url,data=json.dumps(ProductPool_List_data),headers=ProductPool_List_head)
        print(get_ProductPool_List.json()['data']['productPoolDataListModel'][0]['supProductName'])
        supProductName=get_ProductPool_List.json()['data']['productPoolDataListModel'][0]['supProductName']
        assert supProductName


    @pytest.mark.parametrize('expect',[('风控拦截订单价格校验成功')])
    def test_Verify_Control(self,fp_token,expect):
        Verify_Control_url='http://pre-sup-fp-order-interface-api.suuyuu.cn/api/OrderCommon/VerifyControl'
        Verify_Control_data={"orderId": "22010425041674781759",
                              "memberId": "f240ef35-bed2-446a-ba50-b55fffd5a4f4",
                              "fpMemberId": "64cf60f0-d5d3-449b-95a2-03db1c640ace",
                              "supProductId": 500002382,
                              "productPrice": 1.5000,
                              "supProductPrice": 2.0000,
                              "serviceTariffing": 0.0100,
                              "buyNum": 1,
                              "supBuyNum": 1,
                              "clientId": "10000079",
                              "cooperativeType":'' ,
                              "fpMemberCode": 9240931,
                              "productId": 10406476,
                              "clientCode": "API"
                            }
        Verify_Control_head={'authorization':'Bearer {}'.format(fp_token),
                            'Content-Type':'application/json; charset=utf-8'}
        get_Verify_Control=requests.post(Verify_Control_url,data=json.dumps(Verify_Control_data),headers=Verify_Control_head)
        print(get_Verify_Control.json()['message'])
        get_message=get_Verify_Control.json()['message']
        assert get_message==expect


if __name__ == '__main__':
    pytest.main(['-s','order_test.py'])