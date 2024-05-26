import {
  VStack,
  Box,
  Text,
  Heading,
  Accordion,
  AccordionItem,
  AccordionButton,
  AccordionPanel,
  AccordionIcon,
} from "@chakra-ui/react";
import { ReactTyped } from "react-typed";

const AnimatedText = () => {
  return (
    <VStack w="70%" padding={5}>
      <Heading as="h1" size="2xl">
        <ReactTyped
          strings={["Experience the Future of Diagnosis with Dr. AI"]}
          typeSpeed={50}
        />
      </Heading>
      <br />
      <Accordion w="100%">
        <AccordionItem>
          <h2>
            <AccordionButton>
              <Box
                as="span"
                flex="1"
                textAlign="left"
                fontSize="xl"
                fontWeight="900"
                color="#8338ec"
              >
                Dr. AI
              </Box>
              <AccordionIcon />
            </AccordionButton>
          </h2>
          <AccordionPanel pb={4}>
            <Text>
              Dr. AI leverages cutting-edge AI and machine learning algorithms
              to analyze medical data with unparalleled accuracy, helping
              healthcare professionals make faster, more informed decisions.
            </Text>
          </AccordionPanel>
        </AccordionItem>

        <AccordionItem>
          <h2>
            <AccordionButton>
              <Box
                as="span"
                flex="1"
                textAlign="left"
                fontSize="xl"
                fontWeight="900"
                color="#8338ec"
              >
                Just for You
              </Box>
              <AccordionIcon />
            </AccordionButton>
          </h2>
          <AccordionPanel pb={4}>
            <Text>
              Access expert-level diagnostics from the comfort of your own home.
              Dr. AI puts the power of medical expertise in your hands.
            </Text>
          </AccordionPanel>
        </AccordionItem>

        <AccordionItem>
          <h2>
            <AccordionButton>
              <Box
                as="span"
                flex="1"
                textAlign="left"
                fontSize="xl"
                fontWeight="900"
                color="#8338ec"
              >
                How we can help
              </Box>
              <AccordionIcon />
            </AccordionButton>
          </h2>
          <AccordionPanel pb={4}>
            <Text>
              Say goodbye to lengthy wait times and uncertain diagnoses. Dr. AI
              provides swift, precise insights for optimal patient care.
            </Text>
          </AccordionPanel>
        </AccordionItem>
      </Accordion>
    </VStack>
  );
};

export default AnimatedText;
