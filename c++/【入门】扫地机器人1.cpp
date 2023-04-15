#include<bits/stdc++.h>
using namespace std;
int n,m,a[20][20];
void fun(int x,int y,int k){
if(x>=1&&x<=n&&y>=1&&y<=m&&a[x][y]==0){
a[x][y]=k;
fun(x,y+1,k+1);
fun(x+1,y,k+1);
fun(x,y-1,k+1);
fun(x-1,y,k+1);
}
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
