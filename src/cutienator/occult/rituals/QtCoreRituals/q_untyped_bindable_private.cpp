//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qproperty_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qproperty.h>

//  const QtPrivate::QBindableInterface
//      *QUntypedBindablePrivate::getInterface(const QUntypedBindable
//      &bindable)
extern "C" Q_DECL_EXPORT
const QtPrivate::QBindableInterface *ritual_ZN23QUntypedBindablePrivate12getInterfaceERK16QUntypedBindable(
    const QUntypedBindable *bindable) {
  return QUntypedBindablePrivate::getInterface(*bindable);
}

//  QUntypedPropertyData *QUntypedBindablePrivate::getPropertyData(const
//      QUntypedBindable &bindable)
extern "C" Q_DECL_EXPORT
QUntypedPropertyData *ritual_ZN23QUntypedBindablePrivate15getPropertyDataERK16QUntypedBindable(
    const QUntypedBindable *bindable) {
  return QUntypedBindablePrivate::getPropertyData(*bindable);
}

//  QUntypedBindablePrivate::~QUntypedBindablePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QUntypedBindablePrivateD1Ev(QUntypedBindablePrivate *self) {
  delete self;
}
