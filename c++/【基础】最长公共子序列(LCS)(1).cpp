#include<bits/stdc++.h>
using namespace std;
const int N=1000000+5;
int n,a[N],b[N],c[N],d[N],f[N]; 
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
int len=1;
f[1]=d[1];
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
	}
}
cout<<len;
return 0;
}

