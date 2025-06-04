import { Box, Button } from "@mui/material";
import { useState } from "react";
import ReservationTable from "./components/ReservationTable";
import ReservationFormDialog from "./components/ReservationFormDialog";
import SectionTitle from "../shared/components/SectionTitle";

export default function ReservationsPage() {
    const [openForm, setOpenForm] = useState(false);
    const [editingReservation, setEditingReservation] = useState(null);

    const handleEdit = (reservation) => {
        setEditingReservation(reservation);
        setOpenForm(true);
    };

    return (
        <Box p={3}>
            <SectionTitle title="Gestión de Reservas" />
            <Button variant="contained" onClick={() => setOpenForm(true)}>
                Nueva Reserva
            </Button>
            <ReservationTable onEdit={handleEdit} />
            <ReservationFormDialog
                open={openForm}
                onClose={() => {
                    setOpenForm(false);
                    setEditingReservation(null);
                }}
                reservation={editingReservation}
            />
        </Box>
    );
}
