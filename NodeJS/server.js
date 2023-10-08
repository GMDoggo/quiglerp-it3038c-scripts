var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

http.createServer(function(req, res){

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
		uptime = os.uptime(); 
		// 1M Bytes = 1 MB 
		// Displays more Bytes than I have memory?
		totalMemory = Math.floor(os.totalmem() / 1_000_000)
		freeMemory = Math.floor(os.freemem() / 1_000_000)
		numCPUs = os.cpus().length;
        // Function to format uptime
		// 3600 Seconds Per hour
		// 60 Minutes per Hour
		// 24 Hours per Day
        function formatUptime(uptimeInSeconds) {
			// Calculates Days (Uptime in seconds/(3600 * 24) to get days
            const days = Math.floor(uptimeInSeconds / (3600 * 24));
			// Calculates hours using the remainder uptime from the above equation
            const hours = Math.floor((uptimeInSeconds % (3600 * 24)) / 3600);
			// Calculates Minutes after taking out hours
            const minutes = Math.floor((uptimeInSeconds % 3600) / 60);
			// Finalize the seconds by taking the remainder 
            const seconds = Math.floor(uptimeInSeconds % 60);
			// Returns the calculated variables
            return `${days} days, ${hours} hours, ${minutes} minutes, ${seconds} seconds`;
        }
		// Calls the formatUptime function and assigns the result as uptimeFormatted to output
        uptimeFormatted = formatUptime(uptime);
		
        html=`    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${uptimeFormatted}</p>
            <p>Total Memory: ${totalMemory}MB</p>
            <p>Free Memory: ${freeMemory}MB </p>
            <p>Number of CPUs: ${numCPUs} Logical Processors</p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");