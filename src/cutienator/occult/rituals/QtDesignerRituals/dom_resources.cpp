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

//  DomResources::DomResources()
extern "C" Q_DECL_EXPORT
DomResources *ritual_ZN12DomResourcesC1Ev() {
  return new DomResources();
}

//  DomResources::~DomResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN12DomResourcesD1Ev(DomResources *self) {
  delete self;
}

//  void DomResources::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN12DomResources4readER16QXmlStreamReader(
    DomResources *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomResources::write(QXmlStreamWriter &writer, const QString
//      &tagName) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12DomResources5writeER16QXmlStreamWriterRK7QString(
    const DomResources *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  bool DomResources::hasAttributeName() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12DomResources16hasAttributeNameEv(const DomResources *self) {
  return self->hasAttributeName();
}

//  QString DomResources::attributeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12DomResources13attributeNameEv(
    const DomResources *self) {
  return new QString(self->attributeName());
}

//  void DomResources::setAttributeName(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN12DomResources16setAttributeNameERK7QString(
    DomResources *self,
    const QString *a) {
  self->setAttributeName(*a);
}

//  void DomResources::clearAttributeName()
extern "C" Q_DECL_EXPORT
void ritual_ZN12DomResources18clearAttributeNameEv(DomResources *self) {
  self->clearAttributeName();
}

//  QList<DomResource *> DomResources::elementInclude() const
extern "C" Q_DECL_EXPORT
QList<DomResource *> *ritual_ZNK12DomResources14elementIncludeEv(
    const DomResources *self) {
  return new QList<DomResource *>(self->elementInclude());
}

//  void DomResources::setElementInclude(const QList<DomResource *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN12DomResources17setElementIncludeERK5QListIP11DomResourceE(
    DomResources *self,
    const QList<DomResource *> *a) {
  self->setElementInclude(*a);
}
