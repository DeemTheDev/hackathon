import {
  Center,
  Image,
  Text,
  Stack,
  Divider,
  Button,
  Box,
  Heading,
  Card,
  CardBody,
  CardFooter,
} from "@chakra-ui/react";

const FooterContent = () => {
  return (
    <Box mt="3rem">
      <Center>
        <Heading>Developers </Heading>
      </Center>
      <br />
      <Card maxW="xs">
        <CardBody>
          <Image
            src="https://images.unsplash.com/photo-1555041469-a586c61ea9bc?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80"
            borderRadius="lg"
          />
          <Stack mt="6" spacing="3">
            <Heading size="md">Nadeem Mohammed</Heading>

            <Text color="blue.600" fontSize="2xl">
              Team Leader
            </Text>
          </Stack>
        </CardBody>
        <Divider />
        <CardFooter>
          <Button variant="solid" colorScheme="teal">
            GitHub
          </Button>
        </CardFooter>
      </Card>
    </Box>
  );
};

export default FooterContent;
