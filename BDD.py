import re

# --- חלק א': מבנה הנתונים ---
class BDDNode:
    def __init__(self, var, low, high):
        self.var = var
        self.low = low
        self.high = high
        self.id = id(self) # מזהה ייחודי להדפסה

# טרמינלים קבועים (Singleton)
node_0 = BDDNode("0", None, None)
node_1 = BDDNode("1", None, None)

# טבלת הגיבוב למניעת כפילויות (Unique Table)
unique_table = {}

# --- חלק ב': הלוגיקה (Reduce) ---
def mk(var, low, high):
    # 1. צמצום יתירות: אם שני הענפים מובילים לאותו מקום - דלג על הצומת
    if low is high:
        return low
    
    # 2. בדיקת ייחודיות: האם הצומת הזה כבר קיים?
    key = (var, low.id, high.id)
    if key in unique_table:
        return unique_table[key]
    
    # 3. יצירת חדש
    new_node = BDDNode(var, low, high)
    unique_table[key] = new_node
    return new_node

# --- פונקציות עזר ---
def restrict(formula, var, value):
    """
    מחליפה משתנה בערך (0 או 1) בתוך הנוסחה.
    משתמשת ב-Regex כדי להחליף מילים שלמות בלבד.
    """
    # \b מסמן גבול של מילה, כדי ש-a לא יחליף את ה-a בתוך 'and'
    pattern = r'\b' + re.escape(var) + r'\b'
    return re.sub(pattern, str(value), formula)

def try_eval(formula):
    try: 
        return bool(eval(formula))
    except: 
        return None

def is_true(f): return try_eval(f) is True
def is_false(f): return try_eval(f) is False

# --- חלק ג': הבנייה (Shannon Expansion) ---
def build(formula, var_order, index=0):
    # תנאי עצירה
    if is_false(formula): return node_0
    if is_true(formula): return node_1
    
    # הגנה מפני חריגה
    if index >= len(var_order):
        raise ValueError(f"Formula not resolved! Remaining: {formula}")

    var = var_order[index]
    
    # צעד הרקורסיה
    low_child = build(restrict(formula, var, 0), var_order, index + 1)
    high_child = build(restrict(formula, var, 1), var_order, index + 1)
    
    return mk(var, low_child, high_child)

# --- הדפסה ---
def print_bdd(node, indent=""):
    if node is node_0:
        print(indent + "Result: 0")
        return
    if node is node_1:
        print(indent + "Result: 1")
        return
        
    print(indent + f"Var: {node.var}")
    print(indent + "  0 -> ", end="")
    print_bdd(node.low, indent + "      ")
    print(indent + "  1 -> ", end="")
    print_bdd(node.high, indent + "      ")