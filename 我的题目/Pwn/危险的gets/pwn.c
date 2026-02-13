#include <stdio.h>
#include <stdlib.h>

int backdoor() {
    puts("congratulation!");
    system("/bin/sh");
    return 0;
}

int main() {
    char buf[64];
    gets(buf);
    return 0;
}