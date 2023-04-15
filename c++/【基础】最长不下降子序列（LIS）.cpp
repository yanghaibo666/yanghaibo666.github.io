#include<bits/stdc++.h>
using namespace std;
int n,a[10005],f[10005],maxn=INT_MIN;
int main(){
cin>>n;
for(int i=1;i<=n;i++){
	cin>>a[i];	
}
for(int i=1;i<=n;i++){
	f[i]=1;
}
for(int i=1;i<=n;i++){
	for(int j=1;j<i;j++){
		if(a[j]<=a[i]){
			f[i]=max(f[j]+1,f[i]);
			maxn=max(maxn,f[i]);
		}
	}
}
cout<<maxn;
return 0;
}
/*
3 18 7 14 10 12 23 41 16 24
1 2  2 3  3  4  5  6  5  6

 
*/
