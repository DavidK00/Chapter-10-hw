from re import L
import PatientClass as pa
import ProdecureClass as pr

#patient 1
patient_id = 1
name = 'Matt Jones'
address = '123 Main st, Waco TX 76706'
phone = '254-555-7415'
veteran_status = True

patient_1 = pa.patient(patient_id, name, address, phone, veteran_status)

#Procedure 1
name_1 = 'Physical Exam'
date_1 = '2/15/2022'
prac_1 = 'Dr. Irvine'
charge_1  = 250
patient_id_1 = 1

physical = pr.procedure(name_1, date_1, prac_1, charge_1, patient_id_1)

#Procedure 2
name_2 = 'MRI'
date_2 = '2/15/2022'
prac_2 = 'Dr. Hamilton'
charge_2 = 1500
patient_id_2 = 1

MRI = pr.procedure(name_2, date_2, prac_2, charge_2, patient_id_2)

#Procedure 3
name_3 = 'CT Scan'
date_3 = '2/17/2022'
prac_3 = 'Dr. Drey'
charge_3 = 1200
patient_id_3 = 2

ct_scan = pr.procedure(name_3, date_3, prac_3, charge_3, patient_id_3)


procedure_list = [physical, MRI, ct_scan]
patient_procedure_list = []

pat_id = input('Which patient ID would you like to bill? ')

for procedure in procedure_list:
    if procedure.get_id() == int(pat_id):
        patient_procedure_list.append(procedure)
        

def patient_billing(patient_obj, procedure_obj):
     total = 0 
     print('***Patient Bill***')
     print('Name:', patient_obj.get_name())
     print('Address:', patient_obj.get_address())
     print('Phone:', patient_obj.get_phone())
     print()
     for procedure in procedure_obj:
        print('Procedure:', procedure.get_name())
        print('Date', procedure.get_date())
        print('Practitioner:', procedure.get_prac())
        print('Charge: ' + "${:,.2f}".format(procedure.get_charge()))
        total += procedure.get_charge()
        print()

     if patient_obj.get_veteran_status() is True:
         discount = total *.4
         print('Total Charges: ' + "${:,.2f}".format(total - discount))
     else:
         print('Total Charges: ' + "${:,.2f}".format(total))

    




patient_billing(patient_1, patient_procedure_list)


