#include<bits/stdc++.h>
using namespace std;
long long n;
struct sfz{
	int birthday;
	long long data;
}a[100005];
bool cmp(sfz x,sfz y){
	if(x.birthday!=y.birthday)
	return x.birthday>y.birthday;
	return x.data>y.data;
}
int main(){
cin>>n;
for(int i=1;i<=n;i++){
	cin>>a[i].data;
	a[i].birthday=a[i].data/10000%100000000;
}
sort(a+1,a+n+1,cmp);
for(int i=1;i<=n;i++){
	cout<<a[i].data<<endl;
}
return 0;
}
