package easy

import "testing"

func TestTwoSums(t *testing.T) {

	t.Log("Test two sums")

	t.Run("Check if is two sums", func(t *testing.T) {
		nums := []int{2, 7, 11, 15}
		target := 9

		result := twoSumS(nums, target)
		expected := []int{0, 1}

		if result[0] != expected[0] || result[1] != expected[1] {
			t.Errorf("Expected %v but got %v", expected, result)
		}
	})

	t.Run("Check if is two sums", func(t *testing.T) {
		nums := []int{3, 2, 4}
		target := 6

		result := twoSumS(nums, target)
		expected := []int{1, 2}

		if result[0] != expected[0] || result[1] != expected[1] {
			t.Errorf("Expected %v but got %v", expected, result)
		}

	})

}
