import pickle
import numpy as np
from model import config as cf

learning_rate=0.005
test_pkl_1='renminwang_save_result/o0.2p0.5/data1_renminwang_new/data_test.pkl'
id_test_1, x_test_1, L_test_1, y_test_1, sz_test_1, time_test_1, _ ,all_label_1= pickle.load(open(test_pkl_1, 'rb'))
file_1=open('renminwang_save_result/o0.2p0.5/prediction_result__weibo0.0051600_CasCN', 'rb')
predict_1, predict_y_1,predict_loss_1 = pickle.load(file_1)
pred_1=[]
for ele in predict_1:
    tmp=np.exp(ele*np.log(2.0))-1
    final=int(tmp)
    pred_1.append(final)
pred_1=pred_1[0:len(id_test_1)] ###预测的未来0.2-0.5小时的值

test_pkl_2='renminwang_save_result/o0.2p1.0/data1_renminwang_new/data_test.pkl'
id_test_2, x_test_2, L_test_2, y_test_2, sz_test_2, time_test_2, _ ,all_label_2= pickle.load(open(test_pkl_2, 'rb'))
file_2=open('renminwang_save_result/o0.2p1.0/prediction_result__weibo0.0051600_CasCN', 'rb')
predict_2, predict_y_2,predict_loss_2 = pickle.load(file_2)
pred_2=[]
for ele in predict_2:
    tmp=np.exp(ele*np.log(2.0))-1
    final=int(tmp)
    pred_2.append(final)
pred_2=pred_2[0:len(id_test_2)] ##预测的未来0.2-1小时的值

test_pkl_3='renminwang_save_result/o0.2p1.5/data1_renminwang_new/data_test.pkl'
id_test_3, x_test_3, L_test_3, y_test_3, sz_test_3, time_test_3, _ ,all_label_3= pickle.load(open(test_pkl_3, 'rb'))
file_3=open('renminwang_save_result/o0.2p1.5/prediction_result__weibo0.0051700_CasCN', 'rb')
predict_3, predict_y_3,predict_loss_3 = pickle.load(file_3)
pred_3=[]
for ele in predict_3:
    tmp=np.exp(ele*np.log(2.0))-1
    final=int(tmp)
    pred_3.append(final)
pred_3=pred_3[0:len(id_test_3)] ##预测的未来0.2-1.5小时的值

test_pkl_4='renminwang_save_result/o0.2p2.0/data1_renminwang_new/data_test.pkl'
id_test_4, x_test_4, L_test_4, y_test_4, sz_test_4, time_test_4, _ ,all_label_4= pickle.load(open(test_pkl_4, 'rb'))
file_4=open('renminwang_save_result/o0.2p2.0/prediction_result__weibo0.0051600_CasCN', 'rb')
predict_4, predict_y_4,predict_loss_4 = pickle.load(file_4)
pred_4=[]
for ele in predict_4:
    tmp=np.exp(ele*np.log(2.0))-1
    final=int(tmp)
    pred_4.append(final)
pred_4=pred_4[0:len(id_test_4)] ##预测的未来0.2-2小时的值
print('finish!')

test_pkl_5='renminwang_save_result/o0.2p2.5/data1_renminwang_new/data_test.pkl'
id_test_5, x_test_5, L_test_5, y_test_5, sz_test_5, time_test_5, _ ,all_label_5= pickle.load(open(test_pkl_5, 'rb'))
file_5=open('renminwang_save_result/o0.2p2.5/prediction_result__weibo0.0052400_CasCN', 'rb')
predict_5, predict_y_5,predict_loss_5 = pickle.load(file_5)
pred_5=[]
for ele in predict_5:
    tmp=np.exp(ele*np.log(2.0))-1
    final=int(tmp)
    pred_5.append(final)
pred_5=pred_5[0:len(id_test_5)] ##预测的未来0.2-2.5小时的值
print('finish!')


test_pkl_6='renminwang_save_result/o0.2p3.0/data1_renminwang_new/data_test.pkl'
id_test_6, x_test_6, L_test_6, y_test_6, sz_test_6, time_test_6, _ ,all_label_6= pickle.load(open(test_pkl_6, 'rb'))
file_6=open('renminwang_save_result/o0.2p3.0/prediction_result__weibo0.0052200_CasCN', 'rb')
predict_6, predict_y_6,predict_loss_6 = pickle.load(file_6)
pred_6=[]
for ele in predict_6:
    tmp=np.exp(ele*np.log(2.0))-1
    final=int(tmp)
    pred_6.append(final)
pred_6=pred_6[0:len(id_test_6)] ##预测的未来0.2-3小时的值
print('finish!')

test_pkl_7='renminwang_save_result/o0.2p5.0/data1_renminwang_new/data_test.pkl'
id_test_7, x_test_7, L_test_7, y_test_7, sz_test_7, time_test_7, _ ,all_label_7= pickle.load(open(test_pkl_7, 'rb'))
file_7=open('renminwang_save_result/o0.2p5.0/prediction_result__weibo0.0052200_CasCN', 'rb')
predict_7, predict_y_7,predict_loss_7 = pickle.load(file_7)
pred_7=[]
for ele in predict_7:
    tmp=np.exp(ele*np.log(2.0))-1
    final=int(tmp)
    pred_7.append(final)
pred_7=pred_7[0:len(id_test_7)] ##预测的未来0.2-5小时的值
print('finish!')

test_pkl_8='renminwang_save_result/o0.2p7.0/data1_renminwang_new/data_test.pkl'
id_test_8, x_test_8, L_test_8, y_test_8, sz_test_8, time_test_8, _ ,all_label_8= pickle.load(open(test_pkl_8, 'rb'))
file_8=open('renminwang_save_result/o0.2p7.0/prediction_result__weibo0.0051700_CasCN', 'rb')
predict_8, predict_y_8,predict_loss_8 = pickle.load(file_8)
pred_8=[]
for ele in predict_8:
    tmp=np.exp(ele*np.log(2.0))-1
    final=int(tmp)
    pred_8.append(final)
pred_8=pred_8[0:len(id_test_8)] ##预测的未来0.2-5小时的值
print('finish!')


# id,##24小时的真实值##前0.2小时的真实值,##预测的未来0.2-0.5的值,##预测的未来0.2-1的值,##预测的未来0.2-1.5的值,
# ##预测的未来0.2-2的值,##预测的未来0.2-5的值,##预测的未来0.2-15的值,##预测的未来0.2-24的值
# id,##24小时的真实值##前0.1小时的真实值,##预测的未来0.1-0.2的值,##预测的未来0.1-0.5的值,##预测的未来0.1-1的值,
# ##预测的未来0.1-1.5的值,##预测的未来0.1-2的值,##预测的未来0.1-5的值,##预测的未来0.1-10的值

# id，XX先按最后的all_label_7来，sz_test，pred_1,pred_2,pred_3,pred_4,pred_5,pred_6,pred_7


# id,##24小时的真实值##前0.2小时的真实值,##预测的未来0.2-0.5的值,##预测的未来0.2-1的值,##预测的未来0.2-1.5的值,
# ##预测的未来0.2-2的值,##预测的未来0.2-2.5的值,##预测的未来0.2-3.0的值,##预测的未来0.2-5.0的值,##预测的未来0.2-7.0的值,
with open('renminwang_o0.2p0.5-7.0.txt','w') as file:
    for i in range(len(id_test_1)):
        string=str(id_test_1[i])+'\t'+str(all_label_8[i])+'\t'+str(sz_test_1[i])+'\t'+str(pred_1[i])+'\t'+str(pred_2[i])+'\t'+\
               str(pred_3[i])+'\t'+str(pred_4[i])+'\t'+str(pred_5[i])+'\t'+str(pred_6[i])+'\t'+str(pred_7[i])+'\t'+str(pred_8[i])+'\n'
        file.write(string)
file.close()

print('finish!')





# learning_rate=0.005
# test_pkl_1='save_result_o0.1/weibo_o0.1p0.2/data1_weibo_new/data_test.pkl'
# id_test_1, x_test_1, L_test_1, y_test_1, sz_test_1, time_test_1, _ ,all_label_1= pickle.load(open(test_pkl_1, 'rb'))
# file_1=open('save_result_o0.1/weibo_o0.1p0.2/prediction_result__weibo0.0051599_CasCN', 'rb')
# predict_1, predict_y_1,predict_loss_1 = pickle.load(file_1)
# pred_1=[]
# for ele in predict_1:
#     tmp=np.exp(ele*np.log(2.0))-1
#     final=int(tmp)
#     pred_1.append(final)
# pred_1=pred_1[0:len(id_test_1)] ###预测的未来0.2-0.5小时的值
#
# test_pkl_2='save_result_o0.1/weibo_o0.1p0.5/data1_weibo_new/data_test.pkl'
# id_test_2, x_test_2, L_test_2, y_test_2, sz_test_2, time_test_2, _ ,all_label_2= pickle.load(open(test_pkl_2, 'rb'))
# file_2=open('save_result_o0.1/weibo_o0.1p0.5/prediction_result__weibo0.005546_CasCN', 'rb')
# predict_2, predict_y_2,predict_loss_2 = pickle.load(file_2)
# pred_2=[]
# for ele in predict_2:
#     tmp=np.exp(ele*np.log(2.0))-1
#     final=int(tmp)
#     pred_2.append(final)
# pred_2=pred_2[0:len(id_test_2)] ##预测的未来0.2-1小时的值
# print('finish!')
#
# test_pkl_3='save_result_o0.1/weibo_o0.1p1/data1_weibo_new/data_test.pkl'
# id_test_3, x_test_3, L_test_3, y_test_3, sz_test_3, time_test_3, _ ,all_label_3= pickle.load(open(test_pkl_3, 'rb'))
# file_3=open('save_result_o0.1/weibo_o0.1p1/prediction_result__weibo0.005273_CasCN', 'rb')
# predict_3, predict_y_3,predict_loss_3 = pickle.load(file_3)
# pred_3=[]
# for ele in predict_3:
#     tmp=np.exp(ele*np.log(2.0))-1
#     final=int(tmp)
#     pred_3.append(final)
# pred_3=pred_3[0:len(id_test_3)] ##预测的未来0.2-1.5小时的值
# print('finish!')
#
# test_pkl_4='save_result_o0.1/weibo_o0.1p1.5/data1_weibo_new/data_test.pkl'
# id_test_4, x_test_4, L_test_4, y_test_4, sz_test_4, time_test_4, _ ,all_label_4= pickle.load(open(test_pkl_4, 'rb'))
# file_4=open('save_result_o0.1/weibo_o0.1p1.5/prediction_result__weibo0.0052964_CasCN', 'rb')
# predict_4, predict_y_4,predict_loss_4 = pickle.load(file_4)
# pred_4=[]
# for ele in predict_4:
#     tmp=np.exp(ele*np.log(2.0))-1
#     final=int(tmp)
#     pred_4.append(final)
# pred_4=pred_4[0:len(id_test_4)] ##预测的未来0.2-2小时的值
# print('finish!')
#
# test_pkl_5='save_result_o0.1/weibo_o0.1p2/data1_weibo_new/data_test.pkl'
# id_test_5, x_test_5, L_test_5, y_test_5, sz_test_5, time_test_5, _ ,all_label_5= pickle.load(open(test_pkl_5, 'rb'))
# file_5=open('save_result_o0.1/weibo_o0.1p2/prediction_result__weibo0.005468_CasCN', 'rb')
# predict_5, predict_y_5,predict_loss_5 = pickle.load(file_5)
# pred_5=[]
# for ele in predict_5:
#     tmp=np.exp(ele*np.log(2.0))-1
#     final=int(tmp)
#     pred_5.append(final)
# pred_5=pred_5[0:len(id_test_5)] ##预测的未来0.2-5小时的值
# print('finish!')
#
# test_pkl_6='save_result_o0.1/weibo_o0.1p5/data1_weibo_new/data_test.pkl'
# id_test_6, x_test_6, L_test_6, y_test_6, sz_test_6, time_test_6, _ ,all_label_6= pickle.load(open(test_pkl_6, 'rb'))
# file_6=open('save_result_o0.1/weibo_o0.1p5/prediction_result__weibo0.005468_CasCN', 'rb')
# predict_6, predict_y_6,predict_loss_6 = pickle.load(file_6)
# pred_6=[]
# for ele in predict_6:
#     tmp=np.exp(ele*np.log(2.0))-1
#     final=int(tmp)
#     pred_6.append(final)
# pred_6=pred_6[0:len(id_test_6)] ##预测的未来0.2-15小时的值
# print('finish!')
#
# test_pkl_7='save_result_o0.1/weibo_o0.1p10/data1_weibo_new/data_test.pkl'
# id_test_7, x_test_7, L_test_7, y_test_7, sz_test_7, time_test_7, _ ,all_label_7= pickle.load(open(test_pkl_7, 'rb'))
# file_7=open('save_result_o0.1/weibo_o0.1p10/prediction_result__weibo0.005390_CasCN', 'rb')
# predict_7, predict_y_7,predict_loss_7 = pickle.load(file_7)
# pred_7=[]
# for ele in predict_7:
#     tmp=np.exp(ele*np.log(2.0))-1
#     final=int(tmp)
#     pred_7.append(final)
# pred_7=pred_7[0:len(id_test_7)] ##预测的未来0.2-24小时的值
# print('finish!')
#
#
#
# # output_dir = r'E:\0222CasCN-master\result_process'
# # def gen_sql(id,label,pred):
# #     sql = "INSERT INTO `weibo_data_result` VALUES( \"%s\", %d, %d);\n"
# #     with open(output_dir + "/Weibo_Data_result.sql", "w") as file:
# #         for i in range(len(id)):
# #             file.write(sql % (id[i], label[i], pred[i]))
#
# # gen_sql(id_test_1,all_label_1,sz_test_1,pred_1,pred_2)
#
#
# # id,##24小时的真实值##前0.2小时的真实值,##预测的未来0.2-0.5的值,##预测的未来0.2-1的值,##预测的未来0.2-1.5的值,
# # ##预测的未来0.2-2的值,##预测的未来0.2-5的值,##预测的未来0.2-15的值,##预测的未来0.2-24的值
# # id,##24小时的真实值##前0.1小时的真实值,##预测的未来0.1-0.2的值,##预测的未来0.1-0.5的值,##预测的未来0.1-1的值,
# # ##预测的未来0.1-1.5的值,##预测的未来0.1-2的值,##预测的未来0.1-5的值,##预测的未来0.1-10的值
#
# # id，XX先按最后的all_label_7来，sz_test，pred_1,pred_2,pred_3,pred_4,pred_5,pred_6,pred_7
#
# with open('weibo_o0.1.txt','w') as file:
#     for i in range(len(id_test_1)):
#         string=str(id_test_1[i])+'\t'+str(all_label_7[i])+'\t'+str(sz_test_1[i])+'\t'+str(pred_1[i])+'\t'+str(pred_2[i])+'\t'+\
#                str(pred_3[i])+'\t'+str(pred_4[i])+'\t'+str(pred_5[i])+'\t'+str(pred_6[i])+'\t'+str(pred_7[i])+'\n'
#         file.write(string)
# file.close()