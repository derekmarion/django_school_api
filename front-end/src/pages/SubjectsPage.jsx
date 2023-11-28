import Row from "react-bootstrap/esm/Row";
import { useEffect, useState } from "react";
import axios from "axios";
import Button from 'react-bootstrap/Button';
import { useNavigate } from "react-router-dom";

export const Subjects = () => {
  const [subjects, setSubjects] = useState([]);
  const navigate = useNavigate();

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


  const handleButtonClick = (name) => {
    navigate(`/subjects/${name}/`);
}

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
            <Button onClick={()=>handleButtonClick(subject.subject_name)}>More Details</Button>
          </li>
        ))}
      </ul>
    </Row>
  );
};
