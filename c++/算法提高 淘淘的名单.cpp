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
�����������ǡ�WYS������ϣ����ĳ��������KXZSMR����
���������������ǡ�CQ������ϣ����ĳ��������CHAIQIANG����
���������������ǡ�LC������ϣ����ĳ��������DRAGONNET����
���������������ǡ�SYT����SSD����LSS����LYF������ϣ����ĳ��������STUDYFATHER����
���������������������������ֶ�����ͬ����ϣ����ĳ��������DENOMINATOR����
*/
