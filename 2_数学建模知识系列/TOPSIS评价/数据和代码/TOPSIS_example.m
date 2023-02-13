%%第一步：从Excel中导入数据
load data_health.mat

%%第二步：判断某些指标的数据是否需要正向化
[m,n]=size(X);
disp(['共有',num2str(m),'个评价对象',num2str(n),'个评价指标'])
judge=input('请判断矩阵X是否需要正向化处理，是输入1，否输入0:');
if judge==1
    Position=input('请输入需正向化处理的指标所在列：') %如在2，3，4列，则输入[2,3,4]
    disp('请输入这些指标的类型（1：极小型，2：中间型，3：区间型）：')
    Type=input('第2列是极小型，第3列是中间型，第4列是区间型，则输入[1,2,3]:')
    for i=1:size(Position,2)  %得出循环次数
        X(:,Position(i))=Positivization(X(:,Position(i)),Type(i),Position);
    end
    disp('正向化后的矩阵X=')
    disp(X)
end


%%第三步：标准化
Z=X./repmat(sum(X.*X).^0.5,m,1);
disp('标准化矩阵Z=')
disp(Z)

%%第四步：计算得分
D_P=sum([(Z-repmat(max(Z),m,1)).^2],2).^0.5;  %D+与最大值的距离向量
D_N=sum([(Z-repmat(min(Z),m,1)).^2],2).^0.5;  %D-与最小值的距离向量
S=D_N./(D_P+D_N); 
disp('最后得分为：')
Stand_S = S/sum(S)  %归一化
[sorted_S,index] = sort(Stand_S,'descend')
