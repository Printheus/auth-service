import {
  Box,
  Button,
  FormControl,
  FormLabel,
  Link,
  styled,
  TextField,
  Typography,
} from "@mui/material";
import MuiCard from "@mui/material/Card";
import { useForm } from "react-hook-form";

interface BasicLoginForm {
  username: string;
  password: string;
}

const Card = styled(MuiCard)(({ theme }) => ({
  display: "flex",
  flexDirection: "column",
  alignSelf: "center",
  width: "100%",
  padding: theme.spacing(4),
  gap: theme.spacing(2),
  boxShadow:
    "hsla(220, 30%, 5%, 0.05) 0px 5px 15px 0px, hsla(220, 25%, 10%, 0.05) 0px 15px 35px -5px",
  [theme.breakpoints.up("sm")]: {
    width: "450px",
  },
  ...theme.applyStyles("dark", {
    boxShadow:
      "hsla(220, 30%, 5%, 0.5) 0px 5px 15px 0px, hsla(220, 25%, 10%, 0.08) 0px 15px 35px -5px",
  }),
}));

export default function SignInCard() {
  const { register, handleSubmit } = useForm<BasicLoginForm>();
  return (
    <Card>
      <Typography
        component="h1"
        variant="h4"
        sx={{ display: "flex", flexDirection: "column", width: "100%", gap: 2 }}
      >
        Sign in
      </Typography>
      <Box
        component="form"
        onSubmit={handleSubmit((data)=>{console.log(data)})}
        sx={{ display: "flex", flexDirection: "column", width: "100%", gap: 2 }}
      >
        <FormControl>
          <TextField
            {...register("username")}
            label="username"
            variant="standard"
            required
            autoFocus
            fullWidth
          />
        </FormControl>
        <FormControl>
          <TextField
            {...register("password")}
            label="password"
            variant="standard"
            type="password"
            id="password"
            required
            fullWidth
          />
        </FormControl>
        <Button type="submit" fullWidth variant="contained">
          Sign in
        </Button>
        <Typography sx={{ textAlign: "center" }}>
          Don&apos;t have an account?{" "}
          <span>
            <Link
              href="/material-ui/getting-started/templates/sign-in/"
              variant="body2"
              sx={{ alignSelf: "center" }}
            >
              Sign up
            </Link>
          </span>
        </Typography>
      </Box>
    </Card>
  );
}
