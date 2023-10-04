#include<reg51.h>
sfr LCD= 0xA0; //P2 = LCD Data pins
sbit RS=P0^5; //Register Select(RS) pin of 16*2 lcd
sbit RW=P0^6; // Read?Write(RW) pin of 16*2 lcd
sbit EN=P0^7; //Enable(E) pin of 16*2 lcd
	
sfr ADC = 0x90; //P1 = ADC Data pins
sbit RD_ADC = P3^0; //Read(RD) pin of ADC0804
sbit WR_ADC = P3^1; //Write(WR) pin of ADC0804
sbit INTR=P3^2; //Interrupt(INTR) pin of ADC0804

void LCD_CMD(unsigned char x); //LCD command function
void LCD_DATA(unsigned char w); //LCD data function
void LCD_INI(void); //LCD initialised function
void Send_Data(unsigned char *Str);
void msDelay(unsigned int); //function for creating delay

void convert_display(unsigned char); //function for converting ADC value to temperature and display it on 16*2 lcd display
unsigned char i,value;

void main(void) // main function
{
  msDelay(20); //Delay
  LCD_INI(); //Call LCD Initialized Function
  Send_Data("TEMPERATURE"); //Data to Send
  
  INTR=1; //make INTR pin as input
  RD_ADC=1; //set RD pin HIGH
  WR_ADC=1; //set WR pin LOW
  
  while(1)  //repeat forever
  {
  
	WR_ADC=0; // send LOW to HIGH pulse on WR pin
	msDelay(1);
	WR_ADC=1;
	while(INTR==1); // wait for end of conversation
	RD_ADC=0; //make RD=0 to read data from ADC0804
	value=ADC; //copy of ADC data
	convert_display(value);
	msDelay(1000); //interval between every cycles
	RD_ADC=1; // make RD=1 for the next cycle
	}
	}
void convert_display(unsigned char value)
{
  unsigned char x1,x2,x3;
  
  LCD_CMD(0xc6); 
  
  x1=(value/10);
  x1=x1+(0x30);
  x2=value%10;
  x2=x2+(0x30);
  x3=0xDF;
  
  LCD_DATA(x1);
  LCD_DATA(x2);
  LCD_DATA(x3);
  LCD_DATA('C');
  }
  
 void LCD_CMD(unsigned char x)
  {
  LCD=x;
  RS=0;
  RW=0;
  EN=1;
  msDelay(1);
  EN=0;
  return;
  }
  
void LCD_DATA(unsigned char w)
  {
  LCD=w;
  RS=1;
  RW=0;
  EN=1;
  msDelay(1);
  EN=0;
  return;
  }
  
 void Send_Data(unsigned char *Str)
 {
  while(*Str)
  LCD_DATA(*Str++);
  }
  
void LCD_INI(void)
{
msDelay(100);
LCD_CMD(0x38);
LCD_CMD(0x0E);
LCD_CMD(0x01);
}
void msDelay(unsigned int Time)
{
unsigned int y,z;
for(y=0;y<Time;y++)
for(z=0;z<500;z++);
}
