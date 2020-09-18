(define (domain lunar)
(:predicates 	(at ?place)
		(in ?item ?place)
		(has ?item)
		(experiment ?place))

(:action navigate 	:parameters (?placefrom ?placeto)
			:precondition 	(and (at ?placefrom)
					     (not (at ?placeto)))
			:effect 	(and (at ?placeto)
					     (not (at ?placefrom))) )

(:action pickup 	:parameters (?item ?place) 
			:precondition 	(and (at ?place)
					     (in ?item ?place))
			:effect 	(and (not (in ?item ?place))
					     (has ?item)) )

(:action dropoff 	:parameters (?item ?place)
			:precondition 	(and (at ?place)
					     (has ?item))
			:effect 	(and (not (has ?item))
					     (in ?item ?place)) )

(:action science 	:parameters (?place)
			:precondition 	(and (at ?place)
					     (not (experiment ?place)))
			:effect		(experiment ?place) ) )

