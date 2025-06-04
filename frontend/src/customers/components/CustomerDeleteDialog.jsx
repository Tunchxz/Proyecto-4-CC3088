import { Dialog, DialogTitle, DialogActions, Button } from "@mui/material";
import axiosInstance from "../../shared/api/axiosInstance";

export default function CustomerDeleteDialog({ customer, onClose }) {
    if (!customer) return null;

    const handleDelete = async () => {
        await axiosInstance.delete(`/customers/${customer.id}`);
        onClose();
    };

    return (
        <Dialog open={Boolean(customer)} onClose={onClose}>
            <DialogTitle>¿Eliminar a {customer.first_name} {customer.last_name}?</DialogTitle>
            <DialogActions>
                <Button onClick={onClose}>Cancelar</Button>
                <Button color="error" onClick={handleDelete}>Eliminar</Button>
            </DialogActions>
        </Dialog>
    );
}
