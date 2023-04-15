#include<bits/stdc++.h>
using namespace std;
int n,x,a[100005],f[100005],sum;
int main(){
	cin>>n>>x;//输入数据
	a[1]=x;//设置边界值
	for(int i=2;i<=n;i++){//生成数据
		a[i]=(379*a[i-1]+131)%997;
	}
	sum+=x;//将已知的第一个数字加到最后的总和里
	f[1]=x;//设置边界值
	for(int i=2;i<=n;i++){
		f[i]=min(f[i-1],a[i]);//判断一下前面的最小数与新加的数字哪个小
		sum+=f[i];//加上判断好的最小数
	}
	cout<<sum;//输出结果
	return 0;
}