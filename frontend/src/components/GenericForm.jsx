    // src/components/GenericForm.jsx
    import React from 'react';
    import { useForm } from 'react-hook-form';
    import axios from 'axios';
    import '../styles/formStyles.scss';

    const GenericForm = ({ config, endpoint }) => {
    const { register, handleSubmit, formState: { errors } } = useForm();

    const onSubmit = data => {
        axios.post(endpoint, data)
        .then(response => console.log(response.data))
        .catch(error => console.error(error));
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
