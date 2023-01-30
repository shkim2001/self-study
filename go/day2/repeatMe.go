// take in multiple parameters

package main // need a package just to compile

import (
	"fmt"
)

func repeatMe(words ...string) {
	fmt.Println(words)
}

func main() { // always need a function main
	repeatMe("nico", "lynn", "dal", "marl", "flynn")
}
