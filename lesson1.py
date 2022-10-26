#dict словари
#{"key" : "value"}
# dict={
#     "name": "Adil",
#     "age" : 16,
#     "subject" : {
#         "python" : 44,
#
#     },
#
#
# }
# for i in dict:
#     if type(dict[i])== dict:
#         for j in dict[i]:
#             print(j)
python = {
    "alina" : 45,
    "aziza": 67,
    "adil" : 88,
}
# print(python.keys())
# print(python.values())
# print(python.items())
# for key, value in python.items() :
#     print(key,value)
# python["ilgiz"]=100
# print(python)
# dicy=dict()
# print(len(dicy))
for i in python:
    print(len(python))
sun_list=sum(python.values())
arif=sun_list/len(python)
print(arif)
counter= 0
for values in python.values():
    counter+=values
    print(counter / len(python))
# print(python.get("adil"))
# aziza=python.pop("aziza")
# print(aziza)
# # print(python)
# lamg = ["python" , "java", "C++"]
# dict_lang = dict.fromkeys(lamg)
# print(dict_lang)
# python3=python
print(python.setdefault("adilll"))
print(python)
#
#
# # while True:
# #     product_dict={}
# #     product=input("название продукта   :")
# #     product_prace=int(input("Ведите цену продукта : "))
# #     product_dict[product]=product_prace
# #
# #     print(product)
# dict_product= {}
# while True:
#
#     product = input("write a product and prece  ; ")
#     if product == "exit":
#         break
#     key , value = product.split()
#     dict_product[key]=int(value) / 83
#     print(dict_product)
#     dict_product[product]=value
#
#
#
