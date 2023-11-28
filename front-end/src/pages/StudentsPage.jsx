import Row from "react-bootstrap/esm/Row";
import { useEffect, useState } from "react";
import axios from "axios";

export const Students = () => {
  const [students, setStudents] = useState([]);

  const getAllStudents = async () => {
    let response = await axios
      .get("http://127.0.0.1:8000/api/v1/students/")
      .catch((err) => {
        console.log(err);
        alert("something went wrong");
      });
    console.log(response);
    setStudents(response.data);
  };

  useEffect(() => {
    getAllStudents();
  }, []);

  return (
    <Row style={{ textAlign: "center", padding: "0 10vmin" }}>
      <h1>Students</h1>
      <ul>
        {students.map((student) => (
          // iterates through the list of pokemon to render a li for each student within our database
          <li
            key={student.id}
            // use the student's id as the key for each "li" element
            style={{
              margin: "3vmin",
              display: "flex",
              flexDirection: "column",
            }}
          >
            Name: {student.name} <br />
            Student Email: {student.student_email} <br />
            Locker #: {student.locker_number}
          </li>
        ))}
      </ul>
    </Row>
  );
};
