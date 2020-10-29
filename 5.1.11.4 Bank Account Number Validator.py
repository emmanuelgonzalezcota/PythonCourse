# IBAN Validator

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')
if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    print('iban  =',iban) #EMGC
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    print('iban2 =',iban2) #EMGC
    ibann = int(iban2)
    print('ibann =',ibann) #EMGC
    if ibann % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")