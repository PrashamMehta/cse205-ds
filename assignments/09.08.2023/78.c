void backtrack(int* nums, int numsSize, int start, int* subset, int subsetSize, int** subsets, int* count, int** returnColumnSizes) {
    subsets[*count] = (int*)malloc(subsetSize * sizeof(int));
    (*returnColumnSizes)[*count] = subsetSize;
    
    for (int i = 0; i < subsetSize; i++) {
        subsets[*count][i] = subset[i];
    }
    (*count)++;
    
    for (int i = start; i < numsSize; i++) {
        subset[subsetSize] = nums[i];
        backtrack(nums, numsSize, i + 1, subset, subsetSize + 1, subsets, count, returnColumnSizes);
    }
}

int** subsets(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    int maxSubsets = 1 << numsSize; // Total number of subsets (2^n)
    int** subsets = (int**)malloc(maxSubsets * sizeof(int*));
    *returnColumnSizes = (int*)malloc(maxSubsets * sizeof(int));
    *returnSize = 0;
    
    int* subset = (int*)malloc(numsSize * sizeof(int));
    int count = 0;
    
    backtrack(nums, numsSize, 0, subset, 0, subsets, &count, returnColumnSizes);
    
    *returnSize = count;
    return subsets;
}