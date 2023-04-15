#include<bits/stdc++.h>
using namespace std;
int n,a[INT_MAX];
bool zs(int x){
	for(int i=2;i<x;i++){
		if(x%i==0){
			return false;
		}
	}
	return true;
}
int main(){
int n;
cin>>n;
int s=0;
int j=1;
for(int i=2;i<n;i++){
	if(n%i==0&&zs(i)){
		a[j]=i;
		j++; 
		s++;
	}
}
for(int i=1;i<s;i++){
	cout<<a[i]<<" ";
}
cout<<a[s]<<endl;
cout<<s;
return 0;
}

