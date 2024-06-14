import React from 'react';
import { useForm } from 'react-hook-form';
import axios from 'axios';
import '../styles/formStyles.scss';

const GenericForm = ({ config, endpoint }) => {
    const { register, handleSubmit, formState: { errors }, reset } = useForm();

    const onSubmit = data => {
        axios.post(endpoint, data)
            .then(response => {
                console.log('Respuesta del servidor:', response.data);
                reset(); // Resetea el formulario después de enviar con éxito
            })
            .catch(error => {
                console.error('Error al enviar el formulario:', error);
                // Aquí podrías mostrar un mensaje de error al usuario
            });
    };

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            {config.map(field => (
                <div key={field.name}>
                    <label>{field.label}:</label>
                    <input
                        type={field.type || 'text'}
                        {...register(field.name, { required: field.required })}
                    />
                    {errors[field.name] && <span>Este campo es obligatorio</span>}
                </div>
            ))}
            <button type="submit">Enviar</button>
        </form>
    );
};

export default GenericForm;
