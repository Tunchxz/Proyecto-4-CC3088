import { useEffect, useState } from "react";
import axiosInstance from "../../shared/api/axiosInstance";

export const useVehicles = () => {
    const [vehicles, setVehicles] = useState([]);

    const fetch = async () => {
        const res = await axiosInstance.get("/vehicles");
        setVehicles(res.data);
    };

    useEffect(() => {
        fetch();
    }, []);

    return { vehicles, refresh: fetch };
};
