package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/websocket"
)

// We'll need to define an Upgrader
// this will require a Read and Write buffer size
var upgrader = websocket.Upgrader{
	ReadBufferSize:  1024,
	WriteBufferSize: 1024,
	CheckOrigin:     func(r *http.Request) bool { return true },
}

// define a reader which will listen for
// new messages being sent to our WebSocket
// endpoint
func reader(conn *websocket.Conn) {
	for {
		// read in a message
		messageType, p, err := conn.ReadMessage()
		if err != nil {
			log.Println(err)
			return
		}
		// print out that message for clarity
		// Print the message to the console
                fmt.Printf("%s sent: %s\n", conn.RemoteAddr(), string(p))
		//log.Println(string(p))

		if err := conn.WriteMessage(messageType, "aaa"); err != nil {
			log.Println(err)
			return
		}

	}
}

func homePage(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "AUTOME-AI")
}

func ws_userEndpoint(w http.ResponseWriter, r *http.Request) {
	// upgrade this connection to a WebSocket
	// connection
	ws, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		log.Println(err)
	}

	log.Println("USER Connected")
	err = ws.WriteMessage(1, []byte("HI"))
	if err != nil {
		log.Println(err)
	}
	// listen indefinitely for new messages coming
	// through on our WebSocket connection
	reader(ws)
}

func ws_rootMicroControllerEndpoint(w http.ResponseWriter, r *http.Request) {
        // upgrade this connection to a WebSocket
        // connection
        ws, err := upgrader.Upgrade(w, r, nil)
        if err != nil {
                log.Println(err)
        }

        log.Println("ROOT HOME CONTROLLER Connected")
        err = ws.WriteMessage(1, []byte("HI ROOT"))
        if err != nil {
                log.Println(err)
        }
        // listen indefinitely for new messages coming
        // through on our WebSocket connection
        reader(ws)
}

func setupRoutes() {
	http.HandleFunc("/", homePage)
	http.HandleFunc("/user", ws_userEndpoint)
	http.HandleFunc("/rootHC", ws_rootMicroControllerEndpoint)
}

func main() {
	fmt.Println("Hello World")
	setupRoutes()
	log.Fatal(http.ListenAndServe(":8080", nil))
}
