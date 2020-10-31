import React from 'react';
import { Navbar, Nav, Icon } from 'rsuite';
import './Home.css';

export default class Home extends React.Component {
	constructor(props) {
		super(props);
		const user = localStorage.getItem('user');

		if(!user) this.props.history.push('/login');
	}
	render() {
		return (
			<div>
				<Navbar>
					<Navbar.Header>
						<a href="/" className="navbar-brand logo">SOPES 1 GRUPO 4 </a>
					</Navbar.Header>
					<Navbar.Body>
						<Nav onSelect={this.logout}>
							<Nav.Item eventKey="1" > {localStorage.getItem("user")} </Nav.Item>
						
						</Nav>
						<Nav pullRight onSelect={this.logout}>
							<Nav.Item eventKey="3" icon={<Icon icon="sign-out"/>}> Logout </Nav.Item>
						</Nav>
					</Navbar.Body>
				</Navbar>
				<div>
				</div>
			</div>
		);
	}

	logout = (ek, _) => {
		switch (ek) {
			case '1':
				this.props.history.push('/');
				break;
			case '2':
				
				break;
			case '3':
				localStorage.clear();
				this.props.history.push('/login');
				break;
		}
	}
}