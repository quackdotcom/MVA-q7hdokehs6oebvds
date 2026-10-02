import random

def recalc(drug):
	delta_t = 1
	toxthresh = 1500
	mtor_act = 10
	mtor_inh = 10
	prot_syn = 10
	traff_eff = 30
	deg_cap = 100
	health = 100
	a1_dead = 0
	a2_dead = 0
	b1_dead = 0
	b2_dead = 0
	c1_dead = 0
	c2_dead = 0
	d1_dead = 0
	d2_dead = 0
	# DIPLOID HEALTHY 
	for i in range (250):
		a_toxthresh = random.randint(15, 20) / 10 * toxthresh
		a_mtor_act = 1 * mtor_act
		a_mtor_inh = 1 * mtor_inh
		a_prot_syn = 1 * prot_syn
		a_traff_eff = 1 * traff_eff
		a_deg_cap = 1 * deg_cap
		a_health = health
		a_savehealth = a_health
		prot_current = 0
    
		for i in range (60):
			prot_current = (prot_current + (a_prot_syn * a_mtor_act) - a_deg_cap * a_traff_eff / a_mtor_inh) * delta_t
			over_tox = prot_current - a_toxthresh
			if over_tox <= 0:
				dmg = 0
			else:
				dmg = (over_tox) / a_toxthresh
				a_health = a_health - dmg
        
		if a_health <= 0:
			a1_dead = a1_dead + 1
		else: 
			a1_dead = a1_dead
            
		a_health = a_savehealth
		prot_current = 0
        
		for i in range (60):
			prot_current = (prot_current + (drug * a_prot_syn * a_mtor_act) - a_deg_cap * a_traff_eff / a_mtor_inh / drug) * delta_t
			over_tox = prot_current - a_toxthresh
			if over_tox <= 0:
				dmg = 0
			else:
				dmg = (over_tox) / a_toxthresh
				a_health = a_health - dmg
        	    
		if a_health <= 0:
			a2_dead = a2_dead + 1
		else: 
			a2_dead = a2_dead
	
	if (100 - a1_dead/250 * 100) == 0:
		abbota = 0
	else:
		abbota = 100 * (a2_dead/250 * 100 - a1_dead/250 * 100) / (100 - a1_dead/250 * 100)

	# ANEUPLOID HEALTHY
	for i in range (250):
		b_toxthresh = random.randint(10, 15) / 10 * toxthresh
		b_mtor_act = random.randint(10, 15) / 10 * mtor_act
		b_mtor_inh = random.randint(100, 125) / 100 * mtor_inh
		b_prot_syn = random.randint(10, 15) / 10 * prot_syn
		b_traff_eff = random.randint(75, 100) / 100 * traff_eff
		b_deg_cap = random.randint(75, 100) / 100 * deg_cap
		b_health = health
		b_savehealth = b_health
		prot_current = 0
    
		for i in range (60):
			prot_current = (prot_current + (b_prot_syn * b_mtor_act) - b_deg_cap * b_traff_eff / b_mtor_inh) * delta_t
			over_tox = prot_current - b_toxthresh
			if over_tox <= 0:
				dmg = 0
			else:
				dmg = (over_tox) / b_toxthresh
				b_health = b_health - dmg
        
		if b_health <= 0:
			b1_dead = b1_dead + 1
		else: 
			b1_dead = b1_dead
            
		b_health = b_savehealth
		prot_current = 0
        
		for i in range (60):
			prot_current = (prot_current + (drug * b_prot_syn * b_mtor_act) - b_deg_cap * b_traff_eff / b_mtor_inh / drug) * delta_t
			over_tox = prot_current - b_toxthresh
			if over_tox <= 0:
				dmg = 0
			else:
				dmg = (over_tox) / b_toxthresh
				b_health = b_health - dmg
            
		if b_health <= 0:
			b2_dead = b2_dead + 1
		else: 
			b2_dead = b2_dead
            
	if (100 - b1_dead/250 * 100) == 0:
		abbotb = 0
	else:
		abbotb = 100 * (b2_dead/250 * 100 - b1_dead/250 * 100) / (100 - b1_dead/250 * 100)

# DIPLOID CANCER
	for i in range (250):
		c_toxthresh = random.randint(10, 15) / 10 * toxthresh
		c_mtor_act = random.randint(10, 20) / 10 * mtor_act
		c_mtor_inh = random.randint(10, 20) / 10 * mtor_inh
		c_prot_syn = random.randint(10, 15) / 10 * prot_syn
		c_traff_eff = random.randint(25, 100) / 100 * traff_eff
		c_deg_cap = random.randint(75, 100) / 100 * deg_cap
		c_health = health
		c_savehealth = c_health
		prot_current = 0
    
		for i in range (60):
			prot_current = (prot_current + (c_prot_syn * c_mtor_act) - c_deg_cap * c_traff_eff / c_mtor_inh) * delta_t
			over_tox = prot_current - c_toxthresh
			if over_tox <= 0:
				dmg = 0
			else:
				dmg = (over_tox) / c_toxthresh
				c_health = c_health - dmg
        	
		if c_health <= 0:
			c1_dead = c1_dead + 1
		else: 
			c1_dead = c1_dead
            
		c_health = c_savehealth
		prot_current = 0
        
		for i in range (60):
			prot_current = (prot_current + (drug * c_prot_syn * c_mtor_act) - c_deg_cap * c_traff_eff / c_mtor_inh / drug) * delta_t
			over_tox = prot_current - c_toxthresh
			if over_tox <= 0:
				dmg = 0
			else:
				dmg = (over_tox) / c_toxthresh
				c_health = c_health - dmg
            
		if c_health <= 0:
			c2_dead = c2_dead + 1
		else: 
			c2_dead = c2_dead
	
	if (100 - c1_dead/250 * 100) == 0:
		abbotc = 0
	else:
		abbotc = 100 * (c2_dead/250 * 100 - c1_dead/250 * 100) / (100 - c1_dead/250 * 100)

# ----------------------
# ANEUPLOID CANCER
	for i in range (250):
		d_toxthresh = random.randint(5, 10) / 10 * toxthresh
		d_mtor_act = random.randint(10, 20) / 10 * mtor_act
		d_mtor_inh = random.randint(10, 20) / 10 * mtor_inh
		d_prot_syn = random.randint(10, 15) / 10 * prot_syn
		d_traff_eff = random.randint(25, 75) / 100 * traff_eff
		d_deg_cap = random.randint(50, 75) / 100 * deg_cap
		d_health = health
		d_savehealth = d_health
		prot_current = 0
    
		for i in range (60):
			prot_current = (prot_current + (d_prot_syn * d_mtor_act) - d_deg_cap * d_traff_eff / d_mtor_inh) * delta_t
			over_tox = prot_current - d_toxthresh
			if over_tox <= 0:
				dmg = 0
			else:
				dmg = (over_tox) / d_toxthresh
				d_health = d_health - dmg
        
		if d_health <= 0:
			d1_dead = d1_dead + 1
		else: 
			d1_dead = d1_dead
            
		d_health = d_savehealth
		prot_current = 0
        
		for i in range (60):
			prot_current = (prot_current + (drug * d_prot_syn * d_mtor_act) - d_deg_cap * d_traff_eff / d_mtor_inh / drug) * delta_t
			over_tox = prot_current - d_toxthresh
			if over_tox <= 0:
				dmg = 0
			else:
				dmg = (over_tox) / d_toxthresh
				d_health = d_health - dmg
            
		if d_health <= 0:
			d2_dead = d2_dead + 1
		else: 
			d2_dead = d2_dead
            
	if (100 - d1_dead/250 * 100) == 0:
		abbotd = 1000
	else:
		abbotd = 100 * (d2_dead/250 * 100 - d1_dead/250 * 100) / (100 - d1_dead/250 * 100)
        
	return{
    "a1_dead": a1_dead,
    "a2_dead": a2_dead,
    "b1_dead": b1_dead,
    "b2_dead": b2_dead,
    "c1_dead": c1_dead,
    "c2_dead": c2_dead,
    "d1_dead": d1_dead,
    "d2_dead": d2_dead,
    "abbota": abbota, 
    "abbotb": abbotb, 
    "abbotc": abbotc, 
    "abbotd": abbotd,}

def optimize(value):
	best_drug = None
	best_score = float('-inf')
	best_metrics = {}
    
	for drug in value:
		metrics = recalc(drug)
		score = metrics["d2_dead"]+ metrics["c2_dead"] - metrics["b2_dead"] - metrics["a2_dead"] - metrics["a1_dead"] - metrics["b1_dead"] - metrics["c1_dead"] - metrics["d1_dead"]
		if score > best_score:
			best_score = score
			best_drug = drug
			best_metrics = metrics
	return best_drug, best_metrics
    
search_space = (i / 100 for i in range(100, 300))
best_drug, metrics = optimize(search_space)
print(f"BEST CONCENTRATION: {best_drug}")
recalc(best_drug)
print("")
print("Diploid Healthy %")
print(metrics["a1_dead"]/250 * 100)
print("Diploid Healthy + Drug %")
print(metrics["a2_dead"]/250 * 100)
print(f"Abbott Diploid Healthy %")
print(metrics["abbota"])
print("")
print("Aneuploid Healthy %")
print(metrics["b1_dead"]/250 * 100)
print("Aneuploid Healthy + Drug %")
print(metrics["b2_dead"]/250 * 100)
print(f"Abbott Aneuploid Healthy %")
print(metrics["abbotb"])
print("")
print("Diploid Cancer %")
print(metrics["c1_dead"]/250 * 100)
print("Diploid Cancer + Drug %")
print(metrics["c2_dead"]/250 * 100)
print(f"Abbott Diploid Cancer %")
print(metrics["abbotc"])
print("")
print("Aneuploid Cancer %")
print(metrics["d1_dead"]/250 * 100)
print("Aneuploid Cancer + Drug %")
print(metrics["d2_dead"]/250 * 100)
print(f"Abbott Aneuploid Cancer %")
print(metrics["abbotd"])
    



