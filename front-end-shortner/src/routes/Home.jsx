import { Link } from "react-router-dom";

const Home = () => {
    return (
        <>
            <h1>Home Page</h1>
            <Link to="/links"> - See URLs</Link>
            <br></br>
            <Link to="/links/add"> - Create a New Short URL</Link>
            <br></br>
            <Link to="/users"> - See User</Link>
            <br></br>
            <Link to="/register"> - Register as a User</Link>
            <br></br>
            <Link to="/login"> - Login</Link>
        </>
    );
};

export default Home;
