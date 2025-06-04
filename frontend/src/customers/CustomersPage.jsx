import { Box, Button } from "@mui/material";
import { useState } from "react";
import CustomerTable from "./components/CustomerTable";
import CustomerFormDialog from "./components/CustomerFormDialog";
import SectionTitle from "../shared/components/SectionTitle";

export default function CustomersPage() {
    const [openForm, setOpenForm] = useState(false);
    const [editingCustomer, setEditingCustomer] = useState(null);

    const handleEdit = (customer) => {
        setEditingCustomer(customer);
        setOpenForm(true);
    };

    return (
        <Box p={3}>
            <SectionTitle title="Gestión de Clientes" />
            <Button variant="contained" onClick={() => setOpenForm(true)}>
                Nuevo Cliente
            </Button>
            <CustomerTable onEdit={handleEdit} />
            <CustomerFormDialog
                open={openForm}
                onClose={() => {
                    setOpenForm(false);
                    setEditingCustomer(null);
                }}
                customer={editingCustomer}
            />
        </Box>
    );
}
