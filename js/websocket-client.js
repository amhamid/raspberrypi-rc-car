var websocket;
var wsUri = "ws://" + document.domain + ":9090";

// initialize websocket connection
function init() {
  connectWebSocket();
  eventHandler();
}

// websocket connection and handlers
function connectWebSocket() {
  websocket = new WebSocket(wsUri);

  websocket.onopen = function(evt) {
//    alert("READY...");
  };

  websocket.onclose = function(evt) {
//    alert("DISCONNECTED");
  };

  websocket.onmessage = function(evt) {
    console.log(evt.data);
  };

  websocket.onerror = function(evt) {
//    alert(evt.data);
  };
}

// send json message to websocket connection
function doSend(action) {
  console.log("Action: " +action);
  websocket.send(action);
}

function arrowHandler(action) {
    var actionElement = '.' + action;

    // desktop
    $(actionElement).on('mousedown', function() {
        console.log(action);
        doSend(action);
    });
    $(actionElement).on('mouseup', function() {
        console.log("cleanup");
        doSend("cleanup");
    });

    // touch devices
    $(actionElement).on('touchstart', function() {
        console.log(action);
        doSend(action);
    });
    $(actionElement).on('touchend', function() {
        console.log("cleanup");
        doSend("cleanup");
    });
}

function eventHandler() {
    $(document).ready(function() {
        arrowHandler(".forward");
        arrowHandler(".backward");
        arrowHandler(".left");
        arrowHandler(".right");
    });
}
