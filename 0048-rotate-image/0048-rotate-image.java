class Solution {

     static void rotate(int[][] matrix) {

        List<List<Integer>> list = new ArrayList<>();

        int count = 0;

        for(int i=0; i<matrix.length; i++){

            List<Integer> l = new ArrayList<>();

            for(int j=0; j<matrix[0].length; j++){

                

                l.add(matrix[j][i]);

            }

            list.add(l);

        }

        for(int i=0; i<matrix.length; i++){

            List<Integer>l = list.get(i);

           int m = l.size()-1;

            for(int j=0; j<matrix[0].length; j++){

                matrix[i][j] = l.get(m--);

            }

        }

    }

}