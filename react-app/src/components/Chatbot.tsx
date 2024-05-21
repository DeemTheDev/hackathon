import {
  Box,
  Input,
  Button,
  VStack,
  HStack,
  Text,
  Flex,
  useDisclosure,
  IconButton,
} from "@chakra-ui/react";
import { useState } from "react";
import { ChatIcon } from "@chakra-ui/icons";
import { CloseIcon } from "@chakra-ui/icons";

const Chatbot: React.FC = () => {
  const [messages, setMessages] = useState<
    Array<{ text: string; isUser: boolean }>
  >([]);
  const [inputText, setInputText] = useState("");
  const { isOpen, onOpen, onClose } = useDisclosure();

  const handleMessage = () => {
    if (inputText.trim() !== "") {
      setMessages([...messages, { text: inputText, isUser: true }]);
      setInputText("");
    }
  };

  return (
    <>
      <IconButton
        aria-label="Open Chat"
        icon={<ChatIcon />}
        size="lg"
        position={"fixed"}
        bottom={4}
        right={4}
        onClick={onOpen}
        zIndex={1000}
      />

      <Box
        p={4}
        h={"50vh"}
        borderWidth={"1px"}
        borderRadius={"md"}
        position={"fixed"}
        bottom={10}
        right={10}
        display={isOpen ? "block" : "none"}
      >
        <IconButton
          aria-label="Close Chat"
          icon={<CloseIcon />}
          size="sm"
          position={"relative"}
          float={"right"}
          onClick={onClose}
          zIndex={1000}
        />
        <VStack spacing={4} overflowY={"auto"} h="39vh" w="full" pb={4}>
          {messages.map((msg, idx) => (
            <HStack
              key={idx}
              alignSelf={msg.isUser ? "flex-end" : "flex-start"}
              w="full"
            >
              <Box
                bg={msg.isUser ? "blue.500" : "gray.500"}
                color={msg.isUser ? "white" : "black"}
                p={2}
                borderRadius={"md"}
              >
                <Text>{msg.text}</Text>
              </Box>
            </HStack>
          ))}
        </VStack>
        <Flex>
          <Input
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            placeholder="Type your message here"
            mr={2}
          ></Input>
          <Button onClick={handleMessage} colorScheme="blue">
            Send
          </Button>
        </Flex>
      </Box>
    </>
  );
};

export default Chatbot;
