#include<cstdlib>
#include<iostream>
#include<string>
#include<fstream>
#include<time.h>
#include<thread>
#include<chrono>

using namespace std;

int call_MC() 
{
time_t t = time(NULL);
char buf[30];
 string line, e, e1, e2;
string prev=" ";
bool flg=false; 

while(true) {
  sprintf(buf, "nuXmv -source commands.txt >output.txt"); //write the output in output.txt
  system(buf);

//---------Open the output file to get the counterexample in e
  ifstream cmdOutput("output.txt");

//Copy counterexample from line, if it exists
  while(getline(cmdOutput, line)) {
       if(line[0]==' ' && line[1]==' ' && line[2]=='-' && line[3]=='>' || flg) {
    	  flg=true;
	  if(e1.length()==0){
	    if(line[0]==' ' && line[1]==' ' & line[2]==' ' && line[3]==' ' && line[4]=='x') {
			for (int i=0; i<4; i++) {
			   line.erase(1,3); //remove 3 initial blank spaces
			   e1 = e1 + line + " &";
			   getline(cmdOutput, line);
			}
		}
	  }
	  else {
	  if(line[0]==' ' && line[1]==' ' & line[2]==' ' && line[3]==' ' && line[4]=='x') {
	  	for (int i=0; i<4; i++) {
	  	   line.erase(1,3); //remove 3 initial blank spaces
	  	   e2 = e2 + line + " &"; 
	  	   getline(cmdOutput, line);
	 	}
	 	break;
	    }
	  }
	 }
	}
  cmdOutput.close();

//Select the valid counterexample among e1 and e2, and store to e:
  if(e2.length()==0) e = e1;
  else e = e2;

  e1.clear();
  e2.clear(); //once counterexample is copied, empty the buffers


//----------If a counterexample exists, update it to network.smv
  if(e.back()=='&'){
	e.erase(e.end()-1); //to remove \n
	e.erase(e.end()-1); //to remove &

//If counterexample is new --> compare with previous counterexample
	if (e==prev)
		break;
	else {
	  prev.clear();
	  prev = e; //update prev
	  ifstream model("network.smv");
	  ofstream temp("temp.smv");

//Copies all lines to file except the ones starting with "e :="
	  while(getline(model, line)){
		if(line[0]!='e' || line[1]!=' ' || line[2]!=':' || line[3]!='=')
		   temp << line << endl;
		else {
		   line.erase(line.end()-1); //to remove \n
		   line.erase(line.end()-1); //to remove ;
		   line.erase(line.end()-1); //to remove ;
			cout << line << endl; 
		   e = line + " | " + e + ";  "; 
		   temp << e << endl;
		}
	  }
  
	model.close();
	temp.close();

	remove("network.smv");
	rename("temp.smv","network.smv");
	remove("output.txt");
	line.clear();
	e.clear();
	}
   }
  else
	break;

   }
t = time(NULL) - t;
cout << "Elapsed time in seconds : " << ((float)t) << " sec" << endl;
std::terminate();
}

int main() 
{
char buf[50];
   std::thread func_call(call_MC);
   std::this_thread::sleep_for(std::chrono::seconds(300)); //timeout:5min
   cout << "Timeout reached" << endl; 
   sprintf(buf, "kill $(ps | grep nuXmv | awk '{print $1}')");
   system(buf);
   std::this_thread::sleep_for(std::chrono::seconds(3)); //give system time to terminate buf
   cout << endl;
   std::terminate();

   return 0;
}

