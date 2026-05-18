module.exports = {
  content: [
    "./*.html",
    "./**/*.html",
    "./**/*.js",
  ],

  theme: {
    container: {
      center: true,
    },

    extend: {
      colors: {
        primary: {
          // DEFAULT: "#D12329",
          DEFAULT: "#E7000B",
          50: "#fff1f2",
          100: "#ffe0e2",
          200: "#ffc7cb",
          300: "#ff9ea5",
          400: "#ff6570",
          500: "#E7000B",
          600: "#c40009",
          700: "#a30008",
          800: "#88010a",
          900: "#73030b",
        },
        secondary: {
          DEFAULT: "#0EA5E9",
          50: "#f0f9ff",
          100: "#e0f2fe",
          200: "#bae6fd",
          300: "#7dd3fc",
          400: "#38bdf8",
          500: "#0EA5E9",
          600: "#0284c7",
          700: "#0369a1",
          800: "#075985",
          900: "#0c4a6e",
        },
        accent: {
          DEFAULT: "#FACC15",
          50: "#fefce8",
          100: "#fef9c3",
          200: "#fef08a",
          300: "#fde047",
          400: "#facc15",
          500: "#eab308",
          600: "#ca8a04",
          700: "#a16207",
          800: "#854d0e",
          900: "#713f12",
        },

        dark: {
          DEFAULT: "#1D161E",
          50:  "#fafafa",
          100: "#f3f1f3",
          200: "#e7e4e7",
          300: "#d7d0d7",
          400: "#a89ea9",
          500: "#79697b",
          600: "#594c5b",
          700: "#463947",
          800: "#2a212c",
          900: "#1D161E",
          950: "#0c090c"
      }

      },
    },
  },

  plugins: [],
}