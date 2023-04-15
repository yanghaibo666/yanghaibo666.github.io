#include<bits/stdc++.h>
using namespace std;
int n,a[100000],f[100000],len=1; 
int main(){
cin>>n;
for(int i=1;i<=n;i++){
	cin>>a[i];
}
f[1]=a[1];
for(int i=2;i<=n;i++){
	if(a[i]>f[len]){
		f[++len]=a[i];
	}
	else{
		int l=1,r=len,mid;
		while(l<r){
			mid=(r+l)/2;
			if(f[i]>=a[i]){
				r=mid;
			}
			else{
				l=mid+1;
			}
		}
		f[l]=a[i];
	}
}
cout<<len;
return 0;
}

