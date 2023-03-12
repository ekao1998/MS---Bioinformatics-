# include <iostream>
# include <mpi.h>
# include <cstdlib>

using namespace std;

int main (int argc, char **argv){
	int nprocs, rank;

	// Initialize for MPI
	MPI_Init(&argc, &argv);
	MPI_Comm_size(MPI_COMM_WORLD, &nprocs);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);

	// Split the communicator based on the color (global rank/4)
	int color = rank/4;
	MPI_Comm group_comm;
	MPI_Comm_split(MPI_COMM_WORLD, color, rank, &group_comm);
	
	// get the rank and size
	int group_rank, group_nprocs;
	MPI_Comm_rank(group_comm, &group_rank);
	MPI_Comm_size(group_comm, & group_nprocs);
	printf("World_Rank/World_Nprocs:  %d/%d \t Group_Rank/Group_Nprocs: %d/%d\n",
		rank, nprocs, group_rank, group_nprocs);

	// MPI Comm free
	MPI_Comm_free(&group_comm);

	
	MPI_Finalize();
	return 0;

}
