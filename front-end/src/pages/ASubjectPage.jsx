import Row from "react-bootstrap/esm/Row";
import { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
import Spinner from "react-bootstrap/Spinner";

export const ASubject = () => {
  const [subject, setSubject] = useState(null);
  const { id } = useParams();

  const getSubject = async () => {
    let response = await axios
      .get(`http://127.0.0.1:8000/api/v1/subjects/${id}/`) //replace wit appropriate url
      .catch((err) => {
        console.log(err);
        alert("something went wrong");
      });
    console.log(response);
    setSubject(response.data);
  };

  useEffect(() => {
    getSubject();
  }, [id]);

  return (
    <Row style={{ textAlign: "center", padding: "0 10vmin" }}>
      <h1>Subject</h1>
      {subject ? (
        <ul>
          <li
            key={subject.id}
            // use the student's id as the key for each "li" element
            style={{
              margin: "3vmin",
              display: "flex",
              flexDirection: "column",
            }}
          >
            Name: {subject.subject_name} <br />
            Professor: {subject.professor} <br />
            Students: {subject.students} <br />
            Grade Average: {subject.grade_average}
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
