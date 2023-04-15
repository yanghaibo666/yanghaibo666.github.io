#include<bits/stdc++.h>
using namespace std;
long long n,a[15];
int main(){
cin>>n;
for(int i=1;i<=n;i++){
	cin>>a[i];
}
int b=0;
sort(a+1,a+n+1);
int flag=0;
for(int i=1;i<=n;i++){
	if(a!=0||a==0&&flag){
		b*=10;
		b+=a[i];
		a[i]=-1;
		flag=1;
	}
}
cout<<b;
return 0;
}

