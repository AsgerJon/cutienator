//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4module_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4module_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4global_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::Module::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV46Module12staticVTableEv() {
  return QV4::Module::staticVTable();
}

//  void QV4::Module::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Module10__dataTestEv(QV4::Module *self) {
  self->__dataTest();
}

//  QV4::Heap::Module *QV4::Module::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Module *ritual_ZNK3QV46Module11d_uncheckedEv(
    const QV4::Module *self) {
  return self->d_unchecked();
}

//  QV4::Heap::Module *QV4::Module::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Module *ritual_ZNK3QV46Module1dEv(const QV4::Module *self) {
  return self->d();
}

//  void QV4::Module::evaluate()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Module8evaluateEv(QV4::Module *self) {
  self->evaluate();
}

//  const Value *QV4::Module::resolveExport(PropertyKey key) const
extern "C" Q_DECL_EXPORT
const QV4::Value *ritual_ZNK3QV46Module13resolveExportENS_11PropertyKeyE(
    const QV4::Module *self,
    const QV4::PropertyKey *key) {
  return self->resolveExport(*key);
}

//  ReturnedValue QV4::Module::virtualGet(const Managed *m, PropertyKey id,
//      const Value *receiver, bool *hasProperty)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Module10virtualGetEPKNS_7ManagedENS_11PropertyKeyEPKNS_5ValueEPb(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Value *receiver,
    bool *hasProperty) {
  return QV4::Module::virtualGet(m, *id, receiver, hasProperty);
}

//  PropertyAttributes QV4::Module::virtualGetOwnProperty(const Managed *m,
//      PropertyKey id, Property *p)
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes *ritual_ZN3QV46Module21virtualGetOwnPropertyEPKNS_7ManagedENS_11PropertyKeyEPNS_8PropertyE(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    QV4::Property *p) {
  return new QV4::PropertyAttributes(
      QV4::Module::virtualGetOwnProperty(
          m,
          *id,
          p));
}

//  bool QV4::Module::virtualHasProperty(const Managed *m, PropertyKey id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Module18virtualHasPropertyEPKNS_7ManagedENS_11PropertyKeyE(
    const QV4::Managed *m,
    const QV4::PropertyKey *id) {
  return QV4::Module::virtualHasProperty(m, *id);
}

//  bool QV4::Module::virtualPreventExtensions(Managed *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Module24virtualPreventExtensionsEPNS_7ManagedE(
    QV4::Managed *a0) {
  return QV4::Module::virtualPreventExtensions(a0);
}

//  bool QV4::Module::virtualDefineOwnProperty(Managed *a0, PropertyKey a1,
//      const Property *a2, PropertyAttributes a3)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Module24virtualDefineOwnPropertyEPNS_7ManagedENS_11PropertyKeyEPKNS_8PropertyENS_18PropertyAttributesE(
    QV4::Managed *a0,
    const QV4::PropertyKey *a1,
    const QV4::Property *a2,
    const QV4::PropertyAttributes *a3) {
  return QV4::Module::virtualDefineOwnProperty(a0, *a1, a2, *a3);
}

//  bool QV4::Module::virtualPut(Managed *a0, PropertyKey a1, const Value
//      &a2, Value *a3)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Module10virtualPutEPNS_7ManagedENS_11PropertyKeyERKNS_5ValueEPS4_(
    QV4::Managed *a0,
    const QV4::PropertyKey *a1,
    const QV4::Value *a2,
    QV4::Value *a3) {
  return QV4::Module::virtualPut(a0, *a1, *a2, a3);
}

//  bool QV4::Module::virtualDeleteProperty(Managed *m, PropertyKey id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Module21virtualDeletePropertyEPNS_7ManagedENS_11PropertyKeyE(
    QV4::Managed *m,
    const QV4::PropertyKey *id) {
  return QV4::Module::virtualDeleteProperty(m, *id);
}

//  OwnPropertyKeyIterator *QV4::Module::virtualOwnPropertyKeys(const Object
//      *m, Value *target)
extern "C" Q_DECL_EXPORT
QV4::OwnPropertyKeyIterator *ritual_ZN3QV46Module22virtualOwnPropertyKeysEPKNS_6ObjectEPNS_5ValueE(
    const QV4::Object *m,
    QV4::Value *target) {
  return QV4::Module::virtualOwnPropertyKeys(m, target);
}

//  Heap::Object *QV4::Module::virtualGetPrototypeOf(const Managed *a0)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV46Module21virtualGetPrototypeOfEPKNS_7ManagedE(
    const QV4::Managed *a0) {
  return QV4::Module::virtualGetPrototypeOf(a0);
}

//  bool QV4::Module::virtualSetPrototypeOf(Managed *a0, const Object *proto)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Module21virtualSetPrototypeOfEPNS_7ManagedEPKNS_6ObjectE(
    QV4::Managed *a0,
    const QV4::Object *proto) {
  return QV4::Module::virtualSetPrototypeOf(a0, proto);
}

//  bool QV4::Module::virtualIsExtensible(const Managed *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Module19virtualIsExtensibleEPKNS_7ManagedE(
    const QV4::Managed *a0) {
  return QV4::Module::virtualIsExtensible(a0);
}
