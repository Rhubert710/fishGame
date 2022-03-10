






let d = [{n:'bo',s:5},{n:'bo',s:4},{n:'bo',s:3},{n:'bo',s:1},{n:'bo',s:0}];

d.sort();
console.log(d);

let n ={n:'bo',s:2};
let s =[]
for (let i=0;i<d.length;i++) {
    if(n.s>d[i].s)
    {
        d.splice(i, 0, n);
        d.pop();
        break;
    }
}

console.log(d);