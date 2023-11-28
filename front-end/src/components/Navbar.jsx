import Row from "react-bootstrap/esm/Row";
import { Link } from "react-router-dom";

export const Navbar = () => {
    return (
        <Row style={{display:"flex", justifyContent:"space-around"}}>
            <Link to="/">Home</Link>
            <Link to="students">Students</Link>
            <Link to="student">Student</Link>
            <Link to="subjects">Subjects</Link>
            <Link to="subject">Subject</Link>
        </Row>
    )
}