import { Grid, GridItem, Flex } from "@chakra-ui/react";
import { useState, useEffect } from "react";
//component imports:
import Navbar from "./components/Navbar";
import LandingAnimation from "./components/LandingAnimation";
import Chatbot from "./components/Chatbot";
import AnimatedText from "./components/AnimatedText";
import BackendButtons from "./components/BackendButtons";

function App() {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch("/predict")
      .then((res) => res.json())
      .then((data) => {
        setData(data), console.log(data);
      });
  }, []);

  return (
    <>
      <Grid
        templateAreas={{
          base: `"nav" "hero" "footer"`, //Mobile view.
          lg: `"nav nav" "hero hero" "footer footer"`, //Desktop view.
        }}
        alignItems={"center"}
        gap={3}
      >
        {/*NAVBAR*/}
        <GridItem area={"nav"}>
          <Navbar />
        </GridItem>
        {/*NAVBAR*/}
        {/*HERO SECTION ...*/}
        <GridItem area={"hero"}>
          <Flex>
            <AnimatedText />
            <LandingAnimation />
          </Flex>
          <BackendButtons />
          <Chatbot />
        </GridItem>
        {/*HERO SECTION*/}
        {/*FOOTER ...*/}
        <GridItem area={"footer"}>
          {/*Footer goes here with github repo link, and developer names */}
        </GridItem>
        {/*FOOTER ...*/}
      </Grid>
    </>
  );
}

export default App;
