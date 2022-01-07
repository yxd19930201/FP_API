import pytest
import requests
import json

from FP_API.conftest import fp_token


class Test_Product():

    def setup(self):
        pass

    def teardown(self):
        pass


    # H5专属：获取商品原始信息列表
    def test_get_Product(self,fp_token):
        get_Product_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product'
        get_Product_data={}
        get_Product_head={'authorization':'Bearer {}'.format(fp_token),
                          'Content-Type':'application/json; charset=utf-8'}
        get_Product_list=requests.get(get_Product_url,params=get_Product_data,headers=get_Product_head)
        print(get_Product_list.text)
        Product_data=get_Product_list.json()['data'][0]['id']
        assert Product_data


    # 按[商品-应用]查询自有商品列表，带分页
    def test_Product_list(self,fp_token):
        Product_list_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/ProductList'
        Product_list_data={'MemberId':'64cf60f0-d5d3-449b-95a2-03db1c640ace',
                           'ClientId':'10000079',
                           'PageIndex':'1',
                           'PageSize':'10'}
        Product_list_head={'authorization':'Bearer {}'.format(fp_token),
                          'Content-Type':'application/json; charset=utf-8'}
        get_Product_list=requests.get(Product_list_url,params=Product_list_data,headers=Product_list_head)
        code=get_Product_list.status_code
        print(get_Product_list.text)
        assert code==200

    # 按[商品-应用]查询自有商品列表，不带分页
    def test_ProductList_NoPaged(self,fp_token):
        ProductList_NoPaged_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/ProductListNoPaged'
        ProductList_NoPaged_data={'ProductId':'15894934',
                                  'MemberId':'64cf60f0-d5d3-449b-95a2-03db1c640ace',
                                  'ClientId':'10000079'}
        ProductList_NoPaged_head={'authorization':'Bearer {}'.format(fp_token),
                          'Content-Type':'application/json; charset=utf-8'}
        get_ProductList_NoPaged=requests.get(ProductList_NoPaged_url,params=ProductList_NoPaged_data,headers=ProductList_NoPaged_head)
        print(get_ProductList_NoPaged.text)
        code=get_ProductList_NoPaged.status_code
        assert code==200

    # 查询自有商品列表
    def test_ProductList_WithPaged(self,fp_token):
        ProductList_WithPaged_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/ProductListWithPaged'
        ProductList_WithPaged_data={'ProductId':'15894934',
                                    'PageIndex':'1',
                                    'PageSize':'10'}
        ProductList_WithPaged_head={'authorization':'Bearer {}'.format(fp_token),
                          'Content-Type':'application/json; charset=utf-8'}
        get_ProductList_WithPaged=requests.get(ProductList_WithPaged_url,params=ProductList_WithPaged_data,headers=ProductList_WithPaged_head)
        print(get_ProductList_WithPaged.text)
        get_ProductList=get_ProductList_WithPaged.json()['data']['list'][0]['id']
        assert get_ProductList

    # 查询自有商品详情
    def test_Get_ProductInfo(self,fp_token):
        Get_ProductInfo_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/GetProductInfo'
        Get_ProductInfo_data={'ProductId':'15894934'}
        Get_ProductInfo_head = {'authorization': 'Bearer {}'.format(fp_token),
                                      'Content-Type': 'application/json; charset=utf-8'}
        Get_ProductInfo=requests.get(Get_ProductInfo_url,params=Get_ProductInfo_data,headers=Get_ProductInfo_head)
        print(Get_ProductInfo.text)
        Get_ProductInfo_id=Get_ProductInfo.json()['data']['id']
        assert Get_ProductInfo_id

    # 按照指定的自有商品，获取其对接的供货商品列表
    def test_SupProduct_List(self,fp_token):
        SupProduct_List_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/SupProductList'
        SupProduct_List_data={'MemberId':'64cf60f0-d5d3-449b-95a2-03db1c640ace',
                              'ProductId':'15894934'}
        SupProduct_List_head={'authorization': 'Bearer {}'.format(fp_token),
                                      'Content-Type': 'application/json; charset=utf-8'}
        SupProduct_List=requests.get(SupProduct_List_url,params=SupProduct_List_data,headers=SupProduct_List_head)
        print(SupProduct_List.text)
        SupProduct_List_supProductId=SupProduct_List.json()['data'][0]['supProductId']
        assert SupProduct_List_supProductId

    # 匹配平台话费自有商品，返回集合，且商品需满足：上架、不在回收站
    def test_Phone_ProductList(self,fp_token):
        Phone_ProductList_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/MatchPhoneProductList'
        Phone_ProductList_data={"phone": "13714199115", "faceValue": "", "memberId": "", "clientId": ""}
        Phone_ProductList_head={'authorization': 'Bearer {}'.format(fp_token),
                                      'Content-Type': 'application/json; charset=utf-8'}
        get_Phone_ProductList=requests.post(Phone_ProductList_url,data=json.dumps(Phone_ProductList_data),headers=Phone_ProductList_head)
        print(get_Phone_ProductList.text)
        Phone_ProductList_id=get_Phone_ProductList.json()['data'][0]['id']
        assert Phone_ProductList_id

    # 匹配平台话费商品
    def test_MatchPhone_Product(self,fp_token):
        MatchPhone_Product_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/MatchPhoneProduct'
        MatchPhone_Product_data={"memberId": "f240ef35-bed2-446a-ba50-b55fffd5a4f4", "clientId": "10000079", "chargePhone": "13714199115", "chargeValue": 100 }
        MatchPhone_Product_head = {'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_MatchPhone_Product=requests.post(MatchPhone_Product_url,data=json.dumps(MatchPhone_Product_data),headers=MatchPhone_Product_head)
        print(get_MatchPhone_Product.text)
        code=get_MatchPhone_Product.status_code
        assert code==200

    # 在变更Fp后移除商户密价记录，包括组、关系
    def test_After_FpChanged(self,fp_token):
        After_FpChanged_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/RemoveMemberSecretPriceAfterFpChanged'
        After_FpChanged_data={"memberId": "0cfbf1e3-e7c4-4a6c-88e3-7e9d14a79ec1", "oldFpMemberId": ""}
        After_FpChanged_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_After_FpChanged=requests.post(After_FpChanged_url,data=json.dumps(After_FpChanged_data),headers=After_FpChanged_head)
        print(get_After_FpChanged.text)
        code=get_After_FpChanged.status_code
        assert code==200

    # 根据Sup商品Id获取平台商品信息
    def test_GetProductGroup_BySupProduct(self,fp_token):
        GetProductGroup_BySupProduct_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/GetProductGroupBySupProduct'
        GetProductGroup_BySupProduct_data={'supProductIds':'500000314'}
        GetProductGroup_BySupProduct_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        GetProductGroup_BySupProduct=requests.get(GetProductGroup_BySupProduct_url,params=GetProductGroup_BySupProduct_data,headers=GetProductGroup_BySupProduct_head)
        print(GetProductGroup_BySupProduct.text)
        code=GetProductGroup_BySupProduct.status_code
        assert code==200

    # 根据平台商品和商户号查询密价信息
    def test_Member_Product(self,fp_token):
        Member_Product_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/GetSecretPriceByMemberProduct'
        Member_Product_data={
                            "ProductId":"15894934",
                            "MemberCode":"9079788"
                        }
        Member_Product_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_Member_Product=requests.get(Member_Product_url,params=Member_Product_data,headers=Member_Product_head)
        print(get_Member_Product.headers)
        print(get_Member_Product.text)
        get_Member_clientId=get_Member_Product.json()['data']['list'][0]['clientId']
        assert get_Member_clientId


    # 获取sup商品上浮比例
    def test_Rise_Proportion(self, fp_token):
        Rise_Proportion_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/GetSupProductRiseProportion'
        Rise_Proportion_data={"supProductIds": "", "fpMemberId": "2035af55-45c5-46d2-9af8-4b278f0caabf"}
        Rise_Proportion_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_Rise_Proportion=requests.post(Rise_Proportion_url,data=json.dumps(Rise_Proportion_data),headers=Rise_Proportion_head)
        print(get_Rise_Proportion.text)
        get_Rise_supProductId=get_Rise_Proportion.json()['data'][0]['supProductId']
        assert get_Rise_supProductId


    # 获取已授权的sup商品集合（推广大使或战略伙伴）
    def test_Get_Authorized(self, fp_token):
        Get_Authorized_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/GetAuthorizedSupProductList'
        Get_Authorized_data={"fpMemberId": "64cf60f0-d5d3-449b-95a2-03db1c640ace", "cooperativeType": "12"}
        Get_Authorized_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_Get_Authorized=requests.post(Get_Authorized_url,data=json.dumps(Get_Authorized_data),headers=Get_Authorized_head)
        print(get_Get_Authorized.text)
        Get_Authorized=get_Get_Authorized.json()['data'][0]['supProductId']
        assert Get_Authorized

    # 根据商品Id获取商品分类信息
    def test_Category_Type(self,fp_token):
      Category_Type_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/GetProductCategoryType'
      Category_Type_data={'ProductId':'15894934',
                          'ProductType':'1'}
      Category_Type_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
      get_Category_Type=requests.get(Category_Type_url,params=Category_Type_data,headers=Category_Type_head)
      print(get_Category_Type.text)
      print(get_Category_Type.headers)
      get_Category_productId=get_Category_Type.json()['data']['productId']
      assert get_Category_productId

    # 获取平台商品列表（分页）（公共商品 或者 私有商品）
    def test_With_Paged(self,fp_token):
        With_Paged_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/GetProductListWithPaged'
        With_Paged_data={"searchType": "2", "fpMemberId": "", "productId": "", "productName": "", "productType": "", "faceValue": "", "saleStatus": "", "categoryIdL1": "", "categoryIdL2": "", "categoryIdL3": "", "categoryIdL4": "", "invoiceType": "", "secondInvoiceType": "", "invoiceRate": "", "filterCategoryIdL3": "", "pageIndex": "1", "pageSize": "10"}
        With_Paged_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_With_Paged=requests.post(With_Paged_url,data=json.dumps(With_Paged_data),headers=With_Paged_head)
        print(get_With_Paged.text)
        get_With_productId=get_With_Paged.json()['data']['list'][0]['productId']
        assert get_With_productId

    # 获取平台商品列表（不分页）（公共商品 或者 私有商品）（用于导出）
    def test_GetProduct_Paged(self,fp_token):
        GetProduct_Paged_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/GetProductListWithoutPaged'
        GetProduct_Paged_data={"searchType": "2", "fpMemberId": "", "productId": "", "productName": "", "productType": "", "faceValue": "", "saleStatus": "", "categoryIdL1": "", "categoryIdL2": "", "categoryIdL3": "", "categoryIdL4": "", "invoiceType": "", "secondInvoiceType": "", "invoiceRate": ""}
        GetProduct_Paged_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_GetProduct_Paged=requests.post(GetProduct_Paged_url,data=json.dumps(GetProduct_Paged_data),headers=GetProduct_Paged_head)
        print(get_GetProduct_Paged.text)
        get_GetProduct_productId=get_GetProduct_Paged.json()['data']['list'][0]['productId']
        assert get_GetProduct_productId


    # 根据平台商品id获取对应sup商品（分页）（有库存统计信息）
    def test_By_ProductId(self,fp_token):
        GetProduct_Paged_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/GetSupProductPagedListByProductId'
        GetProduct_Paged_data={"productId": "15894934", "supProductId": "", "supProductName": "", "pageIndex": "1", "pageSize": "20"}
        GetProduct_Paged_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_GetProduct_Paged=requests.post(GetProduct_Paged_url,data=json.dumps(GetProduct_Paged_data),headers=GetProduct_Paged_head)
        print(get_GetProduct_Paged.text)
        get_GetProduct_supProductId=get_GetProduct_Paged.json()['data']['list'][0]['supProductId']
        assert get_GetProduct_supProductId


    # 获取推广大使供货商品列表
    def test_Ambassador_ProductList(self,fp_token):
        Ambassador_ProductList_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/GetPromotionAmbassadorProductList'
        Ambassador_ProductList_data={
                                      "productIdList": [
                                        17033310
                                      ]
                                    }
        Ambassador_ProductList_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_Ambassador_ProductList=requests.post(Ambassador_ProductList_url,data=json.dumps(Ambassador_ProductList_data),headers=Ambassador_ProductList_head)
        print(get_Ambassador_ProductList.text)
        get_Ambassador_productId=get_Ambassador_ProductList.json()['data']['list'][0]['productId']
        print(get_Ambassador_productId)
        assert get_Ambassador_productId



    # 查询平台商品(不分页)
    def test_Query_ProductList(self,fp_token):
        Query_ProductList_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/QueryProductList'
        Query_ProductList_data={
                                  "productName": "腾讯-Q币-1元-直充-【Q币3g带票】"
                                }
        Query_ProductList_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_Query_ProductList=requests.post(Query_ProductList_url,data=json.dumps(Query_ProductList_data),headers=Query_ProductList_head)
        print(get_Query_ProductList.text)
        get_Query_productId=get_Query_ProductList.json()['data']['list'][0]['productId']
        assert get_Query_productId


    # 查询SUP商品(不分页)
    def test_Query_SupProduct(self,fp_token):
        Query_SupProduct_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/QuerySupProductList'
        Query_SupProduct_data={"supProductName": "腾讯-Q币-1元-直充-【Q币3g带票】"}
        Query_SupProduct_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_Query_SupProduct=requests.post(Query_SupProduct_url,data=json.dumps(Query_SupProduct_data),headers=Query_SupProduct_head)
        print(get_Query_SupProduct.text)
        get_Query_supProductId=get_Query_SupProduct.json()['data']['list'][0]['supProductId']
        assert get_Query_supProductId


    # 转移密价组
    def test_Trans_ferSpGroup(self,fp_token):
        Trans_ferSpGroup_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/TransferSpGroup'
        Trans_ferSpGroup_data={"fpMemberCode": "9899689"}
        Trans_ferSpGroup_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_Trans_ferSpGroup=requests.post(Trans_ferSpGroup_url,data=json.dumps(Trans_ferSpGroup_data),headers=Trans_ferSpGroup_head)
        print(get_Trans_ferSpGroup.text)
        code=get_Trans_ferSpGroup.status_code
        assert code==200


    # 获取平台商品对接SUP商品最大库存数量
    def test_Max_StockCount(self,fp_token):
        Max_StockCount_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/GetMaxStockCount'
        Max_StockCount_data={"productId": "17033310"}
        Max_StockCount_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_Max_StockCount=requests.post(Max_StockCount_url,data=json.dumps(Max_StockCount_data),headers=Max_StockCount_head)
        print(get_Max_StockCount.text)
        code=get_Max_StockCount.status_code
        assert code==200



    # 查询商品密价，没有密价查询默认密价
    def test_WithSecret_Price(self,fp_token):
        WithSecret_Price_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/GetProductListWithSecretPrice'
        WithSecret_Price_data={
                              "productIdList": [
                                ""
                              ],
                              "productName": "",
                              "productType": 0,
                              "productCategoryIdThreeList": [
                                0
                              ],
                              "memberId": "",
                              "clientId": "10000079",
                              "faceValue": 0,
                              "fpMemberCode": "9240931",
                              "isShowAbnormalProduct": 'true'
                            }
        WithSecret_Price_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_WithSecret_Price=requests.post(WithSecret_Price_url,data=json.dumps(WithSecret_Price_data),headers=WithSecret_Price_head)
        print(get_WithSecret_Price.text)
        code=get_WithSecret_Price.status_code
        assert code==200



    # 查询商品密价，没有密价查询默认密价（分页）
    def test_WithSecret_PriceWith(self,fp_token):
        WithSecret_PriceWith_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/GetProductListWithSecretPriceWithPage'
        WithSecret_PriceWith_data={"productIdList": "", "productName": "", "productType": "", "productCategoryId1": "", "productCategoryId2": "", "productCategoryIdThreeList": "", "memberId": "", "clientId": "10000079", "faceValue": "", "fpMemberCode": "9240931", "isShowAbnormalProduct": "", "categoryIdL4": "", "orderBy": "", "orderByColumn": "", "pageIndex": "1", "pageSize": "10"}
        WithSecret_PriceWith_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_WithSecret_PriceWith=requests.post(WithSecret_PriceWith_url,data=json.dumps(WithSecret_PriceWith_data),headers=WithSecret_PriceWith_head)
        print(get_WithSecret_PriceWith.text)
        get_WithSecret_PriceWith=get_WithSecret_PriceWith.json()['data']['list'][0]['id']
        assert get_WithSecret_PriceWith



    # 获取预售商品分类
    def test_Category_List(self,fp_token):
        Category_List_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/GetPreProductCategoryList'
        Category_List_data={"dealerMemberId": "f240ef35-bed2-446a-ba50-b55fffd5a4f4", "clientId": "10000079", "categoryIdL1": "", "categoryIdL2": "", "categoryIdL3": "", "categoryIdL4": "", "faceValue": "", "productId": "", "productName": "", "productType": ""}
        Category_List_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_Category_List=requests.post(Category_List_url,data=json.dumps(Category_List_data),headers=Category_List_head)
        print(get_Category_List.text)
        code=get_Category_List.status_code
        assert code==200



    # 获取预售商品列表
    def test_GetPre_ProductList(self,fp_token):
        GetPre_ProductList_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/GetPreProductList'
        GetPre_ProductList_data={"memberId": "f240ef35-bed2-446a-ba50-b55fffd5a4f4", "clientId": "10000079", "faceValue": "", "productIdList": "", "productName": "", "productType": "", "categoryIdL1": "", "categoryIdL2": "", "categoryIdL3": "", "categoryIdL4": ""}
        GetPre_ProductList_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_GetPre_ProductList=requests.post(GetPre_ProductList_url,data=json.dumps(GetPre_ProductList_data),headers=GetPre_ProductList_head)
        print(get_GetPre_ProductList.text)
        get_GetPre_id=get_GetPre_ProductList.json()['data']['list'][0]['id']
        assert get_GetPre_id


    # 查询平台商品SUP库存
    def test_ProductSup_List(self,fp_token):
        ProductSup_List_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/Product/GetProductSupList'
        ProductSup_List_data={"memberId": "f240ef35-bed2-446a-ba50-b55fffd5a4f4", "productId": "16374025"}
        ProductSup_List_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_ProductSup_List=requests.post(ProductSup_List_url,data=json.dumps(ProductSup_List_data),headers=ProductSup_List_head)
        print(get_ProductSup_List.text)
        get_ProductSup_supProductId=get_ProductSup_List.json()['data']['list'][0]['supProductId']
        assert get_ProductSup_supProductId



    # 我创建的商品
    def test_create_Produc(self,fp_token):
        create_Produc_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/HawkEye/GetProductPage'
        create_Produc_data={'PageIndex':'1',
                            'PageSize':'10'}
        create_Produc_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_create_Produc=requests.get(create_Produc_url,params=create_Produc_data,headers=create_Produc_head)
        print(get_create_Produc.text)
        get_create_productId=get_create_Produc.json()['data']['list'][0]['productId']
        assert get_create_productId


    # 平台商品库存组(卡密)
    def test_create_CardProduc(self,fp_token):
        create_CardProduc_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/HawkEye/GetCardGroupIdPage'
        create_CardProduc_data={'PageIndex':'1',
                            'PageSize':'10'}
        create_CardProduc_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_create_CardProduc=requests.get(create_CardProduc_url,params=create_CardProduc_data,headers=create_CardProduc_head)
        print(get_create_CardProduc.text)
        get_create_businessId=get_create_CardProduc.json()['data']['list'][0]['businessId']
        assert get_create_businessId



    # 平台商品库存组(直充)
    def test_create_CardProduc(self,fp_token):
        create_CardProduc_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/HawkEye/GetCardGroupIdPage'
        create_CardProduc_data={'PageIndex':'1',
                            'PageSize':'10'}
        create_CardProduc_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_create_CardProduc=requests.get(create_CardProduc_url,params=create_CardProduc_data,headers=create_CardProduc_head)
        print(get_create_CardProduc.text)
        get_create_businessId=get_create_CardProduc.json()['data']['list'][0]['businessId']
        assert get_create_businessId



    # 密价商品
    def test_CodeProuctId_Page(self,fp_token):
        CodeProuctId_Page_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/HawkEye/MemerCodeProuctIdPage'
        CodeProuctId_Page_data={'PageIndex':'1',
                            'PageSize':'10'}
        CodeProuctId_Page_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_CodeProuctId_Page=requests.get(CodeProuctId_Page_url,params=CodeProuctId_Page_data,headers=CodeProuctId_Page_head)
        print(get_CodeProuctId_Page.text)
        get_CodeProuctId_productId=get_CodeProuctId_Page.json()['data']['list'][0]['productId']
        assert get_CodeProuctId_productId




    # 卡密商品池
    def test_CardPool_Page(self,fp_token):
        CardPool_Page_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/HawkEye/CardPoolPage'
        CardPool_Page_data={'PageIndex':'1',
                            'PageSize':'10'}
        CardPool_Page_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_CardPool_Page=requests.get(CardPool_Page_url,params=CardPool_Page_data,headers=CardPool_Page_head)
        print(get_CardPool_Page.text)
        get_CardPool_id=get_CardPool_Page.json()['data']['list'][0]['association1']['id']
        assert get_CardPool_id



    # 直冲商品池
    def test_ChargePool_Page(self,fp_token):
        ChargePool_Page_url='http://pre-fp-supportinterface-api-admin.suuyuu.cn/api/HawkEye/DirectChargePoolPage'
        ChargePool_Page_data={'PageIndex':'1',
                            'PageSize':'10'}
        ChargePool_Page_head={'authorization': 'Bearer {}'.format(fp_token),
                                  'Content-Type': 'application/json; charset=utf-8'}
        get_ChargePool_Page=requests.get(ChargePool_Page_url,params=ChargePool_Page_data,headers=ChargePool_Page_head)
        print(get_ChargePool_Page.text)
        get_ChargePool_id = get_ChargePool_Page.json()['data']['list'][0]['association1']['id']
        assert get_ChargePool_id












if __name__=='__main__':
    pytest.main(['-s','product_test.py'])






















