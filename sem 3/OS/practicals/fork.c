#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {

    pid_t pid = fork();

    if (pid == 0) {
        // Child process
        printf("Hello from Child Process! My PID is %d\n", getpid());
    } else {
        // Parent process
        wait(NULL); // Wait for child to finish
        printf("Hello from Parent Process! My PID is %d and my Child's PID is %d\n", getpid(), pid);
    }

    return 0;
}