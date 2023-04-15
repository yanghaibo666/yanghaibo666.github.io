#include<bits/stdc++.h>
using namespace std;
int n;
int a[1005],b[1005],c[1005],d[1005];
int f[1005];
int main(){
cin>>n;
for(int i=1;i<=n;i++){
cin>>a[i];
c[a[i]]=i;
}
for(int i=1;i<=n;i++){
cin>>b[i];
d[i]=c[b[i]];
}
f[1]=d[1];
int len=1;
for(int i=2;i<=n;i++){
if(d[i]>f[len])f[++len]=d[i];
else{
int l=1,r=len,mid;
while(l<r){
mid=(l+r)/2;
if(f[mid]>=d[i]){
r=mid;
}
else{
l=mid+1;
}
}
f[l]=d[i];
}}
cout<<len;
return 0;
}
