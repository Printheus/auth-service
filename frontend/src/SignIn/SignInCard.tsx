import {
  Alert,
  Box,
  Button,
  FormControl,
  Link,
  Snackbar,
  styled,
  TextField,
  Typography,
} from "@mui/material";
import MuiCard from "@mui/material/Card";
import { useForm } from "react-hook-form";
import apiClient from "../service/api-client";
import { useState } from "react";
import axios from "axios";

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
  const [error, setError] = useState("");
  const [open, setOpen] = useState(false);
  const onSubmit = (data: BasicLoginForm) => {
    const request = apiClient.post("/login", data);
    request
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        if (axios.isAxiosError(err)) {
          if (err.response) {
            setError(err.response.data.detail);
          } else if (err.request) {
            setError("Network error. Please check your connection.");
          } else {
            setError("An unexpected error occurred.");
          }
        } else {
          setError("An unexpected error occurred.");
        }
        setOpen(true);
        console.log(err);
      });
  };
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
        onSubmit={handleSubmit(onSubmit)}
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
              href="/sign-up"
              variant="body2"
              sx={{ alignSelf: "center" }}
            >
              Sign up
            </Link>
          </span>
        </Typography>
      </Box>
      <Snackbar
        open={open}
        autoHideDuration={6000}
        onClose={() => {
          setOpen(false);
        }}
        anchorOrigin={{ vertical: "bottom", horizontal: "left" }}
      >
        <Alert
          onClose={()=>{setOpen(false)}}
          severity="error"
          variant="filled"
          sx={{ width: "100%" }}
        >
          {error}
        </Alert>
      </Snackbar>
    </Card>
  );
}
