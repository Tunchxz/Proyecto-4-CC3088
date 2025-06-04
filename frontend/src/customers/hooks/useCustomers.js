import { useEffect, useState } from "react";
import axiosInstance from "../../shared/api/axiosInstance";

export const useCustomers = () => {
    const [customers, setCustomers] = useState([]);

    const fetch = async () => {
        const res = await axiosInstance.get("/customers");
        setCustomers(res.data);
    };

    useEffect(() => {
        fetch();
    }, []);

    return { customers, refresh: fetch };
};
