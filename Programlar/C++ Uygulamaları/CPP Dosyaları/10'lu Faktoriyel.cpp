#include <iostream>
#include "windows.h."
using namespace std;

int func(int x) {
	int fakt = 1;
	for (int i = 1; i <= x; i++)
	{
		fakt = fakt * i;

	}
	return fakt;
}

int main() {

	int sayi_1, i = 0, sayi_2, sayi_3, sayi_4, sayi_5, sayi_6, sayi_7, sayi_8, sayi_9, sayi_10;
	cin >> sayi_1 >> sayi_2 >> sayi_3 >> sayi_4 >> sayi_5 >> sayi_6 >> sayi_7 >> sayi_8 >> sayi_9 >> sayi_10;
	int slm[10] = { sayi_1, sayi_2, sayi_3, sayi_4, sayi_5, sayi_6, sayi_7, sayi_8, sayi_9, sayi_10 };

	while (i < 10)
	{
		int a = slm[i];
		cout << func(a) << endl;
		i++;

	}


	Sleep(6000000);

	return 0;
}