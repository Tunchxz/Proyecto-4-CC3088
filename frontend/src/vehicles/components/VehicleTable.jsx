import {
    Table, TableHead, TableRow, TableCell,
    TableBody, IconButton
} from "@mui/material";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";
import { useVehicles } from "../hooks/useVehicles";
import VehicleDeleteDialog from "./VehicleDeleteDialog";
import { useState } from "react";

export default function VehicleTable({ onEdit }) {
    const { vehicles, refresh } = useVehicles();
    const [toDelete, setToDelete] = useState(null);

    return (
        <>
            <Table sx={{ mt: 2 }}>
                <TableHead>
                    <TableRow>
                        <TableCell>Placa</TableCell>
                        <TableCell>Kilometraje</TableCell>
                        <TableCell>Estado</TableCell>
                        <TableCell>Acciones</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {vehicles.map((v) => (
                        <TableRow key={v.id}>
                            <TableCell>{v.car_plate}</TableCell>
                            <TableCell>{v.mileage} km</TableCell>
                            <TableCell>{v.status_id}</TableCell>
                            <TableCell>
                                <IconButton onClick={() => onEdit(v)}><EditIcon /></IconButton>
                                <IconButton onClick={() => setToDelete(v)}><DeleteIcon /></IconButton>
                            </TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
            <VehicleDeleteDialog
                vehicle={toDelete}
                onClose={() => {
                    setToDelete(null);
                    refresh();
                }}
            />
        </>
    );
}
