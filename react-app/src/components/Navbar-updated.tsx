import { HStack, Text } from "@chakra-ui/react";
import ColorMode from "./ColorMode";
import { Link } from "@chakra-ui/react";
import '../navbar.css';

const Navbar = () => {
  return (
    <HStack
      className="navbar"
      padding={".5rem"}
      justifyContent={"space-between"}
      alignItems={"center"}
    >
      <Text className="navbar-title" fontSize={"20px"} fontStyle={"italic"}>
        Dr. AI
      </Text>

      <HStack className="navbar-links" spacing={4}>
        <Link href='#' className="navbar-link" fontSize={"15px"}>Treatment Plan</Link>
        <Link href='#' className="navbar-link" fontSize={"15px"}>Disease Diagnosis</Link>
        <button className="navbar-button"><a href="#">Sign Up</a></button>
      </HStack>
      
      <ColorMode />
    </HStack>
  );
};

export default Navbar;
