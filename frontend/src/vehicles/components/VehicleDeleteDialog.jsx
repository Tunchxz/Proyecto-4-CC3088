import { Dialog, DialogTitle, DialogActions, Button } from "@mui/material";
import axiosInstance from "../../shared/api/axiosInstance";

export default function VehicleDeleteDialog({ vehicle, onClose }) {
    if (!vehicle) return null;

    const handleDelete = async () => {
        await axiosInstance.delete(`/vehicles/${vehicle.id}`);
        onClose();
    };

    return (
        <Dialog open={Boolean(vehicle)} onClose={onClose}>
            <DialogTitle>¿Eliminar vehículo con placa {vehicle.car_plate}?</DialogTitle>
            <DialogActions>
                <Button onClick={onClose}>Cancelar</Button>
                <Button color="error" onClick={handleDelete}>Eliminar</Button>
            </DialogActions>
        </Dialog>
    );
}
