# QUICK-TA

1. Chat client interface for student
   - Student starts chat
      - On page load new table create with IP address
      - Table save student question, submit time
      - When student types and presses 'submit' a chat function is activated
      - Chat function
         - Sends POST to update table with question and submit time
         - Updates Chat Area
         - Sends statement to model to parse
   
2. Natural lanugage parser for question
   - Tokenize statement (1-gram 2-gram)
   - Tf-IDF words
   - topic analysis (LDA/ Labeled LDA)

3. Prediction of information requested
   - Multiclass classier predicts:
      - Entity of interest
      - Property of entity being asked

| Entity        | Property           |
|-----------------|---------------------|
| *Exam*  	  |                     |
|        	  | Topic               |
|                 | Location            |
|       	  | Date and Time       |
|       	  | Format              |
|        	  | Number of Questions |
| *Quiz*   	  |                     |
|        	  | Topic               |
|        	  | Location            |
|        	  | Date and Time       |
|         	  | Format              |
|        	  | Number of Questions |
| *Report*	  |                     |
		  | Topic               |
|          	  | Location            |
|                 | Deadline	        |
|                 | Format              |
|                 | Requirements        |
| *Course Policy* |                     |
|       	  | Emergency Contact   |
|      		  | Absence	        |
|      		  | Attendance		|
|      		  | Late Assignments    |
|      		  | Requirements        |
| Grading Policy  |                     |
|      		  | How to calculate grade  |
|                 | Absence	         |
|                 | Attendance		 |
|                 | Late Assignments    |
|                 | Requirements 		 |
| Teaching Assistant |                   |
|                 | Name				 |
|                 | Contact Information |
|                 | Office Hours		 |
| Instructor      |  |
|        	  | Name				 |
|                 | Contact Information |
|                 | Office Hours		 |
	
 
4) Retreive Information matching entiry and property

5) Pass back information

6) Update model
   - Ask for feedback
