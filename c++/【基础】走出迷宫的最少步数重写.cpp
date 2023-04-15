#include<bits/stdc++.h>
using namespace std;
int n,m;
char a[45][45];
int d[45][45];
int fx[5]={0,0,1,0,-1};
int fy[5]={0,1,0,-1,0};
void dfs(int x,int y,int k){
d[x][y]=k;
int tx,ty;
for(int i=1;i<=4;i++){
tx=x+fx[i];
ty=y+fy[i];
if(a[tx][ty]=='.'&&k+1<d[tx][ty])dfs(tx,ty,k+1); 
}
}
int main(){
cin>>n>>m;
for(int i=1;i<=n;i++){
for(int j=1;j<=m;j++){
cin>>a[i][j];
d[i][j]=INT_MAX;
}
}
dfs(1,1,1);
cout<<d[n][m];
return 0;
}
