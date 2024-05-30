
import { useState, useEffect } from 'react';
import { Box, VStack, HStack, Heading, Text } from "@chakra-ui/layout";
import { FormControl, FormLabel } from "@chakra-ui/form-control";
import { Button, Input, Alert, AlertIcon, CloseButton } from "@chakra-ui/react";
import { useNavigate } from 'react-router-dom';


interface LoginProps {
  setIsLoggedIn: React.Dispatch<React.SetStateAction<boolean>>;
  setIsLoginOpen:React.Dispatch<React.SetStateAction<boolean>>;
}

export default function Login({setIsLoggedIn, setIsLoginOpen}: LoginProps) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate(); // Initialize useHistory hook
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

  const handleLogin = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/auth/login', {
        method: 'POST',
        body: JSON.stringify({email: email, password: password }),
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json'
        }
      });

      const data = await response.json();
      if (response.ok) {
        setMessage(data.message);
        setError(false);
        setIsLoggedIn(true); // Set isLoggedIn to true upon successful login
        setIsLoginOpen(false);
      } else {
        setMessage(data.message);
        setError(true);
      }

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      console.log('Login successful');
      navigate('/'); // Navigate to home page upon successful login
    } catch (error) {
      console.error('Error during Login:', error);
    } 
  };
  const handleKeyDown = event => {
    if (event.key === 'Enter') {
      handleLogin();
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
      position={'relative'}
    >
      <CloseButton
        position="absolute"
        top={25}
        right={25}
        onClick={() => setIsLoginOpen(false)}
        colorScheme="red"
        // Call onClose function when close button is clicked
      />
      <VStack spacing={4} align="flex-start" w="full">
        <VStack spacing={4} align="flex-start" w="full">
          <Heading color="white">Login</Heading>
          <Text color="#e1bee7">Enter your email and password to Login</Text>
          {message && (
          <Alert status={error ? "error" : "success"} rounded="md">
            <AlertIcon />
          {message}
         \
          </Alert>
        )}
        </VStack>

        <FormControl>
          <FormLabel color="white">E-mail Address</FormLabel>
          <Input
            rounded="none"
            variant="filled"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            backgroundColor="#e1bee7"
            color="black"
            borderRadius={20}
            _focus={{
              color: "white"
            }}
          />
        </FormControl>
        <FormControl>
          <FormLabel color="white">Password</FormLabel>
          <Input
            rounded="none"
            variant="filled"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            backgroundColor="#e1bee7"
            color="black"
            borderRadius={20}
            onKeyDown={handleKeyDown}
            _focus={{
              color: "white"
            }}
   
          />
        </FormControl>
        <HStack w="full" justify="space-between">
          <Button variant="link" colorScheme="blue" color="#e1bee7">
            Forgot Password?
          </Button>
        </HStack>
        <Button
          rounded="none"
          colorScheme="blue"
          w="center"
          backgroundColor="#e1bee7"
          color="#673ab7"
          onClick={handleLogin}
          borderRadius={20}
          
        >
          Login
        </Button>
      </VStack>
    </Box>
  );
}