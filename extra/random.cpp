#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    srand(time(NULL)); // Seed the random number generator with the current time
    int sum = 0;

    // INSERT into dip () value ();

    // cout<<"INSERT INTO dip (date, ";
    // for (int i = 1; i <= 124; i++) {
    //     std::cout << "roll_"<< i << ", ";
    // }
    // cout<<"sum) VALUES ('2023-01-25', ";

    // for (int i = 0; i < 124; i++) {
    //     int rand_num = rand() % 2; // Generate a random number between 0 and 1
    //     std::cout << rand_num << ", ";
    //     sum+=rand_num;
    // }
    // std::cout<<sum<<");"<<endl;

    // select sum (roll_1),sum(roll_2),.....,sum(roll_124), sum(sum) from dip;

    cout<<"SELECT ";
    for (int i = 1; i <= 124; i++) {
        std::cout << "sum(roll_"<< i << "), ";
    }
    cout<<"sum(sum) FROM dip;"<<endl;

    return 0;
}
