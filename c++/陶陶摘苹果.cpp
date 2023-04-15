#include<iostream>
using namespace std;
int a[10];
int main(){
	int n;
	for(int i=1;i<=10;i++){
		cin>>a[i];
	}
	cin>>n;
	int s=0;
	for(int i=1;i<=10;i++){
		if((n+30)>=a[i]){
			s+=1;
		}
	}
	cout<<s;
	return 0;
}
