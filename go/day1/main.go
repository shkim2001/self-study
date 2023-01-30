package main // need a package just to compile

import (
	"fmt"

	"github.com/shkim2001/learngo/something"
)

func main() { // always need a function main

	fmt.Println("Hello World!") // Capitalize first letter to export
	something.SayHello()        // public function, so can be imported
	// something.sayBye() is a private function (not capitalzied)
}
