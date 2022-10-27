import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import { Route, Routes } from "react-router-dom";
import TablePage from "./Pages/TablePage";
import Modal from "./components/Modal";



function App() {
  return (
      <Routes>
        <Route path="/" element={<TablePage />} />
        <Route path="/formcard" element={<Modal />} />
      </Routes>
  );
}

export default App;