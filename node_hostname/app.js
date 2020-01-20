const http = require('http');

const os = require('os');

//const hostname = '127.0.0.1';
const hostname = os.hostname();
const port = 3000;

const server = http.createServer((req, res) => {
    res.statusCode == 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end(`Host: ${os.hostname()}`)
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});