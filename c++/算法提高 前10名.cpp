#include<bits/stdc++.h>
using namespace std;
int a[205];
int main(){
int n;
cin>>n;
for(int i=1;i<=n;i++){
	cin>>a[i];
}
sort(a+1,a+n+1);
for(int i=n;i>=(n-9);i--){
	cout<<a[i]<<" ";
}
return 0;
}

