class TrainData:
    def __init__(self, delimiter=',', label_columns=None):
        if label_columns is None:
            label_columns = []

        self.delimiter = delimiter
        self.label_columns = label_columns

    record_defaults = {
        'Abdominal_Pain': [-1],
        'Abscess': [-1],
        'Acute_Otitis_Media_and_Sinusitis': [-1],
        'Acute_Renal_Failure': [-1],
        'Acute_Respiratory_Failure': [-1],
        'Addiction_Chemical_Dependency': [-1],
        'Addiction_Adult': [-1],
        'Adjustment_Disorders': [-1],
        'Airway_Abnormality_Including_Peritonsillar_Abscess': [-1],
        'Allergy': [-1],
        'Anemia_Non_Sickle_Cell': [-1],
        'Antepartum_Conditions_and_High_Risk_Pregnancy': [-1],
        'Anxiety_and_Personality_Disorders': [-1],
        'Appendicitis': [-1],
        'Arterial_Embolism': [-1],
        'Asthma': [-1],
        'Asthma_Pediatric': [-1],
        'Autism': [-1],
        'Behavioral_Health_Conditions_Adult': [-1],
        'Behavioral_Health_Conditions_Pediatric': [-1],
        'Benign_Gynecologic_Neoplasms': [-1],
        'Benign_Neoplasm': [-1],
        'Benign_Prostatic_Hyperplasia': [-1],
        'Benign_Skin_Neoplasms': [-1],
        'Biliary_Disease_including_Cholecystitis': [-1],
        'Bipolar_Disorders': [-1],
        'Bladder_Cancer': [-1],
        'Blunt_or_Penetrating_Injury': [-1],
        'Bone_Cancer_and_Other_Sarcomas': [-1],
        'Bone_Metastases': [-1],
        'Bone_Limb_Spine_Congenital_Anomaly': [-1],
        'Brain_CNS_Cancer': [-1],
        'Breast_Cancer': [-1],
        'Breast_Conditions_Non_Cancer': [-1],
        'Bronchitis_and_Other_Upper_Respiratory_Disease': [-1],
        'Burns': [-1],
        'Cardiac_Anomaly': [-1],
        'Cardiac_Disease_Adult': [-1],
        'Carditis_and_Cardiomyopathy': [-1],
        'Cataract': [-1],
        'Cervical_and_Other_Female_Genital_Cancer_Including_Precancer': [-1],
        'Chest_Pain_Noncardiac': [-1],
        'Chronic_Kidney_Disease': [-1],
        'Chronic_Obstructive_Pulmonary_Disease': [-1],
        'Chronic_Otitis_Media_and_Sinusitis': [-1],
        'Chronic_Respiratory_Failure_and_Tracheostomy': [-1],
        'Clostridium_Difficile': [-1],
        'Colorectal_Cancer': [-1],
        'Complex_Cardiac_Conditions_Pediatric': [-1],
        'Complication_of_Device_Implant_or_Graft_Cardiovascular': [-1],
        'Complication_of_Device_Implant_or_Graft_General_Medicine_Surgery': [-1],
        'Complication_of_Device_Implant_or_Graft_Ortho': [-1],
        'Complications_of_Labor_Delivery_or_Postpartum_Period': [-1],
        'Complications_of_Surgical_Procedures_or_Medical_Care': [-1],
        'Concussion': [-1],
        'Congenital_Anomaly_Pulmonary': [-1],
        'Congestive_Heart_Failure': [-1],
        'Conjunctivitis': [-1],
        'Contraception': [-1],
        'Coronary_Heart_Disease': [-1],
        'Cystic_Fibrosis': [-1],
        'Deformities_and_Curvature_of_Spine': [-1],
        'Degenerative_Spine_and_Disc_Injury': [-1],
        'Dementia_and_Cognitive_Disorders': [-1],
        'Disease_of_Venous_System_Varicose_Veins_Phlebitis_Hemorrhoids': [-1],
        'Diseases_of_the_Anus_Rectum': [-1],
        'Disorders_of_Hemoglobin_Including_Sickle_Cell': [-1],
        'Dizziness': [-1],
        'Dysrhythmia_and_Cardiac_Arrest': [-1],
        'ENT_Cleft_Lip_Anomaly': [-1],
        'Early_Pregnancy_w_Complication_or_Abortive_Outcome': [-1],
        'Eating_Disorders': [-1],
        'End_Stage_Renal_Disease': [-1],
        'Epilepsy_and_Seizure_Disorders': [-1],
        'Esophageal_Disease_Including_GERD': [-1],
        'Extreme_Immaturity_or_Respiratory_Distress_Syndrome_Neonate': [-1],
        'Eye_Disease_Other': [-1],
        'Fatigue': [-1],
        'Fluid_Electrolyte_Disorder': [-1],
        'Full_Term_Neonate_w_Major_Problems': [-1],
        'Gastritis_and_Gastroduodenal_Ulcer': [-1],
        'Gastroenteritis_and_Intestinal_Infections': [-1],
        'Gastrointestinal_Congenital_Anomaly': [-1],
        'Gastrointestinal_Hemorrhage': [-1],
        'Genetic_Syndromes_Genetic_Carriers',
        'Genitourinary_Congenital_Anomaly',
        'Glaucoma',
        'Gout',
        'Gynecologic_Hormonal_Disorders',
        'Gynecologic_Infectious_Disease',
        'Gynecologic_Wellness_and_Screening',
        'HIV_Infection',
        'Head_and_Neck_Cancers',
        'Headache_Migraine',
        'Hearing_Loss',
        'Heart_Valve_Disease',
        'Hemorrhagic_Stroke',
        'Hepatitis',
        'Hernia',
        'Hip_Fracture',
        'Hodgkins_Lymphoma',
        'Hydrocephalus_and_Spina_Bifida',
        'Hyperlipidemia',
        'Hypertension',
        'Immunological_Deficiency',
        'Inborn_Errors_of_Metabolism',
        'Incontinence',
        'Infertility',
        'Inflammatory_Bowel_Disease',
        'Inflammatory_and_Autoimmune_Diseases',
        'Influenza',
        'Intestinal_Obstruction_and_Diverticular_Disease',
        'Ischemic_Stroke',
        'Late_Effects_of_Neuro_Trauma_Neurovascular_Disease',
        'Learning_Disorders',
        'Leukemias',
        'Liveborn',
        'Liver_Cancer',
        'Liver_Disease_Noninfective',
        'Lung_Cancer',
        'Melanoma',
        'Mens_Reproductive_Health',
        'Meningitis_and_Encephalitis',
        'Mental_Health_Conditions',
        'Mood_Disorders_Episodic',
        'Mood_Disorders_Persistent',
        'Multiple_Myelomas',
        'Multiple_Sclerosis_and_Demyelinating_Diseases',
        'Musculoskeletal_Injury_Hand_Wrist_Forearm',
        'Musculoskeletal_Injury_Knee',
        'Musculoskeletal_Injury_Lower_Leg_Foot_Ankle',
        'Musculoskeletal_Injury_Pelvis_Hip_Femur',
        'Musculoskeletal_Injury_Shoulder_Elbow_Upper_Arm',
        'Myocardial_Infarction',
        'Nausea_and_Vomiting',
        'Neonate_w_Other_Significant_Problems',
        'Neonates_Died_or_Transferred_to_Another_Acute_Care_Facility',
        'Neuro_Pain_and_Neuropathy',
        'Neurologic_Disease_Other',
        'Neurovascular_Diseases',
        'Non_Hodgkin_Lymphoma',
        'Nonspecific_Back_and_Neck_Pain',
        'Nonspecific_Clinical_and_Laboratory_Findings',
        'Normal_Pregnancy_Delivery',
        'Not_Otherwise_Classified_and_Other_Cancers',
        'Nutritional_Deficiencies',
        'Obesity',
        'Open_or_Superficial_Wounds',
        'Oral_Disease_Not_Otherwise_Specified',
        'Orthopedic_Aftercare',
        'Osteoarthritis',
        'Other_Connective_Tissue_Disorders',
        'Other_Diagnoses_of_Pain',
        'Other_Ear_Disease',
        'Other_Endocrine_Disorders',
        'Other_GI_Cancers_Including_Stomach_and_Esophagus',
        'Other_Gastrointestinal_Diagnosis',
        'Other_Hematologic_Disorders',
        'Other_Infectious_and_Parasitic_Diseases',
        'Other_Injury_Not_Otherwise_Specified',
        'Other_Kidney_Bladder_and_Genitourinary_Disease',
        'Other_Musculoskeletal_Injuries_and_Conditions',
        'Other_Postsurgical_Care_Including_Device_Prosthesis_Fitting',
        'Other_Respiratory_Disease_Including_Pleural_Effusion_Fibrosis_Pneumothorax',
        'Other_Skin_Cancers',
        'Other_Therapy_and_Education',
        'Ovarian_Cancer',
        'Pain_Services',
        'Pancreas_Cancer',
        'Pancreatic_Disease',
        'Paralysis',
        'Parkinsons_and_Movement_Disorders',
        'Pelvic_Floor_Disorders',
        'Perinatal_Jaundice',
        'Peripheral_Atherosclerosis_and_Aneurysm_and_Other_Circulatory_Disease',
        'Peritonitis',
        'Pneumonia_Including_Aspiration_Pneumonia',
        'Poisonings_Commonly_Abused_Drugs',
        'Poisonings_and_Toxic_Exposures',
        'Prematurity_w_Major_Problems',
        'Prematurity_w_o_Major_Problems',
        'Primary_Care_All_Adults',
        'Primary_Care_Geriatrics',
        'Primary_Care_Pediatrics',
        'Prostate_Cancer',
        'Psychosis',
        'Pulmonary_and_Other_Heart_Disease',
        'Pulmonary_Disease_Adult',
        'Rash_Non_Allergic',
        'Renal_Cancer',
        'Septic_Arthritis_and_Osteomyelitis',
        'Septicemia',
        'Sexual_Infections',
        'Shock',
        'Skin_Infection',
        'Skull_Fracture_and_Major_Brain_Injury',
        'Sleep_Apnea',
        'Sleep_Disorders',
        'Soft_Tissue_Ulcers_and_Gangrene',
        'Spinal_Cord_Injury',
        'Spinal_Fracture_or_Dislocation',
        'Sports_Medicine',
        'Syncope',
        'Testicular_and_Other_Male_Genitourinary_Cancers',
        'Thyroid_Cancer',
        'Thyroid_Disorders',
        'Tonsillitis',
        'Transient_Ischemic_Attack',
        'Trauma',
        'Trauma_Related_Disorders',
        'Tuberculosis',
        'Urinary_Calculus',
        'Urinary_Tract_Infection',
        'Uterine_Cancer',
        'Vasculitis',
        'Venous_Thromboembolism',
        'education',
        'estimated_age',
        'ever_diag_prediab',
        'financial_class',
        'race',
        'response',
        'sex',
        'zip',
        'norm_age'
        'age': [-1],
        'race': ['U'],
        'sex': ['U'],
        'education': [-1],
        'occupation': ['U'],
        'wealth_rate': [99],
        'no_of_persons': [-1],
        'last_admit_date': [''],
        'last_discharge_date': [''],
        'Allergy and Immunology': [-1],
        'Breast Health': [-1],
        'Burns and Wounds': [-1],
        'Cancer': [-1],
        'Cardiology': [-1],
        'Dermatology': [-1],
        'ENT': [-1],
        'Endocrine': [-1],
        'Gastroenterology': [-1],
        'General Medicine': [-1],
        'General Surgery': [-1],
        'Gynecology': [-1],
        'Infectious Disease': [-1],
        'Neonatology': [-1],
        'Nephrology': [-1],
        'Neurosciences': [-1],
        'Normal Newborn': [-1],
        'Not Assigned': [-1],
        'Obstetrics': [-1],
        'Ophthalmology': [-1],
        'Orthopedics': [-1],
        'Psychiatry': [-1],
        'Pulmonology': [-1],
        'Rheumatology': [-1],
        'Spine': [-1],
        'Urology': [-1],
        'Vascular': [-1],
    }

    def read(self, filenames, compression_type=None, buffer_size=None, batch_size=64, shuffle_buffer_size=8192):
        ds = tf.data.TextLineDataset(filenames, compression_type, buffer_size)
        ds = ds.map(self._parse_line)

        return ds.batch(batch_size)

    def _parse_line(self, line):
        values = tf.decode_csv(line, list(self.record_defaults.values()), field_delim=self.delimiter)
        features = dict(zip(self.record_defaults.keys(), values))

        xs = {inflect.underscore(col): features.pop(col) for col in x_columns}
        ys = {inflect.underscore(col): features.pop(col) for col in self.label_columns}

        true_weight = 4.
        false_weight = 1.
        label_to_weight = {k: tf.cond(tf.equal(v, 1), lambda: true_weight, lambda: false_weight) for k, v in ys.items()}

        xs['_weights'] = label_to_weight

        return xs, ys


def parse_s3_url(s3url):
    o = urlparse(s3url)
    return o.netloc, o.path


def is_s3_url(s):
    if s.startswith('s3://'):
        return True
    return False


def input_fn(input_train, delimiter, batch_size):
    if is_s3_url(input_train) and input_train.endswith('/'):
        bucket, path = parse_s3_url(input_train)
        path = path[1:]

        client = boto3.client('s3')
        objs = client.list_objects(Bucket=bucket, Prefix=path)
        if 'Contents' not in objs:
            raise Exception('No contents under S3 Directory')

        input_train = [content['Key'] for content in objs['Contents'] if not content['Key'].endswith('_SUCCESS')]
        input_train = ['s3://%s/%s' % (bucket, key) for key in input_train]

        import random
        input_train = random.sample(list(input_train), 10)

        for s3_path in input_train:
            print(s3_path)

        print('Found %d files in %s' % (len(input_train), 's3://%s/%s' % (bucket, path)))

    reader = TrainData(delimiter=delimiter, label_columns=service_lines)
    train_ds = reader.read(input_train, batch_size=batch_size)
    return train_ds
