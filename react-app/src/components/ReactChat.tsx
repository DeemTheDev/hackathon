import { useState } from "react";
import React from "react";

import {
  Button,
  Input,
  useDisclosure,
  Drawer,
  DrawerBody,
  DrawerFooter,
  DrawerHeader,
  DrawerOverlay,
  DrawerContent,
  DrawerCloseButton,
  Flex,
  Text,
} from "@chakra-ui/react";

// Animations
import Lottie from "lottie-react";
import chatbot from "../assets/chatbot.json";

const ReactChat = () => {
  const { isOpen, onOpen, onClose } = useDisclosure();
  const btnRef = React.useRef();
  const [inputText, setInputText] = useState("");
  const [messages, setMessages] = useState([]);

  const handleSend = async () => {
    if (inputText.trim() !== "") {
      const updatedMessages = [
        ...messages,
        { name: "User", message: inputText },
      ];
      setMessages(updatedMessages);
      setInputText("");

      fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        body: JSON.stringify({ message: inputText }),
        mode: "cors",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((data) => {
          const updatedMessagesWithResponse = [
            ...updatedMessages,
            { name: "Chatbot", message: data.answer },
          ];
          setMessages(updatedMessagesWithResponse);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    }
  };

  const handleInputChange = (event) => {
    setInputText(event.target.value);
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      handleSend();
    }
  };

  const renderMessages = () => {
    return messages.map((item, index) => (
      <Flex
        key={index}
        justifyContent={item.name === "User" ? "flex-end" : "flex-start"}
        mb={2} // Add margin bottom to create space between messages
      >
        <Text
          px={3}
          py={2}
          fontWeight={600}
          bg={item.name === "User" ? "#6b38fb" : "teal.300"}
          color={item.name === "User" ? "white" : "black"}
          borderRadius="lg"
          maxWidth="70%"
        >
          {item.message}
        </Text>
      </Flex>
    ));
  };

  console.log("ReactChat component is rendering");

  return (
    <>
      <Lottie
        animationData={chatbot}
        loop={true}
        ref={btnRef}
        onClick={onOpen}
        style={{
          width: "110px",
          height: "110px",
          float: "right",
          marginRight: "20px",
        }}
      />
      <Drawer
        isOpen={isOpen}
        placement="right"
        onClose={onClose}
        finalFocusRef={btnRef}
      >
        <DrawerOverlay />
        <DrawerContent>
          <DrawerCloseButton />
          <DrawerHeader color={"teal.300"} fontWeight={800} fontSize="2xl">
            Chat with Dr. AI
          </DrawerHeader>

          <DrawerBody overflowY="auto" h="calc(100% - 120px)">
            {renderMessages()}
            <br />
          </DrawerBody>

          <DrawerFooter>
            <Input
              placeholder="Type your message..."
              value={inputText}
              onChange={handleInputChange}
              onKeyDown={handleKeyDown}
            />
            <Button colorScheme="teal" onClick={handleSend}>
              Send
            </Button>
          </DrawerFooter>
        </DrawerContent>
      </Drawer>
    </>
  );
};

export default ReactChat;
