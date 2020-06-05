import React from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import Header from './Header';
import MainHeader from './MainHeader';
import FeaturedPost from './FeaturedPost';
import Footer from './Footer';
import MenuButton from './MenuButton';
import CityCard from './CityCard';
import PostForm from './PostForm';
import WeatherCard from './WeatherCard';
import { makeStyles } from '@material-ui/core/styles';


const sections = [
  { title: 'Technology', url: '#' },
  { title: 'Design', url: '#' },
  { title: 'Culture', url: '#' },
  { title: 'Business', url: '#' },
  { title: 'Politics', url: '#' },
  { title: 'Opinion', url: '#' },
  { title: 'Science', url: '#' },
  { title: 'Health', url: '#' },
  { title: 'Style', url: '#' },
  { title: 'Travel', url: '#' },
];

const mainHeadData = {
  image: 'https://source.unsplash.com/random',
};

const featuredPosts = [
  {
    title: 'Featured post',
    date: 'Nov 12',
    description:
      'This is a wider card with supporting text below as a natural lead-in to additional content.',
    image: 'https://source.unsplash.com/random',
    imageText: 'Image Text',
  },
  {
    title: 'Post title',
    date: 'Nov 11',
    description:
      'This is a wider card with supporting text below as a natural lead-in to additional content.',
    image: 'https://source.unsplash.com/random',
    imageText: 'Image Text',
  },
];


const useStyles = makeStyles((theme) => ({
  headCard:{
    zIndex:999,
    position: 'absolute',
    top:'85%',
    paddingLeft:20,
    paddingRight:20,
    
  },
  postSection:{
    padding:20
  }
}));



export default function Base() {

  const classes = useStyles();

  return (
    <React.Fragment>
      <CssBaseline />
      <Box>
        <Header title="TravellingDiaries" sections={sections} />
        <main>
          <Box container>
            <MainHeader post={mainHeadData} />
            <Grid container className={classes.headCard}>
            <Grid item sm={3} >
              <CityCard />
              </Grid>
              <Grid item sm={6} >
                <MenuButton />
                <br />
                <br />
                <Box  className={classes.postSection}>
                  <Box>
                    <PostForm />
                    </Box>
                    <br />
                    <Box>
                      <Typography
                      component="h2"
                      variant="h4"
                      color="inherit"
                      >
                      Selected: Attractions ........
                      </Typography>
                      <hr />
                    </Box>
                    <Box>
                      <Typography
                      component="h2"
                      variant="h4"
                      color="inherit"
                      >
                      Trending near you ........
                      </Typography>
                      <hr />

                    </Box>
                    
                  <Grid container spacing={4}>
                  {featuredPosts.map((post) => (
                   <FeaturedPost key={post.title} post={post} />
                  ))}
                  </Grid>
                </Box>
              </Grid>
              <Grid item sm={3} >
                <WeatherCard />
              </Grid>
            </Grid>
          </Box>
          
        </main>
      </Box>
      {/* <Footer title="Footer" description="Something here to give the footer a purpose!" /> */}
    </React.Fragment>
  );
}
