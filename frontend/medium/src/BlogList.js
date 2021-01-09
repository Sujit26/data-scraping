import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
// import CardActionArea from "@material-ui/core/CardActionArea";
// import CardMedia from "@material-ui/core/CardMedia";

const useStyles = makeStyles({
  root: {
    maxWidth: 345*2,
  },
  media: {
    height: 140*2,
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
              <div>
            <Card className={classes.root}>
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

                  <Typography
                    variant="body1"
                    color="black"
                    component="p"
                  >
                    {"-by "+ data.name}
                  </Typography>
                </CardContent>
              </CardActions>
              <CardActions >
                <h5 size="small" >
                  {data.responses}
                </h5>
                <h5 size="small" color="primary">
                  {data.read_time}
                </h5>
                <Button size="small" color="primary" >
                  read more
                </Button>
              </CardActions>
            </Card>
            </div>
          );
        }
        return null;
      })}
    </>
  );
};
export default BlogItemList;

// function CardTemplate() {
//   const classes = useStyles();
//   return (
//     <Card className={classes.root}>
//       <CardActions>
//         <CardMedia
//           className={classes.media}
//           image="/static/images/cards/contemplative-reptile.jpg"
//           title="Contemplative Reptile"
//         />
//         <CardContent>
//           <Typography gutterBottom variant="h5" component="h2">
//             Lizard
//           </Typography>
//           <Typography variant="body2" color="textSecondary" component="p">
//             Lizards are a widespread group of squamate reptiles, with over 6,000
//             species, ranging across all continents except Antarctica
//           </Typography>
//         </CardContent>
//       </CardActions>
//       <CardActions disableSpacingA >
//         <Button size="small" color="primary">
//           Share
//         </Button>
//         <Button size="small" color="primary">
//           Learn More
//         </Button>
//       </CardActions>
//     </Card>
//   );
//   // return (
//   //   <Card style={{ width: "18rem" }} className="mb-2">
//   //     <Card.Header>Title</Card.Header>
//   //     <Card.Body>
//   //       <Card.Title> Card Title </Card.Title>
//   //       <Card.Text>
//   //         Some quick example text to build on the card title and make up the
//   //         bulk of the card's content.
//   //       </Card.Text>
//   //     </Card.Body>
//   //   </Card>
//   // );
// }
