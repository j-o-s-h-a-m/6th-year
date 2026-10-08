let total = 0
let v1 = [1,2,3,3,4,5,6,7,7,7,7,7]

for(let list of v1){

    total = total + list
}
console.log('the total is:',total/v1.length)
n = v1.length
if (n%2 == 0 ){
    let med = (v1[n/2]+v1[(n/2)-1])/2
    console.log('the median is:',med)
}
else{
    let med = v1[(n+1)/2]
    console.log('the median is:',med)
}
let count = 0 
let count2 = 0 
let largest = 0
let highest = 0 
for(let i of v1){
    count = 0
   for (let j of v1){ 
        if (j == i){
            count = count + 1
            if (count >= count2){
                 count2 = count
                 largest = i
            }
        }
    }
}
console.log('the mode is:',largest)
