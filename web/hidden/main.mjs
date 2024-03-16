import express from 'express';
import * as path from 'path';

const app = express();

app.use((req, res, next) => {
    res.setHeader('flag', 'SURGE{b329b2d7373612098b9a64efad366663}');
    next();
});

app.get('/', (req, res) => {
    res.status(200).send(`
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lorem Ipsum</title>
</head>
<body>
    <h1>Lorem Ipsum</h1>
    <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eget elit ac leo vehicula sodales. Proin non velit sit amet mi scelerisque lacinia ac nec risus. Maecenas non urna nec velit placerat vehicula. Sed finibus nisi vel sapien feugiat, a cursus mi volutpat. Phasellus eget tempor libero. Nam feugiat justo a turpis fringilla tincidunt. Mauris vehicula vestibulum nibh, vitae fermentum dui malesuada quis. Nam pretium magna ac consequat ullamcorper. Vivamus vitae dolor non nisi condimentum dapibus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Cras fermentum ultrices nulla, sed auctor elit aliquam nec. Curabitur vel tellus ut libero bibendum elementum.
    </p>
    <p>
        Donec sit amet metus nec justo iaculis malesuada. Nulla nec est vel felis laoreet convallis. Fusce eget ipsum sed felis accumsan ultricies sed eget lacus. Aliquam erat volutpat. Maecenas feugiat, ligula nec tempus fermentum, justo odio suscipit elit, nec malesuada ex ex non magna. Donec auctor metus non neque interdum convallis. Sed tempus ligula nec sodales accumsan. Vivamus tincidunt ullamcorper justo, id bibendum justo consequat nec. Nam condimentum fermentum leo sit amet tempus. Nullam mattis elit vel nibh facilisis, nec hendrerit ligula elementum. Curabitur suscipit, odio eu pellentesque feugiat, felis nunc accumsan orci, nec interdum nulla arcu vel neque. Vivamus auctor justo eu convallis facilisis. Integer lacinia viverra mi a scelerisque. Curabitur vitae turpis nec lacus commodo egestas. Nunc vel consectetur odio, a convallis ligula.
    </p>
</body>
</html>

    `);
});

const PORT = 15004;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
