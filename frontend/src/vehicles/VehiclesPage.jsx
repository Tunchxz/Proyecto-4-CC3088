import { Box, Button } from "@mui/material";
import { useState } from "react";
import VehicleTable from "./components/VehicleTable";
import VehicleFormDialog from "./components/VehicleFormDialog";
import SectionTitle from "../shared/components/SectionTitle";

export default function VehiclesPage() {
    const [openForm, setOpenForm] = useState(false);
    const [editingVehicle, setEditingVehicle] = useState(null);

    const handleEdit = (vehicle) => {
        setEditingVehicle(vehicle);
        setOpenForm(true);
    };

    return (
        <Box p={3}>
            <SectionTitle title="Gestión de Vehículos" />
            <Button variant="contained" onClick={() => setOpenForm(true)}>
                Nuevo Vehículo
            </Button>
            <VehicleTable onEdit={handleEdit} />
            <VehicleFormDialog
                open={openForm}
                onClose={() => {
                    setOpenForm(false);
                    setEditingVehicle(null);
                }}
                vehicle={editingVehicle}
            />
        </Box>
    );
}
