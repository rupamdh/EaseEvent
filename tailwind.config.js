/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./templates/**/*.html",
    ],
    theme: {
        extend: {
            colors: {
                transparent: 'transparent',
                'white': '#FFFFFF',
                'yellow': '#FFE047',
                'yellow2': '#E6C72E',
                'gray': '#302c55',
                'gray2': '#2B293D',
            },
        },
    },
    plugins: [],
}

