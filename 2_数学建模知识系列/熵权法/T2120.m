disp('输入矩阵A');
A=input('A=');
%%D=max(A);
%%归一化%%
[n,m] = size(A);
minguiyi=repmat(min(A),n,1);
maxguiyi=repmat(max(A),n,1);
B=(A-minguiyi) ./ (maxguiyi-minguiyi);
% disp('归一化结果为 B =  ');
% disp(B);
%%计算信息熵%%
C=B./repmat(sum(B),n,1);
% disp(' P的矩阵为 P=  ');
% disp(C);%%C是概率矩阵

for i = 1:n
    for j = 1:m
        if C(i,j) == 0
            D(i,j)=0;
            
        else
            D(i,j) = C(i,j)*log(C(i,j));
        end
    end
end
E=-sum(D)/log(n);%%每一列的信息熵

%%计算每个指标的信息效用值%%
F=1-E;
%%权重的计算；
sq=F/sum(F,2);

%%加上权重比较%%
A_=sum(A.*repmat(sq,n,1),2);
disp('加权结果为:');
disp(A_);