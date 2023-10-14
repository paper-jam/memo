
module Notable

    MOYENNE = 10

    class MoyenneError < RuntimeError
        def initialize(msg="impossible de calculer une moyenne sans note")
    end


    def self.included(base) # est appelée lorsque le module est inclus dans une classe
        def base.test
            puts "test"
        end
    end

    def ajouterNote(note)
        raise ArgumentError, "note n'est pas un entier " if !note.respond_to? :to_i

        notes << note
    end

    def moyenne?
        moyenne > MOYENNE
    end

    def moyenne
        somme = 0
        raise MoyenneError if notes.length == 0
         @notes.each do |uneNote|
            somme += uneNote
        end
        somme / @notes.length
    end

    def notes
        @notes = [] if !@notes
        @notes
    end
end


class Eleve

    include Notable

    #constante, non modifiable, car en majuscule
    MAJORITE = 18
    MOYENNE  = 10

    # variable instakce ou classe
    @variableInstance = ""
    @@variableClasse = ""

    attr_accessor :age, :taille, :nom, :notes
    # attr_writer :
    # attr_reader :

    @@majorite=18

    # méthode de classe
    # peut-être appelée de l'extérieure sans instancier
    def self.bonjour(nom)
        puts "Salut #{nom}"
        puts "bonjour #{@@majorite}"
    end

    def bonjour
        self.class.bonjour(@nom)
    end

    def initialize (nom)
        puts "initialize"
        @nom = nom
        @notes = []
    end

    # private : ttes les méthodes qui suivent sont privées
    private

end


# unEleve = Eleve.new("Jean")
# unEleve.bonjour
class Delegue < Eleve

    def demo
        puts MOYENNE
    end

    def moyenne
        moyenne = super
        moyenne + 1
    end

    def ajouterNote(uneNote)
        super(uneNote + 1)
    end

    def participeAuConseilDeClasse?
        puts "je participe au conseil" if moyenne?
        puts "je NE participe PAS au conseil" if !moyenne?
    end

end

class Professeur
    include Notable
end

# d = Eleve.new("Carole")
# puts d.nom
# d.ajouterNote 10
# d.ajouterNote 15
# d.ajouterNote 19


prof = Professeur.new

begin
    # prof.ajouterNote 12
    puts "La moyenne du prof est de #{prof.moyenne}"
rescue ArgumentError => e
    puts "impossible d'ajouter une note"
rescue ZeroDivisionError
    puts "le professeur n'a pas de note"
ensure
    puts "FIN"
end
