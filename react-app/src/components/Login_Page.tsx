import User from './User';
import { useState } from 'react';
import { Box, VStack, HStack, Heading, Text } from "@chakra-ui/layout";
import { FormControl, FormLabel } from "@chakra-ui/form-control";
import { Button, Input } from "@chakra-ui/react";
import bcrypt from 'bcrypt';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    try {
      const user = await User.findOne({ where: { email } });
      if (user && (await bcrypt.compare(password, user.password))) {//this one line idk I have tried everything I know
        // Login successful
        console.log('Login successful');
      } else {
        // Login failed
        console.log('Login failed');
      }
    } catch (error) {
      console.error(error);
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
      <VStack spacing={4} align="flex-start" w="full">
        <VStack spacing={4} align="flex-start" w="full">
          <Heading color="white">Login</Heading>
          <Text color="#e1bee7">Enter your email and password to Login</Text>
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
            color="#673ab7"
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
            color="#673ab7"
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
        >
          Login
        </Button>
      </VStack>
    </Box>
  );
}