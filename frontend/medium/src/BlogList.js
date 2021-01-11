import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";

import Grid from "@material-ui/core/Grid";

// styling the card
const useStyles = makeStyles({
  root: {
    width: '60vw',
    height: 140 * 2,
    transitionDuration: '0.3s',
    alignSelf: true,
  },
  media: {
    width: '60vw',
    height: 140 * 2,
  },
});

const BlogItemList = ({ blogList = [] }) => {
  React.useEffect(() => {
    console.log(blogList);
  }, []);

  const classes = useStyles();

  return (
    <>
      {blogList.map((data, index) => {
        if (data) {
          return (
            <Grid
              key={index}
              container
              direction="row"
              justify="center"
              alignItems="center"
              spacing={5}
            >
              <Grid item>
                <Card
                  className={classes.root}
                >
                  <CardActions>
                    <CardContent>
                      <Typography gutterBottom variant="h5" component="h2">
                        {data.title}
                      </Typography>
                      <Typography
                        variant="body2"
                        color="textSecondary"
                        component="p"
                      >
                        {data.short_desciption}
                      </Typography>
                      <br />
                      <br />
                      <Typography
                        variant="body1"
                        // color="black"
                        component="p"
                      >
                        {"-by " + data.name}
                      </Typography>
                    </CardContent>
                  </CardActions>
                  <CardActions>
                    <h5 size="small">{data.responses}</h5>
                    <h5 size="small" color="primary">
                      {data.read_time}
                    </h5>
                    <Button size="small" color="primary">
                      read more
                    </Button>
                  </CardActions>
                </Card>
              </Grid>
            </Grid>
          );
        }
        return null;
      })}
    </>
  );
};
export default BlogItemList;
