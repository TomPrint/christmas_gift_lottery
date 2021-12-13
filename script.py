import random
import pywhatkit as pywk

#your participants and telephone numbers here
tel_numbers = {"Tomek": "+48000000", "Kuba": "+48000000", "Iwona": "+48000000", "Malwina": "+48000000", "Gosia": "+48000000", "Staszek":"+48000000"}


#get_names function joins two lists and creates a dictionary through 'dict comprehension', excluding drawing oneself from the list, i.e Tomek : Tomek.
#while loop allows to return a dictionary of pairs, after loop returns six records (unique pairs)
def get_names():
    names1 = ["Tomek", 'Kuba', "Iwona", "Malwina", "Gosia", "Staszek"]
    names2 = ["Tomek", "Kuba", "Iwona", "Malwina", "Gosia", "Staszek"]
    while True:
        random.shuffle(names2)
        x = {key: value for key, value in zip(names1, names2) if key != value}
        if len(x) == len(names2):
            return x
f = get_names()
print (f) #to check the get_names result

#external pywhatkit sends a whatsupp message to the addressee using get_names result
#first f-string takes dict value and gets the number
#second f-string takes dict value from get_names result

def sending_whatsupp():
    # pywhatkit requires an open whatsupp window in browser
    # sendwhatmsg formatting #TO NUMBER, #BODY, #HOUR, #MINUTE
    
    pywk.sendwhatmsg(f'{tel_numbers["Tomek"]}', f' TEST PROGRAMU LOSOWANIA Na Świąteczny prezent wylosowano {(f["Tomek"])}',00,18)
    pywk.sendwhatmsg(f'{tel_numbers["Kuba"]}', f'TEST PROGRAMULOSOWANIA Na Świąteczny prezent wylosowano {(f["Kuba"])}', 00,19)
    pywk.sendwhatmsg(f'{tel_numbers["Iwona"]}', f'TEST PROGRAMU LOSOWANIA Na Świąteczny prezent wylosowano {(f["Iwona"])}', 00, 20)
    pywk.sendwhatmsg(f'{tel_numbers["Malwina"]}', f'TEST PROGRAMU LOSOWANIA Na Świąteczny prezent wylosowano {(f["Malwina"])}', 00, 21)
    pywk.sendwhatmsg(f'{tel_numbers["Gosia"]}', f'TEST PROGRAMU LOSOWANIA Na Świąteczny prezent wylosowano {(f["Gosia"])}', 00, 22)
    pywk.sendwhatmsg(f'{tel_numbers["Staszek"]}', f'TEST PROGRAMU LOSOWANIA Na Świąteczny prezent wylosowano {(f["Staszek"])}', 00, 23)

sending_whatsupp()
