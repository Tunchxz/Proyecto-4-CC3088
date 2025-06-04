import { Box, Grid, TextField, Button } from "@mui/material";
import { useState } from "react";
import axiosInstance from "../shared/api/axiosInstance";
import SectionTitle from "../shared/components/SectionTitle";
import ReportTable from "./components/ReportTable";
import ExportCSVButton from "./components/ExportCSVButton";

export default function MaintenanceReport() {
    const [filters, setFilters] = useState({});
    const [data, setData] = useState([]);

    const fetchData = async () => {
        const res = await axiosInstance.get("/analytics/maintenance", { params: filters });
        setData(res.data);
    };

    const handleChange = (e) => {
        setFilters({ ...filters, [e.target.name]: e.target.value });
    };

    const fields = ["car_plate", "min_cost", "max_cost", "from_date", "to_date"];

    return (
        <Box p={3}>
            <SectionTitle title="Reporte de Mantenimientos" />
            <Grid container spacing={2} mb={2}>
                {fields.map(f => (
                    <Grid item xs={12} sm={6} md={2.4} key={f}>
                        <TextField
                            fullWidth
                            label={f.replace(/_/g, ' ')}
                            name={f}
                            type={f.includes("date") ? "date" : "number"}
                            InputLabelProps={{ shrink: true }}
                            value={filters[f] || ''}
                            onChange={handleChange}
                        />
                    </Grid>
                ))}
                <Grid item xs={12}>
                    <Button onClick={fetchData} variant="contained">Buscar</Button>
                    <ExportCSVButton data={data} fileName="mantenimientos" />
                </Grid>
            </Grid>
            <ReportTable
                data={data}
                columns={["car_plate", "maintenance_date", "description", "cost"]}
            />
        </Box>
    );
}
