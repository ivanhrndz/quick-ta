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
         - Receives response and updates chat area
   
2. Natural lanugage parser for question
   - Tokenize statement (1-gram 2-gram)
   - Tf-IDF words
   - topic analysis (LDA/ Labeled LDA)

3. Prediction of information requested
   - Multiclass classier
   
   - Scheduling
      - Exams
      - Homework
      - Office Hours
     
   - Grading
         - Current Grade
         - Exam worth
         - Extra credit opportunities
     
   - Course requirements
      - Book requirement
      - Technology Requirement
   
   - Location
      - Office hours
      - Exams
      - Quizzes
   
   - Emergency
      - Missed class
      - Missed exam
      - Upcoming absence
      
   - Resources
      - Tutoring
      - Involved in research
      
4) Retreive Information

5) Pass back information

6) Update model
   - Ask for feedback
