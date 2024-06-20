
### CARE SITE ###



### CONDITION ###

### CONDITION ERA ###

### CONDITION OCCURRENCE COMBINATIONS ###




### DRUG ###

### DRUG COST ###

### DRUG ERA ###

### DRUG EXPOSURE ###

### OBSERVATION PERIOD ###

### OBSERVATION ###

### PAYER PLAN ###

### PROCEDURE ###

### PERSON ###




### GENERAL ###



# G01: Find concept by concept ID
def find_concept_by_concept_id(concept_id, connection):
    """
    This is the most generic look-up for obtaining concept details associated with a concept identifier. The query is intended as a tool for quick reference for the name, class, level and source vocabulary details associated with a concept identifier.
    
    Parameters:
        concept_id (int): The ID of the concept to retrieve.
        connection: An ibis backend connection object to the OMOP CDM database using the ibis framework.

    Returns:
        DataFrame: The result of the query is an Ibis DataFrame.
    """

    query = (
        connection.table('concept').sql(f"""
                        SELECT
                        c.concept_id,
                        c.concept_name,
                        c.concept_code,
                        c.concept_class_id,
                        c.standard_concept,
                        c.vocabulary_id
                        FROM concept AS c
                        WHERE concept_id = {concept_id}
                        ;
                        """)
    )

    return query


# G02: Find a concept by code from a source vocabulary
def find_concept_by_code_form_a_source_vocabulary(concept_id, vocabulary_id, connection):
    """
    This query obtains the concept details associated with a concept code, such as name, class, level and source vocabulary.

    Only concepts from the Standard Vocabularies can be searched using this query. If you want to translate codes from other Source Vocabularies to Standard Vocabularies use G06 query.
    
    Parameters:
        concept_id (int): The ID of the concept to retrieve.
        vocabulary_id (str): The source vocabulary ID of the concept to retrieve.
        connection: An ibis backend connection object to the OMOP CDM database using the ibis framework.

    Returns:
        DataFrame: The result of the query is an Ibis DataFrame.
    """

    query = (
        connection.table('concept').sql(f"""
            SELECT
            c.concept_id,
            c.concept_name,
            c.concept_code,
            c.concept_class_id,
            c.vocabulary_id
            FROM concept AS c
            WHERE 
            c.concept_code = {concept_id} AND
            c.vocabulary_id = {vocabulary_id} AND
            c.invalid_reason IS NULL
            ;
            """)
        )
    
    return query


# G04: Find synonyms for a given concept
def find_synonyms_for_a_given_concept():


# G05: Translate a code from a source to a standard vocabulary.
def translate_a_code_from_a_source_to_a_standard_vocabulary():


# G06: Find concepts and their descendants that are covered by a given source code
def find_concepts_and_their_descendants_that_are_covered_by_a_given_source_code():


# G07: Find concepts that have a relationship with a given concept
def find_concepts_that_have_a_relationship_with_a_given_concept():


# G08: Find ancestors for a given concept
def find_ancestors_for_a_given_concept():


# G09: Find descendants for a given concept
def find_descendants_for_a_given_concept():


# G10: Find parents for a given concept
def find_parents_for_a_given_concept():


# G11: Find children for a given concept
def find_children_for_a_given_concept():


# G12: List current vocabulary release number
def list_current_vocabulary_release_number():


# G13: List available vocabularies
def list_available_vocabularies():


# G14: Statistics about relationships between concepts
def statistics_about_relationships_between_concepts():


# G15: Statistic about Concepts, Vocabularies, Classes and Levels
def statistic_about_concepts_vocabularies_classes_and_levels():


# G16: Statistics about Condition Mapping of Source Vocabularies
def statistics_about_condition_mapping_of_source_vocabularies():


# G17: Statistics about Drugs Mapping of Source Vocabularies
def statistics_about_drugs_mapping_of_source_vocabularies():

