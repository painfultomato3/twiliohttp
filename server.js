const express = require('express');
const bodyParser = require('body-parser');
const MessagingResponse = require('twilio').TwimlResponse;

const app = express();

app.use(bodyParser.urlencoded({ extended: false }));

app.post('/sms', (req, res) => {

  message = req.body.Body;

  const twiml = new MessagingResponse();

  twiml.message('The Robots are coming! Head for the hills!');

  res.type('text/xml').send(twiml.toString());
});

app.listen(1337, () => {
  console.log('Express server listening on port 3000');
});