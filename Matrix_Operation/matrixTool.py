import numpy as np
import sys

def get_matrix_input(name="A"):
    """
    Helper function to get a matrix from user input.
    """
    print(f"\n--- Enter Matrix {name} ---")
    try:
        rows = int(input(f"Enter number of rows for {name}: "))
        cols = int(input(f"Enter number of columns for {name}: "))
    except ValueError:
        print("❌ Invalid input. Please enter integers for dimensions.")
        return None

    matrix = []
    print(f"Enter {rows} rows (separate elements by space):")
    for i in range(rows):
        while True:
            try:
                # Read row, split by space, convert to float
                row_str = input(f"Row {i+1}: ")
                row = list(map(float, row_str.strip().split()))
                
                if len(row) != cols:
                    print(f"⚠️ Error: Row must have exactly {cols} elements. Try again.")
                    continue
                
                matrix.append(row)
                break
            except ValueError:
                print("⚠️ Error: Please enter valid numbers only.")

    return np.array(matrix)

def display_matrix(matrix, title="Result"):
    """
    Prints the matrix in a clean, structured format.
    """
    print(f"\n🔹 {title}:")
    # np.set_printoptions makes arrays look cleaner (suppresses scientific notation for small nums)
    with np.printoptions(precision=2, suppress=True):
        print(matrix)
    print("-" * 20)

def main():
    print("=" * 30)
    print(" Numpy Matrix Operations Tool ")
    print("=" * 30)

    while True:
        print("\nChoose an Operation:")
        print("1. Addition (A + B)")
        print("2. Subtraction (A - B)")
        print("3. Multiplication (A * B)")
        print("4. Transpose (Aᵀ)")
        print("5. Determinant |A|")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == '6':
            print("Exiting... Goodbye!")
            break

        # --- Operations requiring ONE matrix ---
        if choice in ['4', '5']:
            A = get_matrix_input("A")
            if A is None: continue

            if choice == '4':
                # Transpose Operation
                result = A.T
                display_matrix(result, "Transpose of A")

            elif choice == '5':
                # Determinant Operation
                if A.shape[0] != A.shape[1]:
                    print(" Error: Determinant can only be calculated for square matrices.")
                else:
                    det = np.linalg.det(A)
                    print(f"\n🔹 Determinant of A: {det:.2f}")

        # --- Operations requiring TWO matrices ---
        elif choice in ['1', '2', '3']:
            A = get_matrix_input("A")
            if A is None: continue
            
            B = get_matrix_input("B")
            if B is None: continue

            try:
                if choice == '1':
                    # Addition
                    if A.shape != B.shape:
                        print(f" Error: Shape mismatch. A is {A.shape}, B is {B.shape}.")
                    else:
                        display_matrix(np.add(A, B), "Sum (A + B)")

                elif choice == '2':
                    # Subtraction
                    if A.shape != B.shape:
                        print(f" Error: Shape mismatch. A is {A.shape}, B is {B.shape}.")
                    else:
                        display_matrix(np.subtract(A, B), "Difference (A - B)")

                elif choice == '3':
                    # Matrix Multiplication (Dot Product)
                    # Rule: Cols of A must equal Rows of B
                    if A.shape[1] != B.shape[0]:
                        print(f" Error: Cannot multiply {A.shape} with {B.shape}.")
                    else:
                        display_matrix(np.dot(A, B), "Product (A * B)")

            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        else:
            print(" Invalid choice. Please try again.")

if __name__ == "__main__":
    main()