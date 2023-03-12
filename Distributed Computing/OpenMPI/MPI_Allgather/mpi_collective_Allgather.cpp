#include <iostream>
#include <cstdlib>
#include <ctime>
#include "mpi.h"

using namespace std;

int main(int argc, char **argv){
    int data_array[8] = {};
    int recv_buffer[8] = {};
    int nprocs, rank;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &nprocs);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	

	// assign data_array
	for (int i = 0; i<2; i++){
	data_array[i] = 100+i+rank*2;
	}


	int send_count = 2;
	int recv_count = 2;

	cout<< "Before Gather, data_array = ";
	for (int j=0; j<8;j++){cout<< data_array[j]<< " ";}
	cout<< " in rank = " << rank << endl;
	cout<< "Before Gather, recv_buffer = ";
	for (int j=0; j<8;j++){cout<< recv_buffer[j]<< " ";}
	cout<< " in rank = " << rank <<endl;

	MPI_Allgather(&data_array, send_count, MPI_INT, &recv_buffer, recv_count, MPI_INT, MPI_COMM_WORLD);
	
	cout<< "After Gather, data_array = ";
    for (int j=0; j<8;j++){cout<< data_array[j]<< " ";}
    cout<< " in rank = " << rank << endl;
    cout<< "After Gather, recv_buffer = ";
    for (int j=0; j<8;j++){cout<< recv_buffer[j]<< " ";}
    cout<< " in rank = " << rank <<endl;


	// get avg
	//if (rank==0){i
	float avg = 0;
	float sum = 0;
	for (int i=0; i<8; i++){sum += recv_buffer[i];}
	avg = sum/8;
	cout<< "Avg = "<< avg <<endl;

	MPI_Finalize();
	return 0;
	//}
}
