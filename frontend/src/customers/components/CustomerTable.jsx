import {
    Table, TableHead, TableRow, TableCell,
    TableBody, IconButton
} from "@mui/material";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";
import { useCustomers } from "../hooks/useCustomers";
import CustomerDeleteDialog from "./CustomerDeleteDialog";
import { useState } from "react";

export default function CustomerTable({ onEdit }) {
    const { customers, refresh } = useCustomers();
    const [toDelete, setToDelete] = useState(null);

    return (
        <>
            <Table sx={{ mt: 2 }}>
                <TableHead>
                    <TableRow>
                        <TableCell>Nombre</TableCell>
                        <TableCell>Email</TableCell>
                        <TableCell>Teléfono</TableCell>
                        <TableCell>Acciones</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {customers.map((c) => (
                        <TableRow key={c.id}>
                            <TableCell>{c.first_name} {c.last_name}</TableCell>
                            <TableCell>{c.email}</TableCell>
                            <TableCell>{c.phone_number}</TableCell>
                            <TableCell>
                                <IconButton onClick={() => onEdit(c)}><EditIcon /></IconButton>
                                <IconButton onClick={() => setToDelete(c)}><DeleteIcon /></IconButton>
                            </TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
            <CustomerDeleteDialog
                customer={toDelete}
                onClose={() => {
                    setToDelete(null);
                    refresh();
                }}
            />
        </>
    );
}
