#include<bits/stdc++.h>
using namespace std;
int n,x,q,a[1000005];
int ybj(int x){
	int l=1,r=n,mid;
	while(l<=r){
		mid=(l+r)/2;
		if(a[mid]<=x){
			l=mid+1;
		}
		else{
			r=mid-1;
		}
	}
	if(a[l-1]==x){
		return l-1;
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
	cout<<ybj(x)<<" ";
}
return 0;
}

