class Solution {
public:
    double myPow(double x, int n) {
        // If n is negative, we work with its absolute value and invert the result.
        long long N = n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }

        double result = 1;
        double current_product = x;

        for (long long i = N; i; i /= 2) {
            // If the current power is odd, multiply the result by the current product.
            if (i % 2) {
                result *= current_product;
            }
            // Square the current product for the next iteration.
            current_product *= current_product;
        }

        return result;
    }
};
