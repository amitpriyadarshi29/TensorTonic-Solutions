def named_entity_recognition(sentences: list, entity_dict: dict) -> list:
    """
    Returns one list of tag strings per sentence.
    """
    result = []

    for sentence in sentences:
        tag = []

        for token in sentence:
            tag.append(entity_dict.get(token, "O"))

        result.append(tag)

    return result