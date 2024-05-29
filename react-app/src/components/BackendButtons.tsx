import React, {
  Box,
  Flex,
  Link,
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
const BackendButtons = () => {
  const { isOpen, onOpen, onToggle, onClose } = useDisclosure();
  return (
    <Box position="sticky">
      <AbsoluteCenter>
        <Button onClick={onToggle} size="lg" colorScheme="teal" mt="5.5rem">
          Get Started
        </Button>
        <ScaleFade initialScale={0.9} in={isOpen}>
          <AlertDialog isOpen={isOpen} onClose={onClose}>
            <AlertDialogOverlay>
              <AlertDialogContent>
                <AlertDialogBody>
                  <Flex justifyContent="space-evenly" gap="1rem" p="1rem">
                    <Button colorScheme="blue">
                      <Link
                        href="http://localhost:8501"
                        style={{ textDecoration: "none" }}
                      >
                        Take Diagnosis
                      </Link>
                    </Button>
                    <Button colorScheme="purple">
                      <Link
                        href="http://localhost:8502"
                        style={{ textDecoration: "none" }}
                      >
                        Take Treatment
                      </Link>
                    </Button>
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
