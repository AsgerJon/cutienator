//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsscopesbyid_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsscopesbyid_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  bool QQmlJSScopesById::componentsAreBound() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlJSScopesById18componentsAreBoundEv(
    const QQmlJSScopesById *self) {
  return self->componentsAreBound();
}

//  void QQmlJSScopesById::setComponentsAreBound(bool bound)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSScopesById21setComponentsAreBoundEb(
    QQmlJSScopesById *self,
    bool bound) {
  self->setComponentsAreBound(bound);
}

//  void QQmlJSScopesById::setSignaturesAreEnforced(bool enforced)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSScopesById24setSignaturesAreEnforcedEb(
    QQmlJSScopesById *self,
    bool enforced) {
  self->setSignaturesAreEnforced(enforced);
}

//  bool QQmlJSScopesById::signaturesAreEnforced() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlJSScopesById21signaturesAreEnforcedEv(
    const QQmlJSScopesById *self) {
  return self->signaturesAreEnforced();
}

//  void QQmlJSScopesById::setValueTypesAreAddressable(bool addressable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSScopesById27setValueTypesAreAddressableEb(
    QQmlJSScopesById *self,
    bool addressable) {
  self->setValueTypesAreAddressable(addressable);
}

//  bool QQmlJSScopesById::valueTypesAreAddressable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlJSScopesById24valueTypesAreAddressableEv(
    const QQmlJSScopesById *self) {
  return self->valueTypesAreAddressable();
}

//  void QQmlJSScopesById::setValueTypesAreAssertable(bool assertable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSScopesById26setValueTypesAreAssertableEb(
    QQmlJSScopesById *self,
    bool assertable) {
  self->setValueTypesAreAssertable(assertable);
}

//  bool QQmlJSScopesById::valueTypesAreAssertable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlJSScopesById23valueTypesAreAssertableEv(
    const QQmlJSScopesById *self) {
  return self->valueTypesAreAssertable();
}

//  void QQmlJSScopesById::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSScopesById5clearEv(QQmlJSScopesById *self) {
  self->clear();
}

//  bool QQmlJSScopesById::existsAnywhereInDocument(const QString &id) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlJSScopesById24existsAnywhereInDocumentERK7QString(
    const QQmlJSScopesById *self,
    const QString *id) {
  return self->existsAnywhereInDocument(*id);
}

//  Confidence QQmlJSScopesById::confidence(QQmlJSScope::IsComponentRoot a,
//      QQmlJSScope::IsComponentRoot b)
extern "C" Q_DECL_EXPORT
QQmlJSScopesById::Confidence ritual_ZN16QQmlJSScopesById10confidenceEN11QQmlJSScope15IsComponentRootES1_(
    QQmlJSScope::IsComponentRoot a,
    QQmlJSScope::IsComponentRoot b) {
  return QQmlJSScopesById::confidence(a, b);
}

//  QQmlJSScopesById::~QQmlJSScopesById()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSScopesByIdD1Ev(QQmlJSScopesById *self) {
  delete self;
}
