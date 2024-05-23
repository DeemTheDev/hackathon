import { Center, VStack, Divider, Flex } from "@chakra-ui/react";
//Lottie animation import
import Lottie from "lottie-react";
//animation import
import animation from "../assets/main-animation.json";

const LandingAnimation = () => {
  return (
    <>
      <Flex>
        <Divider orientation="vertical" h="400px" float="left" />
        <VStack>
          <Center>
            <Lottie animationData={animation} loop={true} />
          </Center>
        </VStack>
      </Flex>
    </>
  );
};

export default LandingAnimation;
