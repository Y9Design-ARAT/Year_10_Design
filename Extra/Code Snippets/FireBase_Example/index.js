// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
var firebaseConfig = {
    apiKey: "AIzaSyB35aH2JjlB5oTR753kXWBoplgLz3zd5kE",
    authDomain: "year10design-firebase.firebaseapp.com",
    databaseURL: "https://year10design-firebase.firebaseio.com",
    projectId: "year10design-firebase",
    storageBucket: "year10design-firebase.appspot.com",
    messagingSenderId: "462057173057",
    appId: "1:462057173057:web:b7beb64aa198e9e69316c0",
    measurementId: "G-D66K8MFXN5"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
var database = firebase.database();
//firebase.analytics();

var UpdateDisplay = firebase.database().ref('users/');
UpdateDisplay.on('value', (snapshot) =>{
    const data = snapshot.val();

    dataStr = JSON.stringify(data)
    console.log(data)
    
    Object.keys(data).forEach(key=>{
        console.log(key)
        var entryDiv=document.createElement("div")
        entryDiv.className="entry"
        var nameDiv=document.createElement("div")
        nameDiv.className="name"
        nameDiv.innerHTML=data[key]["Name"]
        var foodDiv=document.createElement("div")
        foodDiv.className="food"
        foodDiv.innerHTML=data[key]["Food"]
        entryDiv.appendChild(nameDiv)
        entryDiv.appendChild(foodDiv)
        document.body.appendChild(entryDiv)
    })
    
});