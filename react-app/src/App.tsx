import { Grid, GridItem } from "@chakra-ui/react";

//component imports:
import Navbar from "./components/Navbar";
import LandingAnimation from "./components/LandingAnimation";
import Chatbot from "./components/Chatbot";

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
        <GridItem area={"left"}>{/*Animated Text goes here ...*/}</GridItem>
        <GridItem area={"right"}>
          <LandingAnimation />
          <Chatbot />
        </GridItem>
        <GridItem area={"footer"}>
          {/*Footer goes here with github repo link, and developer names */}
        </GridItem>
      </Grid>
    </>
  );
}

export default App;
