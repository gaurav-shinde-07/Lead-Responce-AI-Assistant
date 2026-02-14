def mock_intent():
    return {"intent": "Dampness"}

def mock_extraction():
    return """
{
"location":"Bedroom wall",
"trigger":"After rains",
"visible_sign":"Damp patches",
"duration":"Not Available"
}
"""

def mock_questions():
    return """
- How long have you noticed the dampness?
- Is the patch spreading?
- Does this wall face outside?
- Any plumbing line behind this wall?
"""

def mock_response():
    return """
Thank you for reaching out.

You mentioned noticing damp patches on your bedroom wall after rainfall. This could indicate possible moisture ingress, but a detailed inspection would be needed to confirm the exact cause.

To understand this better, could you please share:
• How long you have noticed the dampness?
• Whether the patch is spreading?
• If this wall faces outside?
• Any plumbing lines behind this wall?

As an immediate step, ensure proper ventilation in the room and avoid covering the affected area.

A physical inspection would help identify the root cause and recommend suitable treatment.
"""
