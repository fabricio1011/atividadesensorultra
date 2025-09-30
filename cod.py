from machine import Pin, time_pulse_us
import time

led_verde = Pin(26, Pin.OUT)
led_vermelho = Pin(27, Pin.OUT)
trig = Pin(33, Pin.OUT)
echo = Pin(32, Pin.IN)

def medir_distancia():
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()

    duracao = time_pulse_us(echo, 1, 30000)

    if duracao < 0:
        return None
    
    distancia = (duracao * 0.0343) / 2
    return distancia

while True:
    dist = medir_distancia()
    
    if dist is not None and dist < 20:
        led_verde.off()
        led_vermelho.on()
    else:
        led_vermelho.off()
        led_verde.on()
    
    time.sleep(0.2)