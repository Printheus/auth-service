// pages/Home.tsx
import {
  Box,
  Container,
  Typography,
  Button,
  Card,
  CardContent,
  CardHeader,
  Stack,
  Divider,
} from '@mui/material';
import PrintIcon from '@mui/icons-material/Print';
import UploadFileIcon from '@mui/icons-material/UploadFile';
import LocationOnIcon from '@mui/icons-material/LocationOn';
import SchoolIcon from '@mui/icons-material/School';
import { useNavigate } from 'react-router-dom';

export default function Home() {
  const navigate = useNavigate();

  const features = [
    {
      title: 'Easy File Upload',
      description: 'Drag and drop from your laptop or phone. We support PDFs, DOCs, even Google Docs.',
      icon: <UploadFileIcon fontSize="large" color="primary" />,
    },
    {
      title: 'Smart Campus Pickup',
      description: 'We’re right where you are — in your library, student union, or dorm hub.',
      icon: <LocationOnIcon fontSize="large" color="primary" />,
    },
    {
      title: 'Made for Students',
      description: 'No subscriptions. Just a fast way to print exactly what you need — when you need it.',
      icon: <SchoolIcon fontSize="large" color="primary" />,
    },
  ];

  return (
    <Container maxWidth="lg" sx={{ py: { xs: 4, md: 6 } }}>
      {/* Hero Section */}
      <Box textAlign="center" mb={8}>
        <PrintIcon sx={{ fontSize: 60, color: 'primary.main' }} />
        <Typography variant="h3" fontWeight={700} gutterBottom>
          Printheus
        </Typography>
        <Typography variant="h6" color="text.secondary" mb={3}>
          Print smarter, not harder. Upload your docs and pick them up on campus — no lines, no stress.
        </Typography>
        <Button variant="contained" size="large" onClick={() => navigate('/auth')}>
          Get Started
        </Button>
      </Box>

      {/* Features without Grid */}
      <Box
        display="flex"
        flexDirection={{ xs: 'column', sm: 'row' }}
        flexWrap="wrap"
        justifyContent="center"
        gap={4}
        mb={10}
      >
        {features.map((feature, idx) => (
          <Card
            key={idx}
            sx={{
              width: 300,
              textAlign: 'center',
              p: 2,
              flexShrink: 0,
            }}
          >
            <Box mb={2}>{feature.icon}</Box>
            <CardHeader
              title={feature.title}
              titleTypographyProps={{ fontWeight: 600 }}
            />
            <CardContent>
              <Typography color="text.secondary">{feature.description}</Typography>
            </CardContent>
          </Card>
        ))}
      </Box>

      {/* How it Works */}
      <Box mt={10}>
        <Typography variant="h5" fontWeight={700} gutterBottom textAlign="center">
          How It Works
        </Typography>
        <Stack spacing={3} mt={3} divider={<Divider flexItem />} sx={{ maxWidth: 600, mx: 'auto', textAlign: 'center' }}>
          <Typography>1. Upload your file</Typography>
          <Typography>2. Choose your pickup location</Typography>
          <Typography>3. Print & receive a QR code</Typography>
          <Typography>4. Scan at the machine & grab your doc</Typography>
        </Stack>
      </Box>

      {/* Testimonial */}
      {/* <Box mt={10} textAlign="center">
        <Typography variant="h6" fontStyle="italic" color="text.secondary" gutterBottom>
          “I printed my final report during lunch — no waiting in line!”
        </Typography>
        <Typography variant="body2">— Sara K., Biology Major</Typography>
      </Box> */}

      {/* Footer */}
      <Box mt={10} textAlign="center" py={4}>
        <Typography variant="subtitle2" color="text.secondary">
          &copy; {new Date().getFullYear()} Printheus. All rights reserved.
        </Typography>
        <Typography variant="caption" color="text.secondary">
          Contact · FAQ · Instagram
        </Typography>
      </Box>
    </Container>
  );
}