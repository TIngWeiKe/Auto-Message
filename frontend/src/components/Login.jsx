import React, { useContext, useEffect, useState } from "react";
import { AuthProvider, AuthContext } from "../context/LoginContext";
import { Button, Checkbox, Form } from "semantic-ui-react";
import axios from "axios";

const Login = (props) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const { state, dispatch } = useContext(AuthContext);

  useEffect(() => {}, []);

  const handleMailChange = (e) => setEmail(e.target.value);

  const handlePasswordChange = (e) => setPassword(e.target.value);

  const handleSubmit = (e) => {
    axios
      .post("/login/", { username: email, password })
      .then((x) => console.log(x))
      .catch((y) => console.log(y));
    dispatch({ type: "LOGIN", email, password });
  };
  return (
    <div style={Styles.loginContainer} className="ui container">
      <Form onSubmit={handleSubmit}>
        <Form.Field>
          <label>Email 帳號</label>
          <input
            onChange={handleMailChange}
            value={email}
            placeholder="Email"
          />
        </Form.Field>
        <Form.Field>
          <label>密碼</label>
          <input
            onChange={handlePasswordChange}
            value={password}
            placeholder="密碼"
            type="password"
          />
        </Form.Field>
        <Button type="submit">登入</Button>
      </Form>
    </div>
  );
};

export default Login;

const Styles = {
  loginContainer: {
    alignItems: "center",
    paddingTop: "5rem",
  },
};
