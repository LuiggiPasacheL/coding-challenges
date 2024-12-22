package easy

import "testing"

func TestRomanToInteger(t *testing.T) {

	t.Log("Test Roman to Integer")

	t.Run("Test Cases", func(t *testing.T) {

		romanValues := []string{"III", "IV", "IX", "LVIII", "MCMXCIV", "MMMCMXCIX"}
		expectedValues := []int{3, 4, 9, 58, 1994, 3999}

		for i, romanValue := range romanValues {
			if romanToInt(romanValue) != expectedValues[i] {
				t.Errorf("Expected %d, but got %d", expectedValues[i], romanToInt(romanValue))
			}
		}
	})
}
