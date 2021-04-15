import os


def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes


def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """

    t1w = create_key('sub-{subject}/{session}/anat/sub-{subject}_{session}_run-0{item:01d}_T1w')
    task_fonologico = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-fonologico_run-0{item:01d}_bold')
    task_semantico = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-semantico__run-0{item:01d}_bold')
    task_nomeacaoovert = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-nomeacaoovert__run-0{item:01d}_bold')
    task_nomeacaoinner = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-nomeacaoinner_run-0{item:01d}_bold')

    info = {
                t1w: [],
                task_fonologico: [],
                task_semantico: [],
                task_nomeacaoovert: [],
                task_nomeacaoinner: []
            }

    for idx, s in enumerate(seqinfo):
        if ('MPRAGE_p2_1mm_iso' in s.protocol_name):
            info[t1w].append(s.series_id)
        if ('Fonologico' in s.protocol_name):
            info[task_fonologico].append(s.series_id)
        if ('Semantico' in s.protocol_name):
            info[task_semantico].append(s.series_id)
        if ('Nomeacao_OvertSpeech' in s.protocol_name):
            info[task_nomeacaoovert].append(s.series_id)
        if ('Nomeacao_InnerSpeech' in s.protocol_name):
            info[task_nomeacaoinner].append(s.series_id)
    return info
