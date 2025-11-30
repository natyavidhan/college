#include <stdio.h>
#include <pthread.h>

int nums[100], n, sum = 0;

void* calculate_sum(void* arg) {
    for (int i = 0; i < n; i++)
        sum += nums[i];
    return NULL;
}

int main() {
    pthread_t thread;
    
    printf("Enter n: ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%d", &nums[i]);

    pthread_create(&thread, NULL, calculate_sum, NULL);
    pthread_join(thread, NULL);
    
    printf("Sum = %d\n", sum);
    return 0;
}