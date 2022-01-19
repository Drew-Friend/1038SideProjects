/*
 * If using the same arduino that the box was made with: you need to use the "old bootloader" option when uploading code
 * POT should output 1023-0
 * Dividing by 4 gives 255-0, which is the correct range for PWM outputs  
 * See bottom for full wiring
*/
#include <Servo.h>
int POT_IN = A0;  //A0  pin, when looking at the board
int MTR_OUT = 11; //D11 pin, when looking at the board
Servo vic;
int val = 0;

void setup() {
  //Set Pot data line to input
  pinMode(POT_IN, INPUT);
  //Default the motor to neutral
  //analogWrite(MTR_OUT, val/4);
  //All serial lines are debug-specific
  vic.attach(MTR_OUT);
  Serial.begin(115200);

}

void loop() {
  //Recieve value 0-1023
  
  val = analogRead(POT_IN);
  val = map(val, 0, 1023, 40, 145);
  if(86 < val && val < 99) {val = 92;}
  Serial.println(val);
  vic.write(val);
  //val /= 4;
  //Send value 0-255
  //analogWrite(MTR_OUT, val);
}

/*
 * The ground of the victor should connect directly to:
 *  The victor PWM
 *  The power switch
 *  The POT
 * 
 * Victor power   ->   +   on the switch
 * PWM Signal     ->   D11 on the Arduino
 * Switch ground  ->   GND on the arduino
 * Switch signal  ->   VIN on the arduino
 * Pot Power      ->   5V  on the arduino
 * Pot Signal     ->   A0  on the Arduino
 */
