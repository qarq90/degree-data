#include <stdio.h>
#include <string.h>

int login() {
    char password[16];    
    int access = 0;      
    
    printf("Correct password: 'Jack Baker'\n");
    printf("Buffer size: 16 bytes (array size: 17)\n\n");
    
    printf("Enter password: ");
    gets(password); 
    
    printf("\n--- Memory Analysis ---\n");
    printf("Password stored at: %p\n", password);
    printf("Access flag at:     %p\n", &access);
    printf("Access value:       %d\n", access);
    printf("Password entered:   '%s'\n", password);
    printf("Password length:    %lu\n", strlen(password));
    printf("----------------------\n\n");
    
    if (strcmp(password, "Jack Baker") == 0) {
        access = 1; 
        printf("Password correct!\n");
    } else {
        printf("Wrong password!\n");
    }
    
    return access;
}

int main() {

    int result = login();
    
    if (result == 1) {
        printf("ACCESS GRANTED!\n");
        printf("   You are logged in as a Resident Evil!\n");
    } else {
        printf("ACCESS DENIED!\n");
        printf("   Invalid resident!\n");
    }
    
    return 0;
}
