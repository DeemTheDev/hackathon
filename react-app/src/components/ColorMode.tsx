import { HStack, IconButton, useColorMode } from "@chakra-ui/react";
import { SunIcon, MoonIcon } from "@chakra-ui/icons"; // Import MoonIcon

const ColorMode = () => {
  const { toggleColorMode, colorMode } = useColorMode();

  const handleToggleColorMode = () => {
    toggleColorMode();
  };

  return (
    <HStack>
      <IconButton
        onClick={handleToggleColorMode}
        aria-label="Toggle Color Mode" // Corrected aria-label
        icon={colorMode === "light" ? <SunIcon /> : <MoonIcon />} // Conditional icon
      />
    </HStack>
  );
};

export default ColorMode;
