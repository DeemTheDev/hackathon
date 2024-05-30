import {
  Text,
  Button,
  Modal,
  FormControl,
  FormLabel,
  Input,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
} from "@chakra-ui/react";
import { useDisclosure } from "@chakra-ui/react";
import React, { useState } from "react";
import axios from "axios";
import { Alert, AlertIcon} from "@chakra-ui/react";

const SignUp = () => {
  //Form Input
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState('');
  const [error, setError] = useState(false);

  //Page Functionality
  const { isOpen, onOpen, onClose } = useDisclosure();


  //Function to handle when submitted:
  const handleSignup = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/auth/sign-up', {
        method: 'POST',
        body: JSON.stringify({ username:username, email: email, password: password }),
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json'
        }
      });


      const data = await response.json();
      if (response.ok) {
        setMessage(data.message);
        setError(false);
      } else {
        setMessage(data.message);
        setError(true);
      }

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      console.log('Signup successful');
  
    } catch (error) {
      console.error('Error during signup:', error);
    }
  };
  return (
    <>
      <Button colorScheme="purple" size="md" onClick={onOpen}>
        Sign Up
      </Button>
      <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay bgColor="blackAlpha.800" />
        <ModalContent>
          <ModalHeader>
            <Text color="teal.200" fontWeight="bold" fontSize="x-large">
              Create your account
            </Text>
          </ModalHeader>
          <ModalCloseButton />
          {message && (
          <Alert status={error ? "error" : "success"} rounded="md">
            <AlertIcon />
            {message}
          </Alert>
        )}
          
          <ModalBody pb={6}>
            <FormControl>
              <FormLabel fontWeight={700}>Username</FormLabel>
              <Input
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
            </FormControl>

            <FormControl mt={4}>
              <FormLabel fontWeight={700}>Email</FormLabel>
              <Input
                placeholder="Email@email.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </FormControl>
            <br />
            <FormControl>
              <FormLabel fontWeight={700}>Password</FormLabel>
              <Input
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </FormControl>
          </ModalBody>

          <ModalFooter>
            <Button
              colorScheme="teal"
              mr={3}
              type="submit"
              onClick={handleSignup}
            >
              Save
            </Button>
            <Button onClick={onClose}>Cancel</Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  );
};

export default SignUp;
