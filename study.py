def assign_role(user_id, roles=None):
    if roles is None:
        roles = []
    roles.append("junior_dev")
    return {"id": user_id, "roles": roles}

print(assign_role(1)) 
print(assign_role(2)) 