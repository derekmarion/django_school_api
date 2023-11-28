import Row from "react-bootstrap/esm/Row";
import { useEffect, useState } from "react";
import axios from "axios";

export const Subjects = () => {
  const [subjects, setSubjects] = useState([]);

  const getAllSubjects = async () => {
    let response = await axios
      .get("http://127.0.0.1:8000/api/v1/subjects/")
      .catch((err) => {
        console.log(err);
        alert("something went wrong");
      });
    console.log(response);
    setSubjects(response.data);
  };

  useEffect(() => {
    getAllSubjects();
  }, []);

  return (
    <Row style={{ textAlign: "center", padding: "0 10vmin" }}>
      <h1>Subjects</h1>
      <ul>
        {subjects.map((subject) => (
          // iterates through the list of pokemon to render a li for each student within our database
          <li
            key={subject.id}
            // use the student's id as the key for each "li" element
            style={{
              margin: "3vmin",
              display: "flex",
              flexDirection: "column",
            }}
          >
            Subject: {subject.subject_name} <br />
            Professor: {subject.professor} <br />
            Students: {subject.students} <br />
            Grade Average: {subject.grade_average} <br />
          </li>
        ))}
      </ul>
    </Row>
  );
};
