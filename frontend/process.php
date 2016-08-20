<?php

    $function = $_POST['function'];
    
    $log = array();
    
    switch($function) {
    
    	 case('getState'):
        	 if(file_exists('chat.txt')){
               $lines = file('chat.txt');
        	 }
             $log['state'] = count($lines); 
        	 break;	
    	
		
		case('receivedmessage'):
			$nickname = htmlentities(strip_tags($_POST['nickname']));
			$sessionid = $_POST['sessionid'];
			$ip = $_SERVER['REMOTE_ADDR'];
			$message = $_POST['message'];
			$timestamp = date("Y-m-d h:i:sa",time());
			
			$servername = "localhost";
			$username = "root@localhost";
			$password = "";
			$dbname = "quick-ta";
			// Create connection
			$conn = new mysqli($servername, $username, $password, $dbname);
			$sql = "INSERT INTO conversations (id, user, ip, message,time) VALUES ($sessionid, $nickname, $ip,$message,$timestamp)";

			mysqli_query($conn, $sql);

			
    	 case('update'):
        	$state = $_POST['state'];
        	if(file_exists('chat.txt')){
        	   $lines = file('chat.txt');
        	 }
        	 $count =  count($lines);
        	 if($state == $count){
        		 $log['state'] = $state;
        		 $log['text'] = false;
        		 
        		 }
        		 else{
        			 $text= array();
        			 $log['state'] = $state + count($lines) - $state;
        			 foreach ($lines as $line_num => $line)
                       {
        				   if($line_num >= $state){
                         $text[] =  $line = str_replace("\n", "", $line);
        				   }
         
                        }
        			 $log['text'] = $text; 
        		 }
        	  
             break;
    	 
    	 case('send'):
		  $nickname = htmlentities(strip_tags($_POST['nickname']));
			 $reg_exUrl = "/(http|https|ftp|ftps)\:\/\/[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(\/\S*)?/";
			  $message = htmlentities(strip_tags($_POST['message']));
		 if(($message) != "\n"){
        	
			 if(preg_match($reg_exUrl, $message, $url)) {
       			$message = preg_replace($reg_exUrl, '<a href="'.$url[0].'" target="_blank">'.$url[0].'</a>', $message);
				} 
			 
        	
        	$log['text'] = "<span>". $nickname . "</span>" . $message = str_replace("\n", " ", $message) . "\n"; 
		 	

			$sessionid = $_POST['sessionid'];
			$sequence = $_POST['sequence'];
			$ip = $_SERVER['REMOTE_ADDR'];
			$timestamp = date("Y-m-d h:i:sa",time());
			
			$servername = "127.0.0.1";
			$username = "root";
			$password = "";
			$dbname = "quickta";
			// Create connection
			 $conn = mysqli_connect("localhost", $username, $password,"quickta") or die(mysql_error());
			//@mysql_select_db($dbname) or die( "Unable to select database");
			$sql = "INSERT INTO conversations (id, sequence, user, ip, message,time) VALUES ('$sessionid', '$sequence', '$nickname', '$ip', '$message', '$timestamp')";
			
			mysqli_query($conn, $sql);
			mysqli_close($conn);
		 
		 }
        	 break;
    	
    }
    
    echo json_encode($log);


?>