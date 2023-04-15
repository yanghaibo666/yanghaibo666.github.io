#include<bits/stdc++.h>
using namespace std;
int n;
int a[100000],f[100000];
int main(){
cin>>n;
for(int i=1;i<=n;i++){
	cin>>a[i];
}
int s=0;
f[0]=INT_MIN;
for(int i=1;i<=n;i++){
	if(a[i]>f[i-1]){
		f[i]=a[i];
	}
	else{
		f[i]=f[i-1];
		s+=1;
	}
}
cout<<s;
return 0;
}
/*
8
1 5 3 7 2 8 9 4
    1   2     3
1 5 5 7 7 8 9 9
f[i]表示到此为止整个数列最后一个上升的数字
f[1]=max(a[1],f[0])//f[0]=INT_MIN;
f[2]=max(a[2],f[1])
f[3]=max(a[3],f[2])
f[i]=max(a[i],f[i-1])
*/
