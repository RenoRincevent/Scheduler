#define TC_DIV TC_CLOCK2
	
void f1(){}
void f2(){}
void f3(){}
void f4(){}
	
int main(){
	TC0_CCR = TC_CLKDIS;
	TC0_CMR = TC_DIV | TC_CPCTRG;
	TC0_RC = 10_MILLISECOND;
	TC0_CCR = TC_SWTRG | TC_CLKEN;

	while(1){
			f1();
			f2();
			f3();
			while(!(TC0_SR & TC_CPCS));
			f1();
			f3();
			f4();
			while(!(TC0_SR & TC_CPCS));
			f1();
			f2();
			f4();
			while(!(TC0_SR & TC_CPCS));
			f1();
			f4();
			while(!(TC0_SR & TC_CPCS));
			f1();
			f2();
			while(!(TC0_SR & TC_CPCS));
			f1();
			f3();
			while(!(TC0_SR & TC_CPCS));
			f1();
			f2();
			f3();
			while(!(TC0_SR & TC_CPCS));
			f1();
			while(!(TC0_SR & TC_CPCS));
			f1();
			f2();
			while(!(TC0_SR & TC_CPCS));
			f1();
	}
}