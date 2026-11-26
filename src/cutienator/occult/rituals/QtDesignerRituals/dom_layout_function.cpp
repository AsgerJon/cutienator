//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  DomLayoutFunction::DomLayoutFunction()
extern "C" Q_DECL_EXPORT
DomLayoutFunction *ritual_ZN17DomLayoutFunctionC1Ev() {
  return new DomLayoutFunction();
}

//  DomLayoutFunction::~DomLayoutFunction()
extern "C" Q_DECL_EXPORT
void ritual_ZN17DomLayoutFunctionD1Ev(DomLayoutFunction *self) {
  delete self;
}

//  void DomLayoutFunction::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DomLayoutFunction4readER16QXmlStreamReader(
    DomLayoutFunction *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomLayoutFunction::write(QXmlStreamWriter &writer, const QString
//      &tagName) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17DomLayoutFunction5writeER16QXmlStreamWriterRK7QString(
    const DomLayoutFunction *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  bool DomLayoutFunction::hasAttributeSpacing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17DomLayoutFunction19hasAttributeSpacingEv(
    const DomLayoutFunction *self) {
  return self->hasAttributeSpacing();
}

//  QString DomLayoutFunction::attributeSpacing() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17DomLayoutFunction16attributeSpacingEv(
    const DomLayoutFunction *self) {
  return new QString(self->attributeSpacing());
}

//  void DomLayoutFunction::setAttributeSpacing(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DomLayoutFunction19setAttributeSpacingERK7QString(
    DomLayoutFunction *self,
    const QString *a) {
  self->setAttributeSpacing(*a);
}

//  void DomLayoutFunction::clearAttributeSpacing()
extern "C" Q_DECL_EXPORT
void ritual_ZN17DomLayoutFunction21clearAttributeSpacingEv(
    DomLayoutFunction *self) {
  self->clearAttributeSpacing();
}

//  bool DomLayoutFunction::hasAttributeMargin() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17DomLayoutFunction18hasAttributeMarginEv(
    const DomLayoutFunction *self) {
  return self->hasAttributeMargin();
}

//  QString DomLayoutFunction::attributeMargin() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17DomLayoutFunction15attributeMarginEv(
    const DomLayoutFunction *self) {
  return new QString(self->attributeMargin());
}

//  void DomLayoutFunction::setAttributeMargin(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN17DomLayoutFunction18setAttributeMarginERK7QString(
    DomLayoutFunction *self,
    const QString *a) {
  self->setAttributeMargin(*a);
}

//  void DomLayoutFunction::clearAttributeMargin()
extern "C" Q_DECL_EXPORT
void ritual_ZN17DomLayoutFunction20clearAttributeMarginEv(
    DomLayoutFunction *self) {
  self->clearAttributeMargin();
}
