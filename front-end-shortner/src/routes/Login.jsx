import { Form, redirect, Link } from "react-router-dom";

export async function action({ request }) {
    const formData = await request.formData();
    const email = formData.get("email");
    const password = formData.get("password");
    const data = { email, password };

    const url = "http://localhost:8000/login";
    const loginUser = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    }).then((response) => response.json());

    return redirect("/");
}

const Login = () => {
    return (
        <Form method="POST">
            <h1>Login Page</h1>
            <p>
                If you need to create an account,
                <Link to="/register"> click here.</Link>
            </p>
            <label>
                Enter Account Email:
                <input type="text" name="email" />
            </label>
            <label>
                Enter Account Password:
                <input type="password" name="password" />
            </label>
            <button type="submit">Submit</button>
        </Form>
    );
};

export default Login;
