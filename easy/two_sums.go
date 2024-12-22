package easy

// first attempt
func twoSumF(nums []int, target int) []int {
	firstIndex := -1
	nextIndex := -1

	for index, n := range nums {
		search := target - n

		for sIndex, number := range nums {
			if sIndex == index {
				continue
			}

			if search == number {
				firstIndex = index
				nextIndex = sIndex
				break
			}
		}
	}

	return []int{firstIndex, nextIndex}
}

// second attempt
func twoSumS(nums []int, target int) []int {

	m := make(map[int][]int)

	for index, n := range nums {
		if _, ok := m[n]; !ok {
			indexes := make([]int, 0)
			indexes = append(indexes, index)
			m[n] = indexes
		} else {
			m[n] = append(m[n], index)
		}
	}

	for firstIndex, n := range nums {
		search := target - n

		indexes, ok := m[search]
		if ok {
			if len(indexes) > 1 {
				return []int{indexes[0], indexes[1]}
			}
			if firstIndex == indexes[0] {
				continue
			}
			return []int{firstIndex, indexes[0]}
		}
	}

	return []int{-1, -1}
}

func ExecTwoSums() {
	twoSumS([]int{2, 7, 11, 15}, 9)
}
