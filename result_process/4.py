import pickle
import numpy as np
from model import config as cf
import pandas as pd
import matplotlib.pyplot as plt
##¹þ

output_dir = r'E:\0320CasCN-master\result_process'
def gen_sql(id,label,pred):
    sql = "INSERT INTO `weibo_data_result` VALUES( \"%s\", %d, %d);\n"
    with open(output_dir + "/TwitterData_result.sql", "w") as file:
        for i in range(len(id)):
            file.write(sql % (id[i], label[i], pred[i]))


learning_rate=0.005
id_test, x_test, L_test, y_test, sz_test, time_test, _ ,all_label= pickle.load(open(cf.test_pkl, 'rb'))
#（包含源微博）
## id_test：微博id
## sz_test：前3小时的值
## y_test ：真实预测结果log处理值
##all_label ： 24小时总的


# file=open('prediction_result__renminwang0.005800_CasCN', 'rb')
# file=open('prediction_result__weibo0.005699_CasCN', 'rb')
# file=open('prediction_result__twitter0.0051521_CasCN', 'rb')
file=open('prediction_result__weibo_o1p4.0051446_CasCN', 'rb')
predict, predict_y,predict_loss = pickle.load(file)
# data1 = data1[0] #如果file是原始模型生成的，则加这句；如果是restore后生成的，则注释掉
# data_=data1[0:13122]

##模型预测的结果
pred_1=[]
for ele in predict:
    tmp=np.exp(ele*np.log(2.0))-1
    final=int(tmp)
    pred_1.append(final)
pred_1=pred_1[0:len(id_test)]

id_final=[] ##挑出来的微博
label_final=[]
pred_final=[]
for i in range(len(id_test)):
    id=id_test[i]
    pred=pred_1[i] ##预测的未来3-24的值
    sz=sz_test[i]  ##前3小时的真实值
    all=all_label[i]##24小时的真实值
    label=all-sz##真实的未来3-24的值
    if abs(label-pred)<5 : #如果真实值和预测值差距<5
        id_final.append(id)
        label_final.append(all-1) #24小时内一共的转发
        pred_final.append(pred+sz-1) #24小时内一共的转发

print(len(id_final))
gen_sql(id_final,label_final,pred_final)

