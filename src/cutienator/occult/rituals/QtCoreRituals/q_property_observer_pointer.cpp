//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qproperty_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qproperty.h>
#include <QtCore/private/qproperty_p.h>
#include <QtCore/qscopedvaluerollback.h>
#include <QtCore/QScopeGuard>
#include <QtCore/qalloc.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/private/qthread_p.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmutex.h>
#include <QtCore/private/qobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/kernel/qproperty.cpp, line 827, as _ZN24QPropertyObserverPointer25setBindingToNotify_unsafeEP23QPropertyBindingPrivate
inline void QPropertyObserverPointer::setBindingToNotify_unsafe(QPropertyBindingPrivate *binding)
{
    Q_ASSERT(ptr->next.tag() == QPropertyObserver::ObserverNotifiesBinding);
    ptr->binding = binding;
}

//  from src/corelib/kernel/qproperty.cpp, line 847, as _ZN24QPropertyObserverPointer18noSelfDependenciesEP23QPropertyBindingPrivate
#if !defined(QT_NO_DEBUG)
inline void QPropertyObserverPointer::noSelfDependencies(QPropertyBindingPrivate *binding)
{
    auto observer = const_cast<QPropertyObserver*>(ptr);
    // See also comment in notify()
    while (observer) {
        if (QPropertyObserver::ObserverTag(observer->next.tag()) == QPropertyObserver::ObserverNotifiesBinding)
            if (observer->binding == binding) {
                qCritical("Property depends on itself!");
                break;
            }

        observer = observer->next.data();
    }

}
#endif  // !defined(QT_NO_DEBUG)
//  -----------------------------------------------------------------------

//  void QPropertyObserverPointer::unlink()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPropertyObserverPointer6unlinkEv(
    QPropertyObserverPointer *self) {
  self->unlink();
}

//  void QPropertyObserverPointer::unlink_fast()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPropertyObserverPointer11unlink_fastEv(
    QPropertyObserverPointer *self) {
  self->unlink_fast();
}

//  void QPropertyObserverPointer::setBindingToNotify(QPropertyBindingPrivate
//      *binding)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPropertyObserverPointer18setBindingToNotifyEP23QPropertyBindingPrivate(
    QPropertyObserverPointer *self,
    QPropertyBindingPrivate *binding) {
  self->setBindingToNotify(binding);
}

//  void QPropertyObserverPointer::setBindingToNotify_unsafe(QPropertyBinding
//      Private *binding)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPropertyObserverPointer25setBindingToNotify_unsafeEP23QPropertyBindingPrivate(
    QPropertyObserverPointer *self,
    QPropertyBindingPrivate *binding) {
  self->setBindingToNotify_unsafe(binding);
}

//  void QPropertyObserverPointer::notify(QUntypedPropertyData
//      *propertyDataPtr)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPropertyObserverPointer6notifyEP20QUntypedPropertyData(
    QPropertyObserverPointer *self,
    QUntypedPropertyData *propertyDataPtr) {
  self->notify(propertyDataPtr);
}

#if !defined(QT_NO_DEBUG)
//  void QPropertyObserverPointer::noSelfDependencies(QPropertyBindingPrivate
//      *binding)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPropertyObserverPointer18noSelfDependenciesEP23QPropertyBindingPrivate(
    QPropertyObserverPointer *self,
    QPropertyBindingPrivate *binding) {
  self->noSelfDependencies(binding);
}
#endif  // !defined(QT_NO_DEBUG)

//  bool QPropertyObserverPointer::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QPropertyObserverPointercvbEv(
    const QPropertyObserverPointer *self) {
  return self->operator bool();
}

//  QPropertyObserverPointer QPropertyObserverPointer::nextObserver() const
extern "C" Q_DECL_EXPORT
QPropertyObserverPointer *ritual_ZNK24QPropertyObserverPointer12nextObserverEv(
    const QPropertyObserverPointer *self) {
  return new QPropertyObserverPointer(self->nextObserver());
}

//  QPropertyBindingPrivate *QPropertyObserverPointer::binding() const
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivate *ritual_ZNK24QPropertyObserverPointer7bindingEv(
    const QPropertyObserverPointer *self) {
  return self->binding();
}

//  void QPropertyObserverPointer::unlink_common()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPropertyObserverPointer13unlink_commonEv(
    QPropertyObserverPointer *self) {
  self->unlink_common();
}

//  QPropertyObserverPointer::~QPropertyObserverPointer()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPropertyObserverPointerD1Ev(
    QPropertyObserverPointer *self) {
  delete self;
}
