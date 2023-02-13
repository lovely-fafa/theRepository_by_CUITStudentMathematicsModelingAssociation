function [posit_x] = Positivization(x,type,i)
if type==1 %极小型
    disp(['第',num2str(i),'列是极小型'])
    posit_x = Min2Max(x); %调用Min2Max进行正向化
    disp(['第',num2str(i),'列正向化处理完成'])
    disp('————————————————————分界线————————————————————')
elseif type==2 %中间型
    disp(['第',num2str(i),'列是中间型'])
    best = input('请输入最佳值：');
    posit_x = Mid2Max(x,best); %调用Min2Max进行正向化
    disp(['第',num2str(i),'列正向化处理完成'])
    disp('————————————————————分界线————————————————————')
elseif type==3 %区间型
    disp(['第',num2str(i),'列是区间型'])
    a = input('请输入区间的下界：');
    b = input('请输入区间的上界：');
    posit_x = Inter2Max(x,a,b); %调用Inter2Max进行正向化
    disp(['第',num2str(i),'列正向化处理完成'])
    disp('————————————————————分界线————————————————————')
else
    disp('没有该类型指标，请检查Type向量中是否有除1、2、3之外的数字')
end