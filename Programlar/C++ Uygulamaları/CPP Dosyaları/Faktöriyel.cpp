#include <iostream>
using namespace std;


int main() {
	cout << "Faktoriyel Hesaplama Makinesine Hosgeldin" << endl;
	while (true)
		{
		int sayi, *ptr = &sayi; 
		cout << "Sayiyi Giriniz : " << endl; 
		cin >> *ptr; 
		int faktor = 1;
		for (int i = 1; i <= *ptr; i++)
		{ 
			faktor *= i; 
		}
		cout << "Faktoriyel : " << faktor << "\n********************" << endl;
		}	
	return 0;
}
