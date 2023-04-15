#include<bits/stdc++.h>
using namespace std;
int n,m,s=0;
int fx[5]={0,0,1,0,-1};
int fy[5]={0,1,0,-1,0};
char a[105][105];
void dfs(int x,int y){
a[x][y]='.';
int tx,ty;
for(int i=1;i<=4;i++){
	tx=x+fx[i];
	ty=y+fy[i];
	if(a[tx][ty]=='W'){
		dfs(tx,ty);
	}
}
}
int main(){
cin>>n>>m;
for(int i=1;i<=n;i++){
for(int j=1;j<=m;j++){
cin>>a[i][j];
}
}
for(int i=1;i<=n;i++){
for(int j=1;j<=m;j++){
	if(a[i][j]=='W'){
		s++;
		dfs(i,j);
	}
}
}
cout<<s;
return 0;
}
