#include <iostream>
#include <iomanip>
#include <mpi.h>
#include <random>
#include <cmath>
#define MASTER 0
#define SEED 35791246

using namespace std;

int main(int argc, char **argv)
{
    int nprocs, rank, num, val;
	double x, y, pi=0, stime, etime,npoints, circle_count=0,partial_Ccount = 0;

    // MPI Init and rank
    // Your code
    MPI_Init(&argc, &argv);
	// get number of process
	MPI_Comm_size(MPI_COMM_WORLD, &nprocs);
	// get the rank = this process's number (ranges from 0 to nprocs - 1)
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	// MPI status
	MPI_Status status; 
	
    if (rank == MASTER)
        stime = MPI_Wtime(); // start time
	
	// Get number of points
	npoints = 10000000;
	if (argc >= 2)
		npoints = atoi(argv[1]);

	// Calculate number of points for each rank
	// You should consider npoints is not divided nprocs
		
	// Random numbers and count the points of inside of the circle	
	srand(SEED+rank);   // Give rand() a seed value
	
	// I equaly devide the work to master and worker, in this assignment we will not have remainder
	
	if (rank == MASTER) // I am MASTER
    {
		// Your code
		int portion = (npoints/ nprocs);
        for(int i=1; i <= portion; i++){
            x = (double) rand()/RAND_MAX;
            y = (double) rand()/RAND_MAX;
            if (sqrt(pow(x,2)+pow(y,2))<=1)
                partial_Ccount +=1;
		}
		// add partial_Ccount from master
		circle_count += partial_Ccount;

		// add partial_Ccount from worker	
		for (int src_rank =1; src_rank<nprocs; src_rank++){
        	MPI_Recv(&partial_Ccount, 1, MPI_INT, src_rank, MPI_ANY_TAG ,MPI_COMM_WORLD, &status);
        	circle_count += partial_Ccount;
        }
		
		pi = (double) 4.0*(circle_count/npoints);
			
		etime = MPI_Wtime(); // end time
		cout << "  " << setw(10) << "npoints"
             << "  " << setw(10) << "pi"
             << "  " << setw(10) << "nprocs"
             << "  " << setw(30) << "elapsed wall-clock time" << "\n";
        cout << "  " << setw(10) << npoints
             << "  " << setw(10) << pi
             << "  " << setw(10) << nprocs
             << "  " << setw(30) << etime-stime << "\n"; 
	}
	else  // I am WORKER
	{
        // Your code
		int portion = (npoints/ nprocs);
		for(int i=1; i <= portion; i++){
        	x = (double) rand()/RAND_MAX;
        	y = (double) rand()/RAND_MAX;
        	if (sqrt(pow(x,2)+pow(y,2))<=1)
            	partial_Ccount +=1;

    	};
		MPI_Send(&partial_Ccount, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);	
    }

	// MPI finalize
	MPI_Finalize();
	return 0;
}	
