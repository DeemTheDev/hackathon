import { HStack, Text } from "@chakra-ui/react";
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
      <ColorMode />
    </HStack>
  );
};

export default Navbar;
