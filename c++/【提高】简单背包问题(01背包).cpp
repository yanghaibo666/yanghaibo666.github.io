#include<bits/stdc++.h>
using namespace std;
int n,maxw,w[105],v[105],f[20005]; 
int main(){
cin>>maxw>>n;
for(int i=1;i<=n;i++){
	cin>>w[i]>>v[i];
}
for(int i=1;i<=n;i++){
	for(int j=maxw;j>=w[i];j--){
		f[j]=max(f[j],v[i]+f[j-w[i]]);

	}
}
cout<<f[maxw];
return 0;
}
