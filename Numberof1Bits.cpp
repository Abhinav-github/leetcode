#Write a function that takes an unsigned integer 
#and return the number of '1' bits it has (also known as the Hamming weight).

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        uint32_t bitmask = 1;
        for (int a = 0; a < 32; a++) {
            uint32_t check = n & bitmask;
            if(check != 0) {
                count++;
            }
            n = n >> 1;
        }
        return count;
    }
};
