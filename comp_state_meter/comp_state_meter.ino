/*
 * 以下を参考にした(ほぼパクリ)
 * https://qiita.com/keitasumiya/items/25a707c37a73bfd95bac
 */

#define CPU_PIN 0
#define MEM_PIN 0
#define PAK_PIN 0

const int val_size = 3;
int values[val_size] = {0, 0, 0};
bool isValids[val_size] = {false, false, false};

void setup(){
  pinMode( CPU_PIN, OUTPUT);
  pinMode( MEM_PIN, OUTPUT);
  pinMode( PAK_PIN, OUTPUT);
  analogWrite( CPU_PIN, 0);
  analogWrite( MEM_PIN, 0);
  analogWrite( PAK_PIN, 0);
  Serial.begin(9600);
}

void loop(){

  analogWrite( CPU_PIN, values[0]);
  analogWrite( MEM_PIN, values[1]);
  analogWrite( PAK_PIN, values[2]);
  
  if (Serial.available() >= 3*val_size+1) {
    int head = Serial.read();
    if (head == 128){
      bool isValids[val_size] = {false, false, false};
    }
    for (int i=0; i<val_size; i++){
      if (head == 128+i) {
        int high = Serial.read();
        int low  = Serial.read();
        values[i] = (high<<7) + low;
        Serial.print("[");
        Serial.print(i, DEC);
        Serial.print("]");
        if (0 <= values[i] <= 1023) {
          Serial.print("[");
          Serial.print(values[i], DEC);
          if (head == 128+val_size-1) {
            Serial.println("]");
          }else{
            Serial.print("] ");
          }
          isValids[i] = true;
        }
      }
    }
  }
}
