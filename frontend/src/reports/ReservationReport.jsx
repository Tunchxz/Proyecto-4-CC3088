import { Box, Grid, TextField, Button } from "@mui/material";
import { useState } from "react";
import axiosInstance from "../shared/api/axiosInstance";
import SectionTitle from "../shared/components/SectionTitle";
import ReportTable from "./components/ReportTable";
import ExportCSVButton from "./components/ExportCSVButton";

export default function ReservationReport() {
    const [filters, setFilters] = useState({});
    const [data, setData] = useState([]);

    const fetchData = async () => {
        const res = await axiosInstance.get("/analytics/reservations", { params: filters });
        setData(res.data);
    };

    const handleChange = (e) => {
        setFilters({ ...filters, [e.target.name]: e.target.value });
    };

    return (
        <Box p={3}>
            <SectionTitle title="Reporte de Reservas" />
            <Grid container spacing={2} mb={2}>
                {['from_date', 'to_date', 'status', 'customer_name', 'car_plate'].map(f => (
                    <Grid item xs={12} sm={6} md={2.4} key={f}>
                        <TextField
                            fullWidth
                            label={f.replace(/_/g, ' ')}
                            name={f}
                            type={f.includes('date') ? 'date' : 'text'}
                            InputLabelProps={{ shrink: true }}
                            value={filters[f] || ''}
                            onChange={handleChange}
                        />
                    </Grid>
                ))}
                <Grid item xs={12}>
                    <Button onClick={fetchData} variant="contained">Buscar</Button>
                    <ExportCSVButton data={data} fileName="reservas" />
                </Grid>
            </Grid>
            <ReportTable data={data} columns={["reservation_id", "customer_name", "car_plate", "start_date", "end_date", "reservation_status"]} />
        </Box>
    );
}
