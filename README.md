## Project and Process Description
This project uses 10 files, five of the files' data dictionaries are presented below. The data sictionaries that are not present below are the index.hmtl and json files. The code used to prodcue these files are in the file named "PSIPublicationLabel.ipynb" The process taken to produce these files are described in the steps as shown below:
   1) Take the orignal data with 3000 abstracts( ) and labeled buckets data(newModel-Sept 2025(updated).csv) to produce publications_with_newBuckets_labels0.80Named.csv file
   2) Take publications_with_newBuckets_labels0.80Named.csv file and map authors to works to topics and subtopics in order to produce authors_aggregation3(reran).csv
   3) Take publications_with_newBuckets_labels0.80Named.csv file to produce  authors_topic_subtopic5NoDup to make sure no duplicates exist 
   4) Take publications_with_newBuckets_labels0.80Named.csv file and produce authors_per_topic_subtopic_counts(reran).csv to get the counts of the different topic and subtopic combinations
         * Before producing the counts file make sure to clean the "al" from "et al"
   

## Files & Data Dictionary 

### 1) Data Dictionary — works_with_abstracts_updated.csv
coming soon...

### 2) Data Dictionary — newModel-Sept 2025(updated).csv

| Column Name                     | Type        | Description                                                             |
|--------------------------------|-------------|--------------------------------------------------------------------------|
| ID                             | int         | identification number                                                    |
| Topics                         | string      | Assigned main taxonomy topic.                                            |
| Subtopics                      | string/list |  Assigned taxonomy subtopic.                                             |

   
### 3) Data Dictionary — publications_with_newBuckets_labels0.80Named.csv

| Column Name                     | Type        | Description                                                              |
|--------------------------------|-------------|--------------------------------------------------------------------------|
| title                          | string      | Publication title.                                                       |
| abstract                       | string      | Abstract text of the publication.                                        |
| authors                        | string/list | List of publication authors.                                             |
| year                           | integer     | Year of publication.                                                     |
| doi                            | string      | Digital Object Identifier.                                               |
| original_topic_assignment      | string      | Manually assigned or taxonomy-based topic.                               |
| original_subtopic_assignment   | string      | Manually assigned or taxonomy-based subtopic.                            |
| compressed_text                | string      | Condensed form of title + abstract.                                      |
| cleaned_text                   | string      | Fully cleaned and normalized text for modeling.                          |
| semantic_labels_threshold_0_80 | list/string | Semantic topic labels matched at ≥0.80 similarity.                       |
| semantic_subtopic_labels       | list/string | LLM-generated subtopic labels.                                           |
| final_combined_topic           | string      | Final topic combining manual + model labels.                             |
| final_combined_subtopic        | string      | Final subtopic combining manual + model labels.                          |
| hf_indices(0_80)               | list[int]   | HF model topic match indices ≥0.80 threshold.                            |
| hf_topic_names(0_80)           | string      | Names of HF model topics matched ≥0.80 threshold.                        |

### 4) Data Dictionary — authors_aggregation3(reran).csv

| Column Name              | Data Type | Description |
|--------------------------|-----------|-------------|
| author_key               | string    | Unique identifier for each author. |
| author_display_first     | string    | Author's displayed first name. |
| author_display_last      | string    | Author's displayed last name. |
| author_name_variants     | string    | All known name variants for the author (often in a list-like string). |
| author_subtopics_all     | string    | All subtopics associated with the author. |
| num_works                | integer   | Number of works attributed to the author. |
| author_topics_all        | string    | All high-level topics associated with the author. |

   
### 5) Data Dictionary — authors_topic_subtopic5NoDup(reran1)2.csv

| Column Name                                                | Type          | Description                                                                 |
|------------------------------------------------------------|---------------|-----------------------------------------------------------------------------|
| title                                                      | string        | Title of the publication.                                                   |
| abstract                                                   | string        | Abstract text of the publication.                                           |
| year                                                       | integer       | Publication year.                                                            |
| doi                                                        | string        | Digital Object Identifier.                                                  |
| authors                                                    | string/list   | List of authors (delimited string).                                         |
| topic                                                      | string        | Assigned main taxonomy topic.                                               |
| subtopic                                                   | string        | Assigned taxonomy subtopic.                                                 |
| compressed_text                                            | string        | Condensed representation of title + abstract.                               |
| cleaned_text                                               | string        | Fully cleaned and normalized text.                                          |
| embedding_vector                                           | list[float]   | Vector embedding generated by model.                                        |
| clip_score                                                 | float         | Similarity or quality score from CLIP/embedding system.                     |
| matched_topic_index                                        | list[int]     | Indices of matched topics by embedding similarity.                          |
| matched_topic_name                                         | string        | Human-readable names of matched topics.                                     |
| hf_topic_match_indices(0_80)                               | list[int]     | Topic indices matched at ≥0.80 threshold (HF model).                        |
| hf_topic_match_indices(all)                                | list[int]     | All topic indices matched (no threshold).                                   |
| semantically_matched_topicsNames(Title+abstract)_hf_0_80   | string        | Topic names matched semantically at ≥0.80 threshold.                        |
   
### 6) Data Dictionary — authors_per_topic_subtopic_counts(reran).csv

### 6) Data Dictionary — HierarchyData.csv 
| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| Topic       | string    | High-level topic category. |
| Subtopic    | string    | Subtopic under the main Topic (some values may be missing). |
| Count       | float     | Numerical count associated with each Topic/Subtopic pair. |


