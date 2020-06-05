import React from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import Toolbar from '@material-ui/core/Toolbar';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import SearchIcon from '@material-ui/icons/Search';
import Typography from '@material-ui/core/Typography';
import Link from '@material-ui/core/Link';
import SearchBar from './SearchBar';
import { Grid } from '@material-ui/core';
import { TextField } from '@material-ui/core';
import { Container } from '@material-ui/core';
import { Box } from '@material-ui/core';

const useStyles = makeStyles((theme) => ({
  toolbar: {
    borderBottom: `1px solid ${theme.palette.divider}`,
  },
  toolbarTitle: {
    flex: 1,
    fontFamily: 'Pacifico',
    marginBottom: 5,
  },
  toolbarSecondary: {
    justifyContent: 'space-between',
    overflowX: 'auto',
  },
  toolbarLink: {
    padding: theme.spacing(1),
    flexShrink: 0,
  },
  searchBar: {
    paddingBottom: 5,
    marginTop:0,
    flex:1,
  },
  form: {
    display: 'flex',
    flexWrap: 'wrap',
  },formField:{
    flex:1,
    alignSelf: 'stretch',
  },
}));

export default function Header(props) {
  const classes = useStyles();
  const { sections, title } = props;

  return (
    <React.Fragment>
      <Toolbar className={classes.toolbar}>
        <Button size="small">Subscribe</Button>
        <Typography
          component="h1"
          variant="h4"
          color="inherit"
          align="center"
          className={classes.toolbarTitle}
        >
          {title}
        </Typography>
        <IconButton>
          <SearchIcon />
        </IconButton>
        <Button variant="outlined" size="small">
          Sign In
        </Button>
      </Toolbar>
      <Toolbar component="nav" variant="dense" className={classes.toolbarSecondary}>
        <Container>
        {/* {sections.map((section) => ( 
          <Link
            color="inherit"
            noWrap
            key='{section.title}'
            variant="body2"
            href='{section.url}'
            className={classes.toolbarLink}
          >
            {section.title}
          </Link>
        ))} */}
        <Grid container>
          <Grid item xs={6}>
          <Button color="inherit">Default : Attractions</Button>
          <Button color="inherit">Last selected : Hotels</Button>
        </Grid>
        <Grid item xs={6} className={classes.searchBar}>
          <Box width="100%">
            <form className={classes.form} noValidate autoComplete="off" >
              <TextField className={classes.formField} id="standard-basic" placeholder="Search nearby" width="100%" />
            </form>
          </Box>
           
          </Grid>
        </Grid>
        </Container>
      </Toolbar>
    </React.Fragment>
  );
}

Header.propTypes = {
  sections: PropTypes.array,
  title: PropTypes.string,
};
