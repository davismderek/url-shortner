import { Form, redirect } from "react-router-dom";

export async function action({ request }) {
    const formData = await request.formData();
    const title = formData.get("title");
    const original_url = formData.get("original_url");
    const short_url = formData.get("short_url");
    const user_id = formData.get("user_id");
    const data = { title, original_url, short_url, user_id: Number(user_id) };

    const url = "http://localhost:8000/links/add";
    const addLink = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    }).then((response) => response.json());

    // return redirect("/links");
    return null;
}

const AddLink = () => {
    return (
        <Form method="POST">
            <label>
                Title of Link?
                <input type="text" name="title" />
            </label>
            <label>
                Add Original URL
                <input type="text" name="original_url" />
            </label>

            <label>
                Add Short URL
                <input type="text" name="short_url" />
            </label>
            <label>
                Add User_ID
                <input type="number" required name="user_id" />
            </label>
            <button type="submit">Submit</button>
        </Form>
    );
};

export default AddLink;
