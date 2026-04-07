import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

kejelasanInformasi=ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasanInformasi')
kejelasanPersyaratan=ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasanPersyaratan')
kemampuanPetugas=ctrl.Antecedent(np.arange(0, 101, 1), 'kemampuanPetugas')
ketersediaanSarpras=ctrl.Antecedent(np.arange(0, 101, 1), 'ketersediaanSarpras')
kepuasanPelayanan=ctrl.Consequent(np.arange(0, 401, 1), 'kepuasanPelayanan')

kejelasanInformasi['tidak memuaskan']=fuzz.trapmf(kejelasanInformasi.universe, [0,0,60,75])
kejelasanInformasi['cukup memuaskan']=fuzz.trimf(kejelasanInformasi.universe, [60,75,90])
kejelasanInformasi['memuaskan']=fuzz.trapmf(kejelasanInformasi.universe, [75,90,100,100])

kejelasanPersyaratan['tidak memuaskan']=fuzz.trapmf(kejelasanPersyaratan.universe, [0,0,60,75])
kejelasanPersyaratan['cukup memuaskan']=fuzz.trimf(kejelasanPersyaratan.universe, [60,75,90])
kejelasanPersyaratan['memuaskan']=fuzz.trapmf(kejelasanPersyaratan.universe, [75,90,100,100])

kemampuanPetugas['tidak memuaskan']=fuzz.trapmf(kemampuanPetugas.universe, [0,0,60,75])
kemampuanPetugas['cukup memuaskan']=fuzz.trimf(kemampuanPetugas.universe, [60,75,90])
kemampuanPetugas['memuaskan']=fuzz.trapmf(kemampuanPetugas.universe, [75,90,100,100])

ketersediaanSarpras['tidak memuaskan']=fuzz.trapmf(ketersediaanSarpras.universe, [0,0,60,75])
ketersediaanSarpras['cukup memuaskan']=fuzz.trimf(ketersediaanSarpras.universe, [60,75,90])
ketersediaanSarpras['memuaskan']=fuzz.trapmf(ketersediaanSarpras.universe, [75,90,100,100])

kepuasanPelayanan['tidak memuaskan']=fuzz.trapmf(kepuasanPelayanan.universe, [0,0,50,75])
kepuasanPelayanan['kurang memuaskan']=fuzz.trapmf(kepuasanPelayanan.universe, [50,75,100,150])
kepuasanPelayanan['cukup memuaskan']=fuzz.trapmf(kepuasanPelayanan.universe, [100,150,250,275])
kepuasanPelayanan['memuaskan']=fuzz.trapmf(kepuasanPelayanan.universe, [250,275,325,350])
kepuasanPelayanan['sangat memuaskan']=fuzz.trapmf(kepuasanPelayanan.universe, [325,350,400,400])

# kejelasanInformasi.view()
# kejelasanPersyaratan.view()
# kemampuanPetugas.view()
# ketersediaanSarpras.view()
# kepuasanPelayanan.view()
# input("tekan enter untuk melanjutkan")

aturan1  = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['kurang memuaskan'])
aturan2  = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan3  = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['cukup memuaskan'])
aturan4  = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan5  = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan6  = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['cukup memuaskan'])
aturan7  = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan8  = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan9  = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['memuaskan'])
aturan10 = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan11 = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan12 = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['cukup memuaskan'])
aturan13 = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan14 = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan15 = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['memuaskan'])
aturan16 = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan17 = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['memuaskan'])
aturan18 = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['memuaskan'])
aturan19 = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan20 = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan21 = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['memuaskan'])
aturan22 = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan23 = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['memuaskan'])
aturan24 = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['memuaskan'])
aturan25 = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['memuaskan'])
aturan26 = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['memuaskan'])
aturan27 = ctrl.Rule(kejelasanInformasi['tidak memuaskan'] & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['sangat memuaskan'])
aturan28 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan29 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan30 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['cukup memuaskan'])
aturan31 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan32 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan33 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['memuaskan'])
aturan34 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan35 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['memuaskan'])
aturan36 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['memuaskan'])
aturan37 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan38 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan39 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['memuaskan'])
aturan40 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan41 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['memuaskan'])
aturan42 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['memuaskan'])
aturan43 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['memuaskan'])
aturan44 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['memuaskan'])
aturan45 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['sangat memuaskan'])
aturan46 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan47 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['memuaskan'])
aturan48 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['memuaskan'])
aturan49 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['memuaskan'])
aturan50 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['memuaskan'])
aturan51 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['sangat memuaskan'])
aturan52 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['memuaskan'])
aturan53 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['sangat memuaskan'])
aturan54 = ctrl.Rule(kejelasanInformasi['cukup memuaskan'] & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['sangat memuaskan'])
aturan55 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan56 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan57 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['memuaskan'])
aturan58 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan59 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['memuaskan'])
aturan60 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['memuaskan'])
aturan61 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['memuaskan'])
aturan62 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['memuaskan'])
aturan63 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['tidak memuaskan'] & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['sangat memuaskan'])
aturan64 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['cukup memuaskan'])
aturan65 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['memuaskan'])
aturan66 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['memuaskan'])
aturan67 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['memuaskan'])
aturan68 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['memuaskan'])
aturan69 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['sangat memuaskan'])
aturan70 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['memuaskan'])
aturan71 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['sangat memuaskan'])
aturan72 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['cukup memuaskan'] & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['sangat memuaskan'])
aturan73 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['memuaskan'])
aturan74 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['memuaskan'])
aturan75 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['tidak memuaskan'] & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['sangat memuaskan'])
aturan76 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['memuaskan'])
aturan77 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['sangat memuaskan'])
aturan78 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['cukup memuaskan'] & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['sangat memuaskan'])
aturan79 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['tidak memuaskan'], kepuasanPelayanan['sangat memuaskan'])
aturan80 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['cukup memuaskan'], kepuasanPelayanan['sangat memuaskan'])
aturan81 = ctrl.Rule(kejelasanInformasi['memuaskan']  & kejelasanPersyaratan['memuaskan']  & kemampuanPetugas['memuaskan']  & ketersediaanSarpras['memuaskan'],  kepuasanPelayanan['sangat memuaskan'])

engine = ctrl.ControlSystem([
    aturan1,  aturan2,  aturan3,  aturan4,  aturan5,  aturan6,  aturan7,  aturan8,  aturan9,
    aturan10, aturan11, aturan12, aturan13, aturan14, aturan15, aturan16, aturan17, aturan18,
    aturan19, aturan20, aturan21, aturan22, aturan23, aturan24, aturan25, aturan26, aturan27,
    aturan28, aturan29, aturan30, aturan31, aturan32, aturan33, aturan34, aturan35, aturan36,
    aturan37, aturan38, aturan39, aturan40, aturan41, aturan42, aturan43, aturan44, aturan45,
    aturan46, aturan47, aturan48, aturan49, aturan50, aturan51, aturan52, aturan53, aturan54,
    aturan55, aturan56, aturan57, aturan58, aturan59, aturan60, aturan61, aturan62, aturan63,
    aturan64, aturan65, aturan66, aturan67, aturan68, aturan69, aturan70, aturan71, aturan72,
    aturan73, aturan74, aturan75, aturan76, aturan77, aturan78, aturan79, aturan80, aturan81
])
sistem=ctrl.ControlSystemSimulation(engine)

sistem.input['kejelasanInformasi'] = 80
sistem.input['kejelasanPersyaratan'] = 60
sistem.input['kemampuanPetugas'] = 50
sistem.input['ketersediaanSarpras'] = 90
sistem.compute()

print(sistem.output['kepuasanPelayanan'])
kepuasanPelayanan.view(sim=sistem)
input("Tekan ENTER untuk melanjutkan")