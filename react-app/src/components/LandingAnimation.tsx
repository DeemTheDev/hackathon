import { Box, VStack, Divider, Flex } from "@chakra-ui/react";
//Lottie animation import
import Lottie from "lottie-react";
//animation import
import animation from "../assets/animation2.json";

const LandingAnimation = () => {
  return (
    <>
      <Flex>
        <Divider orientation="vertical" h="350px" float="left" ml="7rem" />
        <VStack>
          <Box w="55%">
            <Lottie animationData={animation} loop={true} />
          </Box>
        </VStack>
      </Flex>
    </>
  );
};

export default LandingAnimation;
