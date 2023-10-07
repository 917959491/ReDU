基于CasCN的微博热度预测

Steps to run CasCN
----------------------------------- 

1.split the data to train set, validation set and test set. Then trainsform the datasets to the format of ".pkl"
command: 

    cd preprocessing
    python utils.py
    python preprocess_graph_signal.py
 
2.train Model
command:

    cd model
    python run_graph_sequence.py


