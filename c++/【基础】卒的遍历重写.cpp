#include<bits/stdc++.h>
using namespace std;
int n,m,ant;
int fx[3]={0,1,0};
int fy[3]={0,0,1};
int r[30][2];
void print(int k){
cout<<++ant<<":";
for(int i=1;i<k;i++){
cout<<r[i][1]<<","<<r[i][2]<<"->";
}
cout<<n<<","<<m<<endl;
}
void dfs(int x,int y,int k){
r[k][1]=x;
r[k][2]=y;
if(x==n&&y==m)print(k);
int tx,ty;
for(int i=1;i<=2;i++){
tx=x+fx[i];
ty=y+fy[i];
if(tx>=1&&tx<=n&&ty>=1&&ty<=m){
dfs(tx,ty,k+1);
}
}
}
int main(){
cin>>n>>m;
dfs(1,1,1);
return 0;
}

