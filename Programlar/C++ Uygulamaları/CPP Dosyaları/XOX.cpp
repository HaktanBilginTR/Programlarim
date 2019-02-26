#include <iostream>
#include "windows.h"
using namespace std;
char matris[9] = { '1', '2', '3', '4', '5', '6', '7', '8', '9' };

void render() {
	for (int i = 1; i <= 9; i++) 
	{
		cout << matris[i-1] << "  ";

		if (i % 3 == 0)
		{
			cout << endl;
		}
	}
}

void o_sira() {
	char o_giris;
	cin >> o_giris;
	if (o_giris == '1') {
		matris[0] = 'O';
	}
	else if (o_giris == '2') {
		matris[1] = 'O';
	}
	else if (o_giris == '3') {
		matris[2] = 'O';
	}
	else if (o_giris == '4') {
		matris[3] = 'O';
	}
	else if (o_giris == '5') {
		matris[4] = 'O';
	}
	else if (o_giris == '6') {
		matris[5] = 'O';
	}
	else if (o_giris == '7') {
		matris[6] = 'O';
	}
	else if (o_giris == '8') {
		matris[7] = 'O';
	}
	else if (o_giris == '9') {
		matris[8] = 'O';

	}
	cout << "******************************" << endl;
}

void x_sira() {
	char x_giris;
	cin >> x_giris;
	if (x_giris == '1') {
		matris[0] = 'X';
	}
	else if (x_giris == '2') {
		matris[1] = 'X';
	}
	else if (x_giris == '3') {
		matris[2] = 'X';
	}
	else if (x_giris == '4') {
		matris[3] = 'X';
	}
	else if (x_giris == '5') {
		matris[4] = 'X';
	}
	else if (x_giris == '6') {
		matris[5] = 'X';
	}
	else if (x_giris == '7') {
		matris[6] = 'X';
	}
	else if (x_giris == '8') {
		matris[7] = 'X';
	}
	else if (x_giris == '9') {
		matris[8] = 'X';

	}
	cout << "******************************" << endl;
}

void xxx() 
{
	if (matris[0] == 'X' and matris[1] == 'X' and matris[2] == 'X')
	{
		cout << "X Kazandi !!!" << endl;
		Sleep(10000);
		system("PAUSE");
	}
	else if (matris[3] == 'X' and matris[4] == 'X' and matris[5] == 'X')
	{
		cout << "X Kazandi !!!" << endl;
		Sleep(10000);
		system("PAUSE");

	}
	else if (matris[6] == 'X' and matris[7] == 'X' and matris[8] == 'X')
	{
		cout << "X Kazandi !!!" << endl;
		Sleep(10000);
		system("PAUSE");

	}
	else if (matris[0] == 'X' and matris[3] == 'X' and matris[6] == 'X')
	{
		cout << "X Kazandi !!!" << endl;
		Sleep(10000);
		system("PAUSE");

	}
	else if (matris[1] == 'X' and matris[4] == 'X' and matris[7] == 'X')
	{
		cout << "X Kazandi !!!" << endl;
		Sleep(10000);
		system("PAUSE");

	}
	else if (matris[2] == 'X' and matris[5] == 'X' and matris[8] == 'X')
	{
		cout << "X Kazandi !!!" << endl;
		Sleep(10000);
		system("PAUSE");

	}
	else if (matris[0] == 'X' and matris[4] == 'X' and matris[8] == 'X')
	{
		cout << "X Kazandi !!!" << endl;
		Sleep(10000);
		system("PAUSE");

	}
	else if (matris[2] == 'X' and matris[4] == 'X' and matris[6] == 'X')
	{
		cout << "X Kazandi !!!" << endl;
		Sleep(10000);
		system("PAUSE");

	}
}

void ooo() 
{
	if (matris[0] == 'O' and matris[1] == 'O' and matris[2] == 'O')
	{
		cout << "O Kazandi !!!" << endl;
		Sleep(10000);
		system("PAUSE");
	}
	else if (matris[3] == 'O' and matris[4] == 'O' and matris[5] == 'O')
	{
		cout << "O Kazandi !!!" << endl;
		Sleep(10000);
		system("PAUSE");

	}
	else if (matris[6] == 'O' and matris[7] == 'O' and matris[8] == 'O')
	{
		cout << "O Kazandi !!!" << endl;
		Sleep(10000);
		system("PAUSE");

	}
	else if (matris[0] == 'O' and matris[3] == 'O' and matris[6] == 'O')
	{
		cout << "O Kazandi !!!" << endl;
		Sleep(10000);
		system("PAUSE");

	}
	else if (matris[1] == 'O' and matris[4] == 'O' and matris[7] == 'O')
	{
		cout << "O Kazandi !!!" << endl;
		Sleep(10000);
		system("PAUSE");

	}
	else if (matris[2] == 'O' and matris[5] == 'O' and matris[8] == 'O')
	{
		cout << "O Kazandi !!!" << endl;
		Sleep(10000);
		system("PAUSE");

	}
	else if (matris[0] == 'O' and matris[4] == 'O' and matris[8] == 'O')
	{
		cout << "O Kazandi !!!" << endl;
		Sleep(10000);
		system("PAUSE");

	}
	else if (matris[2] == 'O' and matris[4] == 'O' and matris[6] == 'O')
	{
		cout << "O Kazandi !!!" << endl;
		Sleep(10000);
		system("PAUSE");

	}
}

void bitis() 
{
	xxx();
	ooo();

}

void sira() 
{
	while (true)
		{
		render();
		bitis();
		x_sira();
		render();
		bitis();
		o_sira();
		}
}

int main() {
	cout << "---------------------------------\nTic Tac Toe/XOX Oyununa Hosgeldin\n1. Oyuncu = X\n2. Oyuncu = O\n---------------------------------"<< endl;
	sira();

	return 0;
}
