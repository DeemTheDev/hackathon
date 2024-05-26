import { Code, Divider, HStack, Text, Link, Button } from "@chakra-ui/react";

import ColorMode from "./ColorMode";
const Navbar = () => {
  return (
    <HStack
      padding={".5rem"}
      justifyContent={"space-between"}
      alignItems={"center"}
    >
      <Text color="#8338ec" fontSize={"30px"} fontWeight={"bold"}>
        Doctor AI
      </Text>
      <HStack>
        <Link>
          <Code colorScheme="purple" children="Treatment Plan" />
        </Link>
        <Link href="http://localhost:8501">
          <Code colorScheme="blue" children="Disease Diagnosis" />
        </Link>
        <Divider orientation="vertical" h={5} />
        <Button colorScheme="purple" size="md">
          Sign Up
        </Button>
        <ColorMode />
      </HStack>
    </HStack>
  );
};

export default Navbar;
