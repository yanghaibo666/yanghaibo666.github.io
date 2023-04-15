#include<bits/stdc++.h>
using namespace std;
long long n,c,s,a[1000005],l=1,r,mid;
bool check(int x){ 
	long long sum=0,lp=a[1];
	for(int i=2;i<=n;i++){
		if(a[i]-lp<x){
			sum++;
		}
		else{
			lp=a[i];
		}
		if(sum>s){
			return 0;
		}
	}
	return 1;
}
int main(){
cin>>n>>c;
for(int i=1;i<=n;i++){
	cin>>a[i];
}
sort(a+1,a+1+n);
r=a[n]-a[1];
s=n-c;
while(l<=r){
	mid=(l+r)/2;
	if(check(mid))l=mid+1;
	else r=mid-1;
}
if(check(l))cout<<l;
else cout<<r;
return 0;
}

