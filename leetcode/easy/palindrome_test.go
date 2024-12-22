package easy

import (
	"testing"
)

func TestPalindrome(t *testing.T) {

	t.Log("Test is palindrome")

	t.Run("Check if is palindrome", func(t *testing.T) {
		palindromes := []int{121, 1221, 12321, 123321, 1234321}

		for _, element := range palindromes {
			result := isPalindrome(element)
			if result != true {
				t.Errorf("Expected %v but got %v", true, result)
			}
		}
	})

	t.Run("Check if is not a palindrome", func(t *testing.T) {
		notPalindromes := []int{10, 20, 12, 23, 45, 69, 95}

		for _, element := range notPalindromes {
			result := isPalindrome(element)
			if result != false {
				t.Errorf("Expected %v but got %v", false, result)
			}
		}
	})

	t.Run("Check if is palindrome with negative number", func(t *testing.T) {
		palindromes := []int{-121}

		for _, element := range palindromes {
			result := isPalindrome(element)
			if result != false {
				t.Errorf("Expected %v but got %v", false, result)
			}
		}
	})
}
