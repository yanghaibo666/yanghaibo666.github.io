#include<bits/stdc++.h>
using namespace std;
int a[4][5];
int maxn=INT_MIN;
int maxi,maxj;
int main(){
for(int i=1;i<=3;i++){
for(int j=1;j<=4;j++){
cin>>a[i][j];
if(maxn<a[i][j]){
	maxn=a[i][j];
maxi=i;
maxj=j;
}
}
}
cout<<maxn<<endl<<maxi<<endl<<maxj;
return 0;
}

