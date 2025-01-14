package easy

import (
	"math"
)

func isPalindrome(x int) bool {

	if x < 0 {
		return false
	}

	digits := countDigits(x)

	for i := 0; i < digits/2; i++ {
		left := (x / pow(10, digits-i-1)) % 10
		right := (x % pow(10, i+1))
		if i > 0 {
			right = right / pow(10, i)
		}
		if left != right {
			return false
		}
	}

	return true
}

func countDigits(x int) int {
	digits := 1
	for i := x; i >= 10; i = i / 10 {
		digits++
	}

	return digits
}

func pow(x, y int) int {
	return int(math.Pow(float64(x), float64(y)))
}
