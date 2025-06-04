import {
    Dialog, DialogTitle, DialogContent, DialogActions,
    TextField, Button, Grid
} from "@mui/material";
import { useState, useEffect } from "react";
import axiosInstance from "../../shared/api/axiosInstance";

export default function CustomerFormDialog({ open, onClose, customer }) {
    const [form, setForm] = useState({});

    useEffect(() => {
        setForm(customer || {});
    }, [customer]);

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async () => {
        if (customer?.id) {
            await axiosInstance.put(`/customers/${customer.id}`, form);
        } else {
            await axiosInstance.post("/customers", form);
        }
        onClose();
    };

    return (
        <Dialog open={open} onClose={onClose}>
            <DialogTitle>{customer ? "Editar Cliente" : "Nuevo Cliente"}</DialogTitle>
            <DialogContent>
                <Grid container spacing={2} mt={1}>
                    <Grid item xs={6}>
                        <TextField fullWidth label="Nombre" name="first_name" value={form.first_name || ""} onChange={handleChange} />
                    </Grid>
                    <Grid item xs={6}>
                        <TextField fullWidth label="Apellido" name="last_name" value={form.last_name || ""} onChange={handleChange} />
                    </Grid>
                    <Grid item xs={12}>
                        <TextField fullWidth label="Email" name="email" value={form.email || ""} onChange={handleChange} />
                    </Grid>
                    <Grid item xs={12}>
                        <TextField fullWidth label="Teléfono" name="phone_number" value={form.phone_number || ""} onChange={handleChange} />
                    </Grid>
                </Grid>
            </DialogContent>
            <DialogActions>
                <Button onClick={onClose}>Cancelar</Button>
                <Button onClick={handleSubmit} variant="contained">Guardar</Button>
            </DialogActions>
        </Dialog>
    );
}
