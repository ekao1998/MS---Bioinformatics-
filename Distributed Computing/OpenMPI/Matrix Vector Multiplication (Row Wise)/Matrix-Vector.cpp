#include <iostream>
#include <cstdlib>     // has exit(), etc.
#include <ctime>
#include <mpi.h>
#define MASTER 0

using namespace std;

int main(int argc, char **argv)
{
	// Just simply set M(4) X N(4) matrix 
	// and X(N) vector and Y(M) vector
	int M=4, N=4;


	// Matrix and vector variables
	int A[M][N];  // A matrix (MxN) 
	int Apart[N]; // A row (N)
	int X[N];     // X vector has N size
	int Y[M];     // Y vector has M size
	int Ypart = 0; // Y vector element value 
	int nprocs, rank;  // nproc and rank


	// MPI init
	MPI_Init(&argc, &argv);
	MPI_Comm_size(MPI_COMM_WORLD, &nprocs);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);

	// Initialize matrix
	if (rank == MASTER) {
    for (int i = 0; i < M; i++) {
      for (int j = 0; j < N; j++) {
        A[i][j] = N*i + j+1;
      }
      Y[i] = 0;
    }
    for (int j = 0; j < N; j++) {
      X[j] = j + 1; 
      Apart[j] = 0;
    }
  }
	// MPI Scatter the A Matrix
	MPI_Scatter(A, N, MPI_INT, // send one row which contain N integers
				Apart, N, MPI_INT, // receive one row which contain N integers
				MASTER, MPI_COMM_WORLD 
				);
	
	//for(int i=0; i<N; i++){cout<< Apart[i]<< " ";}
	//cout<<" in rank "<< rank<<"\n";

	// Broadcast the X vector
	MPI_Bcast(X, M, MPI_INT, MASTER, MPI_COMM_WORLD);

	//for(int i=0; i<M; i++){cout<< X[i]<< " ";}
    //cout<<" in rank "<< rank<<"\n"; 
 
  	// Calculate each Ypart at each rank
 	for(int i=0; i<N; i++){
	Ypart += (X[i]*Apart[i]);
	};
 
	// MPI Gather all Ypart to Y
 	MPI_Gather(&Ypart, 1, MPI_INT, &Y, 1, MPI_INT, MASTER, MPI_COMM_WORLD);

	// Print results 
	
	if (rank == MASTER) {
    	for (int i = 0; i < M; i++) {
      		cout << "Y[" << i << "]=" << Y[i] << endl;
    } 
  }   

  MPI_Finalize();  // MPI finalize
  return 0;     // Exit 
}
	
