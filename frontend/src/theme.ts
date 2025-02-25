import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    primary: {
      main: "#007BFF", // Electric Blue (Technology, Innovation)
      contrastText: "#FFFFFF",
    },
    secondary: {
      main: "#FF6F00", // Fiery Orange (Prometheus' Fire, Energy)
      contrastText: "#FFFFFF",
    },
    background: {
      default: "#F4F4F4", // Cloud White (Clean, Minimal)
      paper: "#FFFFFF",
    },
    text: {
      primary: "#2C2C2C", // Charcoal Black (Readability)
      secondary: "#00A896", // Teal Green (Fresh, Accessible)
    },
    warning: {
      main: "#FFC107", // Gold (Premium, Highlight Color)
    },
  },
  typography: {
    fontFamily: "'Inter', 'Roboto', 'Arial', sans-serif",
    h1: {
      fontSize: "2.5rem",
      fontWeight: 700,
      color: "#2C2C2C",
    },
    h2: {
      fontSize: "2rem",
      fontWeight: 600,
      color: "#2C2C2C",
    },
    body1: {
      fontSize: "1rem",
      color: "#2C2C2C",
    },
    button: {
      textTransform: "none",
      fontWeight: 600,
    },
  },
  shape: {
    borderRadius: 12,
  },
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: 8,
          padding: "10px 16px",
          fontWeight: 600,
        },
      },
    },
    MuiCard: {
      styleOverrides: {
        root: {
          borderRadius: 16,
          boxShadow: "0px 4px 10px rgba(0,0,0,0.1)",
        },
      },
    },
  },
});

export default theme;
