//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  DomIncludes::DomIncludes()
extern "C" Q_DECL_EXPORT
DomIncludes *ritual_ZN11DomIncludesC1Ev() {
  return new DomIncludes();
}

//  DomIncludes::~DomIncludes()
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomIncludesD1Ev(DomIncludes *self) {
  delete self;
}

//  void DomIncludes::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomIncludes4readER16QXmlStreamReader(
    DomIncludes *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomIncludes::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11DomIncludes5writeER16QXmlStreamWriterRK7QString(
    const DomIncludes *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  QList<DomInclude *> DomIncludes::elementInclude() const
extern "C" Q_DECL_EXPORT
QList<DomInclude *> *ritual_ZNK11DomIncludes14elementIncludeEv(
    const DomIncludes *self) {
  return new QList<DomInclude *>(self->elementInclude());
}

//  void DomIncludes::setElementInclude(const QList<DomInclude *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11DomIncludes17setElementIncludeERK5QListIP10DomIncludeE(
    DomIncludes *self,
    const QList<DomInclude *> *a) {
  self->setElementInclude(*a);
}
