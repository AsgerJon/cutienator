//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  DomChar::DomChar()
extern "C" Q_DECL_EXPORT
DomChar *ritual_ZN7DomCharC1Ev() {
  return new DomChar();
}

//  DomChar::~DomChar()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomCharD1Ev(DomChar *self) {
  delete self;
}

//  int DomChar::elementUnicode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7DomChar14elementUnicodeEv(const DomChar *self) {
  return self->elementUnicode();
}

//  void DomChar::setElementUnicode(int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomChar17setElementUnicodeEi(DomChar *self, int a) {
  self->setElementUnicode(a);
}

//  bool DomChar::hasElementUnicode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7DomChar17hasElementUnicodeEv(const DomChar *self) {
  return self->hasElementUnicode();
}

//  void DomChar::clearElementUnicode()
extern "C" Q_DECL_EXPORT
void ritual_ZN7DomChar19clearElementUnicodeEv(DomChar *self) {
  self->clearElementUnicode();
}
