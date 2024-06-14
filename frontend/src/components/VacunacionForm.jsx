// src/components/VacunacionForm.jsx
import React from 'react';
import GenericForm from './GenericForm';

const vacunacionConfig = [
  { name: 'id_galpon', label: 'ID del galpon', type: 'number', required: true },
  { name: 'nombre_Vacuna', label: 'Nombre de la Vacuna', required: true },
  { name: 'fecha', label: 'Fecha', type: 'date', required: true },
];

const VacunacionForm = () => (
  <div>
    <h1>Formulario vacunacion</h1>
    <GenericForm config={vacunacionConfig} endpoint="http://localhost:5000/api/vacunacion" />
  </div>
);

export default VacunacionForm;
