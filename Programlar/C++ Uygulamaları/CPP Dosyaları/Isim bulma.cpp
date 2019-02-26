#include "windows.h"
#include <iostream>



using namespace std;

int main() {
	string array[10] = { "Mehmet","Anil","Ahmet","Burak","Bartu","Kubilay","Mirza","Necat","Arif","Arda" };
	string *ptr = array;
	char isim[20];

	cout << "Isim girin : " << endl;
	cin >> isim;
	int i = 0;
	while (i < 10)
	{
		if (isim == *ptr or isim == *(ptr + 1) or isim == *(ptr + 2) or isim == *(ptr + 3) or isim == *(ptr + 4) or isim == *(ptr + 5) or isim == *(ptr + 6) or isim == *(ptr + 7) or isim == *(ptr + 8) or isim == *(ptr + 9))
		{
			cout << "Tebrikler !!";
			Sleep(99999999);
			break;
			
		}
		else cout << "agla bulamadin"; Sleep(5000);break;
	}
	return 0;
}
