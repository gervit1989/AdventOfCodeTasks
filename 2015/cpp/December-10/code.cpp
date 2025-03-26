#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
using namespace std;
std::string work_on(std::string sIn)
{
	string res = "";
	std::stringstream row1;
	int pos = 0, length = sIn.length();
	while (1) {
		int icount = 1;
		string letter = sIn.substr(pos, 1);
		if (pos + 1 == length) {
			row1 << icount << letter;
			break;
		}
		else {
			int posinit = pos;
			for (int i = pos + 1; i < length; i++) {
				string letter2 = sIn.substr(i, 1);
				if (letter2 == letter)
					icount++;
				else {
					pos = i;
					row1 << icount << letter;
					break;
				}
			}
			if (posinit + icount == length) {
				row1 << icount << letter;
				break;
			}
		}
	}

	return row1.str();
}

int main()
{
	std::string sInput = "1113122113", sWork;
	for (int iTry=0; iTry < 50;iTry++)
	{
		sWork = work_on(sInput);
		sInput = sWork;

		cout << iTry <<"\t"<< sWork.length() << "\n";
	}
	cout << sWork.length() << "\n";
	system("pause");
    return 0;
}