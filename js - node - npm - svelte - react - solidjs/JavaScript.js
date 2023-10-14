/* ====== memo javascript */
const PI=3.14
var nom="jean\n"
nom.length

var eleve={				// eleve.nom
	nom:'jean',			// eleve.taille = 140  (rajout ! )
	moyenne:[1,5]
}
"bonjour" + " Jean" // concat
i++							// incrémente
if (b===undefined) {...}	// var non définie
parsint("12")				// renvoie 12 (int) (et parsefloat
Math.round(465.25)			// .ceil (arrondi au sup.)n .random, .round...

// object
myObject = {var1:"test",var 2:"test2"}          // object
myObject.var1 || myObject["var2"]
myObject.newVar = "newvalue"
delete myObject.newVar      // supprime

// ------------------ ARRAY ---------------------
Tvaleur = [1, 2, 'string', true]
Tvaleur.[Tvaleur.length] = "new value"
Tvaleur.push() or Tvaleur.pop()
Tvaleur.splice(2,1)         // supprime le 2ème élément
[...Tvaleur, element]       // ajoute element dans Tarray, renvoie un array

const Titems = [ {name:"bike", price:100}, {name:"computer", price:1000},{name:"book", price:5}];
Titems.filter((item)=>{return item.price<10})		// returns an array, keeps the order
Titems.map((item)=>{return item.name})  			// returns an array, keeps the order
Titems.find((item)=>{return item.name==="book"})	// return an object
Titems.forEach((item)=>{ console.log(item.name)})	// iterate on array
Titems.some((item)=>{return item.price<100})		// returns boolean 
Titems.every((item)=>{return item.price<=1000})		// returns boolean 
Titems.reduce((totalAmount, item)=>{return item.price+ totalAmount},0)		// returns 1105, 0 is the starting value

const Titems = [1,2,3,4,5]
Titems.includes(2)          // easy...

// pour savoir si un object est un array :
typeof varT === "object" && var.hasOwnProperty("length")


// rexexp
regex = /this/;
regex.test(varString);  // true or false
regex = /^this/i;       // case insensitive
regex = /^this/;        // en début de ligne
regex = /this$/;        // en fin de ligne

// comparaison
===    !==                 // strict equality (same value, same type)
==   !=                    // same value only 1 = "1"

// Math
%                   // modulo
var++               // inc

// logical
|| or    && and     // && est prioritaire

// ter
animal === "cat" ? console.log("gardien de chat") : console.log("gardien de chien");
var job = animal === "cat" ? "gardien de chat" : "gardien de chien";

// type checking
typeof {}   //--> object
typeof []   //--> object !!



Nan, Number.isNumber         // Not a Number

// =========== FETCH
// permet d'aller chercher des données sur ...



// =========== PROMISE
// une promesse prend deux paramètres : resolve reject
new Promise((resolve, reject) => {...

// pour appeler la promesse
fonctionQuiRetourneunePromesse.then(...)  .catch(...) . finally(...)

// execute tts les promesses simultanément, 
// retourne un tableau de resultat
promises.all([promesse1, promesse2, promesse3])
	.then(messages => {console.log(messages)}  

// idem, mais s'arrête dès qu'une promesse a fini
// donc ne retourne qu'un résultat
promises.race([promesse1, promesse2, promesse3])
	.then(messages => {console.log(messages)}  


// =========== AWAIT - ASYNC
// une fonction qui comporte un await doit être qualifiée par async 
// une fonction async retourne une promesse
// await bloque l'éxécution du code dans la fonction, mais le code en dehors de la fonction async
async function doStuff() {
  const msg1 = await setTimeoutPromise(250)
  const msg2 = await setTimeoutPromise(500)
}
// use try/catch bloc to handle error
//never using async/await in a loop unless you specifically need to wait for each previous iteration of the loop
// before the next iteration can be completed.



// ---- condition boucles
if (cond) {...} else if (cond) {...} else {...}
switch (cons) {case "A": ... break case "B" ... break default: ... }
(cond) code si vrai : code si faux
for (start;cond;inc) {code}		// avec break ou continue
for (var in iterable) {...}
while (cond) {code}		// idem
do {} while ()

// -- functions
function F1 (a, b=1) {...}   // param par defaut
appelFunction (1,2,3,4,5...) // arguments illimités, les arguments PeP sont dans arguments[]
appelFunction(objet)         // les object sont passés par référence, donc modifiables ds la function
//une fonction peut être une property d'un object
var TmyDoubles = TmyNumbers.map(doubleIt);    // fonction appelée dans un tableau

doubleIt = number => (number *= 2);           // novelle facon d'écrire une fonction


// ---- fonction
var demo = function() {}	// une variable peut contenir une fonction

// -- tools
babel -> javascript compiler

// async / await







// Portée des variables & Hoisting
// attention : une fonction peut accéder à une variable externe et en modifier la valeur !
// une variable déclarée dans un script est globale
// hoisting : à l'interprétation, JS élève toutes les variables d'un script au début de celui-ci !!

// variable this
// - appelé globalement -> objet window
// - appellé au sein d'une méthode -> objet lui-même

// -- MODULES
// export defaut : permet l'export par defaut d'une seul varaible ou fonction
// to import : 
//		in html : <script>type="module" defer src="main.js"</script>

// ---- PURE FUNCTIONS
// -> always return the same result for the same parameter, (no use of random())
// -> no side effect, do not modify variable passed by reference


// -------- DEFER ans ASYNC
// -- loading javascript code faster in the browser
// -- async for small size of js code
// -- defer for big size of js code

// Les scripts avec defer s’exécutent toujours lorsque le DOM est prêt, mais avant l’événement DOMContentLoaded.
// Les scripts avec defer ne bloquent jamais la page. leur ordre d'éxécution est respecté

// Les scripts asynchrones n’attendent pas les uns les autres. ”load-first”
// DOMContentLoaded peut arriver soit avant ou après async, aucune garantie ici.


// ----- JWT : Json Web Token -> 
// nothing to store on the server, the token stores all information about user  
// 3 parts : HEADER + PAYLOAD + SIGNATURE VERIF.
// https://jwt.io/
// sub : subject  = id of the user
// eat / iat : expired at / issued at










// windows
(function() {... }) ()   // isole les variables de l'extérieur (sinon la var devient propriété de Window)
window.alert()
value = window.prompt()
confirm = window.confirm (OK, Annuler ) // renvoie true ou false //
timer = window.setInterval		// timer asynchrone, pas de blocage du code, renvoie un id
timer = window.setTimeout		// idem mais n'exécute qu'une seule fois, renvoie un id
clearInterval, clearTimeout		// permet de stopper un timer

// le DOM
document.getElementById
document.getElementByClassName // tous les éléments de la même classe
document.getElementByTagName // tous les éléments avec le même tag
document.queryselector('.paragraph') // on passe en param, un sélecteur css
document.queryselector('#demo p') 		// le tag p inclus dans un élément de id="#demo"
										// ne renvoie u'un seul résultat
document.queryselectorAll('p')			// renvoie plusieurs élements
document.queryselector('paragraph').classList    // tableau avec les différentes classes
document.queryselector('.paragraph').className = 'paragraph bleu' // modif class
p.classList.remove('bleu')
p.classList.contains('bleu')	// contient-il la classe bleu ?
p.classList.toggle('red')		// alterne
p.style.font-size = "20px"		// attention au tiret
p.innerHtml = 'salut'			// modif le contenu html
p.innerText						// texte brut ! (attention version navigateur)
p.textContent					// idem !! (attention version navigateur)
if (demo.textContent) {}		// permet de tester
.children 						// elément enfant
.chidNodes						// elément enfant, avec le noeud text en +
.chidElementCount
.firstElementChild				// premier element enfant, sans le text
.lastChild
ul.queryselector('li')			// les méthodes s'apliquent aussi à des nodes
.previousElementSibling			// elémént précédent de m^me niveau
.nextElementSibling				// elémént suivant de m^me niveau
.parentElement					//
.parentElement.children			// tous les éléments de même niveau
.removeChild
document.body.appendChild()		// ajoute
var li2 = li.cloneNode(true)	// créé un clone en profondeur
var li2 = document.createElement
.replaceChild					//
.insertbefore					//

// les évènements
	// dans une fct appelée par un écouteur, this a pour valeur la référence de l'élément écouté
	// evt: clic, mouseover, mouseout	// MDN event reference
	// certains event sur annulable		// voir doc MDN currentTarget thisTarget (attentio console Chrome)
lien.addEventListener('click', function(event) {
	e.stopPropagation()			// avec arrêt de la propagation
	//...
	event.preventDefault()
})
p.removeEventlistener
Finput.addEventListener('change',		// event change : pris en compte uniquement lorsqu'on quitte le champ
Finput.addEventListener('keyup',			// n'est pas annulable
Finput.addEventListener('keydown',		// est annulable
Fform.addEventListener('submit',		// pour les formulaires
Fselect.selectedOptions					// liste déroulante , tag html select
Finput.focus()
Finput.blur()							// contraire de focus
document.addEventListener('DOMContentLoaded',  // MDN event reference pour doc sur ts les event

// window
window.scrollY 					// quantité de scroll en pixel
window.getBoundingClientRect 	// taille et position relative // zone affichage (viewport)
window.pageYOffset				//

//  les tailles d'écrans
screen
https://addons.mozilla.org/en-US/firefox/addon/window-resizer-webextension/



// =========== AJAX

// video grakikart
// a la minute 09:46, insertion du resultat dans une requête
// à 10:30 faire une fonction add event listener pour attacher  le code AJAX aux boutons 3COL, 1COL, 6 COL, etc

// pr tester avec connexion lente : utiliser 12:12
// les header CORS permettent de faire du CROSS-DOMAINS

// pour tester du JSON, un serveur de demo qui envoie du JSON
// JSONplaceholder.typicode.com/users

// à 22:55 envoi d'information
// 24:56 encode des information envoyés pour echapper les caratères
// 26:47 utilisation de FormData

// ========= SVG  vidéo Grafikart : https://www.youtube.com/watch?v=39RU-32QzWg&t=512s
// site web flatico: bib
// attribut fill : permet de changer la couleur
// viewbox : taille de l'objet / ratio
// on peut attcher du CSS directement à un SVG : (6:37)
// mettre des class= directement dans le SVG
// 9:57 la balise xlink:ref permet de réutiliser le groupe d'une SVG déj présent sanla pageYOffset
// fill = currentcolor : on prend la couleur de la police du parent
// reprendre  12:35
