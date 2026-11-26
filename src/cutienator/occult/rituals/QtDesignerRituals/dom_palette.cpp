//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  DomPalette::DomPalette()
extern "C" Q_DECL_EXPORT
DomPalette *ritual_ZN10DomPaletteC1Ev() {
  return new DomPalette();
}

//  DomPalette::~DomPalette()
extern "C" Q_DECL_EXPORT
void ritual_ZN10DomPaletteD1Ev(DomPalette *self) {
  delete self;
}

//  void DomPalette::read(QXmlStreamReader &reader)
extern "C" Q_DECL_EXPORT
void ritual_ZN10DomPalette4readER16QXmlStreamReader(
    DomPalette *self,
    QXmlStreamReader *reader) {
  self->read(*reader);
}

//  void DomPalette::write(QXmlStreamWriter &writer, const QString &tagName)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10DomPalette5writeER16QXmlStreamWriterRK7QString(
    const DomPalette *self,
    QXmlStreamWriter *writer,
    const QString *tagName) {
  self->write(*writer, *tagName);
}

//  DomColorGroup *DomPalette::elementActive() const
extern "C" Q_DECL_EXPORT
DomColorGroup *ritual_ZNK10DomPalette13elementActiveEv(
    const DomPalette *self) {
  return self->elementActive();
}

//  DomColorGroup *DomPalette::takeElementActive()
extern "C" Q_DECL_EXPORT
DomColorGroup *ritual_ZN10DomPalette17takeElementActiveEv(DomPalette *self) {
  return self->takeElementActive();
}

//  void DomPalette::setElementActive(DomColorGroup *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN10DomPalette16setElementActiveEP13DomColorGroup(
    DomPalette *self,
    DomColorGroup *a) {
  self->setElementActive(a);
}

//  bool DomPalette::hasElementActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10DomPalette16hasElementActiveEv(const DomPalette *self) {
  return self->hasElementActive();
}

//  void DomPalette::clearElementActive()
extern "C" Q_DECL_EXPORT
void ritual_ZN10DomPalette18clearElementActiveEv(DomPalette *self) {
  self->clearElementActive();
}

//  DomColorGroup *DomPalette::elementInactive() const
extern "C" Q_DECL_EXPORT
DomColorGroup *ritual_ZNK10DomPalette15elementInactiveEv(
    const DomPalette *self) {
  return self->elementInactive();
}

//  DomColorGroup *DomPalette::takeElementInactive()
extern "C" Q_DECL_EXPORT
DomColorGroup *ritual_ZN10DomPalette19takeElementInactiveEv(
    DomPalette *self) {
  return self->takeElementInactive();
}

//  void DomPalette::setElementInactive(DomColorGroup *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN10DomPalette18setElementInactiveEP13DomColorGroup(
    DomPalette *self,
    DomColorGroup *a) {
  self->setElementInactive(a);
}

//  bool DomPalette::hasElementInactive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10DomPalette18hasElementInactiveEv(const DomPalette *self) {
  return self->hasElementInactive();
}

//  void DomPalette::clearElementInactive()
extern "C" Q_DECL_EXPORT
void ritual_ZN10DomPalette20clearElementInactiveEv(DomPalette *self) {
  self->clearElementInactive();
}

//  DomColorGroup *DomPalette::elementDisabled() const
extern "C" Q_DECL_EXPORT
DomColorGroup *ritual_ZNK10DomPalette15elementDisabledEv(
    const DomPalette *self) {
  return self->elementDisabled();
}

//  DomColorGroup *DomPalette::takeElementDisabled()
extern "C" Q_DECL_EXPORT
DomColorGroup *ritual_ZN10DomPalette19takeElementDisabledEv(
    DomPalette *self) {
  return self->takeElementDisabled();
}

//  void DomPalette::setElementDisabled(DomColorGroup *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN10DomPalette18setElementDisabledEP13DomColorGroup(
    DomPalette *self,
    DomColorGroup *a) {
  self->setElementDisabled(a);
}

//  bool DomPalette::hasElementDisabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10DomPalette18hasElementDisabledEv(const DomPalette *self) {
  return self->hasElementDisabled();
}

//  void DomPalette::clearElementDisabled()
extern "C" Q_DECL_EXPORT
void ritual_ZN10DomPalette20clearElementDisabledEv(DomPalette *self) {
  self->clearElementDisabled();
}
