import "semantic-ui-css/semantic.min.css";
import "./App.css";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Login from "./components/Login";
import { AuthProvider, AuthContext } from "./context/LoginContext";
import axios from "axios";

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/">
          <AuthProvider>
            <Login />
          </AuthProvider>
        </Route>
      </Switch>
    </Router>
  );
}

axios.defaults.baseURL = process.env.REACT_APP_API_URL;
// axios.defaults.withCredentials = true;

export default App;
