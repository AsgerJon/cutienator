//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsscopesbyid_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsscopesbyid_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/QString>
#include <QtCore/QFlags>

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

//  QString QQmlJSScopesById::id(const QQmlJSScope::ConstPtr &scope, const
//      QQmlJSScope::ConstPtr &referrer, QQmlJSScopesByIdOptions options)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQmlJSScopesById2idERK22QDeferredSharedPointerIK11QQmlJSScopeES5_6QFlagsI22QQmlJSScopesByIdOptionE(
    const QQmlJSScopesById *self,
    const QQmlJSScope::ConstPtr *scope,
    const QQmlJSScope::ConstPtr *referrer,
    int options) {
  return new QString(
      self->id(
          *scope,
          *referrer,
          QFlags<QQmlJSScopesByIdOption>::fromInt(options)));
}

//  QQmlJSScope::ConstPtr QQmlJSScopesById::scope(const QString &id, const
//      QQmlJSScope::ConstPtr &referrer, QQmlJSScopesByIdOptions options)
//      const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK16QQmlJSScopesById5scopeERK7QStringRK22QDeferredSharedPointerIK11QQmlJSScopeE6QFlagsI22QQmlJSScopesByIdOptionE(
    const QQmlJSScopesById *self,
    const QString *id,
    const QQmlJSScope::ConstPtr *referrer,
    int options) {
  return new QQmlJSScope::ConstPtr(
      self->scope(
          *id,
          *referrer,
          QFlags<QQmlJSScopesByIdOption>::fromInt(options)));
}

//  void QQmlJSScopesById::insert(const QString &id, const
//      QQmlJSScope::ConstPtr &scope)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSScopesById6insertERK7QStringRK22QDeferredSharedPointerIK11QQmlJSScopeE(
    QQmlJSScopesById *self,
    const QString *id,
    const QQmlJSScope::ConstPtr *scope) {
  self->insert(*id, *scope);
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

//  std::multimap<QQmlJSScope::ConstPtr, IdWithScope>
//      QQmlJSScopesById::computeComponentRootsToIds()
extern "C" Q_DECL_EXPORT
std::multimap<QQmlJSScope::ConstPtr, QQmlJSScopesById::IdWithScope> *ritual_ZN16QQmlJSScopesById26computeComponentRootsToIdsEv(
    QQmlJSScopesById *self) {
  return new std::multimap<QQmlJSScope::ConstPtr, QQmlJSScopesById::IdWithScope>(
      self->computeComponentRootsToIds());
}

//  Confidence QQmlJSScopesById::confidence(QQmlJSScope::IsComponentRoot a,
//      QQmlJSScope::IsComponentRoot b)
extern "C" Q_DECL_EXPORT
QQmlJSScopesById::Confidence ritual_ZN16QQmlJSScopesById10confidenceEN11QQmlJSScope15IsComponentRootES1_(
    QQmlJSScope::IsComponentRoot a,
    QQmlJSScope::IsComponentRoot b) {
  return QQmlJSScopesById::confidence(a, b);
}

//  bool QQmlJSScopesById::isComponentVisible(const QQmlJSScope::ConstPtr
//      &observed, const QQmlJSScope::ConstPtr &observer,
//      QQmlJSScopesByIdOptions options) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlJSScopesById18isComponentVisibleERK22QDeferredSharedPointerIK11QQmlJSScopeES5_6QFlagsI22QQmlJSScopesByIdOptionE(
    const QQmlJSScopesById *self,
    const QQmlJSScope::ConstPtr *observed,
    const QQmlJSScope::ConstPtr *observer,
    int options) {
  return self->isComponentVisible(
      *observed,
      *observer,
      QFlags<QQmlJSScopesByIdOption>::fromInt(options));
}

//  QQmlJSScopesById::~QQmlJSScopesById()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlJSScopesByIdD1Ev(QQmlJSScopesById *self) {
  delete self;
}

//  a QQmlJSScope::ConstPtr a ritual of QQmlJSScopesById gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSScopesById__QQmlJSScope_ConstPtr(
    QQmlJSScope::ConstPtr *self) {
  delete self;
}

//  a std::multimap<QQmlJSScope::ConstPtr, QQmlJSScopesById::IdWithScope> a
//      ritual of QQmlJSScopesById gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSScopesById__std_multimap_QQmlJSScope_ConstPtr_QQmlJSScopesById_IdWithScope(
    std::multimap<QQmlJSScope::ConstPtr, QQmlJSScopesById::IdWithScope> *self) {
  delete self;
}
