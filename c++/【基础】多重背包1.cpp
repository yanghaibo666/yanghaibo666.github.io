#include<bits/stdc++.h>
using namespace std;
int N,V,vi,wi,si,xb=1,v[10005],w[10005],f[10005];
int main(){
cin>>N>>V;
for(int i=1;i<=N;i++){
	cin>>vi>>wi>>si;
	for(int j=1;j<=si;j++){
		v[xb]=vi;
		w[xb]=wi;
		xb++;
	}
}
for(int i=1;i<xb;i++){
	for(int j=V;j>=v[i];j--){
		f[j]=max(f[j],w[i]+f[j-v[i]]);
	}
}
cout<<f[V];
return 0;
}

