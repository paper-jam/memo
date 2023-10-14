


# -- ========== divers
rails new monblog -d mysql #or sqlite3 default 

bundle install				# à chaque modif  du fichier gemfile

# -- ========== création
rails generate controller home index	# génère 2 controleurs

# -- ========== BDD
# créé une migration
rails g migration CreateArticle titre:string  libelle:text

# créé la classe Admin qui hérite de User
rails g model admin --parent user

migration : change_table timestamp -> créé 2 champs (creation / last update)



rails db:migrate   # applique les migrations
rails db:rollback

# -- ========== rails enligne de commande
rails route             # affiche les routes
rails g migration
rails g controller
rails g model		# model = nom de la table au singulier
rails console       # (ou rails c) passe en mode IRB

# -- ========== méthode bdd ACTIVERECORD
# console IRB, clear screen=>créer fichier .irbrc

p.save
p.find
p.destroy           # delete BDD puis freeze l'instance 
p=nomClass.new      # puis p.save (création nouvel objet)
p.create(...        # créé instance puis insert BDD
p.update            # modifie instance et update BDD

Article.create(titre: "table", libelle: "Ikea Rosa", qte: 50)
Article.create(titre: "chaise", libelle: "sokoa tertio", qte: 10)
Article.create(titre: "chevet", libelle: "douce nuit", qte: 103)
Article.create(titre: "armoire", libelle: "La normande", qte: 4)

Article.find(4)
Article.first
Article.last
Article.all
Article.count
lesArticles = Article.all   # ActiveRecord::Relation
lesArticles[0]              # premier article

# dans l'aide, chercher à ActiveRecord::Relation
Article.order(:titre)
Article.where(titre: "chaise")
Article.destroy_all         # select ts les enregs, puis les suppr uns par un
Article.delete_all          # utilis e directement requete SQL

# -- ========== bootstrap
class col-xs-xx col-sm-xx col-md-xx col-lg-xx # // very small/small/medium/large 

# -- ==========

# -- ==========

# -- ==========
# -- ==========
# -- ==========

rails s // demarre
rails server // idem

rails generate controller home index

