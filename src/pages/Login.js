import React, { useState } from "react";
import { Button, Form,FormGroup,Label,Input } from "reactstrap";
import backendAPI from './../api/travellingdiaries';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const PostData = async () => {
        console.log(email,password);
        const response = await backendAPI.post('/rest-auth/login/', { "username":email, "password":password});
        console.log(response.data.key);
    }


  return (
      <React.Fragment>
          <Form>
            <FormGroup>
                <Label for="exampleEmail">Email</Label>
                <Input type="text" onChange={e => setEmail(e.target.value)} name="username" id="exampleEmail" placeholder="with a placeholder" />
            </FormGroup>
            <FormGroup>
                <Label for="examplePassword">Password</Label>
                <Input type="password" onChange={e => setPassword(e.target.value)} name="password" id="examplePassword" placeholder="password placeholder" />
            </FormGroup>
            <Button onClick={PostData}>Submit</Button>
          </Form>
      </React.Fragment>
  );
};

export default Login;
