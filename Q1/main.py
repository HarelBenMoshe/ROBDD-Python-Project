import BDD
from BDD import build, print_bdd

def run_test(name, formula, var_order):
    print(f"\n{'='*40}")
    print(f"Testing Formula: {name}")
    print(f"Expression: {formula}")
    print(f"Variable Order: {var_order}")
    print(f"{'-'*40}")
    
    try:
        root = build(formula, var_order)
        print("ROBDD Structure:")
        print_bdd(root)
    except Exception as e:
        print(f"Error: {e}")

# ==========================================
# 1. Formulas from Assignment 3 (Question 3)
# ==========================================

# Q3a: F(q /\ H~p) \/ G(p -> XFr)
# הנוסחה מתורגמת למשתנים בוליאניים המייצגים את הביטויים הטמפורליים
f3a = "(q and H_neg_p) or (not p or XFr)"
vars3a = ['p', 'q', 'H_neg_p', 'XFr']
run_test("Q3a", f3a, vars3a)

# Q3b: G(p -> (q U (r /\ Fs)))
f3b = "not p or q_Until_r_and_Fs"
vars3b = ['p', 'q_Until_r_and_Fs']
run_test("Q3b", f3b, vars3b)

# ==========================================
# 2. Formulas from Assignment 3 (Question 4)
# ==========================================

# Q4: Phi = Phi1 -> ~Phi2
# שקול ל: not Phi1 or not Phi2
f4 = "not Phi1 or not Phi2"
vars4 = ['Phi1', 'Phi2']
run_test("Q4 (Main Logic)", f4, vars4)

# בדיקה פנימית של Phi1 (אופציונלי)
# Phi1 = G(p -> Xq)
run_test("Q4 (Phi1 Internal)", "not p or Xq", ['p', 'Xq'])

# בדיקה פנימית של Phi2 (אופציונלי)
# Phi2 = G(p \/ q)
run_test("Q4 (Phi2 Internal)", "p or q", ['p', 'q'])

# ==========================================
# 3. Our Own Formula (Question 1c)
# ==========================================

# נוסחת XOR (משלנו)
my_formula = "(a and not b) or (not a and b)"
my_vars = ['a', 'b']
run_test("My Formula (XOR)", my_formula, my_vars)