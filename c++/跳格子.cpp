#include<bits/stdc++.h>
using namespace std;
long long n,A,B,C,f[100005],x[100005];
int main(){
    cin>>n>>A>>B>>C;//输入数据
    for (int i = 1; i <= n; i++){//生成数据
        int tmp = ((long long)A * i * i + B * i + C) % 20000;
        x[i] = tmp - 10000;
    }
    f[0]=0;//设置边界值
    f[1]=x[1];
    for(int i=2;i<=n+1;i++){
        f[i]=x[i]+max(f[i-1],f[i-2]);//寻找前面两个数字之中的最大数，并加上已经跳到的格子上的数字
    }
    cout<<f[n+1];//输出最后结果
return 0;
}
