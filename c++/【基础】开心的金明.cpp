#include<bits/stdc++.h>
using namespace std;
int n,m,v[30],p[30],f[30],min=INT_MAX;
int main(){
cin>>n>>m;
for(int i=1;i<=m;i++){
	cin>>v[i]>>p[i];
}
for(int i=1;i<=m;i++){
	for(int j=n;j>=v[i];j--){
		f[j]=max(f[j],f[j-v[i]]+v[i]*p[i]);
	}
}
cout<<f[n];
return 0;
}

