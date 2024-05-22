import React, { useState } from 'react';
import './style.css'; // Import CSS file

function Chatbox() {
  const [isOpen, setIsOpen] = useState(false);
  const [inputText, setInputText] = useState('');
  const [messages, setMessages] = useState([]);

  const toggleChatbox = () => {
    setIsOpen(!isOpen);
  };

  const handleSend = () => {
    if (inputText.trim() !== '') {
      setMessages([...messages, { name: 'User', message: inputText }]);
      setInputText('');

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
        console.log(data.answer);
        setMessages([...messages, { name: 'Chatbot', message: data.answer }]);
      })
      .catch(error => {
        console.error('Error:', error);
      });
    }
  };

  const handleInputChange = event => {
    setInputText(event.target.value);
  };

  const updateChatText = () => {
    const reversedMessages = messages.slice().reverse();

    const html = reversedMessages.map((item, index) => (
      <div key={index} className={`messages__item ${item.name === "Sam" ? "messages__item--visitor" : "messages__item--operator"}`}>
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
            <img src="https://img.icons8.com/color/48/000000/circled-user-female-skin-type-5--v1.png" alt="image" />
          </div>
          <div className="chatbox__content--header">
            <h4 className="chatbox__heading--header">Chat support</h4>
          </div>
        </div>
        <div className="chatbox__header--footer">
          <p className="chatbox__description--header">Hi. My name is Sam. How can I help you?</p>
        </div>
        <div className="chatbox__messages">
          {updateChatText()}
        </div>
        <div className="chatbox__footer">
          <input type="text" value={inputText} onChange={handleInputChange} placeholder="Write a message..." />
          <button className="chatbox__send--footer send__button" onClick={handleSend}>Send</button>
        </div>
      </div>
      <div className="chatbox__button">
        <button onClick={toggleChatbox}>
          <img src="https://th.bing.com/th/id/R.7ed88e34422ab9fa2554f689c642870a?rik=6QlbwuWmzWT79A&riu=http%3a%2f%2fwww.freepngimg.com%2fdownload%2fchat%2f1-2-chat-png-image.png&ehk=WJg1aiuswHh5jpW%2fuE9ipZJfd4CWVlQ6kYyWtRbC29M%3d&risl=&pid=ImgRaw&r=0-icon.svg" alt="Chatbox Icon" />
        </button>
      </div>
    </div>
  );
}

export default Chatbox;
