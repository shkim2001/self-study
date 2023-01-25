package something

import "fmt"

func sayBye() { // private function, so cannot be exported (not capitalized)
	fmt.Println("Bye")
}

func SayHello() { // public function, so can be exported (capitalized)
	fmt.Println("Hello")
}
