import Stack from "@mui/material/Stack";
import Content from "../temp/SignInSide/components/Content";
import SignInCard from "./SignInCard";


function SignIn() {


  return (
    <Stack
      direction={"column"}
      component={"main"}
      sx={[
        {
          justifyContent: "center",
          height: "calc((1 - var(--template-frame-height, 0)) * 100%)",
          marginTop: "max(40px - var(--template-frame-height, 0px), 0px)",
          minHeight: "100%",
        },          
        () => ({
            '&::before': {
                content: '""',
                display: 'block',
              position: 'absolute',
              zIndex: -1,
              inset: 0,
              backgroundImage:
              'radial-gradient(ellipse at 50% 50%, hsl(210, 100%, 97%), hsl(0, 0%, 100%))',
              backgroundRepeat: 'no-repeat',
            },
        })

      ]}
    >
      <Stack
        direction={{ xs: "column-reverse", md: "row" }}
        sx={{
          justifyContent: "center",
          gap: { xs: 6, sm: 12 },
          p: { xs: 2, sm: 4 },
          m: "auto",
        }}
      >
        <Content />
        <SignInCard />
      </Stack>
    </Stack>
  );
}

export default SignIn;
