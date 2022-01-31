/*
 * If using the same arduino that the box was made with: you need to use the "old bootloader" option when uploading code
 * POT should output 1023-0
 * Dividing by 4 gives 255-0, which is the correct range for PWM outputs  
 * ^^^That is the theoretical range. On testing, the current code lines function correctly^^^
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
  vic.attach(MTR_OUT);
  //All serial lines are debug-specific
  Serial.begin(115200);

}

void loop() {
  //Recieve value 0-1023
  val = analogRead(POT_IN);
  //Change the 0-1023 range into a 40-145 range
  //Don't ask me why 40-145, that's the range that works
  val = map(val, 0, 1023, 40, 145);
  //Create a deadband so the zero doesn't need to be perfetly balanced
  if(86 < val && val < 99) {val = 92;}
  Serial.println(val);
  vic.write(val);
}

/*    WIRING FOR ENCLOSED, CAN-LESS BOX, USED FOR CIM AND NEO
 * The ground of the victor should connect directly to:
 *  The victor PWM
 *  The power switch
 *  The POT
 * 
 * Victor power   ->   +   on the switch
 * PWM Signal     ->   D11 on the Arduino
 * Switch ground  ->   GND on the Arduino
 * Switch signal  ->   VIN on the Arduino
 * Pot Power      ->   5V  on the Arduino
 * Pot Signal     ->   A0  on the Arduino
 */
 
// Code is the same for both boxes, but wiring changes
 
 /*    WIRING FOR CAN-COMPATIBLE BOX, USED FOR FALCON
 * The ground WAGO terminal should contain:
 *  Battery GND
 *  Switch GND
 *  Potentiometer GND
 *  Arduino GND
 *  Output GND
 *  
 *  The power WAGO terminal should contain:
 *  Battery 12v
 *  Switch +
 *  Output 12v
 * 
 * Switch signal  ->   VIN on the Arduino
 * CAN Yellow     ->   D11 on the Arduino
 * CAN Green      ->   GND on the Arduino
 * Pot Power      ->   5V  on the Arduino
 * Pot Signal     ->   A0  on the Arduino
 */
