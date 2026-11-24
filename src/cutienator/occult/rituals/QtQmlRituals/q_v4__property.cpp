//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4property_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4property_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4global_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Property::fullyPopulated(PropertyAttributes *attrs)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Property14fullyPopulatedEPNS_18PropertyAttributesE(
    QV4::Property *self,
    QV4::PropertyAttributes *attrs) {
  self->fullyPopulated(attrs);
}

//  void QV4::Property::completed(PropertyAttributes *attrs)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Property9completedEPNS_18PropertyAttributesE(
    QV4::Property *self,
    QV4::PropertyAttributes *attrs) {
  self->completed(attrs);
}

//  bool QV4::Property::isSubset(const PropertyAttributes &attrs, const
//      Property *other, PropertyAttributes otherAttrs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Property8isSubsetERKNS_18PropertyAttributesEPKS0_S1_(
    const QV4::Property *self,
    const QV4::PropertyAttributes *attrs,
    const QV4::Property *other,
    const QV4::PropertyAttributes *otherAttrs) {
  return self->isSubset(*attrs, other, *otherAttrs);
}

//  Heap::FunctionObject *QV4::Property::getter() const
extern "C" Q_DECL_EXPORT
QV4::Heap::FunctionObject *ritual_ZNK3QV48Property6getterEv(
    const QV4::Property *self) {
  return self->getter();
}

//  Heap::FunctionObject *QV4::Property::setter() const
extern "C" Q_DECL_EXPORT
QV4::Heap::FunctionObject *ritual_ZNK3QV48Property6setterEv(
    const QV4::Property *self) {
  return self->setter();
}

//  void QV4::Property::setGetter(FunctionObject *g)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Property9setGetterEPNS_14FunctionObjectE(
    QV4::Property *self,
    QV4::FunctionObject *g) {
  self->setGetter(g);
}

//  void QV4::Property::setSetter(FunctionObject *s)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Property9setSetterEPNS_14FunctionObjectE(
    QV4::Property *self,
    QV4::FunctionObject *s) {
  self->setSetter(s);
}

//  void QV4::Property::copy(const Property *other, PropertyAttributes attrs)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Property4copyEPKS0_NS_18PropertyAttributesE(
    QV4::Property *self,
    const QV4::Property *other,
    const QV4::PropertyAttributes *attrs) {
  self->copy(other, *attrs);
}

//  QV4::Property::Property()
extern "C" Q_DECL_EXPORT
QV4::Property *ritual_ZN3QV48PropertyC1Ev() {
  return new QV4::Property();
}

//  QV4::Property::Property(Heap::FunctionObject *getter,
//      Heap::FunctionObject *setter)
extern "C" Q_DECL_EXPORT
QV4::Property *ritual_ZN3QV48PropertyC1EPNS_4Heap14FunctionObjectES3_(
    QV4::Heap::FunctionObject *getter,
    QV4::Heap::FunctionObject *setter) {
  return new QV4::Property(getter, setter);
}
