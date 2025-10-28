#include <stdio.h>
#include <pthread.h>

#define MAX 100

int arr[MAX];
int n, sum = 0;
pthread_mutex_t lock;

void* add(void* arg) {
    int i, part = *(int*)arg;
    int local_sum = 0;
    for (i = part; i < n; i += 2) local_sum += arr[i];
    pthread_mutex_lock(&lock);
    sum += local_sum;
    pthread_mutex_unlock(&lock);
    return NULL;
}

int main() {
    pthread_t t1, t2;
    pthread_mutex_init(&lock, NULL);
    
    printf("Enter n: ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

    int a = 0, b = 1;
    pthread_create(&t1, NULL, add, &a);
    pthread_create(&t2, NULL, add, &b);
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    printf("Sum = %d\n", sum);
    pthread_mutex_destroy(&lock);
}
