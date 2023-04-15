#include<iostream>
using namespace std;
int main(){
	int n,m,k;
	cin>>n>>m>>k;
	int cj=0,cjz=0;
	int s=0;
	for(int i=1;i<=n;i++){
		cjz=0;
		for(int j=1;j<=m;j++){
			cin>>cj;
			cjz+=cj;
		}
		if(cjz>=k){
			s+=1;
		}
	}
	cout<<s;
	return 0;
}
