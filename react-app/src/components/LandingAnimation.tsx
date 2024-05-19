import { Center, VStack } from "@chakra-ui/react";
//Lottie animation import
import Lottie from "lottie-react";
//animation import
import animation from "../assets/main-animation.json";

const LandingAnimation = () => {
  return (
    <VStack w={"100%"}>
      <Center>
        <Lottie animationData={animation} loop={true} />
      </Center>
    </VStack>
  );
};

export default LandingAnimation;
