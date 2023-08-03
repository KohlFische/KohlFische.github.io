document.querySelectorAll('.social-icon[title="Email"]').forEach(element => {
    element.target = '_self'
})

// document.querySelector('.social-icon[title="Email"]').target = '_self'

async function copyEmail() {
    await navigator.clipboard.writeText('wuorbs@gmail.com')
    btf.snackbarShow('Email copied!')
}