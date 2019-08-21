let fs = require('fs');
let jsonObj = require('./style.json')

for(let key in jsonObj){
	let value = jsonObj[key]
	for( let i = 0; i  < value.length; i++){
		let char = value.charAt(i)
		if(char == char.toUpperCase()){
			let front = value.substring(0,i);
			let tail = value.substring(i+1);
			let middle = "-"+char.toLowerCase();
			value = front+middle+tail
			i += 1
		}
	}
	jsonObj[key] = value
}

let data = JSON.stringify(jsonObj);
fs.writeFileSync('parsed_style.json', data);
