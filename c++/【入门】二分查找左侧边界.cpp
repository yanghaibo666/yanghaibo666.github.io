#include<bits/stdc++.h>
using namespace std;
int n,x,q,a[1000005];
int zbj(int x){
	int l=1,r=n+1,mid;
	while(l<r){
		mid=(l+r)/2;
		if(a[mid]>=x){
			r=mid;
		}
		else{
			l=mid+1;
		}
	}
	if(a[l]>=x){
		return l;
	}
	return -1;
}
int main(){
cin>>n;
for(int i=1;i<=n;i++){
	cin>>a[i];
}
cin>>q;
for(int i=1;i<=q;i++){
	cin>>x;
	cout<<zbj(x)<<" ";
}
return 0;
}
