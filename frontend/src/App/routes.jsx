import { createBrowserRouter } from "react-router";
import DashboardLayout from "./layout/DashboardLayout";

import CustomersPage from "../customers/CustomersPage";
import VehiclesPage from "../vehicles/VehiclesPage";
import ReservationsPage from "../reservations/ReservationsPage";
import ReservationReport from "../reports/ReservationReport";
import MaintenanceReport from "../reports/MaintenanceReport";
import ContractIncomeReport from "../reports/ContractIncomeReport";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <DashboardLayout />,
        children: [
            { path: "", element: <CustomersPage /> },
            { path: "customers", element: <CustomersPage /> },
            { path: "vehicles", element: <VehiclesPage /> },
            { path: "reservations", element: <ReservationsPage /> },
            { path: "reports/reservations", element: <ReservationReport /> },
            { path: "reports/maintenance", element: <MaintenanceReport /> },
            { path: "reports/contracts", element: <ContractIncomeReport /> }
        ]
    }
]);
