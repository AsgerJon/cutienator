//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  DomLayoutDefault::DomLayoutDefault()
extern "C" Q_DECL_EXPORT
DomLayoutDefault *ritual_ZN16DomLayoutDefaultC1Ev() {
  return new DomLayoutDefault();
}

//  DomLayoutDefault::~DomLayoutDefault()
extern "C" Q_DECL_EXPORT
void ritual_ZN16DomLayoutDefaultD1Ev(DomLayoutDefault *self) {
  delete self;
}

//  void DomLayoutDefault::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DomLayoutDefault4readER16QXmlStreamReader(
    DomLayoutDefault *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomLayoutDefault::write(QXmlStreamWriter &writer, const QString
//      &tagName) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16DomLayoutDefault5writeER16QXmlStreamWriterRK7QString(
    const DomLayoutDefault *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  bool DomLayoutDefault::hasAttributeSpacing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16DomLayoutDefault19hasAttributeSpacingEv(
    const DomLayoutDefault *self) {
  return self->hasAttributeSpacing();
}

//  int DomLayoutDefault::attributeSpacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16DomLayoutDefault16attributeSpacingEv(
    const DomLayoutDefault *self) {
  return self->attributeSpacing();
}

//  void DomLayoutDefault::setAttributeSpacing(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DomLayoutDefault19setAttributeSpacingEi(
    DomLayoutDefault *self,
    int a) {
  self->setAttributeSpacing(a);
}

//  void DomLayoutDefault::clearAttributeSpacing()
extern "C" Q_DECL_EXPORT
void ritual_ZN16DomLayoutDefault21clearAttributeSpacingEv(
    DomLayoutDefault *self) {
  self->clearAttributeSpacing();
}

//  bool DomLayoutDefault::hasAttributeMargin() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16DomLayoutDefault18hasAttributeMarginEv(
    const DomLayoutDefault *self) {
  return self->hasAttributeMargin();
}

//  int DomLayoutDefault::attributeMargin() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16DomLayoutDefault15attributeMarginEv(
    const DomLayoutDefault *self) {
  return self->attributeMargin();
}

//  void DomLayoutDefault::setAttributeMargin(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN16DomLayoutDefault18setAttributeMarginEi(
    DomLayoutDefault *self,
    int a) {
  self->setAttributeMargin(a);
}

//  void DomLayoutDefault::clearAttributeMargin()
extern "C" Q_DECL_EXPORT
void ritual_ZN16DomLayoutDefault20clearAttributeMarginEv(
    DomLayoutDefault *self) {
  self->clearAttributeMargin();
}
