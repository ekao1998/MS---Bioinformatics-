#include <iostream>
#include <mpi.h>
#define MASTER 0

using namespace std;

int main(int argc, char **argv){
	int nprocs, rank;
	
	// initialize for mpi
	MPI_Init(&argc, &argv);
	// get number of process
	MPI_Comm_size(MPI_COMM_WORLD, &nprocs);
	// get the rank = this process's number (ranges from 0 to nprocs - 1)
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);

	// print a greeting
	cout << "Hello from process rank = " << rank << endl;
	
	int val = 0;
	// master send value to workers
	if (rank == MASTER) {
		cout<<"Process rank = " <<rank<< " had a value of "<<val<<endl;
		val = 100;
		cout<<"Process rank = " <<rank<< " has a value of "<<val<<endl;
		for (int dest_rank = 1; dest_rank<nprocs; dest_rank++){
		MPI_Send(&val, 1, MPI_INT, dest_rank, 0, MPI_COMM_WORLD);
		}
	}
	// workers get the message
	else{
		cout<<"Process rank = " <<rank<< " had a value of "<<val<<endl;
		MPI_Status status;
		MPI_Recv(&val, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, &status);
		cout<<"Process rank = " <<rank<< " has got a value of "<<val<<endl;
		val = val + rank;
		cout<<"Process rank = " <<rank<< " has updated the value of "<<val<<endl;
	}

	MPI_Finalize();
	return 0;
}
