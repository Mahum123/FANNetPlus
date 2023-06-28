#include<cstdlib>
#include<iostream>
#include<string>
#include<fstream>
#include<time.h>
#include<thread>
#include<chrono>
#include<unistd.h>

using namespace std;

int call_MC() 
{
time_t t = time(NULL); //value returned generally represents the number of seconds since 00:00 hours, Jan 1, 1970 UTC
char buf[30];
sprintf(buf, "nuXmv -source commands.txt > Output.txt"); //write the output
system(buf);
std::this_thread::sleep_for(std::chrono::seconds(1)); //subtract this 1 sec from the output time
t = time(NULL) - t;
cout << "Elapsed time in seconds : " << ((float)t) << " sec" << endl;
std::terminate();
}

int main() 
{
char buf[50];
   std::thread func_call(call_MC);
   std::this_thread::sleep_for(std::chrono::seconds(7200)); //timeout 
   cout << "Timeout reached" << endl; 
   sprintf(buf, "kill $(ps | grep nuXmv | awk '{print $1}')");
   system(buf);
   std::this_thread::sleep_for(std::chrono::seconds(3)); //give system time to terminate buf
   cout << endl;
   std::terminate();

   return 0;
}

