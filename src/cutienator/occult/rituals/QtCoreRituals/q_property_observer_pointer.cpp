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

//  from src/corelib/kernel/qproperty.cpp, line 603, as _ZN9QtPrivate22BindingEvaluationStateC1EP23QPropertyBindingPrivateP14QBindingStatus
namespace QtPrivate {
inline BindingEvaluationState::BindingEvaluationState(QPropertyBindingPrivate *binding, QBindingStatus *status)
    : binding(binding)
{
    Q_ASSERT(status);
    QBindingStatus *s = status;
    // store a pointer to the currentBindingEvaluationState to avoid a TLS lookup in
    // the destructor (as these come with a non zero cost)
    currentState = &s->currentlyEvaluatingBinding;
    previousState = *currentState;
    *currentState = this;
    binding->clearDependencyObservers();
}
}  // namespace QtPrivate

//  from src/corelib/kernel/qproperty.cpp, line 827, as _ZN24QPropertyObserverPointer25setBindingToNotify_unsafeEP23QPropertyBindingPrivate
inline void QPropertyObserverPointer::setBindingToNotify_unsafe(QPropertyBindingPrivate *binding)
{
    Q_ASSERT(ptr->next.tag() == QPropertyObserver::ObserverNotifiesBinding);
    ptr->binding = binding;
}

//  from src/corelib/kernel/qproperty.cpp, line 816, as _ZN24QPropertyObserverPointer16setChangeHandlerEPFvP17QPropertyObserverP20QUntypedPropertyDataE
inline void QPropertyObserverPointer::setChangeHandler(QPropertyObserver::ChangeHandler changeHandler)
{
    Q_ASSERT(ptr->next.tag() != QPropertyObserver::ObserverIsPlaceholder);
    ptr->changeHandler = changeHandler;
    ptr->next.setTag(QPropertyObserver::ObserverNotifiesChangeHandler);
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

//  from src/corelib/kernel/qproperty.cpp, line 864, as _ZN24QPropertyObserverPointer16evaluateBindingsER15QVarLengthArrayI26QPropertyBindingPrivatePtrLx256EEP14QBindingStatus
inline void QPropertyObserverPointer::evaluateBindings(PendingBindingObserverList &bindingObservers, QBindingStatus *status)
{
    Q_ASSERT(status);
    auto observer = const_cast<QPropertyObserver*>(ptr);
    // See also comment in notify()
    while (observer) {
        QPropertyObserver *next = observer->next.data();

        if (QPropertyObserver::ObserverTag(observer->next.tag()) == QPropertyObserver::ObserverNotifiesBinding) {
            auto bindingToEvaluate = observer->binding;
            QPropertyObserverNodeProtector protector(observer);
            // binding must not be gone after evaluateRecursive_inline
            QPropertyBindingPrivatePtr currentBinding(observer->binding);
            const bool evalStatus = bindingToEvaluate->evaluateRecursive_inline(bindingObservers, status);
            if (evalStatus)
                bindingObservers.push_back(std::move(currentBinding));
            next = protector.next();
        }

        observer = next;
    }
}
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

//  void QPropertyObserverPointer::setChangeHandler(QPropertyObserver::Change
//      Handler changeHandler)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPropertyObserverPointer16setChangeHandlerEPFvP17QPropertyObserverP20QUntypedPropertyDataE(
    QPropertyObserverPointer *self,
    void *changeHandler) {
  self->setChangeHandler(
      reinterpret_cast<QPropertyObserver::ChangeHandler>(changeHandler));
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

#if !defined(QT_NO_DEBUG)
//  void
//      QPropertyObserverPointer::evaluateBindings(PendingBindingObserverList
//      &bindingObservers, QBindingStatus *status)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPropertyObserverPointer16evaluateBindingsER15QVarLengthArrayI26QPropertyBindingPrivatePtrLx256EEP14QBindingStatus(
    QPropertyObserverPointer *self,
    PendingBindingObserverList *bindingObservers,
    QBindingStatus *status) {
  self->evaluateBindings(*bindingObservers, status);
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
