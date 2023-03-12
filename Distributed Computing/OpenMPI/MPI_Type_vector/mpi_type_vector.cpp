# include <iostream>
# include <mpi.h>
# define MASTER 0 
# define WORKER 1

using namespace std;

int main (int argc, char **argv){
	int nprocs, rank;

	// Initialize for MPI
	MPI_Init(&argc, &argv);
	MPI_Comm_size(MPI_COMM_WORLD, &nprocs);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);

	// Master send value to workers
	if (rank == MASTER){
	
	// Create datatype
	MPI_Datatype column_type;
	MPI_Type_vector(3,1,3,MPI_INT,&column_type);
	MPI_Type_commit(&column_type);

	// Send the message
	int buffer[3][3] = {0,1,2,3,4,5,6,7,8};
	MPI_Request request;
	cout << "MPI process " << rank << " sends values "
		 << buffer[0][1] << " , " << buffer[1][1]
		 << ", and  " << buffer[2][1] << endl;
	MPI_Send(&buffer[0][1], 1, column_type, WORKER, 0, MPI_COMM_WORLD);
	}

	// Workers receive the message
	if (rank == WORKER){
	int received[3];
	MPI_Recv(&received, 3, MPI_INT, MASTER, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
	cout << "MPI process " << rank << " received values "
		 << received[0] << " , " << received[1]
         << ", and  " << received[2] << endl;
	}
	
	MPI_Finalize();
	return 0;

}
