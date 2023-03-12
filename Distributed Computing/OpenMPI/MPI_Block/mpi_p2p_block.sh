#!/bin/bash
#SBATCH --job-name=mpi_p2p_block_job #Job name
#SBATCH --ntasks=4 #Job CPU request
#SBATCH --mem=1gb #Job memory request
#SBATCH --time=00:01:00 #Time limit hr:min:sec
#SBATCH --output=mpi_p2p_block_job_%j.log
#Standard output/error log
module load openmpi/4.0.5-gcc-11.1.0
mpiexec -np 4 /home/ethan.kao/CSCI-4620/mpi/mpi_p2p_block
