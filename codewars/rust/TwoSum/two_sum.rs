fn two_sum(numbers: &[i32], target: i32) -> (usize, usize) {
    for (i, elem) in numbers.iter().enumerate() {
        for (j, elem1) in numbers.iter().skip(i+1).enumerate() {
            if elem + elem1 == target {
                return (i, j+i+1)
            }
        }
    }
    (0,0)
}