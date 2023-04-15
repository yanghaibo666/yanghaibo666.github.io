#include<bits/stdc++.h>
using namespace std;
int a[105],maxn=INT_MIN,s[105],n; 
int main(){
cin>>n;
for(int i=1;i<=n;i++){
	cin>>a[i];
	s[i]=s[i-1]+a[i];
}
for(int i=1;i<=n;i++){
for(int j=i;j<=n;j++){
	maxn=max(maxn,s[j]-s[i-1]);
}
}
cout<<maxn;
return 0;
}

