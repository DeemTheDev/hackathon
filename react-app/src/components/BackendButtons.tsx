import React, {
  Box,
  Flex,
  Button,
  ScaleFade,
  AbsoluteCenter,
  useDisclosure,
  AlertDialog,
  AlertDialogBody,
  AlertDialogFooter,
  AlertDialogContent,
  AlertDialogOverlay,
} from "@chakra-ui/react";


interface BackendButtonsProps {
  isLoggedIn: boolean;
}
const BackendButtons = ({isLoggedIn}: BackendButtonsProps) => {
  const { isOpen, onToggle, onClose } = useDisclosure();
  return (
    <Box position="sticky">
      <AbsoluteCenter>
        {isLoggedIn }
        <Button onClick={onToggle} size="lg" colorScheme="teal" mt="5.5rem">
          Get Started
        </Button>
        
        <ScaleFade initialScale={0.9} in={isOpen}>
          <AlertDialog isOpen={isOpen} onClose={onClose}>
            <AlertDialogOverlay>
              <AlertDialogContent>
                <AlertDialogBody>
                  <Flex justifyContent="space-evenly" gap="1rem" p="1rem">
                    <Button colorScheme="blue">Disease Diagnosis</Button>
                    <Button colorScheme="purple">Treatment Plan</Button>
                  </Flex>
                </AlertDialogBody>

                <AlertDialogFooter>
                  <Button colorScheme="red" onClick={onClose}>
                    Cancel
                  </Button>
                </AlertDialogFooter>
              </AlertDialogContent>
            </AlertDialogOverlay>
          </AlertDialog>
        </ScaleFade>
      </AbsoluteCenter>
    </Box>
  );
};

export default BackendButtons;
