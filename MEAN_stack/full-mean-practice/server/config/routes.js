var products = require('../controllers/products.js');
module.exports = function(app){
    
    //  app.get('/products', (req, res, next)=>{
    //    /* retrieve the products from the database */ 
    //    /* and respond with the products using 'res.json(products)' */
    //  });
    
    //  app.get('/products/:id', (req, res, next)=>{
    //    /* retrieve the product from the database (find the product by the req.params.id)  */
    //    /* and respond with the product using 'res.json(product)' */
    //  });
    
    //  app.post('/products', (req, res, next)=>{
    //    /* create a product, and respond with a success of failed message */
    //  });
    
    //  app.put('/products/:id', (req, res, next)=>{
    //    /* update the product (find the product by the req.params.id) */ 
    //    /* update that product with the posted product found through the req.body */
    //    /* and respond with the updated version of the product */
    //  });
    
    //  app.delete('/products/:id', (req, res, next)=>{
    //    /* delete the product (find the product by the req.params.id) */ 
    //    /* and respond with a success of failed message */
    //  });
     

     module.exports = function(app){
      app.get('/products', products.index);
      app.get('/products/:id', products.show);
      app.post('/products', products.create);
      app.put('/products/:id', products.update);
      app.delete('/products/:id', products.delete);
   
      app.all("*", (req,res,next) => {
          res.sendFile(path.resolve("./public/dist/index.html"))
      });
  }
  
   }
   