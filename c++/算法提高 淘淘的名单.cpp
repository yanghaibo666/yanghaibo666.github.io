#include<bits/stdc++.h>
using namespace std;
int n;
string a[100005];
int main(){
cin>>n;
for(int i=1;i<=n;i++){
	cin>>a[i];
}
for(int i=1;i<=n;i++){
	if(a[i]=="WYS")cout<<"KXZSMR\n";
	else if(a[i]=="CQ")cout<<"CHAIQIANG\n";
	else if(a[i]=="LC")cout<<"DRAGONNET\n";
	else if(a[i]=="SYT"||a[i]=="SSD"||a[i]=="LSS"||a[i]=="LYF")cout<<"STUDYFATHER\n";
	else cout<<"DENOMINATOR\n";
}
return 0;
}
/*
如果这个名字是“WYS”，他希望你的程序输出“KXZSMR”。
　　如果这个名字是“CQ”，他希望你的程序输出“CHAIQIANG”。
　　如果这个名字是“LC“，他希望你的程序输出“DRAGONNET”。
　　如果这个名字是“SYT”或“SSD”或“LSS”或“LYF”，他希望你的程序输出“STUDYFATHER”。
　　如果这个名字与上述任意名字都不相同，他希望你的程序输出“DENOMINATOR”。
*/
