#include<bits/stdc++.h>
using namespace std;
int maxw,n,w[105],p[105],f[20005];
int main(){
cin>>maxw>>n;
for(int i=1;i<=n;i++){
cin>>w[i]>>p[i];
}
for(int i=1;i<=n;i++){
for(int j=maxw;j>=w[i];j--){
f[j]=max(f[j],f[j-w[i]]+p[i]);
}
}
cout<<f[maxw];
return 0;
}
