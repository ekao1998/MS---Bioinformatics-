#include <iostream>
#include <cstdlib>
#include <ctime>
#include "mpi.h"

using namespace std;

int main(int argc, char **argv){
	int nprocs, rank;
	MPI_Init(&argc, &argv);
	MPI_Comm_size(MPI_COMM_WORLD, &nprocs);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	
	int data = 0;
	cout<<"Before Bcast, data = "<<data<< " in rank = " << rank <<endl;
	
	if (rank ==0){
	data = 100;
	
	}
	MPI_Bcast(&data, 1, MPI_INT, 0, MPI_COMM_WORLD);
	cout << "After Bcast, data = " << data << " in rank = "<< rank <<endl;

	MPI_Finalize();
	return 0;
}
