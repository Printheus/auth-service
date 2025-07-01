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
import { useSearchParams } from "react-router-dom";

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
  const [searchParams] = useSearchParams();
  const { register, handleSubmit } = useForm<BasicLoginForm>();
  const [msg, setMsg] = useState("");
  const [open, setOpen] = useState(false);
  const [isError, setIsError] = useState(true);
  const onSubmit = (data: BasicLoginForm) => {
    const request = apiClient.post("/login", data, {  withCredentials: true});
    request
      .then((res) => {
        console.log(res);
        setIsError(false)
        setMsg("Signed in")
        setOpen(true)
        
        const redirectUrl = searchParams.get('redirect');
        setTimeout(() => {
          if (redirectUrl) {
            window.location.href = redirectUrl;
          }
          else{
            window.location.href = import.meta.env.VITE_API_DASHBOARD_URL;
          }
        }, 2000); // 2 seconds
      
      })
      .catch((err) => {
        if (axios.isAxiosError(err)) {
          if (err.response) {
            setMsg(err.response.data.detail);
          } else if (err.request) {
            setMsg("Network error. Please check your connection.");
          } else {
            setMsg("An unexpected error occurred.");
          }
        } else {
          setMsg("An unexpected error occurred.");
        }
        setIsError(true)
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
          severity={isError? "error": "success"}
          variant="filled"
          sx={{ width: "100%" }}
        >
          {msg}
        </Alert>
      </Snackbar>
    </Card>
  );
}
