import { Form, redirect, Link } from "react-router-dom";

export async function action({ request }) {
    const formData = await request.formData();
    const email = formData.get("email");
    const password = formData.get("password");
    const data = { email, password };

    const url = "http://localhost:8000/register";
    const addUser = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    }).then((response) => response.json());

    return redirect("/");
}

const Register = () => {
    return (
        <Form method="POST">
            <h1>Create an Account</h1>
            <p>
                If you already have an account,
                <Link to="/login"> click here</Link> to login.
            </p>
            <label>
                Enter Email Address
                <input type="text" name="email" />
            </label>
            <label>
                Create a Password
                <input type="password" name="password" />
            </label>
            <button type="submit">Submit</button>
        </Form>
    );
};

export default Register;
