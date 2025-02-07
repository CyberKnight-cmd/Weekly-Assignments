#include<stdio.h>
int generateStars(int n)
{

}
int main(){
    int n = 0;
    printf("Enter n = ");
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++)
    {
        for(int j = n-i; j > 0; j--){
            printf("  ");
        }
        for (int a = 0; a < 2*i+1; a++)
        {
            printf("* ");
        }
        printf("\n");
    }
    for (int i = 0; i < n-1; i++)
    {
        for(int j = 0; j < n-i; j++){
            printf("  ");
        }
        for(int j = 0; j < 2*i+1; j++){
            ;
        }
        
    }
    
    
    
    return 0;
}
 **
  *