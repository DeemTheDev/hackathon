import { useState } from "react";
import { Code, Divider, HStack, Text, Link, Button } from "@chakra-ui/react";
import { BrowserRouter as Router, Route, Routes, Link as RouterLink } from 'react-router-dom';
import Sign_up_page from './Sign_up_page'; // Import the Sign_up_page component
import Login_Page from './Login_Page';
import ColorMode from "./ColorMode";

function Navbar() {
  const [isSignUpOpen, setIsSignUpOpen] = useState(false); // State variable to track sign-up block visibility
  const [isLoginOpen, setIsLoginOpen] = useState(false); // State variable to track login block visibility

  // Function to toggle the visibility of the sign-up block
  const toggleSignUpBlock = () => {
    setIsSignUpOpen(!isSignUpOpen);
  };

  // Function to toggle the visibility of the login block
  const toggleLoginBlock = () => {
    setIsLoginOpen(!isLoginOpen);
  };

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
          <Link ><Code colorScheme="purple" children="Treatment Plan" /></Link>
          <Link><Code colorScheme="blue" children="Disease Diagnosis" /></Link>
          <Divider orientation="vertical" h={5} />
          <Button as={RouterLink} to="/sign-up" colorScheme="purple" size="md" onClick={toggleSignUpBlock}>
            {isSignUpOpen ? 'Close Sign Up' : 'Sign Up'}
          </Button>
          <Button as={RouterLink} to="/login" colorScheme="purple" size="md" onClick={toggleLoginBlock}>
            {isLoginOpen ? 'Close Login' : 'Login'}
          </Button>
        </HStack>
      </HStack>
      <Routes>
        {isSignUpOpen && ( // Render sign-up page only if isSignUpOpen is true
          <Route path="/sign-up" element={<Sign_up_page />} />
        )}
        {isLoginOpen && ( // Render login page only if isLoginOpen is true
          <Route path="/login" element={<Login_Page />} />
        )}
      </Routes>
    </Router>
  );
};

export default Navbar;
