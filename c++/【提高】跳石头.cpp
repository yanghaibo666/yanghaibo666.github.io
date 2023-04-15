#include<bits/stdc++.h>
using namespace std;
int L,n,m,a[50005];
bool check(int x){
	long long cnt=0,lp=0;
	for(int i=1;i<=n;i++){
		if(a[i]-lp<x){
			cnt++;
		}
		else{
			lp=a[i];
		}
	}
	if(L-lp<x){
		cnt++;
	}
	return cnt<=m;
}
int main(){
cin>>L>>n>>m;
for(int i=1;i<=n;i++){
	cin>>a[i];
}
int l=1,r=L,mid;
while(l<=r){
mid=(l+r)/2;
if(check(mid))l=mid+1;
else r=mid-1;
}
cout<<l-1;
return 0;
}
