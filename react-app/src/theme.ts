
import { extendTheme, ThemeConfig } from '@chakra-ui/react'


const config: ThemeConfig = {
  initialColorMode: 'dark',
}

// 3. extend the theme
const theme = extendTheme({ config })

export default theme