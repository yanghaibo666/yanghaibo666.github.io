#include<bits/stdc++.h>
using namespace std;
int x,m,n;
bool pd(int x1){
while(x1!=0){
int c=x1%10;
x1/=10;
if(c==x){
return 1;
}
}
return 0;
} 
int main(){
cin>>x>>m>>n;
int sum=0;
for(int i=m;i<=n;i++){
if(pd(i)){
sum++;
}
}
cout<<sum;
return 0;
}
