import { Code, Divider, HStack, Text, Link, Button } from "@chakra-ui/react";
import ColorMode from "./ColorMode";
import { BrowserRouter as Router, Route, Routes, Link as RouterLink } from 'react-router-dom';
import Sign_up_page from './Sign_up_page'; // Import the Sign_up_page component

const Navbar = () => {
  return (
    <Router>
      <HStack
        padding={".5rem"}
        justifyContent={"space-between"}
        alignItems={"center"}
      >
        <Text color="#8338ec" fontSize={"30px"} fontWeight={"bold"}>
          Doctor AI
        </Text>
        <HStack>
          <Link><Code colorScheme="purple" children="Treatment Plan" /></Link>
          <Link><Code colorScheme="blue" children="Disease Diagnosis" /></Link>
          <Divider orientation="vertical" h={5} />
          <Button as={RouterLink} to="/sign-up" colorScheme="purple" size="md"> {/* Link to the sign-up page */}
            Sign Up
          </Button>
          <ColorMode />
        </HStack>
      </HStack>
      <Routes>
        <Route path="/sign-up" element={<Sign_up_page />} /> {/* Define the route for the sign-up page */}
      </Routes>
    </Router>
  );
};

export default Navbar;
