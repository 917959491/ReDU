import math
DATA_PATHA = "../data1_renminwang_new"


train_pkl = DATA_PATHA+"/data_train.pkl"
val_pkl = DATA_PATHA+"/data_val.pkl"
test_pkl = DATA_PATHA+"/data_test.pkl"
information = DATA_PATHA+"/information.pkl"

##11.29
# cascades  = DATA_PATHA+"/dataset_weibo.txt"

##11.30
cascades  = DATA_PATHA+"/test.txt"


cascade_train = DATA_PATHA+"/cascade_train.txt"
cascade_val = DATA_PATHA+"/cascade_val.txt"
cascade_test = DATA_PATHA+"/cascade_test.txt"
shortestpath_train = DATA_PATHA+"/shortestpath_train.txt"
shortestpath_val = DATA_PATHA+"/shortestpath_val.txt"
shortestpath_test = DATA_PATHA+"/shortestpath_test.txt"
pre_times = [1.5 * 3600]


#11.29
#parameters
observation = 0.5*60*60-1

##11.30
# observation = 24*60*60-1
print ("observation time",observation)
n_time_interval = 6
print ("the number of time interval:",n_time_interval)
time_interval = math.ceil((observation+1)*1.0/n_time_interval)#向上取整
print ("time interval:",time_interval)
lmax = 2
