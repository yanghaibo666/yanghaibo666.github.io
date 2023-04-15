#include<bits/stdc++.h>
using namespace std;
int n,m,a[20][20];
void fun(int x,int y,int k){
a[x][y]=k;
if(y+1<=m&&a[x][y+1]==0)fun(x,y+1,k+1);
if(x+1<=n&&a[x+1][y]==0)fun(x+1,y,k+1);
if(y-1>=1&&a[x][y-1]==0)fun(x,y-1,k+1);
if(x-1>=1&&a[x-1][y]==0)fun(x-1,y,k+1);
}
int main(){
cin>>n>>m;
fun(1,1,1);
for(int i=1;i<=n;i++){
	for(int j=1;j<=m;j++){
		cout<<setw(3)<<a[i][j];
	}
	cout<<endl;
}
return 0;
}
