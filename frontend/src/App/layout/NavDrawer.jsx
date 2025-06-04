import {
    Drawer, List, ListItemButton, ListItemIcon, ListItemText, Divider, Typography
} from "@mui/material";
import PeopleIcon from "@mui/icons-material/People";
import DirectionsCarIcon from "@mui/icons-material/DirectionsCar";
import EventNoteIcon from "@mui/icons-material/EventNote";
import AssessmentIcon from "@mui/icons-material/Assessment";
import { useNavigate, useLocation } from "react-router";

const sections = [
    {
        title: "CRUD",
        items: [
            { label: "Clientes", path: "/customers", icon: <PeopleIcon /> },
            { label: "Vehículos", path: "/vehicles", icon: <DirectionsCarIcon /> },
            { label: "Reservas", path: "/reservations", icon: <EventNoteIcon /> }
        ]
    },
    {
        title: "Reportes",
        items: [
            { label: "Reservas", path: "/reports/reservations", icon: <AssessmentIcon /> },
            { label: "Mantenimientos", path: "/reports/maintenance", icon: <AssessmentIcon /> },
            { label: "Ingresos por Contrato", path: "/reports/contracts", icon: <AssessmentIcon /> }
        ]
    }
];

export default function NavDrawer() {
    const navigate = useNavigate();
    const location = useLocation();

    return (
        <Drawer variant="permanent" anchor="left" sx={{ width: 250, [`& .MuiDrawer-paper`]: { width: 250 } }}>
            {sections.map((section, i) => (
                <div key={i}>
                    <Typography variant="subtitle2" sx={{ px: 2, py: 1, color: "gray" }}>{section.title}</Typography>
                    <List>
                        {section.items.map(({ label, path, icon }) => (
                            <ListItemButton
                                key={path}
                                selected={location.pathname === path}
                                onClick={() => navigate(path)}
                            >
                                <ListItemIcon>{icon}</ListItemIcon>
                                <ListItemText primary={label} />
                            </ListItemButton>
                        ))}
                    </List>
                    <Divider />
                </div>
            ))}
        </Drawer>
    );
}
