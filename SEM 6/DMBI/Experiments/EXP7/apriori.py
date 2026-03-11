import pandas as pd
from itertools import combinations

class Apriori:
    def __init__(self, min_sup=0.3, min_conf=0.6, min_lift=1.0):
        self.min_sup = min_sup
        self.min_conf = min_conf
        self.min_lift = min_lift
        self.transactions = []
        
    def fit(self, data):
        self.transactions = data
        self.items = sorted(set(i for t in data for i in t))
        self.freq_itemsets = {}
        self.rules = []
        self._apriori()
        self._generate_rules()
        return self
        
    def _support(self, itemset):
        return sum(1 for t in self.transactions if all(i in t for i in itemset)) / len(self.transactions)
    
    def _apriori(self):
        
        candidates = [[i] for i in self.items]
        k = 1
        while candidates:
            
            frequent = {}
            for c in candidates:
                sup = self._support(c)
                if sup >= self.min_sup:
                    frequent[tuple(sorted(c))] = sup
            
            if not frequent:
                break
                
            self.freq_itemsets[k] = frequent
            
            
            k += 1
            candidates = []
            prev_items = list(self.freq_itemsets[k-1].keys())
            for i in range(len(prev_items)):
                for j in range(i+1, len(prev_items)):
                    
                    if list(prev_items[i])[:-1] == list(prev_items[j])[:-1]:
                        candidate = sorted(set(prev_items[i] + prev_items[j]))
                        
                        subsets = combinations(candidate, len(candidate)-1)
                        if all(tuple(sorted(s)) in self.freq_itemsets[k-1] for s in subsets):
                            candidates.append(candidate)
    
    def _generate_rules(self):
        for k in range(2, max(self.freq_itemsets.keys())+1):
            for itemset in self.freq_itemsets[k]:
                itemset = list(itemset)
                for i in range(1, len(itemset)):
                    for ant in combinations(itemset, i):
                        ant = list(ant)
                        cons = [i for i in itemset if i not in ant]
                        
                        sup_ant = self.freq_itemsets[len(ant)][tuple(sorted(ant))]
                        sup_itemset = self.freq_itemsets[k][tuple(sorted(itemset))]
                        
                        conf = sup_itemset / sup_ant
                        sup_cons = self.freq_itemsets[len(cons)][tuple(sorted(cons))]
                        lift = conf / sup_cons
                        
                        if conf >= self.min_conf and lift >= self.min_lift:
                            self.rules.append({
                                'antecedent': ' + '.join(ant),
                                'consequent': ' + '.join(cons),
                                'support': round(sup_itemset, 3),
                                'confidence': round(conf, 3),
                                'lift': round(lift, 3)
                            })
    
    def display_rules(self, n=10):
        df = pd.DataFrame(self.rules).sort_values('lift', ascending=False)
        print(f"\nTop {min(n, len(df))} Association Rules:")
        print(df.head(n).to_string(index=False))
        return df

if __name__ == "__main__":
    
    dataset = [
        ['white-monster', 'max-protein', 'slice-cake'],
        ['white-monster', 'max-protein'],
        ['max-protein', 'slice-cake'],
        ['white-monster', 'max-protein', 'slice-cake', 'pringle-chips'],
        ['white-monster', 'slice-cake'],
        ['max-protein', 'pringle-chips'],
        ['white-monster', 'max-protein', 'pringle-chips'],
        ['white-monster', 'slice-cake', 'cornetto-ice-cream'],
        ['max-protein', 'slice-cake', 'cornetto-ice-cream'],
        ['white-monster', 'max-protein', 'slice-cake', 'cornetto-ice-cream']
    ]
    
    model = Apriori(min_sup=0.3, min_conf=0.6)
    model.fit(dataset)
    model.display_rules()