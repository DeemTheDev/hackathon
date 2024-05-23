import {
  VStack,
  Box,
  Text,
  Button,
  Divider,
  ScaleFade,
  useDisclosure,
  Heading,
  Accordion,
  AccordionItem,
  AccordionButton,
  AccordionPanel,
  AccordionIcon,
} from "@chakra-ui/react";
import { ReactTyped } from "react-typed";

const AnimatedText = () => {
  const { isOpen, onToggle } = useDisclosure();
  return (
    <VStack w={"48%"} padding={5}>
      <Heading as="h1" size="xl">
        <ReactTyped
          strings={["Experience the Future of Diagnosis with Dr. AI"]}
          typeSpeed={100}
        />
      </Heading>
      <Divider />
      <Accordion w="55%">
        <AccordionItem>
          <h2>
            <AccordionButton>
              <Box as="span" flex="1" textAlign="left">
                Section 1 title
              </Box>
              <AccordionIcon />
            </AccordionButton>
          </h2>
          <AccordionPanel pb={4}>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat.
          </AccordionPanel>
        </AccordionItem>

        <AccordionItem>
          <h2>
            <AccordionButton>
              <Box as="span" flex="1" textAlign="left">
                Section 2 title
              </Box>
              <AccordionIcon />
            </AccordionButton>
          </h2>
          <AccordionPanel pb={4}>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat.
          </AccordionPanel>
        </AccordionItem>
      </Accordion>
      <Button float={"left"} onClick={onToggle}>
        View more
      </Button>
      <ScaleFade initialScale={0.9} in={isOpen}>
        <Box
          width="100%"
          p="40px"
          color="white"
          mt="4"
          bg="teal.500"
          rounded="md"
          shadow="md"
        >
          Fade idk
        </Box>
      </ScaleFade>
    </VStack>
  );
};

export default AnimatedText;
