import { Typography } from "@mui/material";

export default function SectionTitle({ title }) {
    return (
        <Typography variant="h5" sx={{ mb: 2 }}>
            {title}
        </Typography>
    );
}
