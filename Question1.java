/*
Question 1:
Write a program that takes as input a sorted array of numbers. The objective is to return the array arranged in an
alternate order such that max value is followed by min value in a descending fashion, so that the 1st element is the
max value, 2nd element is the min value, 3rd element is the second max value, 4th element is the second min value &
so on.
Example: For an input array [2, 4, 6, 8, 10],
the expected result would be [10, 2, 8, 4, 6]

*/

// Time Complexity = O(n)
// Space Complexity = O(1)
// Test Cases [2, 4, 6, 8, 10] = [10, 2, 8, 4, 6],
// [1 2 5 7 9] = [9 1 7 2 5]

import java.util.Scanner;

public class Question1 {
	
	public static void rearrange(int arr[], int n) {
        // initialize index of first minimum and first maximum element
		int max_idx = n - 1, min_idx = 0;
		 
        // store maximum element of array
        int max_elem = arr[n - 1] + 1;
 
        // traverse array elements
        for(int i = 0; i < n; i++) {
            // at even index : we have to put
            // maximum element
        	// at odd index : we have to put minimum element
            if (i % 2 == 0) {
                arr[i] += (arr[max_idx] % max_elem) * max_elem;
                max_idx--;
            } else {
                arr[i] += (arr[min_idx] % max_elem) * max_elem;
                min_idx++;
            }
        }
 
        // array elements back to it's original form
        for (int i = 0; i < n; i++)
            arr[i] = arr[i] / max_elem;
    }

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number of test cases");
		int T = sc.nextInt();
		while(T != 0) {
			System.out.println("Enter the length of array");
			int n = sc.nextInt();
			int arr[] = new int[n];
			System.out.println("Enter the elements of the array");
			for(int i = 0; i < n; i++) {
				arr[i] = sc.nextInt();
			}
			System.out.println("Original Array");
			for (int i = 0; i < n; i++)
				System.out.print(arr[i] + " ");
			
			rearrange(arr, n);
			
			System.out.print("\nModified Array\n");
			for (int i = 0; i < n; i++)
				System.out.print(arr[i] + " ");
			T--;
		}
 

	}

}
