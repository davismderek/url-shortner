import { useLoaderData } from "react-router-dom";

export async function loader() {
    const url = "http://localhost:8000/users";
    const data = await fetch(url).then((response) => response.json());

    return { data };
}

const Users = () => {
    const { data } = useLoaderData();
    return (
        <>
            <h1>Users List</h1>
            <ul>
                {data.map((user, index) => {
                    return (
                        <li key={index}>
                            {/* <Link to={url.slug}> */}
                            {user.email}
                            {/* </Link> */}
                        </li>
                    );
                })}
            </ul>
        </>
    );
};

export default Users;
