#include<bits/stdc++.h>
using namespace std;
int n,w[105],v[105],f[100005],maxw; 
int main(){
cin>>maxw>>n;
for(int i=1;i<=n;i++){
	cin>>w[i]>>v[i];
}
for(int i=1;i<=n;i++){
	for(int j=maxw;j>=w[i];j--){
		f[j]=max(f[j],f[j-w[i]]+v[i]);
	}
}
cout<<f[maxw]; 
return 0;
}

