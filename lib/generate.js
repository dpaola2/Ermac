var p = require('./parse-js.js');
var fs = require('fs');

fs.readFile(
            './test.js', 
            'utf8', 
            function(err, data) { 
                ast = p.parse(data);
                var json_data = JSON.stringify(ast, null, 2);
                fs.writeFile('test_ast.json', json_data);
            });