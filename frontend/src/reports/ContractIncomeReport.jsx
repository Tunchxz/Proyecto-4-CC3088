import { Box, Grid, TextField, Button } from "@mui/material";
import { useState } from "react";
import axiosInstance from "../shared/api/axiosInstance";
import SectionTitle from "../shared/components/SectionTitle";
import ReportTable from "./components/ReportTable";
import ExportCSVButton from "./components/ExportCSVButton";

export default function ContractIncomeReport() {
    const [filters, setFilters] = useState({});
    const [data, setData] = useState([]);

    const fetchData = async () => {
        const res = await axiosInstance.get("/analytics/contracts/income", { params: filters });
        setData(res.data);
    };

    const handleChange = (e) => {
        setFilters({ ...filters, [e.target.name]: e.target.value });
    };

    const fields = [
        "contract_id", "min_total_income", "max_total_income",
        "min_fines", "max_fines"
    ];

    return (
        <Box p={3}>
            <SectionTitle title="Reporte de Ingresos por Contrato" />
            <Grid container spacing={2} mb={2}>
                {fields.map(f => (
                    <Grid item xs={12} sm={6} md={2.4} key={f}>
                        <TextField
                            fullWidth
                            label={f.replace(/_/g, ' ')}
                            name={f}
                            type="number"
                            InputLabelProps={{ shrink: true }}
                            value={filters[f] || ''}
                            onChange={handleChange}
                        />
                    </Grid>
                ))}
                <Grid item xs={12}>
                    <Button onClick={fetchData} variant="contained">Buscar</Button>
                    <ExportCSVButton data={data} fileName="ingresos_contrato" />
                </Grid>
            </Grid>
            <ReportTable
                data={data}
                columns={["contract_id", "total_payments", "total_fines", "total_income"]}
            />
        </Box>
    );
}
