import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import { Home } from "./pages/HomePage";
import { Subjects } from "./pages/SubjectsPage";
import { ASubject } from "./pages/ASubjectPage";
import { Students } from "./pages/StudentsPage";
import { AStudent } from "./pages/AStudentPage"

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      {
        index: true,
        element: <Home />,
      },
      {
        path: "subjects",
        element: <Subjects/>,
      },
      {
        path: "subject",
        element: <ASubject />,
      },
      {
        path: "students",
        element: <Students />,
      },
      {
        path: "student",
        element: <AStudent />,
      }
    ],
  },
]);

export default router;