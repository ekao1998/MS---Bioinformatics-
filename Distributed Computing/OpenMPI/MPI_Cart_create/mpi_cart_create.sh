#!/bin/bash
#SBATCH --job-name=mpi_cart_create_job #Job name
#SBATCH --ntasks=4 #Job CPU request
#SBATCH --mem=1gb #Job memory request
#SBATCH --time=00:01:00 #Time limit hr:min:sec
#SBATCH --output=mpi_cart_create_job_%j.log

#Standard output/error log
module load openmpi/mlnx/gcc/64/4.0.3rc4
#module load openmpi/4.0.5-gcc-11.1.0
mpiexec -np 4 /home/ethan.kao/CSCI-4620/assignment10/mpi_cart_create
