javascript: (function() {
    if(document.URL.match("discog")!=null){
        if(document.getElementsByClassName("playlist")[0].getElementsByClassName("tracklist_track track").length<=2){
            try{
                socket = new WebSocket("ws://localhost:42069");
                socket.onopen = function(){
                    socket.send(document.documentElement.outerHTML);
                    socket.close()
                };
            }catch(error){
                console.log(error);
            }
        }else{
            alert("More then 3 songs, maybe not a single ?");
        }
    }else{
        alert("Discogs script clicked without being on discogs");
    }
})();