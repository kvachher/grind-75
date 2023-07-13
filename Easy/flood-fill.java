class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        // top : sr-1, sc
        // right : sr, sc + 1
        // left : sr, sc - 1
        // down : sr + 1, sc

        int startColor = image[sr][sc];

        if (image[sr][sc] != color) {
            image[sr][sc] = color;

            if (sr - 1 >= 0 && image[sr-1][sc] == startColor) 
                floodFill(image, sr - 1, sc, color);

            if (sr + 1 < image.length && image[sr + 1][sc] == startColor) 
                floodFill(image, sr + 1, sc, color);

            if (sc + 1 < image[0].length && image[sr][sc + 1] == startColor)
                floodFill(image, sr, sc + 1, color);
            
            if (sc - 1 >= 0 && image[sr][sc - 1] == startColor)
                floodFill(image, sr, sc - 1, color);
            }

        return image;
    }
}
