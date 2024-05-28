import React, { useState } from 'react';
import './style.css'; // Import CSS file

function Chatbox() {
  const [isOpen, setIsOpen] = useState(false);
  const [inputText, setInputText] = useState('');
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);


  const toggleChatbox = () => {
    setIsOpen(!isOpen);
  };

  const handleSend = () => {
    if (inputText.trim() !== '') {
      const updatedMessages = [...messages, { name: 'User', message: inputText }];
      setMessages(updatedMessages);
      setInputText('');
      setIsLoading(true); // Set isLoading to true before sending request
  
      setTimeout(() => {
        fetch('http://127.0.0.1:5000/predict', {
          method: 'POST',
          body: JSON.stringify({ message: inputText }),
          mode: 'cors',
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(response => response.json())
        .then(data => {
          const updatedMessagesWithResponse = [...updatedMessages, { name: 'Chatbot', message: data.answer }];
          setMessages(updatedMessagesWithResponse);
          setIsLoading(false); // Set isLoading to false after receiving response
        })
        .catch(error => {
          console.error('Error:', error);
        });
      }, 1500); // Delay response by 3 seconds
    }
  };
  

  const handleInputChange = event => {
    setInputText(event.target.value);
  };
  const handleKeyDown = event => {
    if (event.key === 'Enter') {
      handleSend();
    }
  };
  const updateChatText = () => {
    const reversedMessages = messages.slice().reverse();

    const html = reversedMessages.map((item, index) => (
      <div key={index} className={`messages__item ${item.name === "User" ? "messages__item--visitor" : "messages__item--operator"}`}>
        {item.message}
      </div>
    )); 

    return html;
  };

  return (
    <div className={`chatbox ${isOpen ? 'chatbox--active' : ''}`}>
      <div className="chatbox__support">
        
        <div className="chatbox__header">

          <div className="chatbox__image--header">
            <img src="https://th.bing.com/th/id/R.8e2c571ff125b3531705198a15d3103c?rik=muXZvm3dsoQqwg&riu=http%3a%2f%2fpluspng.com%2fimg-png%2fpng-user-icon-person-icon-png-people-person-user-icon-2240.png&ehk=MfHYkGonqy7I%2fGTKUAzUFpbYm9DhfXA9Q70oeFxWmH8%3d&risl=&pid=ImgRaw&r=0" alt="image" />
          </div>

          <div className="chatbox__content--header">
            <h4 className="chatbox__heading--header">Chat support</h4>
          </div>

        </div>

        <div className="chatbox__header--footer">
          <p className="chatbox__description--header">Hi. How can I help you?</p>
        </div>

        <div className="chatbox__messages">
        
        {updateChatText()} 
        
        </div>
        
        <div style={{ display: 'flex', marginLeft: '10px', margin: '3px' }}>
        {isLoading && <div className="typing-bubble"></div>}
        {isLoading && <div className="typing-bubble"></div>}
        {isLoading && <div className="typing-bubble"></div>}
        </div>

        <div className="chatbox__footer">
          <input type="text" value={inputText} onChange={handleInputChange} onKeyDown={handleKeyDown} placeholder="Write a message..." />
          <button className="chatbox__send--footer send__button" onClick={handleSend}>Send</button>
          
        </div>
      </div>

      <div className="chatbox__button">
        <button onClick={toggleChatbox}>
          <img className="chatbox_icon" src="https://th.bing.com/th/id/R.a5b49ccb833a953658c7ef94596f3287?rik=0XVN2ybEkq66ng&pid=ImgRaw&r=0&sres=1&sresct=1" alt="Chatbox Icon" />
        </button>
      </div>

    </div>
  );
}

export default Chatbox;
