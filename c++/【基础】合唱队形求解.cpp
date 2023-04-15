#include<bits/stdc++.h>
using namespace std;
int n,a[105],lf[105],rf[105],maxn;
int main() {
	cin>>n;
	for(int i=1; i<=n; i++) {
		cin>>a[i];
	}
	for(int i=1; i<=n; i++) {
		lf[i]=1;
		for(int j=1; j<i; j++) {
			if(a[j]<a[i])lf[i]=max(lf[i],lf[j]+1);
		}
	}
	for(int i=n; i>=1; i--) {
		rf[i]=1;
		for(int j=n; j>i; j--) {
			if(a[j]<a[i])rf[i]=max(rf[i],rf[j]+1);
		}
	}
	for(int i=1; i<=n;i++) {
		maxn=max(maxn,lf[i]+rf[i]-1);
	}
	cout<<n-maxn;
	return 0;
}

