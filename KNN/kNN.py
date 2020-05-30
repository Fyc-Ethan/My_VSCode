import numpy as np
import matplotlib.pyplot as plt 
from os import listdir
from sklearn.neighbors import KNeighborsClassifier as KNN


"""
函数说明:将32x32的二进制图像转换为1x1024向量
"""
def imgvector(filename):
    #创建1x1024零向量
    returnVect = np.zeros((1, 1024))
    #打开文件
    fr = open(filename)
    #按行读取
    for i in range(32):
        #读一行数据
        lineStr = fr.readline()
        #每一行的前32个元素依次添加到returnVect中
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])
    #返回转换后的1x1024向量
    #print(returnVect)
    return returnVect

"""
函数说明:通过KNeighborsClassifier函数训练KNN分类器
"""
def KNNtrain(k):
    #训练集的Labels
    trainLabels = []
    #返回train集目录下的文件名
    trainFileList = listdir('trainSet')
    #返回文件夹下文件的个数
    mTrain = len(trainFileList)
    #初始化训练集的Mat矩阵,训练集
    trainMat = np.zeros((mTrain, 1024))
    #从文件名中解析出训练集的类别
    for i in range(mTrain):
        #获得文件的名字
        fileName = trainFileList[i]
        #获得分类的数字
        classNumber = int(fileName.split('_')[0])
        #将获得的类别添加到hwLabels中
        trainLabels.append(classNumber)
        #将每一个文件的1x1024数据存储到trainingMat中
        trainMat[i,:] = imgvector('trainSet/%s' % (fileName))
    #构建kNN分类器
    knn =KNN(n_neighbors = k, algorithm = 'auto')
    # n_neighbors: 表示查询k个最近邻的数目
    # algorithm:指定用于计算最近邻的算法，auto表示试图采用最适合的算法计算最近邻
   
    #拟合模型, trainMat为训练矩阵,trainLabels为对应的标签
    knn.fit(trainMat, trainLabels)
    return knn

"""
函数说明:手写数字分类测试
"""
def handwritingClassTest(k):
    
    #获得KNN分类器
    knn = KNNtrain(k)
    #返回testSet目录下的文件列表
    testFileList = listdir('testSet')
    #统计识别个数
    Count = 0
    #测试集的数量
    mTest = len(testFileList)
    #从文件中解析出测试集的类别并进行 分类测试
    for i in range(mTest):
        #获得文件的名字
        fileName = testFileList[i]
        #获得分类的数字
        classNumber = int(fileName.split('_')[0])
        #获得测试集的1x1024向量,用于训练
        Testvector = imgvector('testSet/%s' % (fileName))
        #获得预测结果
        classResult = knn.predict(Testvector)
        #print("实验结果为%d\t实际结果为%d" % (classResult, classNumber))
        if(classResult == classNumber):
            Count += 1
    #print("总共%d个数据，识别%d个\n识别率为%f%%" % (mTest,Count, Count/mTest * 100))
    #返回识别率
    return Count/mTest * 100


"""
函数说明:main函数
"""
if __name__=='__main__':
    #记录K的值
    x = []
    #记录识别率
    y = []
    #计算K取1-10时的识别率
    for i in range(1,11):
        #显示识别率
        print(i,':',handwritingClassTest(i))
        #将K值记录到x中
        x.append(i)
        #将识别率记录到y中
        y.append(handwritingClassTest(i))

    #获得k与识别率的关系图
    plt.plot(x,y) 
    plt.xlabel('K Value') 
    plt.ylabel('Recognition Rate') 
    plt.show() 