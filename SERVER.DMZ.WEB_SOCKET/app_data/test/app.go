package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/websocket"
)

var upgrader = websocket.Upgrader{
	ReadBufferSize:  1024,
	WriteBufferSize: 1024,
}

func main() {
	http.HandleFunc("/echo", func(w http.ResponseWriter, r *http.Request) {
		conn, err := upgrader.Upgrade(w, r, nil)
		if err != nil {
			log.Println("upgrade:", err)
			return
		}
		defer conn.Close()

		for {
			// Read message from browser
			msgType, msg, err := conn.ReadMessage()
			if err != nil {
				log.Println("read:", err)
				break
			}
			// Print the message to the console
			fmt.Printf("%s sent: %s\n", conn.RemoteAddr(), string(msg))

			// Write message back to browser
			if err = conn.WriteMessage(msgType, msg); err != nil {
				log.Println("write:", err)
				break
			}
		}
	})

	log.Fatal(http.ListenAndServe(":8080", nil))
}
