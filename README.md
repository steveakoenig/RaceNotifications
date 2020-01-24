# RaceNotifications
This is a simple prototype to demonstrate how to use Twilio to send notifications about race status and results. At [RMQMA](http://rmqma.com) all such notifications are currently via PA system, which can be hard to hear while the cars are running. This would add a way for members to be notified when they need to know.   
The numbering system (1-9, 0, X, Y) is what is used in Quarter Midget racing.

To use set the following environment variables:
 * `TWILIO_ACCOUNT_SID`: Twilio account SID
 * `TWILIO_AUTH_TOKEN`: Twilio authorization tiekn
 * `TWILIO_PHONE_NUMBER`: Number to use to send the SMS messages from

The only input into the script is a file containing the lineups. The format for that file is a class name (i.e. Jr. Novice, Heavy World Formula, etc) without commas, then lines containing the driver names and phone numbers separated by commas. The last driver should be followed by a new line, after that another class may be added with the same format. The newline after the last class is optional.  
Example:

```
Junior Honda
Joey L., +17205551111 
Kyle P., +17205552222
Dale E., +17205553333

Senior Honda
Kyle B., +17205554444
Kurt B., +17205556666
Dale E., +17205557777

```

