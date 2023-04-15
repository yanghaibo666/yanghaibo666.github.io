#include<bits/stdc++.h>
using namespace std;
int n;
int a[1000005],x;
int main(){
cin>>n;
for(int i=1;i<=n;i++){
	cin>>a[i];
}
cin>>x;
int l=1,r=n,mid,f=INT_MIN;
while(l<=r){
	mid=(l+r)/2;
	if(a[mid]==x){
		f=mid;
		break;
	}
	if(a[mid]>x){
		r=mid-1;
	}
	else{
		l=mid+1;
	}
}
if(f==INT_MIN){
	cout<<-1;
}
else{
	cout<<f;
}
return 0;
}
