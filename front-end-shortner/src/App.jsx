import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Home from "./routes/Home";
import Links, { loader as linksLoader } from "./routes/Links";
import AddLink, { action as linksAction } from "./routes/AddLink";
import Register, { action as registerAction } from "./routes/Register";
import Users, { loader as userLoader } from "./routes/Users";
import Login, { action as loginAction } from "./routes/Login";
// import './App.css'

const router = createBrowserRouter([
    {
        path: "/",
        element: <Home />,
    },
    {
        path: "/links",
        element: <Links />,
        loader: linksLoader,
    },
    {
        path: "/links/add",
        element: (
            <>
                <AddLink />
                <Links />
            </>
        ),
        action: linksAction,
        loader: linksLoader,
    },
    {
        path: "/users",
        element: <Users />,
        loader: userLoader,
    },
    {
        path: "/register",
        element: <Register />,
        action: registerAction,
    },
    {
        path: "/login",
        element: <Login />,
        action: loginAction,
    },
]);

function App() {
    return <RouterProvider router={router} />;
}

export default App;
