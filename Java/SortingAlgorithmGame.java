import java.util.*;
import java.util.concurrent.CountDownLatch;

class SortingProgram {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Input array from the user
        System.out.print("Enter the number of elements in the array: ");
        int n = input.nextInt();
        int[] arr = new int[n];

        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; i++) {
            arr[i] = input.nextInt();
        }

        // Choose a sorting algorithm
        System.out.println("\nChoose a sorting algorithm (1-10):");
        System.out.println("1- Selection sort");
        System.out.println("2- Bubble sort");
        System.out.println("3- Insertion sort");
        System.out.println("4- Merge sort");
        System.out.println("5- Quick sort");
        System.out.println("6- Heap sort");
        System.out.println("7- Counting sort");
        System.out.println("8- Radix sort");
        System.out.println("9- Bucket Sort");
        System.out.println("10- Shell Sort");
        System.out.println("11- Cycle sort");
        System.out.println("12- Bogosort");
        System.out.println("13- Gnome sort");
        System.out.println("14- Strand sort");
        System.out.println("15- Bitonic sort");
        System.out.println("16- Pancake sorting");
        System.out.println("17- Sleep sort");
        System.out.println("18- Tree sort");
        System.out.println("19- Odd-Even sort");
        System.out.println("20- 3-way Merge sort");
        System.out.print("Enter your choice: ");
        int choice = input.nextInt();

        switch (choice) {
            case 1 -> selectionSort(arr);
            case 2 -> bubbleSort(arr);
            case 3 -> insertionSort(arr);
            case 4 -> mergeSort(arr);
            case 5 -> quickSort(arr, 0, n - 1);
            case 6 -> heapSort(arr);
            case 7 -> countingSort(arr);
            case 8 -> radixSort(arr);
            case 9 -> bucketSort(arr);
            case 10 -> shellSort(arr);
            case 11 -> cycleSort(arr);
            case 12 -> bogoSort(arr);
            case 13 -> gnomeSort(arr);
            case 14 -> strandSort(arr);
            case 15 -> bitonicSort(arr);
            case 16 -> pancakeSort(arr);
            case 17 -> sleepSort(arr);
            case 18 -> treeSort(arr);
            case 19 -> oddEvenSort(arr);
            case 20 -> threeWayMergeSort(arr);
            default -> System.out.println("Invalid choice. No sorting performed.");
        }

        // Print the sorted array
        System.out.println("Sorted array: " + Arrays.toString(arr));
    }

    // Selection Sort
    public static void selectionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            int temp = arr[minIndex];
            arr[minIndex] = arr[i];
            arr[i] = temp;
        }
    }

    // Bubble Sort
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        boolean swapped;
        for (int i = 0; i < n - 1; i++) {
            swapped = false;
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            if (!swapped) {
                break;
            }
        }
    }

    // Insertion Sort
    public static void insertionSort(int[] arr) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }

    // Merge Sort
    public static void mergeSort(int[] arr) {
        mergeSort(arr, 0, arr.length - 1);
    }

    private static void mergeSort(int[] arr, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;
            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }

    private static void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;
        int[] L = new int[n1];
        int[] R = new int[n2];

        System.arraycopy(arr, left, L, 0, n1);
        for (int i = 0; i < n2; i++) {
            R[i] = arr[mid + 1 + i];
        }

        int i = 0, j = 0, k = left;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    // Quick Sort
    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pivotIndex = partition(arr, low, high);
            quickSort(arr, low, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, high);
        }
    }

    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        return i + 1;
    }

    // Heap Sort
    public static void heapSort(int[] arr) {
        int n = arr.length;
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }
        for (int i = n - 1; i >= 0; i--) {
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;
            heapify(arr, i, 0);
        }
    }

    private static void heapify(int[] arr, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < n && arr[left] > arr[largest]) {
            largest = left;
        }
        if (right < n && arr[right] > arr[largest]) {
            largest = right;
        }

        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;
            heapify(arr, n, largest);
        }
    }

    // Counting Sort
    public static void countingSort(int[] arr) {
        int n = arr.length;
        int max = Arrays.stream(arr).max().getAsInt();
        int min = Arrays.stream(arr).min().getAsInt();
        int range = max - min + 1;
        int[] count = new int[range];
        int[] output = new int[n];

        for (int j : arr) {
            count[j - min]++;
        }

        for (int i = 1; i < range; i++) {
            count[i] += count[i - 1];
        }

        for (int i = n - 1; i >= 0; i--) {
            output[count[arr[i] - min] - 1] = arr[i];
            count[arr[i] - min]--;
        }

        System.arraycopy(output, 0, arr, 0, n);
    }

    // Radix Sort
    public static void radixSort(int[] arr) {
        int max = Arrays.stream(arr).max().getAsInt();
        for (int exp = 1; max / exp > 0; exp *= 10) {
            countingSortByDigit(arr, exp);
        }
    }

    private static void countingSortByDigit(int[] arr, int exp) {
        int n = arr.length;
        int[] output = new int[n];
        int[] count = new int[10];
        Arrays.fill(count, 0);

        for (int j : arr) {
            count[(j / exp) % 10]++;
        }

        for (int i = 1; i < 10; i++) {
            count[i] += count[i - 1];
        }

        for (int i = n - 1; i >= 0; i--) {
            output[count[(arr[i] / exp) % 10] - 1] = arr[i];
            count[(arr[i] / exp) % 10]--;
        }

        System.arraycopy(output, 0, arr, 0, n);
    }

    // Bucket Sort
    public static void bucketSort(int[] arr) {
        int n = arr.length;
        int max = Arrays.stream(arr).max().getAsInt();
        int min = Arrays.stream(arr).min().getAsInt();
        int range = max - min + 1;

        int bucketSize = Math.min(range / n, n);
        int bucketCount = (range + bucketSize - 1) / bucketSize;

        // Create buckets
        int[][] buckets = new int[bucketCount][];
        Arrays.fill(buckets, new int[0]);

        // Add elements to buckets
        for (int k : arr) {
            int index = (k - min) / bucketSize;
            buckets[index] = append(buckets[index], k);
        }

        // Sort individual buckets and merge
        int index = 0;
        for (int i = 0; i < bucketCount; i++) {
            insertionSort(buckets[i]);
            for (int j = 0; j < buckets[i].length; j++) {
                arr[index++] = buckets[i][j];
            }
        }
    }

    private static int[] append(int[] arr, int value) {
        int[] result = Arrays.copyOf(arr, arr.length + 1);
        result[arr.length] = value;
        return result;
    }

    // Shell Sort
    public static void shellSort(int[] arr) {
        int n = arr.length;
        for (int gap = n / 2; gap > 0; gap /= 2) {
            for (int i = gap; i < n; i++) {
                int temp = arr[i];
                int j;
                for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                    arr[j] = arr[j - gap];
                }
                arr[j] = temp;
            }
        }
    }

    // Cycle Sort
    public static void cycleSort(int[] arr) {
        int n = arr.length;
        for (int cycleStart = 0; cycleStart < n - 1; cycleStart++) {
            int item = arr[cycleStart];
            int pos = cycleStart;
            for (int i = cycleStart + 1; i < n; i++) {
                if (arr[i] < item) {
                    pos++;
                }
            }
            if (pos == cycleStart) {
                continue;
            }
            while (item == arr[pos]) {
                pos++;
            }
            int temp = arr[pos];
            arr[pos] = item;
            item = temp;
            while (pos != cycleStart) {
                pos = cycleStart;
                for (int i = cycleStart + 1; i < n; i++) {
                    if (arr[i] < item) {
                        pos++;
                    }
                }
                while (item == arr[pos]) {
                    pos++;
                }
                temp = arr[pos];
                arr[pos] = item;
                item = temp;
            }
        }
    }

    // Bogosort
    public static void bogoSort(int[] arr) {
        while (!isSorted(arr)) {
            shuffle(arr);
        }
    }

    private static boolean isSorted(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            if (arr[i - 1] > arr[i]) {
                return false;
            }
        }
        return true;
    }

    private static void shuffle(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            int j = (int) (Math.random() * arr.length);
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    // Gnome Sort
    public static void gnomeSort(int[] arr) {
        int n = arr.length;
        int index = 0;
        while (index < n) {
            if (index == 0) {
                index++;
            }
            if (arr[index] >= arr[index - 1]) {
                index++;
            } else {
                int temp = arr[index];
                arr[index] = arr[index - 1];
                arr[index - 1] = temp;
                index--;
            }
        }
    }

    // Strand Sort
    public static void strandSort(int[] arr) {
        List<Integer> sortedList = new ArrayList<>();
        List<Integer> sublist = new ArrayList<>();

        for (int num : arr) {
            sublist.add(num);
            if (sublist.size() > 1) {
                if (sublist.get(sublist.size() - 1) < sublist.get(sublist.size() - 2)) {
                    sortedList.addAll(strandSortInternal(sublist));
                    sublist.clear();
                }
            }
        }

        sortedList.addAll(strandSortInternal(sublist));

        for (int i = 0; i < sortedList.size(); i++) {
            arr[i] = sortedList.get(i);
        }
    }

    private static List<Integer> strandSortInternal(List<Integer> sublist) {
        if (sublist.size() <= 1) {
            return sublist;
        }

        List<Integer> sortedList = new ArrayList<>();
        List<Integer> result = new ArrayList<>();

        sortedList.add(sublist.get(0));
        sublist.remove(0);

        for (int num : sublist) {
            if (num >= sortedList.get(sortedList.size() - 1)) {
                sortedList.add(num);
            } else {
                result.add(num);
            }
        }

        result.addAll(strandSortInternal(result));
        result.addAll(sortedList);

        return result;
    }


    // Bitonic Sort
    public static void bitonicSort(int[] arr) {
        bitonicSortInternal(arr, 0, arr.length, true);
    }

    private static void bitonicSortInternal(int[] arr, int low, int count, boolean direction) {
        if (count > 1) {
            int k = count / 2;
            bitonicMerge(arr, low, k, direction);
            bitonicSortInternal(arr, low, k, true);
            bitonicSortInternal(arr, low + k, k, false);
        }
    }

    private static void bitonicMerge(int[] arr, int low, int count, boolean direction) {
        if (count > 1) {
            int k = count / 2;
            for (int i = low; i < low + k; i++) {
                if (direction == (arr[i] > arr[i + k])) {
                    int temp = arr[i];
                    arr[i] = arr[i + k];
                    arr[i + k] = temp;
                }
            }
            bitonicMerge(arr, low, k, direction);
            bitonicMerge(arr, low + k, k, direction);
        }
    }

    // Pancake Sorting
    public static void pancakeSort(int[] arr) {
        int n = arr.length;
        for (int currSize = n; currSize > 1; currSize--) {
            int maxIndex = findMaxIndex(arr, currSize);

            if (maxIndex != currSize - 1) {
                flip(arr, maxIndex);
                flip(arr, currSize - 1);
            }
        }
    }

    private static int findMaxIndex(int[] arr, int n) {
        int maxIndex = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] > arr[maxIndex]) {
                maxIndex = i;
            }
        }
        return maxIndex;
    }

    private static void flip(int[] arr, int i) {
        int start = 0;
        while (start < i) {
            int temp = arr[start];
            arr[start] = arr[i];
            arr[i] = temp;
            start++;
            i--;
        }
    }

    // Sleep Sort
    public static void sleepSort(int[] arr) {
        CountDownLatch doneSignal = new CountDownLatch(arr.length);

        for (int num : arr) {
            new Thread(() -> {
                try {
                    Thread.sleep(num * 100L); // Sleep for num * 100 milliseconds
                    System.out.print(num + " ");
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                } finally {
                    doneSignal.countDown();
                }
            }).start();
        }

        try {
            doneSignal.await();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    // Tree Sort
    public static void treeSort(int[] arr) {
        TreeNode root = null;
        for (int num : arr) {
            root = insert(root, num);
        }
        inOrderTraversal(root, arr);
    }

    static class TreeNode {
        int data;
        TreeNode left, right;

        TreeNode(int item) {
            data = item;
            left = right = null;
        }
    }

    private static TreeNode insert(TreeNode root, int key) {
        if (root == null) {
            root = new TreeNode(key);
            return root;
        }
        if (key < root.data) {
            root.left = insert(root.left, key);
        } else if (key > root.data) {
            root.right = insert(root.right, key);
        }
        return root;
    }

    private static void inOrderTraversal(TreeNode root, int[] arr) {
        int index = 0;
        if (root != null) {
            inOrderTraversal(root.left, arr);
            arr[index++] = root.data;
            inOrderTraversal(root.right, arr);
        }
    }

    // Odd-Even Sort
    public static void oddEvenSort(int[] arr) {
        int n = arr.length;
        boolean sorted = false;
        while (!sorted) {
            sorted = true;
            for (int i = 1; i <= n - 2; i += 2) {
                if (arr[i] > arr[i + 1]) {
                    int temp = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = temp;
                    sorted = false;
                }
            }
            for (int i = 0; i <= n - 2; i += 2) {
                if (arr[i] > arr[i + 1]) {
                    int temp = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = temp;
                    sorted = false;
                }
            }
        }
    }

    // 3-way Merge Sort
    public static void threeWayMergeSort(int[] arr) {
        if (arr.length > 1) {
            int mid1 = arr.length / 3;
            int mid2 = 2 * mid1;
            int[] left = Arrays.copyOfRange(arr, 0, mid1);
            int[] middle = Arrays.copyOfRange(arr, mid1, mid2);
            int[] right = Arrays.copyOfRange(arr, mid2, arr.length);

            threeWayMergeSort(left);
            threeWayMergeSort(middle);
            threeWayMergeSort(right);

            merge(arr, left, middle, right);
        }
    }

    private static void merge(int[] arr, int[] left, int[] middle, int[] right) {
        int i = 0, j = 0, k = 0;
        while (i < left.length && j < middle.length && k < right.length) {
            if (left[i] <= middle[j] && left[i] <= right[k]) {
                arr[i + j + k] = left[i++];
            } else if (middle[j] <= left[i] && middle[j] <= right[k]) {
                arr[i + j + k] = middle[j++];
            } else {
                arr[i + j + k] = right[k++];
            }
        }
        while (i < left.length) {
            arr[i + j + k] = left[i++];
        }
        while (j < middle.length) {
            arr[i + j + k] = middle[j++];
        }
        while (k < right.length) {
            arr[i + j + k] = right[k++];
        }
    }
}
