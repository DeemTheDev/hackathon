import { Grid, GridItem } from "@chakra-ui/react";

//component imports:
import Navbar from "./components/Navbar";
import LandingAnimation from "./components/LandingAnimation";
import Chatbot from "./components/Chatbot";
import AnimatedText from "./components/AnimatedText"; //Yash did this.
import Footer from "./components/Footer";

function App() {
  return (
    <>
      <Grid
        templateAreas={{
          base: `"nav" "left" "right" "footer"`, //Mobile view.
          lg: `"nav nav" "left right" "footer footer"`, //Desktop view.
        }}
        gap={3}
      >
        <GridItem area={"nav"}>
          <Navbar />
        </GridItem>
        <GridItem area={"left"}>
          <AnimatedText />
        </GridItem>
        <GridItem area={"right"}>
          <LandingAnimation />
          <Chatbot />
        </GridItem>
        <GridItem area={"footer"}>
          <Footer />
        </GridItem>
      </Grid>
    </>
  );
}

export default App;
