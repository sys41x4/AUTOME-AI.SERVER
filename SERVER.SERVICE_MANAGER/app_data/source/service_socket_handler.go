package main

import (
        "fmt"
	"os"
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

                if err := conn.WriteMessage(messageType, p); err != nil {
                        log.Println(err)
                        return
                }

        }
}

func homePage(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "WELCOME TO AUTOME-AI :)")
}
func ws_AIEndpoint(w http.ResponseWriter, r *http.Request) {
        // upgrade this connection to a WebSocket
        // connection
        ws, err := upgrader.Upgrade(w, r, nil)
        if err != nil {
                log.Println(err)
        }

        log.Println("AI Connected")
        err = ws.WriteMessage(1, []byte("HELLO AI"))
        if err != nil {
                log.Println(err)
        }
        // listen indefinitely for new messages coming
        // through on our WebSocket connection
        reader(ws)
}

func ws_NLPEndpoint(w http.ResponseWriter, r *http.Request) {
        // upgrade this connection to a WebSocket
        // connection
        ws, err := upgrader.Upgrade(w, r, nil)
        if err != nil {
                log.Println(err)
        }

        log.Println("NLP Connected")
        err = ws.WriteMessage(1, []byte("HELLO NLP"))
        if err != nil {
                log.Println(err)
        }
        // listen indefinitely for new messages coming
        // through on our WebSocket connection
        reader(ws)
}

func ws_userEndpoint(w http.ResponseWriter, r *http.Request) {
        // upgrade this connection to a WebSocket
        // connection
        ws, err := upgrader.Upgrade(w, r, nil)
        if err != nil {
                log.Println(err)
        }

        log.Println("USER Connected")
        err = ws.WriteMessage(1, []byte("HELLO USER"))
        if err != nil {
                log.Println(err)
        }
        // listen indefinitely for new messages coming
        // through on our WebSocket connection
        reader(ws)
}

func ws_userIOTslaveEndpoint(w http.ResponseWriter, r *http.Request) {
        // upgrade this connection to a WebSocket
        // connection
        ws, err := upgrader.Upgrade(w, r, nil)
        if err != nil {
                log.Println(err)
        }

        log.Println("USER IOT Slave Connected")
        err = ws.WriteMessage(1, []byte("HELLO USER IOT Slave"))
        if err != nil {
                log.Println(err)
        }
        // listen indefinitely for new messages coming
        // through on our WebSocket connection
        reader(ws)
}

func setupRoutes() {
        http.HandleFunc("/", homePage)
	// http.HandleFunc("/ai", ws_AIEndpoint)
	// http.HandleFunc("/nlp", ws_NLPEndpoint)
        http.HandleFunc("/usr", ws_userEndpoint)
	http.HandleFunc("/iot_slave", ws_userIOTslaveEndpoint)
}

func main() {
	fmt.Println("Starting SERVER.MANAGER")
        setupRoutes()
        fmt.Println("SERVICE.MANAGER STARTED")
        log.Fatal(http.ListenAndServe(":"+os.Args[1], nil))
}
