#include <iostream>
#include <windows.h>

using namespace std;



int main() {
	while (TRUE) {
		char islem;
		double a, b;
		cout << "1. Sayiyi Girin : ";
		cin >> a;
		cout << "Islemi Girin : ";
		cin >> islem;
		cout << "2. Sayiyi Girin : ";
		cin >> b;

		switch (islem) {

		case '+':
			cout << a + b << endl;

			break;

		case '-':
			cout << a - b << endl;

			break;

		case '/':
			cout << a / b << endl;

			break;

		case '*':
			cout << a * b << endl;
			break;

		default:
			cout << "HATA !!!" << endl;
			break;

		}
	}
	return 0;
}



