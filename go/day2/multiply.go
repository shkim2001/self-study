package main // need a package just to compile

import "fmt"

func multiply(a int, b int) int {
	return a * b
}

// func multiply(a , b int) int {
// 	return a * b
// }

func main() { // always need a function main
	fmt.Println(multiply(2, 2))

}
