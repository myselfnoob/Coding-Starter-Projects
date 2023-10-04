#include <reg51.h>
sbit rs=P1^0;
sbit rw=P1^1;
sbit e= P1^2;
void delay(unsigned int);
void cmd(unsigned char);
void dat(unsigned char);

void main(void)
{
	unsigned char ch[]="Display";
	unsigned char ch1[]="in LCD";
	unsigned int i,j,k;
	
	cmd(0x38);
	cmd(0x01);
	cmd(0x0c);
	cmd(0x83);
	cmd(0x06);
	
	
	for(i=0;ch[i]!='\0';i++)
	    dat(ch[i]);

		cmd(0xc3);
	for(j=0;ch1[j]!='\0';j++)
	{
		dat(ch1[j]);
 	 }
	 while(1){
	for(k=0;k<16;k++)
	{
	cmd(0x1c);
	}
	}
}
void delay(unsigned int t)
{
	unsigned int i,j;
	e=1;
	for(i=0;i<t;i++)
	for(j=0;j<1275;j++);
	e=0;
}

void cmd(unsigned char ch)
{
    
	rs=0;
	rw=0;
	 P2=ch;
	delay(20);
}
void dat(unsigned char ch)
{
	
	rs=1;
	rw=0;
	P2=ch;
	delay(20);
}
