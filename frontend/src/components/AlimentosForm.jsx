import React from 'react';
import GenericForm from './GenericForm';
import api from '../services/api';

const alimentosConfig = [
  { name: 'id_galpon', label: 'ID del galpon', type: 'number', required: true },
  { name: 'marca_Alimento', label: 'Marca del Alimento', required: true },
  { name: 'etapa_alimento', label: 'Etapa del Alimento', required: true },
  { name: 'fecha_consumo', label: 'Fecha de Consumo', type: 'date', required: true },
  { name: 'cantidad_kg', label: 'Cantidad en Kg', type: 'number', required: true },
];

const AlimentosForm = () => (
  <div>
    <h1>Formulario de Alimentos</h1>
    <GenericForm config={alimentosConfig} endpoint="/alimentos" api={api} />
  </div>
);

export default AlimentosForm;
