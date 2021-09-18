#include <iostream>
#include <sstream>
using namespace std ;

void success(unsigned int num_words, unsigned int num_typed);

int main()
{


	cout << "Hello World!" << endl;
	return 0;
}

void success( unsigned int num_words, unsigned int num_typed) {

	if (num_words > num_typed) {
		cout << "Sorry, you typed " << num_typed << " words, and you needed " << num_words << ". Try again!" << endl;
	}
	else {
		cout << "You typed " << num_typed << " words, and you needed " << num_words << ". Great job! Starting next level..." << endl;
	}


}