async function loadTheme() {
    const localTheme = localStorage.getItem('theme');

    if (localTheme) {
        setTheme(localTheme, false);
        console.log('using-localStorage')
    } else {
        const response = await fetch('/api/theme/');
        const data = await response.json();
        setTheme(data.value, false);
        console.log('fetching-from-db')
    }

    // Set the toggler state
    const toggler = document.getElementById('theme-toggler');
    toggler.checked = localStorage.getItem('theme') === 'dark';
}

function toggleTheme() {
    const toggler = document.getElementById('theme-toggler');
    const theme = toggler.checked ? 'dark' : 'light';
    setTheme(theme);
}

function setTheme(theme, updateAPI = true) {
    const stylesheet = document.getElementById('theme-stylesheet');
    stylesheet.href = `/static/css/${theme}.css`;
    localStorage.setItem('theme', theme);

    if (updateAPI) {
        updateThemeAPI(theme);
    }
}

async function updateThemeAPI(theme) {
    await fetch('/api/theme/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ value: theme }),
    });
}

document.addEventListener('DOMContentLoaded', loadTheme);