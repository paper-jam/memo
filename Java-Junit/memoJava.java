JAVA SE : standard edition
JAVA EE : entreprise Edition (serveur)
JAVA ME : pour mobile
JAVA FX : remplcament flex (client riche)
JAVA API : essemble des fonctions de l'API

JDK incus le JRE
J2EE : version entreprise
CLASSPATH : classe à compiler et à exécuter

-- version
une version LTS tous les 3 ans
JAVA SE 11 LTS


-- Eclipse : origine IBM
Eclipse MArket

- convention JAVA
    - 1 fichier par classe (même si on peut mettre 2 classes dans 1 fichier)
    - 1 classe commence par une majuscule, écriture chameau
    - 1 variable commence par une minuscule
    - 1 méthode commence par une minuscule
    - 1 package entièrement en majuscule
    - constante entièrement en majuscule

méthode Main est le point d'entrée, elle doit être placée dans une classe

type : primitif ou objet
    - les var. de type primmitif sont supprimées à la fin du bloc
    - cela ne serait pas le cas
Integer var1 = Integer.valueOf

-- méthode en JAVA
public : la classe est accessible depuis l'ext.
void : ne renvoie rien. Toute méthode doit avoir un type de retour. (sauf...)
static : pas besoin d'instantier pour appeler la méthode
surcharge : la surcharge est résolu à la compilation en java

- passage de param.
    - de type primitif => par valeur (forçage impossible !)
    - de type objet => par référene

commentaire JAVADOC /** ... @author @param  */
pour générer la doc dans Eclipse : PROJECT => GENERATE JAVADOC


-- == Operateur
= ++ --
float af = 3.0f (le f converti )
float gère l'infini donc division par zéro possible

conversion Implicite / Explicite
mon_short= (short) mon_int;

les opérateur arithmétiques sont défini pour des types
INT minimum

-- ==  Promotion entiere
les types BYTE, CHAR, SHORT sont transformés en INT
pour le besoin d'un calcul

-- == opérateurs relationnels et logiques
test sur des types primitifs !!
== test
!= inégalité
> >= < <=
&& ||
resultat = (val1 > val2) ? 3 : 4;

-- == les variables
public final double PI = 3.14159 // constante
static int var // variable de classe
float pi = 3.14_15_92F
portée variable => bloc
une variable n'est pas initialisée par défaut
il l'iniatiliser explicitement

-- == type primitif
byte    1 octet
short   2 octet
int     4 octet
long    8 octet

double  8 octet
float   4 octet
pour utiliser les valeurs flottantes de façon précise
il faut utiliser la classe BigDecimal

-- == CHAR et BOOL
boolean unBool = true;
Boolean.parseBoolean("true");
aucun rapport entre un INT et un booléen !

char 2 octect
char test = '\u4E2D';
Character.isIdeographic(test);
Character.getName(test ) // nom du caratère

//String n'est pas un type primitif !

-- == BIGINTEGER
est une classe immuable
bg = bg.add(1) // et non pas : bg.add(1)

-- == CYCLE DE VIE
system.gc() // appel du garbage collector
les var de type primitives vivent ds un bloc
les var de type objet  vivent jusqu'au passage du GC

-- == TABLEAU
int[] monTableau = {4,5,6} // premier indice -> 0
monTableau = new int[]
monTableau.length
int[][] tabMulti
System.arraycopy // permet de dupliquer un tableau
jav.utils.arrays // fourni des outils pour les tableaux

-- == IF - SWITCH
if (cond) une seule instruction;
if (cond) { plusieurs insctructions }
if (cond) {} else if {} else if {} else {}
rappel : un entier = 0 ou 1 nest pas un booléen
switch(variable){
    case 0 : instructions; break;
    case 1 : instructions;  break;
    default : instructions;
}
-- == BOUCLE
while (exprBool) {instructions}
do {instructions} while (exprBool);
for (...; cond; inc) {instrutions};

int[] tab = ...
for (int valeur : tab) {instructions}; // balaye le tableau
continue; // passe à l'itération suivante
break ; // casse la boucle

-- == STRING : object bâtard !
String s1 = "toto"; // meilleur
String s1 = new String("toto"); // à éviter
.charAt(idx) .indexOf('a') // entre autres
.split('t') // pour découper
.substring(...) // sous chaines
.equals()// égalité entre deux châines
.equalsIgnoreCase()
s2 = s1.toUppercase() // because immutabilité
s2 = s1.replace(...)  // because immutabilité

-- == STRINGBUILDER STRING
StringBuffer // mutable, insensible multithread
StringBuilder // mutable, Sensible multithread !! mais + rapide
strBuff.append(...)

-- == CHAINES ET NUMERIQUE
Integer.parseInt(str,16) //16, base hexa
Integer.toHexString(...)
String.format(...) // https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Formatter.html

-- == STRINGTOKENIZER SCANNER
StringTokenizer // devient obsolète
Scanner         // API plus riche
java.util.regex // extraire des e-mails, ...

-- == CLASSES
class NomClasse
private invisible depuis l'exterieur
this.attribut
il peut y avoir plusieurs constructeurs


-- == MEMBRE STATIC
variable static -> partagée par tous les objets
méthode static -> appelable sans instancier
static private int compteur = 0 // var de classe

-- == PACKAGE
package nom_package
import nom_package.NomClasse
import nom_package.*

-- == VISIBILITE
public private protected
"voisinage" : les membres d'une classe JAVA sont accessibles
depuis les classes d'une même package
idem pour la classe qui doit être PUBLIC
une Class sans Public  est private

-- == ENUMERE
public ENUM Type {
    REVUE, LIVRE
}
Type.REVUE


-- == GENERALISATION HERITAGE
public Class Revue Extends Livre {}
super() // appel de la méthode dans le parent

-- == POLYMORPHISME
if objet instanceof NomClasse
redéfinition d'une méthode dans une classe fille
=> même signature de méthode !
@Override -> indique au compilateur qu'il s'agit d'une redéfinition
et qu'il doit vérifier

-- == FINAL
final class Livre
=> la classe NE peut PAS être dérivée
une méthode FINAL ne peut pas être redéfinie dans une classe fille

-- == CLASSE ABSTRAITE
abstract class NomClasse {}
une méthode peut être abstraite,
dans ce cas la classe doit être abstraite

-- == INTERFACE
une classe peut implémenter plusieurs interfaces
une interface peut hériter de plusieurs interfaces

-- == EXCEPTION
try ... catch ... catch ... finally
dans un catch, et depuis Java 7, on peut attraper
plusieurs exceptions

-- == EXCEPTION hiérarchie
Exception <- exception mère
throw new Exception()

-- == COLLECTION JAVA
ArrayList<Document> lesDocs = new ArrayList<Document>();
List<Document> lesDocs = new ArrayList<Document>();
lesDocs.add(new nomClass...)
List<Document> lesDocs = new LinkedList<Document>();
lesDocs.size() // nbre déléments
for(Document d : lesDocs) {} // iterate

-- == MAP : tableau associatif
Map<String,Document> index = new HashMap<String,Document>();
index.keyset() // ensemble des clés

-- == SET
conteneur sequentiel avec des objets uniques
l'ordre des éléments n'est pas conservé.

-- == ITERATEUR
for(Object o : bib.getDocuments())
// ne fonctionne que si bib.getDocuments retourne un iterator

-- == Math
java.lang.MATH // pas besoin d'import
Math.abs() .random() .secureRandom()
.pow() // puissance
StrictMath // conformité algorithme

-- == SYSTEM
long tps = System.currentTimeMillis()
System.arrayCopy()
System.gc() .getenv()
System.err.println()
Sysem.ini.read()
System.exit() // tue le processus
string src = System.console().readLine()
char[] cc = System.console().readPassword()

-- == DATE
// la classe Date est depréciée
Calendar c = Calendar.getInstance()
c.getTime()
if (c.get(Calendar.MONTH) == Calendar.JANUARY

--== FORMATAGE DATE
SimpleDateFormat sdf = new SimpleDateFormat("dd-MM-yyyy");
String str2 = sdf.format(d);
Date d1  = sdf.parse("11-12-1968"); //

-- == FILE SYSTEM
import java.io.*
File monFichier  = new File("toto.txt");
boolean b = monFichier.createNewFile();
File leRep = new File(".");
File[] lesFichiers = leRep.listFiles();
f.getAbsolutePath() .

import java.nio.*
Path dir = leRep.toPath(); // plus récent, plus complet que IO
//observateur sur un répertoire
WatchService w = FileSystems.getDefault().newWatchService();


-- == CLASSE DE FLUX
Reader / Write -> fichier texte
InputStream / Output Stream -> fichier binaire
FileWriter fw = new FileWriter("toto.txt");
PrintWriter pw = new PrintWriter(fw); // plus rapide

-- == FICHIERS TEXTE
PrintWriter pw =new PrintWriter(new FileWriter(monFichier))) {
    pw.println(bib.getNom());
    ...
-- == FICHIERS BINAIRES
DataOutputStream dos=new DataOutputStream(new BufferedOutputStream(new FileOutputStream(monFichier))))
dos.writeUTF(bib.getNom());
dos.writeInt(bib.getCompteur());

-- == SERIALISATION
// on écrit directement le contenu de la bib.
// dans un fichier
ObjectOutputStream oos =new ObjectOutputStream(new FileOutputStream(monFichier))
oos.writeObject(bib);
// ... mais les classe Biblio et Document
// doivent être sérializable
public final class Bibliotheque implements java.io.Serializable
abstract class Document implements java.io.Serializable{

-- == DE JAVA 8 à JAVA 11
JIGSAW , le système modulaire, nécessite le fichier
module-info.java, à la racine du JAR

possibilité d'implémenter des méthodes privées
dans les interfaces

JAVA 9
API FLOW









