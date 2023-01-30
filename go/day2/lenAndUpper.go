// returning multiple values

package main // need a package just to compile

import (
	"fmt"
	"strings"
)

func lenAndUpper(name string) (int, string) {
	return len(name), strings.ToUpper(name)
}

// naked return
func lenAndUpper2(name string) (length int, uppercase string) {
	// length and uppercase are already initially defined
	length = len(name)
	uppercase = strings.ToUpper(name)
	return
}

// defer
func lenAndUpper3(name string) (length int, uppercase string) {
	defer fmt.Println("I'm done.")
	// length and uppercase are already initially defined
	length = len(name)
	uppercase = strings.ToUpper(name)
	return
}

func main() { // always need a function main
	totalLength, upperName := lenAndUpper("nico")
	totalLength2, upperName2 := lenAndUpper2("nico")
	totalLength3, upperName3 := lenAndUpper2("nico")
	// totalLength,_ := lenAndUpper("nico") // ignore one value (if variable not used, go returns error)
	fmt.Println(totalLength, upperName)
	fmt.Println(totalLength2, upperName2)
	fmt.Println(totalLength3, upperName3)
}
