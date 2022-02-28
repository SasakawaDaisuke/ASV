#include <Servo.h>

byte servoPin_right = 9;
// byte servoPin_left = ;

Servo servo_right;
Servo servo_left;


void setup() {
  
  Serial.begin(9600); // シリアル通信のデータ転送レートを指定

  servo_right.attach(servoPin_right);  // サーボ変数をピンに割り当てます
  servo_left.attach(servoPin_left);

  servo_right.writeMicroseconds(1500); // send "stop" signal to ESC.
  // delay(7000); // delay to allow the ESC to recognize the stopped signal
  // 同時に初期化してしまっていいのかわからない

  servo_left.writeMicroseconds(1500);  // サーボに対しマイクロ秒単位で角度を指定
  delay(7000); // delay to allow the ESC to recognize the stopped signal

}

void loop() {
  
  Serial.println("Enter PWM signal value 1100 to 1900, 1500 to stop");
  
  while (Serial.available() == 0); // 受信したデータが存在する場合
  
  int val_right val_left = Serial.parseInt(); 
  
  if(val < 1100 || val > 1900)
  {
    Serial.println("not valid");
  }
  else
  {
    servo_right.writeMicroseconds(val_right); // Send signal to ESC.
    servo_left.writeMicroseconds(val_left); // Send signal to ESC.
  }
}