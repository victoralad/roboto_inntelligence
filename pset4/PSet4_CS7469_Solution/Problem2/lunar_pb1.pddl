(define (problem pb1)
(:domain lunar)

(:objects 	site_a site_b site_c 
		cargo_a cargo_b)

(:init 		(in cargo_a site_a)
		(in cargo_b site_b)
		(at site_a))

(:goal		(and (in cargo_a site_b) (experiment site_c))))
