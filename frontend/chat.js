/* 
Created by: Kenrick Beckett

Name: Chat Engine
*/


function randomint(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
var sessionid = randomint(0,1000000000000)
 var sequence = 0
function Chat () {
    this.update = updateChat;
    this.send = sendChat;
}


//Updates the chat
function updateChat(data){
				   if(data.text){
                            $('#chat-area').append($("<p>"+ data.text +"</p>"));						  
				   }
				   document.getElementById('chat-area').scrollTop = document.getElementById('chat-area').scrollHeight;
			   }


//send the message
function sendChat(message, nickname)
{
	sequence = sequence + 1	
     $.ajax({
		   type: "POST",
		   url: "process.php",
		   data: {  
		   			'function': 'send',
					'message': message,
					'nickname': nickname,
					'sessionid':sessionid,
					'sequence':sequence
				 },
		   dataType: "json",
		   success: function(data){
			   updateChat(data);
		   },
		});

		}
