import React, { useState, useEffect } from "react";
import { Input, Button, Alert, AlertIcon, CloseButton } from "@chakra-ui/react";
import { Box, VStack, Heading, Text } from "@chakra-ui/layout";
import { FormControl, FormLabel } from "@chakra-ui/form-control";
import { useNavigate } from "react-router-dom";


export default function Signup() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  const navigate = useNavigate()
  const [message, setMessage] = useState('');
  const [error, setError] = useState(false);
 
  useEffect(() => {
    // Clear message after 5 seconds
    const timer = setTimeout(() => {
      setMessage('');
      setError(false);
    }, 2000);

    return () => clearTimeout(timer); // Clear timeout on component unmount
  }, [message]);

  const handleSignup = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/auth/sign-up', {
        method: 'POST',
        body: JSON.stringify({ name: name, email: email, password: password }),
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
      navigate('/')
    } catch (error) {
      console.error('Error during signup:', error);
    }
  };

  const handleKeyDown= event => {
    if (event.key === 'Enter') {
      handleSignup();
    }
  };
 
  return (
    <Box
      w={["full", "md"]}
      p={[8, 10]}
      mt={[20, "10vh"]}
      mx="auto"
      border={["none", "1px"]}
      borderColor={["", "gray.300"]}
      borderRadius={10}
      backgroundColor="#673ab7"
    >
      <CloseButton
        position="absolute"
        top={155}
        right={180}
    
        colorScheme="red"
        onClick={() => onClose(false)} // Call onClose function when close button is clicked
      />

      <VStack spacing={4} align="flex-start" w="full">
        <VStack spacing={4} align="flex-start" w="full">
          <Heading color="white">Sign Up</Heading>
          <Text color="#e1bee7">Enter your details to create an account</Text>
          {message && (
          <Alert status={error ? "error" : "success"} rounded="md">
            <AlertIcon />
            {message}
          </Alert>
        )}
        </VStack>
        <FormControl>
          <FormLabel color="white">Full Name :</FormLabel>
          <Input
            rounded="none"
            variant="filled"
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            backgroundColor="#e1bee7"
            color="white"
            id= "name"
            borderRadius={20}
          />
        </FormControl>
        <FormControl>
          <FormLabel color="white">E-mail Address :</FormLabel>
          <Input
            rounded="none"
            variant="filled"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            backgroundColor="#e1bee7"
            color="white"
            id="email"
            borderRadius={20}
          />
        </FormControl>
        <FormControl>
          <FormLabel color="white">Password :</FormLabel>
          <Input
            rounded="none"
            variant="filled"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            backgroundColor="#e1bee7"
            color="white"
            id="password"
            borderRadius={20}
          />
        </FormControl>
        <Button
          rounded="none"
          colorScheme="blue"
          w="center"
          backgroundColor="#e1bee7"
          color="black"
          onClick={handleSignup}
          borderRadius={20}
          onKeyDown={handleKeyDown}
        >
          Sign Up
        </Button>
      </VStack>
    </Box>
  );
}