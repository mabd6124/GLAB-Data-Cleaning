import re
# Cleaning function

def vehicle_cleaning_variantkey(df_vehicles):
    '''This function takes in a vehicle dataframe and cleans its variant, body, transmission, fuel, drive & engine size to create a variantkey '''
    
    ############################################### Cleaning vcVariants
    vcVariant_list = df_vehicles['vcVariant']
    clean_vcVariant_list = []

    for i in vcVariant_list:
    
        #Remove (...) from variant description
        clean_variant = (re.sub("[\(\[].*?[\)\]]", "", i)).strip()
    
         #Remove HYBRID from variant description
        if 'HYBRID' in clean_variant:
            clean_variant = clean_variant.replace('HYBRID', '')
    
        #Replace descriptions
        if 'SPORTS LUX' in clean_variant:
            test = clean_variant.split()
        
            if 'LUX' in test:
                clean_variant = clean_variant.replace('SPORTS LUX', 'SPORTS-LUXURY')
            else:
                clean_variant = clean_variant.replace('SPORTS LUXURY', 'SPORTS-LUXURY')
        if 'F SPORT' in clean_variant:
            clean_variant = clean_variant.replace('F SPORT', 'F-SPORT')
        if '+EP' in clean_variant:
            clean_variant = clean_variant.replace('+EP', 'EP')
        if '+ EP' in clean_variant:
            clean_variant = clean_variant.replace('+ EP', 'EP')
        if 'EDITION' in clean_variant:
            clean_variant = clean_variant.replace(' EDITION', '-EDITION')
        if 'TWO TONE' in clean_variant:
            clean_variant = clean_variant.replace('TWO TONE', 'TWO-TONE')
        if '+' in clean_variant:
            test = clean_variant.split()
            if '+' in test:
                clean_variant = clean_variant.replace('+', '')
            else:
                clean_variant = clean_variant.replace('+', ' ')
        if 'OPTION' in clean_variant:
            clean_variant = clean_variant.replace('OPTION', '')
   
    
        clean_vcVariant_list.append(clean_variant.strip())
    

    df_vehicles['clean_vcVariant'] = clean_vcVariant_list
    
    ######################################################### Clean vcTransmissionType
    clean_transmission_list = []

    for index, row in df_vehicles.iterrows():
        if (row['vcTransmissionType'].lower() == '6 sp automatic' or
           row['vcTransmissionType'].lower() == 'automatic' or 
           row['vcTransmissionType'].lower() == 'continuous variable' or
           row['vcTransmissionType'].lower() == '8 sp automatic' or 
           row['vcTransmissionType'].lower() == '4 sp automatic' or 
           row['vcTransmissionType'].lower() == '6 sp auto sequential' or 
           row['vcTransmissionType'].lower() == 'cvt auto 6 speed' or
           row['vcTransmissionType'].lower() == '8 sp auto sports d/shift' or
           row['vcTransmissionType'].lower() == 'cvt auto 6 sp sequential' or
           row['vcTransmissionType'].lower() == 'cvt auto 7 sp sequential' or 
           row['vcTransmissionType'].lower() == '10 sp auto seq sportshift' or 
           row['vcTransmissionType'].lower() == 'direct shift cvt' or
           row['vcTransmissionType'].lower() == 'electronic cvt' or
           row['vcTransmissionType'].lower() == '10 sp auto multi stage' or
           row['vcTransmissionType'].lower() == '6 sp electronic automatic' or
           row['vcTransmissionType'].lower() == 'multi stage hybrid trans' or 
           row['vcTransmissionType'].lower() == '5 sp automatic' or 
           row['vcTransmissionType'].lower() == '10 sp automatic' or 
           row['vcTransmissionType'].lower() == '8 sp auto spr d/shift seq' or
           row['vcTransmissionType'].lower() == '6 sp auto activematic' or
           row['vcTransmissionType'].lower() == '5 sp sequential auto' or
           row['vcTransmissionType'].lower() == 'cvt auto sequencial' or
           row['vcTransmissionType'].lower() == '4 sp auto multi stage' or
           row['vcTransmissionType'].lower() == '10 sp auto direct shift' or
           row['vcTransmissionType'].lower() == '10 speed sports auto' or
           row['vcTransmissionType'].lower() == 'cvt auto 8 sp sequential') :

                clean_transmission_list.append('AUTO')

        elif (row['vcTransmissionType'].lower() == '6 sp manual' or
              row['vcTransmissionType'].lower() == 'manual' or 
              row['vcTransmissionType'].lower() == '5 sp manual' or
              row['vcTransmissionType'].lower() == '6 sp manual + double o/d') :

                clean_transmission_list.append('MANUAL')

        else :
            clean_transmission_list.append('')

    df_vehicles['clean_vcTransmissionType'] = clean_transmission_list
    
    ################################################################ Clean vcFuelType
    clean_fuel_list = []

    for index, row in df_vehicles.iterrows():
        if (row['vcFuelType'].strip().lower() == 'unleaded petrol' or
            row['vcFuelType'].strip().lower() == 'premium unleaded petrol' or
            row['vcFuelType'].strip().lower() == 'unleaded' or
            row['vcFuelType'].strip().lower() == 'premium unleaded'):

            clean_fuel_list.append('PETROL')

        elif row['vcFuelType'].strip().lower() == 'diesel':

            clean_fuel_list.append('DIESEL')

        elif (row['vcFuelType'].strip().lower() == 'unleaded petrol/electric' or
              row['vcFuelType'].strip().lower() == 'premium unleaded/electric'):

            clean_fuel_list.append('HYBRID')

        elif row['vcFuelType'].strip().lower() == 'electric':

            clean_fuel_list.append('ELECTRIC')

        elif row['vcFuelType'].lower() == 'unknown':

            clean_fuel_list.append('UNKNOWN')

        else:
            clean_fuel_list.append('')

    df_vehicles['clean_vcFuelType'] = clean_fuel_list

    ############################################################ Clean vcBodyStyle
    clean_body_list = []

    for index, row in df_vehicles.iterrows():
        body = row['vcBodyStyle'].lower()

        if (('SEDAN'.lower() in body) or
           ('SALOON'.lower() in body)):
                clean_body_list.append('SEDAN')

        elif (('WAGON'.lower() in body) or 
             ('ESTATE'.lower() in body)):
                clean_body_list.append('WAGON')

        elif (('CABRIOLET'.lower() in body) or 
             ('CONVERTIBLE'.lower() in body) or 
             ('SOFTTOP'.lower() in body) or 
             ('HARDTOP'.lower() in body)):
                clean_body_list.append('CONVERTIBLE')

        elif (('HATCH'.lower() in body) or 
             ('BACK'.lower() in body)):
                clean_body_list.append('HATCH')

        elif (('COUPE'.lower() in body) or
             ('ROADSTER'.lower() in body)):
                clean_body_list.append('COUPE')

        elif (('DOUBLE C/CHAS'.lower() in body) or
             ('DUAL C/CHAS'.lower() in body) or 
             ('DUAL CAB'.lower() in body) or 
             ('CREW'.lower() in body) or 
             ('SUPER CAB'.lower() in body) or 
             ('DOUBLE CAB'.lower() in body) or 
             ('SPACE C/CHAS'.lower() in body)):
                clean_body_list.append('4D_UTILITY')

        elif (('C/CHAS'.lower() in body) or 
             ('UTILITY'.lower() in body) or
             ('CAB'.lower() in body) or
             ('P/UP'.lower() in body)):
                clean_body_list.append('UTILITY')

        elif (('BUS'.lower() in body) or 
             ('VAN'.lower() in body) or 
             ('TROOP'.lower() in body)):
                clean_body_list.append('PEOPLE_MOVER')
        else:
            clean_body_list.append('UNKNOWN')

    df_vehicles['clean_vcBodyStyle'] = clean_body_list
    
    ############################################################# Clean vcDriveType
    clean_drive_list = []

    for index, row in df_vehicles.iterrows():
        if (row['vcDriveType'].lower() == 'front wheel drive' or
            row['vcDriveType'].lower() == 'rear wheel drive' or
            row['vcDriveType'].lower() == '4x2'):

            clean_drive_list.append('2WD')

        elif (row['vcDriveType'].lower() == 'all wheel drive' or
              row['vcDriveType'].lower() == 'four wheel drive' or
              row['vcDriveType'].lower() == '4x4'):

              clean_drive_list.append('4WD')

        else:
              clean_drive_list.append('')

    df_vehicles['clean_vcDriveType'] = clean_drive_list
    
    ############################################################## Clean vcEngineSize
    clean_engine_list = []

    for index, row in df_vehicles.iterrows():

        engine = row['vcEngineSize'].replace("L", '').replace(" ", '')

        if engine.lower() == '':
            clean_engine_list.append('UNKNOWN')

        elif engine.lower() == '0': 
            clean_engine_list.append('0.0L')

        elif ('.' in engine.lower()):
            clean_engine_list.append(engine + 'L')

        elif ('.' not in engine.lower()):
            clean_engine_list.append(engine + '.0L')

        else:
            clean_engine_list.append('')

    df_vehicles['clean_vcEngineSize'] = clean_engine_list
    
    ########################################################### Create VARIANT KEY
    variant_list1 = []
    variant_list2 = []
    variantKey_list = []

    for index, row in df_vehicles.iterrows():
        vcVariant_array = row['clean_vcVariant'].split()
        variantKey = ''

        if row['clean_vcVariant'] != '':
            variant_list1.append(vcVariant_array[0])
            variant_list2.append('_'.join(vcVariant_array[1:]))

            variantKey = vcVariant_array[0] +' ' + '_'.join(vcVariant_array[1:]) + ' ' + row['clean_vcBodyStyle'] + ' ' + row['clean_vcTransmissionType'] + ' ' + row['clean_vcFuelType'] + ' ' + row['clean_vcDriveType']
            variantKey_list.append(variantKey)

        else :
            variant_list1.append('')
            variant_list2.append('') 
            #REMEMBER TO INCLUDE MODEL IF VARIANT IS EMPTY!!!!!!!!
            #variantKey = row['vcModel'] + ' ' + row['clean_vcBodyStyle'] + ' ' + row['clean_vcTransmissionType'] + ' ' + row['clean_vcFuelType'] + ' ' + row['clean_vcDriveType'] + ' ' + row['nvic_family']
            #variantKey_list.append(variantKey)

    df_vehicles['vcVariant_1'] = variant_list1
    df_vehicles['vcVariant_2'] = variant_list2
    #df_vehicles['variantKey'] = variantKey_list
    
    return df_vehicles

""" def node_assignment(df_vehicles):
    '''This function assigns the node under which each nvic falls ''' 
    '''Refer to pages 24-28 of the GFV model documentation when editing this code '''  

    'Create empty lists to represent node levels'
    node_1 = []
    node_2 = []
    node_3 = []
    node_4 = []
    node_5 = []
    node_6 = []
    node_7 = []

    'Loop through each row in the dataframe and assign node 1 (The vehicles make)'
    for index, row in df_vehicles.iterrows():
        node_1.append(row['vcMake'])
    df_vehicles['node_1'] = node_1

    'Assign node 2 (The vehicle class)'
    for index, row in df_vehicles.iterrows():
        if row['node_1' == 'TOYOTA']:
            if (row['vcModel'] == 'YARIS' or
                row['vcModel'] == 'PRIUS-C' or
                row['vcModel'] == 'COROLLA' or
                row['vcModel'] == 'RUKUS' or
                row['vcModel'] == 'PRIUS' or
                row['vcModel'] == 'CAMRY' or
                row['vcModel'] == 'AURION' or
                row['vcModel'] == '86'):

                node_2.append('CAR')

            elif (row['vcModel'] == 'RAV4' or
                row['vcModel'] == 'C-HR' or
                row['vcModel'] == 'KLUGER' or
                row['vcModel'] == 'FORTUNER' or  
                row['vcModel'] == 'PRIUS V' or
                (row['vcModel'] == 'LANDCRUISER' and 'PRADO' in row['vcVariant']) or
                (row['vcModel'] == 'LANDCRUISER' and 'LC200' in row['vcVariant']) or 
                row['vcModel'] == 'FJ CRUISER'):

                node_2.append('SUV')

            elif (row['vcModel'] == 'HILUX' or
                row['vcModel'] == 'TARAGO' or
                row['vcModel'] == 'HIACE'):

                node_2.append('LCV')

            else:
                node_2.append('UNKNOWN')
        else:
            node_2.append(row['UNKNOWN'])
    df_vehicles['node_2'] = node_2

    'Assign node 3 (the vehicle model group)'
    for index, row in df_vehicles.iterrows():
        if row['node_1' != 'TOYOTA']:
            node_3.append(row['vcModel'])
        else:
            if row['vcModel'] == 'YARIS' or row['vcModel'] == 'PRIUS-C':
                node_3.append('YARIS/PRIUS-C')
            elif row['vcModel'] == 'COROLLA' or row['vcModel'] == 'RUKUS':
                node_3.append('COROLLA/RUKUS')
            elif row['vcModel'] == 'CAMRY' or row['vcModel'] == 'AURION':
                node_3.append('CAMRY/AURION')
            elif row['vcModel'] == 'RAV4' or row['vcModel'] == 'C-HR':
                node_3.append('RAV4/C-HR')
            elif row['vcModel'] == 'KLUGER' or row['vcModel'] == 'FORTUNER' or row['vcModel'] == 'PRIUS V':
                node_3.append('KLUGER/FORTUNER/PRIUS V')
            elif row['vcModel'] == 'LANDCRUISER' and ('PRADO' in row['vcVariant']):
                node_3.append('PRADO')
            elif row['vcModel'] == 'FJ CRUISER' or (row['vcModel'] == 'LANDCRUISER' and ('LC200' in row['vcVariant'])):
                node_3.append('LC 200/ FJ CRUISER')
            elif row['vcModel'] == 'LANDCRUISER' and ('LC70' in row['vcVariant']):
                node3.append('LC 70')
            else:
                node3.append(row['vcModel'])
    df_vehicles['node_3'] = node_3

    'Assign node 4 (this node level differs across vehicles, for some it is variant group for others it is cylinders or even engine size)'
    for index, row in df_vehicles.iterrows():
        if (row['node_3'] == 'YARIS/PRIUS-C'):
            if 'ASCENT' in row['vcVariant']:
                node_4.append('ASCENT')
            else:
                node_4.append('OTHER')
        elif (row['node_3'] == 'COROLLA/RUKUS'):
            if 'ASCENT' in row['vcVariant']:
                node_4.append('ASCENT')
            elif 'RUKUS' in row['vcVariant']:
                node_4.append('RUKUS')
            else:
                node_4.append('OTHER')
        elif (row['node_3'] == 'PRIUS'):
            node_4.append(row['vcEngineSize'])
        elif (row['node_3'] == 'CAMRY'):
            node_4.append(row['cCylinders'])
        elif (row['node_3'] == '86' or row['node_3'] == 'BRZ' or row['node_3'] == 'MX-5'):
            row['node_3'] = '86'
            if (row['vcModel'] == '86'):
                node_4.append(row['86'])
            elif (row['vcModel'] == 'BRZ'):
                node_4.append(row['BRZ'])
            elif (row['vcModel'] == 'MX-5'):
                node_4.append(row['MX-5'])
            else: 
                node_4.append('UNKNOWN')
        elif (row['node_3'] == 'RAV4/C-HR'):
            node_4.append(row['cCylinders'])
        elif (row['node_3'] == 'KLUGER/FORTUNER/PRIUS V'):
            node_4.append(row['clean_vcDriveType'])
        elif (row['node_3'] == 'PRADO'):
            if ('Ldfjgfndkgjdfngkjdfngdkfgndkfgjndkgdngkdngdkjfgndkfjgndkfjgndfkjgdkdkfjgndfkjdfsfgsdgsdjgnsgsdg' in node_3):
                node_4.append(row['clean_vcDriveType'])
        elif (row['node_3'] == 'LC 200/ FJ CRUISER'):
            if ('LC200' in row[vcVariant]):
                node_4.append('LC 200xxcvxvmxcvckvjbsdvsdbsdbvsdjhvbsdjvbsdvjhbvsjdvbsdjvbhsdjvhsdbvjsdvbsjv')
            elif ('FJ CRUISER' in row['vcVariant']):
                node_4.append('FJ CRUISER')
            else:
                node_4.append('UNKNOWN')
        elif (row['node_3'] == 'HILUX'):
            node_4.append(row['cCylinders'])
        elif (row['node_3'] == 'TARAGO'):
            node_4.append(row['cCylinders'])
        elif (row['node_3'] == 'HIACE'):
            if ('VAN' in row['vcBodyStyle']):
                node_4.append('VAN')
            elif ('BUS' in row['vcBodyStyle']):
                node_4.append('BUS')
            else:
                node_4.append('UNKNOWN')
    df_vehicles['node_4'] = node_4
        
    'Assign node 5'    
    for index, row in df_vehicles.iterrows():
        if (row['node_3'] == 'YARIS/PRIUS-C'):
            if (row['node_4'] == 'OTHER'):
                if ('SX' in row['vcVariant']):
                    node_5.append('SX')
                elif('ZR' in row['vcVariant']):
                    node_5.append('ZR')
                else:
                    node_5.append('UNKNOWN')
            else:
                if (row['vcVariant'] == 'HYBRID'):
                    node_5.append('HYBRID')
                elif (row['vcVariant'] == 'i-TECH'):
                    node_5.append('i-TECH')
                else: 
                    node_5.append('ASCENT')
        elif (row['node_3'] == 'COROLLA/RUKUS'):
            node_5.append(row['clean_vcFuelType'])
        elif row['node_3'] == 'PRIUS':
            node_5.append('UNKNOWN')
        elif row['node_3'] == 'CAMRY':
            if (row['node_4'] == '4'):  
                node_5.append(row['clean_vcFuelType'])
            else:
                node_5.append(row['vcVariant'])
        elif row['node_3'] == '86':
            node_5.append('UNKNOWN')  
        elif row['node_3'] == 'RAV4/C-HR'):
            if (row['node_4'] == '4'):
                node_5.append(row['clean_vcFuelType'])
            else:
                node_5.append('UNKNOWN')
        elif row['node_3'] == 'KLUGER/FORTUNER/PRIUS V'):
            if (row['node_4' == '2WD']):
                if (('GRANDE' in row['vcVariant']) or ('i-TECH' in row['vcVariant'])):
                    node_5.append('GRANDE')
                elif (('GXL' in row['vcVariant']) or (row['vcVariant'] == 'HYBRID')):
                    node_5.append('GXL')
                else:
                    node_5.append('GX')
            else:
                if (row['vcVariant'] == 'GRANDE'):
                    node_5.append('GRANDE')
                elif (row['vcVariant'] == 'GXL'):
                    node_5.append('GXL')
                else:
                    node_5.append('GX')
        elif row['node_3'] == 'LC 200/FJ CRUISER'):
            if (row['node_4'] == 'LC 200'):
                node_5.append(row['clean_vcFuelType'])
            else:
                node_5.append('UNKNOWN')
        elif row['node_3'] == 'HILUX'):
            if (row['node_4'] == '4'):
                node_5.append(row['clean_vcFuelType'])
            else:
                node_5.append('UNKNOWN')

    return df_vehicles
 """
    

if __name__ == '__main__':
    pass
