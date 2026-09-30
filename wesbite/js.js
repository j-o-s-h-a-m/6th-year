function calculate_mean(){
//Get the user data
let data_from_user = document.getElementById('user_dataset_1').value;
//split string data_from_user to list
let data_in_list = data_from_user.split(',')
//set up our variables
let total = 0
let num_items = 0
//iterate through the list to get the total
for (let temp of data_in_list){
//input is text so we need to cast to float
total = total + parseFloat(temp);
}
//get the number of items in the list
num_items = data_in_list.length;
//calculate the average
let average = total/num_items
return average
}
function calculate_mean_btn(){
document.getElementById('user_dataset_1_placeholder').innerHTML = calculate_mean();
}

function update_user_name_btn(){
document.getElementById('user_name_place_holder').innerHTML = document.getElementById('user_name').value;
}
