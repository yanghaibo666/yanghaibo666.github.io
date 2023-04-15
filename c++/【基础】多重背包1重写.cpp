#include<bits/stdc++.h>
using namespace std;
int N,V,v1,w1,v[105],w[105],si,f[1000005],xb=1;
int main(){
cin>>N>>V;
for(int i=1;i<=N;i++){
cin>>w1>>v1>>si;
for(int j=1;j<=si;j++){
v[xb]=v1;
w[xb]=w1;
xb++;
}
}
for(int i=1;i<xb;i++){
for(int j=V;j>=w[i];j--){
f[j]=max(f[j],f[j-w[i]]+v[i]);
}
}
cout<<f[V];
return 0;
}

