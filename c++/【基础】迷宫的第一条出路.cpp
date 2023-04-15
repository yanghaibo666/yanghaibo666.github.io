#include<bits/stdc++.h>
using namespace std;
int n;
int r[405][3];
char a[25][25];
int fx[5]={0,0,-1,0,1};
int fy[5]={0,-1,0,1,0};
void print(int k){
for(int i=1;i<k;i++){
cout<<"("<<r[i][1]<<","<<r[i][2]<<")->";
}
cout<<"("<<r[k][1]<<","<<r[k][2]<<")";
exit(0);
}
void dfs(int x,int y,int k){
r[k][1]=x;
r[k][2]=y;
a[x][y]='1';
if(x==n&&y==n){
print(k);
}
int tx,ty;
for(int i=1;i<=4;i++){
tx=x+fx[i];
ty=y+fy[i];
if(a[tx][ty]=='0')dfs(tx,ty,k+1);
}
}
int main(){
cin>>n;
for(int i=1;i<=n;i++){
for(int j=1;j<=n;j++){
cin>>a[i][j];
}
}
dfs(1,1,1);
return 0;
}
