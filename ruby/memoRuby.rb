=begin
	commentaire muli lignes
	doc en ligne : http://devdocs.io/ruby/
=end

# ===== string
varString = "aaa" 
varString.upcase			# mise en majuscule (voir doc pour toutes les méthodes)
"aaa".upcase 				#
"2".to_i					# 
prenom = gets.chomp 		# saisie au clavier ds variable prenom, chomp : suppression saut de ligne
puts "bonjour #{prenom}, comment ca va " + " ce matin ?"
prenom.upcase!				# ! => la variable prenom a été modifiée directement

# ===== integer
2.even?				# fonction ou méthode qui se termine par ? => renvoie un booléen
"2".to_i.even?		# attention au type !
a += 1				# incrémente

# ===== variable et autres
MAJORITE = 18    	# constante, non modifiable, car en majuscule
@variableInstance	# visible seulement dans l'instance de la classe
@@variableClasse    # partagée entre toutes les instances de la même classe
$variableGlobale
:red 				# symbol = micro constante

# ===== condition
if a==b ... elsif ... else ... end  ## && and -- || or -- ! not, a>=b a<=b a!=b
unless a==b ...  else ... end  		# à moins que a ne soit égal à b ....
puts "c'est pair" if 2.even?
defined? variable    	# vrai si la variable est initilisée
a += 1 unless a.zero?	# incrémente a sauf si a est égal à zéro
estCeEgal = a==b ? "egalite" : "inegal"		# si a==b, estCeEgal sera égal à "egalite" sinon "inegal" (expression ternaire)
case var when "val1" ... when "val2"... else ... end

# ===== boucle
while i<0 ... end
for num in 1..10  ... end 
...next... break... 			# next : passe au suivant, break sort de la boucle
loop do ...next...break... end
until a > 10 do ......next...break... end
a += 1 until a > 10
a += 1 while a < 10
3.times do |idx| ... end		#  for idx in 0..2 do
# voir en plus, les itérations sur les arrays et sur les hash.

# ===== tableau
 tab = [ "elem1", "elem2", "elem3"]
 tab = %w{pomme, kiwi, ananas}				# notation + facile
 tab.sort_by{|mot| mot.length}				# tri selon longueur des mots			
 tab.join(", ") 							#=> affiche les éléments séparés par une virgule
 tab.reverse
 tab.first									# premier element du tableau
 tab.push('elem4') OU tab << 'elem4'		# c'est la même chose
 tab[0][2]									# si tableau de tableau
 tab.each do |item|							# si plusieurs instructions 
	puts "bonjour #{item}"}
end 
tab.each {|item| puts "bonjour #{item}"} 	# si une seule instruction, on peut utiliser des accolades
mots = texte.split(' ')						# réparti les mots d'un texte avec un espace comme séparateur 

tab = %w{1 2 3 4 }
tab = tab.map{|valeur| valeur.to_i}			# chaque élément du tableau est passé au to_i
tab.map!(&:to_i)							# idem ligne précédente : nouvelle notation pour ce qui est du &:

# ===== hash
varHash = {}
varHash[:cle]='value1'							# utiliser les symboles pour les clés des Hash
varHash = {nom: "dupont", prenom: "albert"}		# nom et prenom deviennent des symboles
hash.each do |cle,valeur|
	puts "#{cle}, #{valeur}"
end 

# ===== méthodes
# ds une méthode, c'est la dernière ligne qui est retourné, sauf si instruction return avant
def liste(prefix, *noms)	# *param : si l'on ne connait pas le nb de param. attendu
	noms.each do |nom|
		puts "cher #{prefix} #{nom}, bienvenue ! "
	end 				
end	

# ====== divers 
if var.respond_to(:to_s) # si la méthode to_s est appliocable à var...
# un bloc sur une seule ligne peut s'écrire avec {}
# si plusieurs lignes, il faut utiliser un do ... end 

# ====== Proc & bloc & lambda
# -- bloc
def methode(param) ... yield(unParam) ... end 		# definition d'une méthode à laquelle il faudra passer un bloc
methode(params) do ... end 							# appel de la méthode en passant un bloc 
# -- proc
carre = Proc.new(|n| n**2)	# creation bloc memorisé ds une variable
a = [1,2,3]
a.map!(&carre)				# ! => le tableau est modifié directement, &carre => le & transforme la Proc en bloc
							# car la methode map ne fonctionne qu'avec des blocs
# -- lambda
inc = lambda{|valeur| valeur += 1}
inc = ->(valeur){ valeur += 1}		# idem ligne précédente, c'est une nouvelle notation
puts inc.call(25)			# retoune 26

#notes :
# on ne peut passer qu'un seul bloc (car un seul yield), mais on peut passer plusieurs proc en parametres
# lambda : le nb de paramètre doit être identique, le return renvoie à la fonction
# proc : peu importe les paramètres, prends le contôle au dessu de la fonction
# le & permet de convertir un bloc en proc et inversement, lorsqu'on le passe en paramètre

# ====== classe héritage module: voir memoRuby_eleve.rb
# il est possible d'enrichir des classes du core ruby
Class String
	def bonjour
		"bonjour #{self}"s
	end
end
puts "Jean".bonjour 

Cercle::PI 		# accès la constante du module Cercle
require 'date'	# appel d'un module
require_relative 'lib/util'# va chercher un fichier util.rb dans le sous-dossier lib

# module : ni instantiable, ni héritable
module nomModule... end 			# entourer du code de cette façon...
nomModule::nomClasse.methode... 	# permet l'appel ainsi

# ====== modul mixins
class Humain
    include Marche		# Marche est un module, et la classe Humain 
end						# bénéficie des méthodes de ce module

# ====== exceptions
 
begin 
...	 
rescue ArgumentExceptionError
...
rescue ZeroDivisionError
...
ensure
	... code executé qquoiqu'il arrive...
end




