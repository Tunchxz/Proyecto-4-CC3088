import { Dialog, DialogTitle, DialogActions, Button } from "@mui/material";
import axiosInstance from "../../shared/api/axiosInstance";

export default function ReservationDeleteDialog({ reservation, onClose }) {
    if (!reservation) return null;

    const handleDelete = async () => {
        await axiosInstance.delete(`/reservations/${reservation.id}`);
        onClose();
    };

    return (
        <Dialog open={Boolean(reservation)} onClose={onClose}>
            <DialogTitle>¿Eliminar reserva #{reservation.id}?</DialogTitle>
            <DialogActions>
                <Button onClick={onClose}>Cancelar</Button>
                <Button color="error" onClick={handleDelete}>Eliminar</Button>
            </DialogActions>
        </Dialog>
    );
}
