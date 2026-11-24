//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  DocumentModel::XmlLocation::XmlLocation(int theLine, int theColumn)
extern "C" Q_DECL_EXPORT
DocumentModel::XmlLocation *ritual_ZN13DocumentModel11XmlLocationC1Eii(
    int theLine,
    int theColumn) {
  return new DocumentModel::XmlLocation(theLine, theColumn);
}

//  DocumentModel::XmlLocation::~XmlLocation()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel11XmlLocationD1Ev(
    DocumentModel::XmlLocation *self) {
  delete self;
}
