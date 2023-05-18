// ---------------------------------------------------------------------------------------------
//Authentications
window.LoginDone = LoginDone;
function LoginDone(event) {
  event.preventDefault();
  var Email = document.getElementById("validationCustom01").value;
  var Password = document.getElementById("validationCustom02").value;
  try {
    Login(Email, Password);
  } catch (e) {
    console.log(e.message);
  }
}
// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.2/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.6.2/firebase-analytics.js";
import {
  getAuth,
  signInWithEmailAndPassword,
  onAuthStateChanged,
} from "https://www.gstatic.com/firebasejs/9.6.2/firebase-auth.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDfeDYHwqseDZAoPxGMzqI8gN9axq1RfP8",
  authDomain: "wuzzuf-project.firebaseapp.com",
  projectId: "wuzzuf-project",
  storageBucket: "wuzzuf-project.appspot.com",
  messagingSenderId: "468922707390",
  appId: "1:468922707390:web:fc1f9417234a4487fc9def",
  measurementId: "G-8GSMJ17PT4",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth();

function Login(Email, Password) {
  signInWithEmailAndPassword(auth, Email , Password).catch((error) => {
    console.log(error.message);
    alert("Email or Password is wrong");
  });
}

onAuthStateChanged(auth, (user) => {
  if (user) location.assign("../explore.html");
});
