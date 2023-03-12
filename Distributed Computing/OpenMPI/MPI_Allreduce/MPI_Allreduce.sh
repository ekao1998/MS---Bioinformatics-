#!/bin/bash
#SBATCH --job-name=MPI_Allreduce_job #Job name
#SBATCH --ntasks=4 #Job CPU request
#SBATCH --mem=1gb #Job memory request
#SBATCH --time=00:01:00 #Time limit hr:min:sec
#SBATCH --output=MPI_Allreduce_job_%j.log
#Standard output/error log
module load openmpi/mlnx/gcc/64/4.0.3rc4
#module load openmpi/4.0.5-gcc-11.1.0
mpiexec -np 4 /home/ethan.kao/CSCI-4620/mpi/MPI_Allreduce
