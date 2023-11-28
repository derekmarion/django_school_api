import Row from "react-bootstrap/esm/Row";
import { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
import Spinner from "react-bootstrap/Spinner";

export const AStudent = () => {
  const [student, setStudent] = useState(null);
  const { id } = useParams();

  const getStudent = async () => {
    let response = await axios
      .get(`http://127.0.0.1:8000/api/v1/students/${id}/`) //replace wit appropriate url
      .catch((err) => {
        console.log(err);
        alert("something went wrong");
      });
    console.log(response);
    setStudent(response.data);
  };

  useEffect(() => {
    getStudent();
  }, [id]);

  return (
    <Row style={{ textAlign: "center", padding: "0 10vmin" }}>
      <h1>Student</h1>
      {student ? (
        <ul>
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
        </ul>
      ) : (
        <div className="container text-center" style={{ marginTop: "275px" }}>
          <Spinner animation="border" role="status">
            <span className="visually-hidden">Loading...</span>
          </Spinner>
        </div>
      )}
    </Row>
  );
};
