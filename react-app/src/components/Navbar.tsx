import { Code, Divider, HStack, Text, Link, Image } from "@chakra-ui/react";

import ColorMode from "./ColorMode";

//Import Sign Up Button
import SignUp from "./SignUp";

//Import Logo
import Logo from "../assets/2.svg";

const Navbar = () => {
  return (
    <HStack
      padding={".5rem"}
      justifyContent={"space-between"}
      alignItems={"center"}
    >
      {/* <Text color="#8338ec" fontSize={"30px"} fontWeight={"bold"}>
        Doctor AI
      </Text> */}
      <Image src={Logo} alt="Logo" width={90} height={90} />
      <HStack>
        <Link href="http://localhost:8502">
          <Code colorScheme="purple" children="Treatment Plan" />
        </Link>
        <Link href="http://localhost:8501">
          <Code colorScheme="blue" children="Disease Diagnosis" />
        </Link>
        <Divider orientation="vertical" h={5} />
        <SignUp />
        <ColorMode />
      </HStack>
    </HStack>
  );
};

export default Navbar;
