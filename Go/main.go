package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

func getWeather(city string) {
	url := fmt.Sprintf("https://wttr.in/%s?format=3", city)
	resp, err := http.Get(url)

	if err != nil {
		fmt.Println("Ein Fehler ist aufgetreten:", err)
		return
	}

	defer resp.Body.Close()

	if resp.StatusCode == http.StatusOK {
		bodyBytes, err := ioutil.ReadAll(resp.Body)
		if err != nil {
			fmt.Println("Ein Fehler ist aufgetreten:", err)
			return
		}
		bodyString := string(bodyBytes)
		fmt.Printf("Wetter in %s: %s\n", city, bodyString)
	} else {
		fmt.Println("Stadt nicht gefunden oder Serverfehler.")
	}
}

func main() {
	fmt.Println("Gib den Namen der Stadt ein:")
	var city string
	fmt.Scanln(&city)

	getWeather(strings.TrimSpace(city))
}
