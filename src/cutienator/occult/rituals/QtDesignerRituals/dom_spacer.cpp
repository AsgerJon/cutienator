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

//  DomSpacer::DomSpacer()
extern "C" Q_DECL_EXPORT
DomSpacer *ritual_ZN9DomSpacerC1Ev() {
  return new DomSpacer();
}

//  DomSpacer::~DomSpacer()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomSpacerD1Ev(DomSpacer *self) {
  delete self;
}

//  void DomSpacer::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomSpacer4readER16QXmlStreamReader(
    DomSpacer *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomSpacer::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9DomSpacer5writeER16QXmlStreamWriterRK7QString(
    const DomSpacer *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  bool DomSpacer::hasAttributeName() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9DomSpacer16hasAttributeNameEv(const DomSpacer *self) {
  return self->hasAttributeName();
}

//  QString DomSpacer::attributeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9DomSpacer13attributeNameEv(const DomSpacer *self) {
  return new QString(self->attributeName());
}

//  void DomSpacer::setAttributeName(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomSpacer16setAttributeNameERK7QString(
    DomSpacer *self,
    const QString *a) {
  self->setAttributeName(*a);
}

//  void DomSpacer::clearAttributeName()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomSpacer18clearAttributeNameEv(DomSpacer *self) {
  self->clearAttributeName();
}

//  QList<DomProperty *> DomSpacer::elementProperty() const
extern "C" Q_DECL_EXPORT
QList<DomProperty *> *ritual_ZNK9DomSpacer15elementPropertyEv(
    const DomSpacer *self) {
  return new QList<DomProperty *>(self->elementProperty());
}

//  void DomSpacer::setElementProperty(const QList<DomProperty *> &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomSpacer18setElementPropertyERK5QListIP11DomPropertyE(
    DomSpacer *self,
    const QList<DomProperty *> *a) {
  self->setElementProperty(*a);
}
