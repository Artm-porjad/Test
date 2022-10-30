from sqlalchemy import text, bindparam

SELECT_DOCUMENTS = '''
SELECT d.id, p.lastname, dir.name, fp.name, d.doc_type, dc.description, f.short_name, d.document_name, d.regnum_mc, dl.linked_doc, d.incoming_date_mc, d.regnum_incoming, d.yac_control, d.ach_control, d.fin_assessment, d.exp_assessment, d.regnum_out, d.out_date, d.dkr_director_signed_date, d.current_matching
FROM documents d
LEFT JOIN foiv f ON d.id_foiv = f.id
LEFT JOIN directions dir ON f.id_directions = dir.id
LEFT JOIN gov_supervisors gs ON f.id_gov_supervisors = gs.id
LEFT JOIN persons p ON gs.id_persons = p.id
LEFT JOIN fed_projects fp on d.id_fed_projects = fp.id
LEFT JOIN doc_status dc on d.id_doc_status = dc.id
LEFT JOIN doc_links dl on d.id = dl.id_documents
'''

SELECT_DIRECTIONS = '''
SELECT d.name
FROM directions d
'''

SELECT_DOCUMENTS_STATUSES = '''
SELECT d.description
FROM doc_status d
'''

SELECT_FED_PROJECTS = '''
SELECT d.name
FROM fed_projects d
'''

SELECT_PERSONS = '''
SELECT p.lastname
FROM persons p
'''

INSERT_ROW = '''
INSERT INTO documents (id, fin_assessment, exp_assessment, id_foiv, id_doc_status, ach_control, yac_control, regnum_mc,
                       regnum_incoming, document_name, regdate_mc, pages_number, incoming_date_mc, out_to_ceki_date,
                       dkr_signed_date, agreement_creation_date, regnum_out, out_date, current_matching,
                       dkr_incoming_date, dkr_director_signed_date, agreement_signed_departments,
                       agreement_signed_former_minister, doc_type, id_fed_projects, id_foiv_supervisors)
WITH id_doc_status AS (
    SELECT id FROM doc_status WHERE description = :id_doc_status
),
id_fed_projects AS (
    SELECT id FROM fed_projects WHERE name = :fed_proj
),
id_foiv_supervisors AS (
    SELECT f.id
    FROM foiv_supervisors f
    LEFT JOIN persons p ON f.id_persons = p.id
    WHERE p.lastname = :ivanov
),
id_foiv AS (
    SELECT f.id
    FROM foiv f
    LEFT JOIN gov_supervisors gs on f.id_gov_supervisors = gs.id
    LEFT JOIN persons p on gs.id_persons = p.id
    LEFT JOIN directions d on f.id_directions = d.id
    WHERE p.lastname = :lastname AND d.name = :dir_name
)
SELECT :id as id, :fin_assessment as fin_assessment, :exp_assessment as exp_assessment, (SELECT * FROM id_foiv) as id_foiv, (SELECT * FROM id_doc_status) as id_doc_status, :ach_control as ach_control, :yac_control as yac_control, :regnum_mc as reqnum_mc, :regnum_incoming as regnum_incoming, :document_name as document_name, :regdate_mc as regdate_mc, :pages_number as pages_number, :incoming_date_mc as incoming_date_mc, :out_to_ceki_date as out_to_ceki_date, :dkr_signed_date as dkr_signed_date, :agreement_creation_date as agreement_creation_date, :regnum_out as regnum_out, :out_date as out_date, :current_matching as current_matching, :dkr_incoming_date as dkr_incoming_date, :dkr_director_signed_date as dkr_director_signed_date, :agreement_signed_departments as agreement_signed_departments, :agreement_signed_former_minister as agreement_signed_former_minister, :doc_type as doc_type, (SELECT * FROM id_fed_projects) as id_fed_projects, (SELECT * FROM id_foiv_supervisors) as id_foiv_supervisors
ON CONFLICT (id)
DO UPDATE
    SET fin_assessment = excluded.fin_assessment,
        exp_assessment = excluded.exp_assessment,
        id_foiv = excluded.id_foiv,
        id_doc_status = excluded.id_doc_status,
        ach_control = excluded.ach_control,
        yac_control = excluded.yac_control,
        regnum_mc = excluded.regnum_mc,
        regnum_incoming = excluded.regnum_incoming,
        document_name = excluded.document_name,
        regdate_mc = excluded.regdate_mc,
        pages_number = excluded.pages_number,
        incoming_date_mc = excluded.incoming_date_mc,
        out_to_ceki_date = excluded.out_to_ceki_date,
        dkr_signed_date = excluded.dkr_signed_date,
        agreement_creation_date = excluded.agreement_creation_date,
        regnum_out = excluded.regnum_out,
        out_date = excluded.out_date,
        current_matching = excluded.current_matching,
        dkr_incoming_date = excluded.dkr_incoming_date,
        dkr_director_signed_date = excluded.dkr_director_signed_date,
        agreement_signed_departments = excluded.agreement_signed_departments,
        agreement_signed_former_minister = excluded.agreement_signed_former_minister,
        doc_type = excluded.doc_type,
        id_fed_projects = excluded.id_fed_projects,
        id_foiv_supervisors = excluded.id_foiv_supervisors

'''


def select_documents_sql():
    return text(SELECT_DOCUMENTS).bindparams()


def select_directions_sql():
    return text(SELECT_DIRECTIONS).bindparams()


def select_documents_statuses_sql():
    return text(SELECT_DOCUMENTS_STATUSES).bindparams()


def select_fed_projects_sql():
    return text(SELECT_FED_PROJECTS).bindparams()


def select_persons_sql():
    return text(SELECT_PERSONS).bindparams()


def insert_row_sql(params):
    return text(INSERT_ROW).bindparams(**params)
