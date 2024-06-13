// src/components/GalponForm.jsx
import React from 'react';
import GenericForm from './GenericForm';

const galponConfig = [
  { name: 'numero_Galpon', label: 'numero del Galpon', type: 'number', required: true },
  { name: 'numero_aves', label: 'numero aves', type: 'number', required: true },

];

const GalponForm = () => (
  <div>
    <h1>Formulario Galpones</h1>
    <GenericForm config={galponConfig} endpoint="http://localhost:5000/api/galpon" />
  </div>
);

export default GalponForm;
