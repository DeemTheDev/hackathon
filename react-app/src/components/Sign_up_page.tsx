import { useState } from 'react';
import { Box, VStack, Heading, Text } from "@chakra-ui/layout";
import { FormControl, FormLabel } from "@chakra-ui/form-control";
import { Button, Input } from "@chakra-ui/react";
import User from './User';

export default function Signup() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');

  const handleSignup = async () => {
    try {
      await User.create({ email, password, name });
      console.log('Signup successful');
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
          <Heading color="white">Sign Up</Heading>
          <Text color="#e1bee7">Enter your details to create an account</Text>
        </VStack>
        <FormControl>
          <FormLabel color="white">Full Name</FormLabel>
          <Input
            rounded="none"
            variant="filled"
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            backgroundColor="#e1bee7"
            color="#673ab7"
          />
        </FormControl>
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
        <Button
          rounded="none"
          colorScheme="blue"
          w="center"
          backgroundColor="#e1bee7"
          color="#673ab7"
          onClick={handleSignup}
        >
          Sign Up
        </Button>
      </VStack>
    </Box>
  );
}