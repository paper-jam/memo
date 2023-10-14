-- ======== SETUP
https://flutter.dev/docs/get-started/install/windows#android-setup


-- ========== FLUTTER



flutter doctor      // chekck configuration
/path_to_android_sdk/sdkmanager



//-- package

//flutter pub add nom_du_package      -- ajout package par download
//pubspec.yaml                        -- config du projet
//pub.dev             -- official repository for package


class MyApp extends StatelessWidget   -- in flutter, almost everything is a widget
Stateless widgets are immutable
Stateful widgets maintain state that might change during the lifetime of the widget



-- ========== DART

//identifiers that start with an underscore (_) are visible only inside the library

//déclaration varaibales : var / dynamic 		-- dynamic permet de changer le type à la volée

print('vous avez ' + age.toString() + ' ans');
print('vous avez $age ans');
print('Dans 10 ans, vous aurez ${age+10} ans');
  
// une liste commence toujours à l'indice 0, elle est désordonnée
// continent des éléments de type dynamic par défaut, sinon List<int> nomList = [...]
nomList.add(7)
nomList.length


// spread operator pour concatenantion des lignes 
if () {} else {};
print('bienvenue ${user ?? 'user'}') // 
// test == 
// != différent de 

// -- 
for (;;) {}							// il existe un while aussi
for (;i < maList.length;i++) {...}  // pour boucler sur une liste
for (var item in maList ) {print(item)} // idem

// fonctions
int nomFonction(int p1, int p2) {... ; return var} 
nomFonction(int p1, int p2) {... ; return var}		// indiquer le type de retour est optionnel
nomFonction(int p1, int p2) => a + b;				// pour une fonction qui ne contient qu'une seule ligne

nomFonction({int p1, int p2}) {...} 				// paramètre nommé 
nomFonction({int p1, int p2=10}) {...} 				// paramètre nommé avec valeur prédéfini
x = nomFonction(p1:5, p2:10}); 						// paramètre nommé -> permet de ne pas respecter l'ordre des param
x = nomFonction(p1:5);								// p2 prend la valeur 10 par défaut

nomFonction(int p1, [int p2]) { if (p2 == null)...} // paramètre optionnel 
nomFonction(int p1, [int p2=0]) { if (p2 > 0)...} // paramètre optionnel 


// ----- les class
// en dart, on peut inclure plusieurs classe ds un seul fichier
void main() {
  Person p1 = Person('Eric'); // new Facultatif et pas recommandé
  print (p1.name);
  Person p2 = Person.fromPerson(p1);
  p2.speak();
}


class Person {
  var name = '';
  Person(this.name);
  Person.fromPerson(Person p): name = p.name {
    print('fin du constructeur');
  }
  void speak() => print ('mon nom est $name');
}


// ----- héritages
void main() {
  Employee e1 = Employee('Boulanger', 'Eric');
  print (e1.name);
  print (e1.jobname);
  e1.speak();
}

class Person {
  var name = '';
  Person(this.name);
  void speak() => print ('mon nom est $name');
 }

class Employee extends Person {
  var jobname='';
  Employee(this.jobname, var name): super(name);
  
  @override
  void speak() => print ('mon vrai nom est $name');
  
}


// ---- CONST FINAL
// const --> valeur doit être affectée à la compilation
const b = 5;
  
// final --> valeur peut être affectée à l'éxécution
final c = 5; 

final now = DateTime.now(); 	// OK
const now = DateTime.now(); 	// ERREUR

// une collection de type CONST, NE peut PAS être modifié
// une collection de type FINAL, peut être modifié
final list1 = [1,2];
list1[0] = 10 ;			// OK
const list2 = [3,4];
list2[0] = 10 ; 		// ERREUR

// ------- asynchronisme

// ----- appel asynchrone
void main() {

  print('Début du code');
  
  // appel asynchrone 
  var res2= addAsync(10,8);
  res2.then((value) {
    print(value); 
  });

  print(res2);
  print('Fin du code');

}

Future<int> addAsync(int a, int b) async {
  const duration = Duration(seconds: 5);
  await Future.delayed(duration, (){
    print('Fin des 5 secondes');
  });
  return a + b;
  
}

// ------appel sequentiel 
void main() async {

  print('Début du code');
  
  // appel asynchrone 
  var res2= await addAsync(10,8);
  print(res2);
  print('Fin du code');

}

Future<int> addAsync(int a, int b) async {
  const duration = Duration(seconds: 5);
  await Future.delayed(duration, (){
    print('Fin des 5 secondes');
  });
  return a + b;
}











