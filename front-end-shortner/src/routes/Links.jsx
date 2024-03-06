import { useLoaderData } from "react-router-dom";

export async function loader() {
    const url = "http://localhost:8000/links";
    const data = await fetch(url).then((response) => response.json());

    return { data };
}

const Links = () => {
    const { data } = useLoaderData();
    return (
        <>
            <h1>Links List</h1>
            <ul>
                {data.map((url, index) => {
                    return (
                        <li key={index}>
                            {/* <Link to={url.slug}> */}
                            {url.title} - {url.short_url}
                            {/* </Link> */}
                        </li>
                    );
                })}
            </ul>
        </>
    );
};

export default Links;
