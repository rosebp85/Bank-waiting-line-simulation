import os
import pygame
import time


sounds_path = 'sounds_fixed'
pygame.mixer.init()



# تابع برای خواندن حالات مختلف اعداد : 

def play_number(number):

    if number < 20:
        play_sound(f'{number}.wav')

    elif 20 <= number < 100:
        tens = (number // 10) * 10
        ones = number % 10

        if ones == 0:
            play_sound(f'{tens}.wav')
        else:
            play_sound(f'{tens}_and.wav')
            play_sound(f'{ones}.wav')

    elif 100 <= number < 120:
        if number == 100:
            play_sound('100.wav')  # صد رو به تنهایی میگه
        if number > 100:
            play_sound('100_and.wav')  # صدو "رو اضافه میکنه"
            play_number(number % 100)

    elif number > 119:
        if number == 0:
            play_number((number // 100) * 100)
        else:
            number % 100 != 0
            play_sound('100_and.wav')
            play_number(number % 100)




# تابع برای پخش صدا :

def play_sound(filename):

    file_path = os.path.join(sounds_path, filename)
    
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)




# تابع برای پخش جمله کامل :

def play_sentence(customer, cabin):

    play_sound("customer.wav")
    play_number(customer)
    play_sound("to.wav")
    play_number(cabin)







#Sources : 

#def play_sound() :  use youtube and github
#https://youtu.be/lUMSK6LmXCQ?si=uOax9J_v8l5AjEAl

#creating a library in programm : use youtube
#https://youtu.be/5SGqHlQTxLA?si=8G8aJpdxjohbFQ5X

#and pygame Documentation 