import { Button } from "@mui/material";
import Papa from "papaparse";

export default function ExportCSVButton({ data, fileName = 'reporte' }) {
    const handleExport = () => {
        const csv = Papa.unparse(data);
        const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
        const url = URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", `${fileName}.csv`);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    };

    return (
        <Button onClick={handleExport} sx={{ ml: 2 }}>
            Exportar CSV
        </Button>
    );
}
