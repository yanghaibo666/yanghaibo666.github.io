#include<bits/stdc++.h>
using namespace std;
int N,V,vi,wi,si,v[1000005],w[1000005],s[1000005],xb=0,f[1000005];
int main(){
cin>>N>>V;
for(int i=1;i<=N;i++){
	cin>>vi>>wi>>si;
	if(si>0){
		for(int j=1;j<=si;j++){
			xb++;
			v[xb]=vi;
			w[xb]=wi;
			s[xb]=-1;
		}
	}
	else{
		xb++;
		v[xb]=vi;
		w[xb]=wi;
		s[xb]=si;
		
	}
}
for(int i=1;i<=xb;i++){
	if(s[i]==0){
		for(int j=v[i];j<=V;j++){
			f[j]=max(f[j],w[i]+f[j-v[i]]);
		}
	}
	else{
		for(int j=V;j>=v[i];j--){
			f[j]=max(f[j],w[i]+f[j-v[i]]);
		}
	}
}
cout<<f[V];
return 0;
}
