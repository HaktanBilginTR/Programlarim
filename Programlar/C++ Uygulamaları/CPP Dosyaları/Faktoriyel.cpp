#include <iostream>
using namespace std;
int main() {cout<<"Faktoriyel Hesaplama Makinesine Hosgeldin"<<endl;
	while(true){int sayi;cout<<"Sayiyi Giriniz : "<<endl;cin>>sayi;int faktor=1;
	for(int i=1;i<=sayi;i++){faktor*=i;}
	cout<<"Faktoriyel : "<< faktor<<"\n********************"<<endl;}
	return 0;}
