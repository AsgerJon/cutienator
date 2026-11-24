//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlobjectcreator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlobjectcreator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  RequiredPropertyKey::RequiredPropertyKey()
extern "C" Q_DECL_EXPORT
RequiredPropertyKey *ritual_ZN19RequiredPropertyKeyC1Ev() {
  return new RequiredPropertyKey();
}

//  RequiredPropertyKey::RequiredPropertyKey(const QObject *object, const
//      QQmlPropertyData *data)
extern "C" Q_DECL_EXPORT
RequiredPropertyKey *ritual_ZN19RequiredPropertyKeyC1EPK7QObjectPK16QQmlPropertyData(
    const QObject *object,
    const QQmlPropertyData *data) {
  return new RequiredPropertyKey(object, data);
}

//  bool operator==(const RequiredPropertyKey &a, const RequiredPropertyKey
//      &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK19RequiredPropertyKeyS1_(
    const RequiredPropertyKey *a,
    const RequiredPropertyKey *b) {
  return operator==(*a, *b);
}

//  RequiredPropertyKey::~RequiredPropertyKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN19RequiredPropertyKeyD1Ev(RequiredPropertyKey *self) {
  delete self;
}
