import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

barangTerjual=ctrl.Antecedent(np.arange(0, 101, 1), 'barangTerjual')
permintaan=ctrl.Antecedent(np.arange(0, 301, 1), 'permintaan')
hargaPerItem=ctrl.Antecedent(np.arange(0, 100001, 1), 'hargaPerItem')
profit=ctrl.Antecedent(np.arange(0, 4000001, 1), 'profit')
stokMakanan=ctrl.Consequent(np.arange(0, 1001, 1), 'stokMakanan')

barangTerjual['rendah']=fuzz.trimf(barangTerjual.universe, [0,0,40])
barangTerjual['sedang']=fuzz.trimf(barangTerjual.universe, [30,50,70])
barangTerjual['tinggi']=fuzz.trimf(barangTerjual.universe, [60,100,100])

permintaan['rendah']=fuzz.trimf(permintaan.universe, [0,0,100])
permintaan['sedang']=fuzz.trimf(permintaan.universe, [50,150,250])
permintaan['tinggi']=fuzz.trimf(permintaan.universe, [200,300,300])

hargaPerItem['murah']=fuzz.trimf(hargaPerItem.universe, [0,0,40000])
hargaPerItem['sedang']=fuzz.trimf(hargaPerItem.universe, [30000,50000,80000])
hargaPerItem['mahal']=fuzz.trimf(hargaPerItem.universe, [60000,100000,100000])

profit['rendah']=fuzz.trimf(profit.universe,  [0,0,1000000])
profit['sedang']=fuzz.trimf(profit.universe,  [1000000,2000000,2500000])
profit['banyak']=fuzz.trapmf(profit.universe, [1500000,2500000,4000000,4000000])

stokMakanan['sedang']=fuzz.trimf(stokMakanan.universe, [100,500,900])
stokMakanan['banyak']=fuzz.trimf(stokMakanan.universe, [600,1000,1000])

# barangTerjual.view()
# permintaan.view()
# hargaPerItem.view()
# profit.view()
# stokMakanan.view()
# input("tekan enter untuk melanjutkan")

aturan1 = ctrl.Rule(barangTerjual['tinggi'] & permintaan['tinggi'] & hargaPerItem['murah'] & profit['banyak'], stokMakanan['banyak'])
aturan2 = ctrl.Rule(barangTerjual['tinggi'] & permintaan['tinggi'] & hargaPerItem['murah'] & profit['sedang'], stokMakanan['sedang'])
aturan3 = ctrl.Rule(barangTerjual['tinggi'] & permintaan['sedang'] & hargaPerItem['murah'] & profit['sedang'], stokMakanan['sedang'])
aturan4 = ctrl.Rule(barangTerjual['sedang'] & permintaan['tinggi'] & hargaPerItem['murah'] & profit['sedang'], stokMakanan['sedang'])
aturan5 = ctrl.Rule(barangTerjual['sedang'] & permintaan['tinggi'] & hargaPerItem['murah'] & profit['banyak'], stokMakanan['banyak'])
aturan6 = ctrl.Rule(barangTerjual['rendah'] & permintaan['rendah'] & hargaPerItem['sedang'] & profit['sedang'], stokMakanan['sedang'])

engine=ctrl.ControlSystem([aturan1,aturan2,aturan3,aturan4,aturan5,aturan6])
sistem=ctrl.ControlSystemSimulation(engine)

sistem.input['barangTerjual'] = 80
sistem.input['permintaan'] = 255
sistem.input['hargaPerItem'] = 25000
sistem.input['profit'] = 3500000
sistem.compute()

print(sistem.output['stokMakanan'])
stokMakanan.view(sim=sistem)
input("Tekan ENTER untuk melanjutkan")