import { Grid, GridItem } from "@chakra-ui/react";
import { useState, useEffect } from "react";
//component imports:
import Navbar from "./components/Navbar";
import LandingAnimation from "./components/LandingAnimation";
import Chatbot from "./components/Chatbot";
import AnimatedText from "./components/AnimatedText";

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
          base: `"nav" "left" "right" "footer"`, //Mobile view.
          lg: `"nav nav" "left right" "footer footer"`, //Desktop view.
        }}
        alignItems={"center"}
        gap={3}
      >
        {/*NAVBAR*/}
        <GridItem area={"nav"}>
          <Navbar />
        </GridItem>
        {/*NAVBAR*/}
        {/*ANIMATED TEXT AREA ...*/}
        <GridItem bg="whitesmoke" area={"left"}>
          <AnimatedText />
        </GridItem>
        {/*ANIMATED TEXT AREA ...*/}
        {/*ANIMATION ...*/}
        <GridItem area={"right"}>
          <LandingAnimation />
          <Chatbot />
        </GridItem>
        {/*ANIMATION ...*/}
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
