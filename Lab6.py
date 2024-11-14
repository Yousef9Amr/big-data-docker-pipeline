# from mpi4py import MPI
# import numpy as np

# def main():
#     # Initialize MPI
#     comm = MPI.COMM_WORLD
#     world_size = comm.Get_size()  # Get the number of processes
#     my_rank = comm.Get_rank()     # Get the rank of the current process

#     # Set N
#     N = 100000

#     # Initialize array a and measure time
#     start_time = MPI.Wtime()
#     a = np.ones(N)  # Using numpy to initialize array a
#     end_time = MPI.Wtime()

#     # Print time only from process 0
#     if my_rank == 0:
#         print(f"Initialize a time: {end_time - start_time}")

#     # Initialize array b and measure time
#     start_time = MPI.Wtime()
#     b = np.array([1.0 + float(i) for i in range(N)])  # Initialize array b
#     end_time = MPI.Wtime()

#     # Print time only from process 0
#     if my_rank == 0:
#         print(f"Initialize b time: {end_time - start_time}")

#     # Add the two arrays and measure time
#     start_time = MPI.Wtime()
#     a = a + b  # Element-wise addition using numpy
#     end_time = MPI.Wtime()

#     # Print the time only from process 0
#     if my_rank == 0:
#         print(f"Add arrays time: {end_time - start_time}")

#     # Finalize MPI
#     MPI.Finalize()

# if __name__ == "__main__":
#     main()

from mpi4py import MPI
import numpy as np

def main():
     # Initialize MPI
     comm = MPI.COMM_WORLD
     world_rank = comm.Get_rank()  # Get the rank of the current process
    
     # Process-specific actions
    if world_rank == 0:
         number = 21
         number_array = np.array([number], dtype='i')  # Wrap number in a NumPy array
         comm.Send([number_array, MPI.INT], dest=1, tag=0)  # Send number from process 0 to process 1
    elif world_rank == 1:
         number_array = np.empty(1, dtype='i')  # Empty NumPy array to receive the number
         comm.Recv([number_array, MPI.INT], source=0, tag=0)  # Receive number in process 1 from process 0
         print(f"Process 1 received number {number_array[0]} from process 0")


 if __name__ == "__main__":
     main()