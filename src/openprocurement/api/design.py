# -*- coding: utf-8 -*-
from couchdb.design import ViewDefinition


def sync_design(db):
    views = [j for i, j in globals().items() if "view" in i]
    ViewDefinition.sync_many(db, views)


tenders_all_view = ViewDefinition('tenders', 'all', '''function(doc) {
    if(doc.doc_type == 'Tender') {
        emit(doc.tenderID, null);
    }
}''')


tenders_by_dateModified_view = ViewDefinition('tenders', 'by_dateModified', '''function(doc) {
    if(doc.doc_type == 'Tender') {
        emit(doc.dateModified, null);
    }
}''')

tenders_real_by_dateModified_view = ViewDefinition('tenders', 'real_by_dateModified', '''function(doc) {
    if(doc.doc_type == 'Tender' && !doc.mode) {
        emit(doc.dateModified, null);
    }
}''')

tenders_test_by_dateModified_view = ViewDefinition('tenders', 'test_by_dateModified', '''function(doc) {
    if(doc.doc_type == 'Tender' && doc.mode == 'test') {
        emit(doc.dateModified, null);
    }
}''')
