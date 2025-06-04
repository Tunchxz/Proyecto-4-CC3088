import {
    Dialog, DialogTitle, DialogContent, DialogActions,
    TextField, Button, Grid
} from "@mui/material";
import { useState, useEffect } from "react";
import axiosInstance from "../../shared/api/axiosInstance";

export default function ReservationFormDialog({ open, onClose, reservation }) {
    const [form, setForm] = useState({});

    useEffect(() => {
        setForm(reservation || {});
    }, [reservation]);

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async () => {
        if (reservation?.id) {
            await axiosInstance.put(`/reservations/${reservation.id}`, form);
        } else {
            await axiosInstance.post("/reservations", form);
        }
        onClose();
    };

    return (
        <Dialog open={open} onClose={onClose}>
            <DialogTitle>{reservation ? "Editar Reserva" : "Nueva Reserva"}</DialogTitle>
            <DialogContent>
                <Grid container spacing={2} mt={1}>
                    <Grid item xs={12}>
                        <TextField fullWidth label="Cliente ID" name="customer_id" value={form.customer_id || ""} onChange={handleChange} />
                    </Grid>
                    <Grid item xs={12}>
                        <TextField fullWidth label="Vehículo ID" name="vehicle_id" value={form.vehicle_id || ""} onChange={handleChange} />
                    </Grid>
                    <Grid item xs={6}>
                        <TextField fullWidth label="Fecha inicio" type="date" name="start_date" value={form.start_date || ""} onChange={handleChange} InputLabelProps={{ shrink: true }} />
                    </Grid>
                    <Grid item xs={6}>
                        <TextField fullWidth label="Fecha fin" type="date" name="end_date" value={form.end_date || ""} onChange={handleChange} InputLabelProps={{ shrink: true }} />
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
