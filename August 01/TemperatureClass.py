#Conversion of Temperatures into other units......

class TemperatureConverter:
    global temp;
    global unit;
    unit = input('Enter unit of the temperature(K/C/F): ')
    temp = int(input('Enter temperature: '))
    
    def convertF_to_C():
        print('Converted Farenheit in Celsius is '+str((temp - 32)/1.80))
    def convertK_to_C():
        print('Converted Kelvin in Celsius is '+str(temp - 273))
    def convertC_to_F():
        print('Converted Celsius in Farenheit is '+str((9/5)*(temp) + 32))
    def convertK_to_F():
        print('Converted Kelvin in Farenheit is '+str((9/5)*(temp - 273) + 32))
    def convertC_to_K():
        print('Converted Celsius in Kelvin is '+str(temp + 273))
    def convertF_to_K():
        print('Converted Farenheit in Kelvin is '+str((5/9)*(temp - 32) + 273.15))

if unit =='K' or unit == 'k':
    TemperatureConverter.convertK_to_C()
    TemperatureConverter.convertK_to_F()
    
elif unit =='C' or unit == 'c':
    TemperatureConverter.convertC_to_F()
    TemperatureConverter.convertC_to_K()
        
elif unit =='F' or unit == 'f':
   TemperatureConverter.convertF_to_C()
   TemperatureConverter.convertF_to_K()
else:
    print('Enter Valid Unit')
  
