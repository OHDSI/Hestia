SELECT
  c.concept_id,
  c.concept_name,
  c.concept_code,
  c.concept_class_id,
  c.standard_concept,
  c.vocabulary_id
FROM @vocab.concept AS c
WHERE c.concept_id = 192671
;