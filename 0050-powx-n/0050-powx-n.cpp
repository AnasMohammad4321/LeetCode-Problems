class Solution {
public:
    double myPow(double x, int n) {
        // Base cases
        if (x == 0) return 0;
        if (n == 0) return 1;
        if (x == 1) return 1;

        // Handle negative exponent
        if (n < 0) {
            x = 1 / x;
            // Using long long to avoid overflow when n is INT_MIN
            n = -(n + 1);
        } else {
            n = n - 1;
        }

        double result = 1;
        double current_product = x;

        while (n > 0) {
            // Use bitwise AND to check if current exponent is odd
            if (n & 1) {
                result *= current_product;
            }
            current_product *= current_product;
            // Shift right to divide by 2
            n >>= 1;
        }

        // Correct for the initial subtraction
        return result * x;
    }
};
