#include<bits/stdc++.h>
using namespace std;
int L,n,k;
int a[100005];
bool check(int x){
long long cnt=0;
for(int i=2;i<=n;i++){
if(a[i]-a[i-1]>x){
cnt+=(a[i]-a[i-1])/x;
if((a[i]-a[i-1])%x==0)cnt--;
}
}
return cnt<=k;
}
int main(){
cin>>L>>n>>k;
for(int i=1;i<=n;i++){
	cin>>a[i];
}
sort(a+1,a+n+1); 
int l=1,r=L,mid;
while(l<=r){
mid=(l+r)/2;
if(check(mid))r=mid-1;
else l=mid+1;
}
cout<<l;
return 0;
}

