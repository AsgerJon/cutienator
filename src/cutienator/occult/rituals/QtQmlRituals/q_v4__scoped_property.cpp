//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4scopedvalue_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4scopedvalue_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::ScopedProperty::ScopedProperty(Scope &scope)
extern "C" Q_DECL_EXPORT
QV4::ScopedProperty *ritual_ZN3QV414ScopedPropertyC1ERNS_5ScopeE(
    QV4::Scope *scope) {
  return new QV4::ScopedProperty(*scope);
}

//  Property *QV4::ScopedProperty::operator->()
extern "C" Q_DECL_EXPORT
QV4::Property *ritual_ZN3QV414ScopedPropertyptEv(QV4::ScopedProperty *self) {
  return self->operator->();
}

//  const Property *QV4::ScopedProperty::operator const QV4::Property *()
//      const
extern "C" Q_DECL_EXPORT
const QV4::Property *ritual_ZNK3QV414ScopedPropertycvPKNS_8PropertyEEv(
    const QV4::ScopedProperty *self) {
  return self->operator const QV4::Property *();
}

//  Property *QV4::ScopedProperty::operator QV4::Property *()
extern "C" Q_DECL_EXPORT
QV4::Property *ritual_ZN3QV414ScopedPropertycvPNS_8PropertyEEv(
    QV4::ScopedProperty *self) {
  return self->operator QV4::Property *();
}

//  QV4::ScopedProperty::~ScopedProperty()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414ScopedPropertyD1Ev(QV4::ScopedProperty *self) {
  delete self;
}
