import { useState } from "react";
import { Code, Divider, HStack, Text, Link, Button } from "@chakra-ui/react";
import { BrowserRouter as Router, Route, Routes, Link as RouterLink } from 'react-router-dom';
import Sign_up_page from './Sign_up_page'; // Import the Sign_up_page component
import Login_Page from './Login_Page';
import ColorMode from "./ColorMode";
import Login from './Login_Page'; // Import the Login component
import BackendButtons from "./BackendButtons";

interface NavbarProps {
  setIsLoggedIn: React.Dispatch<React.SetStateAction<boolean>>;
}

function Navbar() {
  
  const [isSignUpOpen, setIsSignUpOpen] = useState(false); // State variable to track sign-up block visibility
  const [isLoginOpen, setIsLoginOpen] = useState(false); // State variable to track login block visibility
  const [isLoggedIn, setIsLoggedIn] = useState(false); // State variable to track user login status

  // Function to toggle the visibility of the sign-up block
  const toggleSignUpBlock = () => {
    setIsSignUpOpen(!isSignUpOpen);
  };

  // Function to toggle the visibility of the login block
  const toggleLoginBlock = () => {
    setIsLoginOpen(!isLoginOpen);
  };


  const handleLogout = () => {
    setIsLoggedIn(false); 
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
          {isLoggedIn &&
          <div>
          <Link ><Code colorScheme="purple" children="Treatment Plan" /></Link>
          <Link><Code colorScheme="blue" children="Disease Diagnosis" /></Link>
          <Divider orientation="vertical" h={5} />
          </div>
          }
          <Button as={RouterLink} to="/sign-up" colorScheme="purple" size="md" onClick={toggleSignUpBlock}>
            {isSignUpOpen ? 'Close Sign Up' : 'Sign Up'}
          </Button>

          {isLoggedIn ? (
            <Button colorScheme="purple" size="md" onClick={handleLogout}>
              Logout
            </Button>
          ) : (
            <Button as={RouterLink} to="/login" colorScheme="purple" size="md" onClick={toggleLoginBlock}>
              {isLoginOpen ? 'Close Login' : 'Login'}
            </Button>
          )}
        </HStack>
      </HStack>
      <Routes>
        {isSignUpOpen && ( // Render sign-up page only if isSignUpOpen is true
          <Route path="/sign-up" element={<Sign_up_page />} />
        )}
        {isLoginOpen && ( // Render login page only if isLoginOpen is true
          <Route path="/login" element={<Login_Page setIsLoggedIn={setIsLoggedIn} setIsLoginOpen={setIsLoginOpen} />} />
        )}
        {isLoggedIn && ( // Render login page only if user is logged in
          <Route path="/home" element={<Login/>} />
        )}
      </Routes>
     
    </Router>
  );
};

export default Navbar;
