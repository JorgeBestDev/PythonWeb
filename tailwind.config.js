/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./app/static/src/**/*.js"
  ],
  theme: {
    extend: {
      aspectRatio: {
        '3/2': '3 / 2',
      },
    },
  },
  plugins: [],
}

