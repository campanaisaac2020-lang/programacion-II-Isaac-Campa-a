class RadarDragon:
  region1: int
  region2: int  
  def __init__(self, region1: int, region2: int):
      self.region1 = region1
      self.region2 = region2
 
  def buscar_esferas(self):
      print("Cantidad de esferas:", self.region1 + self.region2)
      Total_esferas= self.region1 + self.region2
      esferas_faltantes = 7 - Total_esferas
      print("El numero de esferas encotradas es:", Total_esferas)
      print("Las esferas que faltan son:", esferas_faltantes)
      return Total_esferas, esferas_faltantes

radar_bulma = RadarDragon(3,2)

Total_esferas, esferas_faltantes = radar_bulma.buscar_esferas()

print("Radar de Bulma")
print(f"Esferas encontradas:{Total_esferas}")
print(f"Esferas que faltan:{esferas_faltantes}")



