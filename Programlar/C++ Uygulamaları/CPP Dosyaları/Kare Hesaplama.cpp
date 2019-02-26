#include <iostream>
using namespace std;
int main() {
	int sayi, *ptr;
	ptr = &sayi;
	cout << "Kare Hesaplamaya Hosgeldin!" << endl;
	while (true) {
		cout << "Sayiyi Girin :" << endl;
		cin >> *ptr;
		*ptr *= *ptr;
		cout << "Sayiniz : " << *ptr << "\n*********************" << endl;
	}

	return 0;
}
