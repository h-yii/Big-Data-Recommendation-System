from SVD import *

mySVD=SVDModel()
#读取训练集
mySVD.loadTrainSet()
#进行训练
mySVD.train()
#读取物品属性集
#mySVD.linear()
#在验证集上测试
begin=time.time()
mySVD.evaluate()
end=time.time()
duration = end - begin
print("评估模型花费时间为：", "%.6f" % duration, "秒")
#在测试集上测试
begin=time.time()
mySVD.predictOnTestDataset()
end=time.time()
duration = end - begin
print("预测花费时间为：", "%.6f" % duration, "秒")

