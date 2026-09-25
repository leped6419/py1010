"""

Arbeidskrav 1
Beregning av årlig totalkostnad for elbil og bensinbil.
Lene Kristin Pedersen (lenekp@gmail.com) (leped6419@usn.no)
Oppdatert 2026.09.25

"""

km = 10000  # [Antall km pr år]
forsikring_elbil = 5000  # [Forsikring elbil pr år]
forsikring_bensinbil = 7500  # [Forsikring bensinbil pr år]
tfa = 8.38*365  # [Trafikkforsikringsavgift pr år]
drivstoff_elbil = 0.2 * km * 2.00  # [Pris drifstofforbruk elbil pr år]
drivstoff_bensinbil = km * 1.0  # [Pris drifstofforbruk bensinbil pr år]
bom_elbil = 0.1 * km  # [Pris bompenger elbil pr år]
bom_bensinbil = 0.3 * km  # [Pris bompenger bensinbil pr år]
total_elbil = forsikring_elbil + tfa + drivstoff_elbil + bom_elbil  # [Totalpris elbil pr år]
total_bensinbil = forsikring_bensinbil + tfa + drivstoff_bensinbil + bom_bensinbil  # [Totalpris bensinbil pr år]
diff = total_bensinbil - total_elbil  # [Differanse mellom elbil og bensinbil]

print ("Antall km pr år: ", km)
print ("Totalpris elbil =",total_elbil)
print ("Totalpris bensinbil =",total_bensinbil)
print ("Differanse mellom elbil og bensinbil =",diff)
 