import {
    Table, TableHead, TableRow, TableCell,
    TableBody, IconButton
} from "@mui/material";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";
import { useReservations } from "../hooks/useReservations";
import ReservationDeleteDialog from "./ReservationDeleteDialog";
import { useState } from "react";

export default function ReservationTable({ onEdit }) {
    const { reservations, refresh } = useReservations();
    const [toDelete, setToDelete] = useState(null);

    return (
        <>
            <Table sx={{ mt: 2 }}>
                <TableHead>
                    <TableRow>
                        <TableCell>ID</TableCell>
                        <TableCell>Cliente</TableCell>
                        <TableCell>Vehículo</TableCell>
                        <TableCell>Fechas</TableCell>
                        <TableCell>Acciones</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {reservations.map((r) => (
                        <TableRow key={r.id}>
                            <TableCell>{r.id}</TableCell>
                            <TableCell>{r.customer_id}</TableCell>
                            <TableCell>{r.vehicle_id}</TableCell>
                            <TableCell>{r.start_date} a {r.end_date}</TableCell>
                            <TableCell>
                                <IconButton onClick={() => onEdit(r)}><EditIcon /></IconButton>
                                <IconButton onClick={() => setToDelete(r)}><DeleteIcon /></IconButton>
                            </TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
            <ReservationDeleteDialog
                reservation={toDelete}
                onClose={() => {
                    setToDelete(null);
                    refresh();
                }}
            />
        </>
    );
}
