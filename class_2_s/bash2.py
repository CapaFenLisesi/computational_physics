import os
#a = [0.95, 0.87, 0.93, 0.89, 0.88, 0.885, 0.881, 0.905, 0.903]
a = [0.82, 0.81, 0.8, 0.79, 0.78]
for rho in a:
 with open('in.lj','r') as file:
  data = file.readlines()
 typein = "variable rho  equal " + str(rho) + '\n'
 data[3] = typein
 with open('in.lj','w') as file:
  file.writelines(data)
 os.system('./../lammps/src/lmp_mpi < in.lj')
 commandname = 'mv log.lammps T0.9/' "rho" + str(rho) + ".lammps"
 os.system(commandname)


