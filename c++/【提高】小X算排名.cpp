#include<bits/stdc++.h>
using namespace std;
int l,r,mid;
int n,a[100005],b[100005];
bool cmp(int x,int y){
	return x>y;
}

int zbj(int x){
	l=1;
	r=n;
	while(l<=r){
		mid=(l+r)/2;
		if(a[mid]<=x){
			r=mid-1;
		}
		else{
			l=mid+1;
		}
	}
	return l;
}
 
int main(){
cin>>n;
for(int i=1;i<=n;i++){
	cin>>a[i];
	b[i]=a[i];
}

sort(a+1,a+n+1,cmp);
for(int i=1;i<=n;i++){
cout<<zbj(b[i])<<endl;
}
return 0;
}

