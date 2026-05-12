# 🧮 Ultimate Smart Calculator

A modern, feature-rich calculator with an elegant glassmorphism UI design. Built with vanilla JavaScript with no dependencies.

## ✨ Features

- **Real-time Calculation** - Instant mathematical operations
- **Keyboard Support** - Use your keyboard for faster input
  - Numbers: `0-9`
  - Operations: `+`, `-`, `*`, `/`, `%`
  - Enter: Calculate result
  - Backspace: Delete last character
  - Escape: Clear all
- **Calculation History** - Track all your calculations
- **Error Handling** - Smart error detection and display
- **Responsive Design** - Works on all screen sizes
- **Modern UI** - Beautiful glassmorphism design with smooth animations
- **Parentheses Support** - Complex mathematical expressions

## 📦 Installation

### Option 1: Direct Use
Simply open `index.html` in your web browser.

### Option 2: Local Server
```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000

# Node.js with http-server
npx http-server
```

Then navigate to `http://localhost:8000`

## 🚀 Usage

1. **Click buttons** or **use keyboard** to enter calculations
2. **Press `=` or `Enter`** to calculate
3. **Press `C`** to clear display
4. **View history** of calculations in the history panel

### Examples
```
10 + 5 = 15
100 * 2 - 50 = 150
(20 + 30) * 2 = 100
100 / 4 = 25
```

## 🎨 Design

- **Color Scheme**: Dark theme with neon accents
  - Cyan: `#00f3ff`
  - Magenta: `#ff00ff`
  - Lime: `#39ff14`
- **Typography**: Orbitron font for a modern feel
- **Effects**: Glassmorphism, smooth transitions, animations

## 📁 Project Structure

```
ultimate-smart-calculator/
├── index.html          # Main calculator application
├── README.md           # This file
├── LICENSE             # MIT License
└── .gitignore          # Git ignore rules
```

## 🔧 Technologies

- **HTML5** - Semantic markup
- **CSS3** - Modern styling with CSS Grid and Flexbox
- **JavaScript (ES6+)** - Pure vanilla JavaScript, no frameworks

## 📋 Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

## 🐛 Known Limitations

- Uses JavaScript's `Function()` constructor for evaluation (safe for mathematical expressions)
- Limited to mathematical operations (no variable storage)
- History is cleared on page refresh

## 🚀 Future Enhancements

- [ ] Local storage for persistent history
- [ ] Scientific calculator mode
- [ ] Dark/Light theme toggle
- [ ] Calculation export (CSV/PDF)
- [ ] Custom color themes
- [ ] Unit conversion

## 📄 License

MIT License - See LICENSE file for details

## 👨‍💻 Author

**Huzaifa Rakhani**
- GitHub: [@huzaifarakhangi2425-cloud](https://github.com/huzaifarakhangi2425-cloud)

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 💡 Tips

- Use parentheses for complex calculations: `(100 + 50) * 2`
- Keyboard shortcuts make calculations faster
- Check the history panel to review your calculations

---

**Made with ❤️ by Huzaifa Rakhani**
