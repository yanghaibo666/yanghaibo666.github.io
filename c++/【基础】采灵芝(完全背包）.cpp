#include<bits/stdc++.h>
using namespace std;
int n,maxw,w[2005],v[2005],f[100005]; 
int main(){
cin>>maxw>>n;
for(int i=1;i<=n;i++){
	cin>>w[i]>>v[i];
}
for(int i=1;i<=n;i++){
	for(int j=w[i];j<=maxw;j++){
		f[j]=max(f[j],v[i]+f[j-w[i]]);

	}
}
cout<<f[maxw];
return 0;
}
