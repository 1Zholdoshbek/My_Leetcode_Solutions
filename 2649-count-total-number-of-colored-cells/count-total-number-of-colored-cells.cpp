class Solution {
public:
    /**
     * Calculates the total number of colored cells in a pattern where:
     * - There are n lines with n cells each
     * - And n-1 lines with n-1 cells each
     * 
     * Visual Pattern Example for n=3:
     *     *      (1 cell)
     *    ***     (3 cells)
     *   *****    (5 cells)
     *    ***     (3 cells)
     *     *      (1 cell)
     * 
     * @param n Number of steps
     * @return Total number of colored cells
     */
    long long coloredCells(int n) {
        // Convert to long long to handle large numbers
        long long steps = n;
        
        // Calculate cells in n lines of n cells each
        long long mainLines = steps * steps;
        
        // Calculate cells in (n-1) lines of (n-1) cells each
        long long secondaryLines = (steps - 1) * (steps - 1);
        
        // Total cells = cells in main lines + cells in secondary lines
        return mainLines + secondaryLines;
    }
};