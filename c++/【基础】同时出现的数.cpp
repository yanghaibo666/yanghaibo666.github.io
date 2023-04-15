#include<bits/stdc++.h>
using namespace std;
int n,m,a[100005],b[100005];
bool zbz(int x){
	int l=1,r=n,mid;
	while(l<=r){
		mid=(l+r)/2;
		if(a[mid]==x){
			return true;
		}
		else if(a[mid]<x){
			l=mid+1;
		}
		else{
			r=mid-1;
		}
	}
	return false;
}
int main(){
cin>>n;
cin>>m;
for(int i=1;i<=n;i++){
	cin>>a[i];
}
sort(a+1,a+n+1);
for(int i=1;i<=m;i++){
	cin>>b[i];
	
}
sort(b+1,b+1+m);
for(int i=1;i<=m;i++){
	if(zbz(b[i])){
		cout<<b[i]<<" ";
	}
}
return 0;
}
