#include<bits/stdc++.h>
using namespace std;
int m,n,a[1000005],b[1000005],l,r,mid,sum;
int main(){
cin>>m>>n;
for(int i=1;i<=m;i++){
	cin>>a[i];
}
for(int i=1;i<=n;i++){
	cin>>b[i];
}
sort(a+1,a+m+1);
for(int i=1;i<=n;i++){
	l=1;
	r=m;
	while(l<=r){
		mid=(l+r)/2;
		if(a[mid]>=b[i]){
			r=mid-1;
		}
		else{
			l=mid+1;
		}
	}
	if(b[i]<=a[1])sum+=a[1]-b[i];
	else sum+=min(abs(a[l]-b[i]),abs(a[l-1]-b[i]));
}
cout<<sum;
return 0;
}

