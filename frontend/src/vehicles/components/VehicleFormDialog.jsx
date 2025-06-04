import {
    Dialog, DialogTitle, DialogContent, DialogActions,
    TextField, Button, Grid
} from "@mui/material";
import { useState, useEffect } from "react";
import axiosInstance from "../../shared/api/axiosInstance";

export default function VehicleFormDialog({ open, onClose, vehicle }) {
    const [form, setForm] = useState({});

    useEffect(() => {
        setForm(vehicle || {});
    }, [vehicle]);

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async () => {
        if (vehicle?.id) {
            await axiosInstance.put(`/vehicles/${vehicle.id}`, form);
        } else {
            await axiosInstance.post("/vehicles", form);
        }
        onClose();
    };

    return (
        <Dialog open={open} onClose={onClose}>
            <DialogTitle>{vehicle ? "Editar Vehículo" : "Nuevo Vehículo"}</DialogTitle>
            <DialogContent>
                <Grid container spacing={2} mt={1}>
                    <Grid item xs={12}>
                        <TextField fullWidth label="Placa" name="car_plate" value={form.car_plate || ""} onChange={handleChange} />
                    </Grid>
                    <Grid item xs={12}>
                        <TextField fullWidth label="Kilometraje" type="number" name="mileage" value={form.mileage || ""} onChange={handleChange} />
                    </Grid>
                    <Grid item xs={12}>
                        <TextField fullWidth label="Estado ID" type="number" name="status_id" value={form.status_id || ""} onChange={handleChange} />
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
