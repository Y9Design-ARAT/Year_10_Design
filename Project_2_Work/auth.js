//Step 1: I going grab all the objects on the page I need for manipulation of page
const login_form = document.querySelector("#login_form")
const login_nav = document.getElementById("login_nav")
const logout_nav = document.getElementById("logout_nav")
const learn_more_nav = document.getElementById("learn_more_nav")
const elements_nav = document.getElementById("elements_nav")


var users =["user1","user2","user3"]
var pwords = ["pword1","pword","pword3"]




login_form.addEventListener("submit", (e) => {

	console.log(e)
	e.preventDefault() //Stops page from reloading

	//Step 1:
	//Take form information
	user = login_form["user_name"].value
	password = login_form["user_password"].value
	console.log(user,password)
	

	//changed display states of nav bar buttons
	window.location.href = "dashboard.html"
	login_nav.style.display = "none"
	logout_nav.style.display = "block" //display the logout_nav button
	learn_more_nav.style.display = "block"
	elements_nav.style.display = "block"





	//Cleared and closed modal
	//manually close modal
	//General
	const modal = document.querySelector('#login_modal'); 
	M.Modal.getInstance(modal).close();
	//Clears the content in the modal
	login_form.reset()

});

// logout_nav.addEventListener("click",(e) => {

// 	console.log(e)

// 	//changed display states of nav bar buttons
// 	login_nav.style.display = "block"
// 	logout_nav.style.display = "none" //display the logout_nav button
// 	learn_more_nav.style.display = "none"
// 	elements_nav.style.display = "none"
// });







