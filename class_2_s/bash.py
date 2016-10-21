import os
a = [0.95, 0.87, 0.93, 0.89, 0.88, 0.885, 0.881, 0.905, 0.903, 0.84, 0.85, 0.86, 0.82, 0.81, 0.8, 0.79, 0.78]
for v in range(5,21):
 with open('in.lj','r') as file:
  data = file.readlines()
 vreal = v/10.
 rhoreal = round(1./vreal,2)
 typein = "variable rho  equal " + str(rhoreal) + '\n'
 #print typein
 data[3] = typein
 with open('in.lj','w') as file:
  file.writelines(data)
 os.system('./../lammps/src/lmp_mpi < in.lj')
 commandname = 'mv log.lammps T3/' "rho" + str(rhoreal) + ".lammps"
 os.system(commandname)

for rho in a:
 with open('in.lj','r') as file:
  data = file.readlines()
 typein = "variable rho  equal " + str(rho) + '\n'
 data[3] = typein
 with open('in.lj','w') as file:
  file.writelines(data)
 os.system('./../lammps/src/lmp_mpi < in.lj')
 commandname = 'mv log.lammps T3/' "rho" + str(rho) + ".lammps"
 os.system(commandname)
