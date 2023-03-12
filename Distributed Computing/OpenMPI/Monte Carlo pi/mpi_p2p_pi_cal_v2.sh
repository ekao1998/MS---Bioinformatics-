#!/bin/bash
#SBATCH --job-name=mpi_p2p_pi_cal_v2_job #Job name
#SBATCH --ntasks=16 #Job CPU request
#SBATCH --mem=16gb #Job memory request
#SBATCH --time=00:30:00 #Time limit hr:min:sec
#SBATCH --output=mpi_p2p_pi_cal_v2_job_%j.log
#Standard output/error log

module load openmpi/4.0.5-gcc-11.1.0
#module load openmpi/mlnx/gcc/64/4.0.3rc4
mpiexec -np 1 /home/ethan.kao/CSCI-4620/assignment7/mpi_p2p_pi_cal_v2 10000000
mpiexec -np 2 /home/ethan.kao/CSCI-4620/assignment7/mpi_p2p_pi_cal_v2 10000000
mpiexec -np 4 /home/ethan.kao/CSCI-4620/assignment7/mpi_p2p_pi_cal_v2 10000000
mpiexec -np 8 /home/ethan.kao/CSCI-4620/assignment7/mpi_p2p_pi_cal_v2 10000000
mpiexec -np 16 /home/ethan.kao/CSCI-4620/assignment7/mpi_p2p_pi_cal_v2 10000000
