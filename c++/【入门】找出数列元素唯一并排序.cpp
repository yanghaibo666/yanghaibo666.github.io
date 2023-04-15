#include<bits/stdc++.h>
using namespace std;
int n;
int a[1005]; 
int main(){
cin>>n;
for(int i=1;i<=n;i++){
cin>>a[i];
}
sort(a+1,a+n+1);
for(int i=2;i<=n;i++){
	if(a[i]==a[i-1]){
		a[i-1]=-1;
	}
}
for(int i=1;i<=n;i++){
	if(a[i]!=-1){
		cout<<a[i]<<" ";
	}
}
return 0;
}
