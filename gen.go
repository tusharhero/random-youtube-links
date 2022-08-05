package main

import (
    "fmt"
    "time"
    "math/rand"
	"log"
	"net/http"
)


var letters = []rune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_")

func randSeq(n int) string {
	rand.Seed(time.Now().UnixNano())	
    b := make([]rune, n)
    for i := range b {
        b[i] = letters[rand.Intn(len(letters))]
    }
    return string(b)
}
func checkyt(link string) bool {
	resp, err := http.Get(link)
    if err != nil {
        log.Fatal(err)
    }
	fmt.Println(resp.StatusCode)
	return resp.StatusCode <= 200
}

func main() {

    ytid := randSeq(11)
	fmt.Println(checkyt("https://inv.vern.cc/watch?v="+ytid))
}