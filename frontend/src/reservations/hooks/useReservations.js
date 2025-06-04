import { useEffect, useState } from "react";
import axiosInstance from "../../shared/api/axiosInstance";

export const useReservations = () => {
    const [reservations, setReservations] = useState([]);

    const fetch = async () => {
        const res = await axiosInstance.get("/reservations");
        setReservations(res.data);
    };

    useEffect(() => {
        fetch();
    }, []);

    return { reservations, refresh: fetch };
};
