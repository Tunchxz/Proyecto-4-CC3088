import { Box } from "@mui/material";
import NavDrawer from "./NavDrawer";
import { Outlet } from "react-router";

export default function DashboardLayout() {
    return (
        <Box display="flex">
            <NavDrawer />
            <Box component="main" flexGrow={1} p={3} sx={{ bgcolor: "#f5f5f5", minHeight: "100vh" }}>
                <Outlet />
            </Box>
        </Box>
    );
}
