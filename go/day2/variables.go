package main // need a package just to compile

import "fmt"

func main() { // always need a function main
	var name string = "nico"
	// name := "nico" // shorthanded way to define variable, go assumes type of variable
	name = "lynn"
	fmt.Println(name)

}
