import {
    Table, TableHead, TableRow,
    TableCell, TableBody
} from "@mui/material";

export default function ReportTable({ data, columns }) {
    return (
        <Table sx={{ mt: 2 }}>
            <TableHead>
                <TableRow>
                    {columns.map((col) => (
                        <TableCell key={col}><strong>{col.replace(/_/g, ' ')}</strong></TableCell>
                    ))}
                </TableRow>
            </TableHead>
            <TableBody>
                {data.map((row, i) => (
                    <TableRow key={i}>
                        {columns.map((col) => (
                            <TableCell key={col}>{row[col]}</TableCell>
                        ))}
                    </TableRow>
                ))}
            </TableBody>
        </Table>
    );
}
