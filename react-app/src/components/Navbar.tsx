import { HStack, Text } from "@chakra-ui/react";
import ColorMode from "./ColorMode";
const Navbar = () => {
  return (
    <HStack
      padding={".5rem"}
      justifyContent={"space-between"}
      alignItems={"center"}
    >
      <Text fontSize={"20px"} fontWeight={"bold"}>
        Dr. AI
      </Text>
      <ColorMode />
    </HStack>
  );
};

export default Navbar;
