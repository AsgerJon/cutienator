//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qproperty_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qproperty.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
//  -----------------------------------------------------------------------

//  size_t QPropertyBindingPrivate::getSizeEnsuringAlignment()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN23QPropertyBindingPrivate24getSizeEnsuringAlignmentEv() {
  return QPropertyBindingPrivate::getSizeEnsuringAlignment();
}

//  const QtPrivate::BindingFunctionVTable
//      *QPropertyBindingPrivate::bindingFunctionVTable() const
extern "C" Q_DECL_EXPORT
const QtPrivate::BindingFunctionVTable *ritual_ZNK23QPropertyBindingPrivate21bindingFunctionVTableEv(
    const QPropertyBindingPrivate *self) {
  return self->bindingFunctionVTable();
}

//  bool QPropertyBindingPrivate::isUpdating()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QPropertyBindingPrivate10isUpdatingEv(
    QPropertyBindingPrivate *self) {
  return self->isUpdating();
}

//  void QPropertyBindingPrivate::setSticky(bool keep)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPropertyBindingPrivate9setStickyEb(
    QPropertyBindingPrivate *self,
    bool keep) {
  self->setSticky(keep);
}

//  bool QPropertyBindingPrivate::isSticky()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QPropertyBindingPrivate8isStickyEv(
    QPropertyBindingPrivate *self) {
  return self->isSticky();
}

//  void QPropertyBindingPrivate::scheduleNotify()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPropertyBindingPrivate14scheduleNotifyEv(
    QPropertyBindingPrivate *self) {
  self->scheduleNotify();
}

//  QPropertyBindingPrivate::QPropertyBindingPrivate(QMetaType metaType,
//      const QtPrivate::BindingFunctionVTable *vtable, const
//      QPropertyBindingSourceLocation &location, bool isQQmlPropertyBinding)
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivate *ritual_ZN23QPropertyBindingPrivateC1E9QMetaTypePKN9QtPrivate21BindingFunctionVTableERK30QPropertyBindingSourceLocationb(
    const QMetaType *metaType,
    const QtPrivate::BindingFunctionVTable *vtable,
    const QPropertyBindingSourceLocation *location,
    bool isQQmlPropertyBinding) {
  return new QPropertyBindingPrivate(
      *metaType,
      vtable,
      *location,
      isQQmlPropertyBinding);
}

//  QPropertyBindingPrivate::~QPropertyBindingPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPropertyBindingPrivateD1Ev(QPropertyBindingPrivate *self) {
  delete self;
}

//  void QPropertyBindingPrivate::setProperty(QUntypedPropertyData
//      *propertyPtr)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPropertyBindingPrivate11setPropertyEP20QUntypedPropertyData(
    QPropertyBindingPrivate *self,
    QUntypedPropertyData *propertyPtr) {
  self->setProperty(propertyPtr);
}

//  void QPropertyBindingPrivate::setStaticObserver(QtPrivate::QPropertyObser
//      verCallback callback, QtPrivate::QPropertyBindingWrapper
//      bindingWrapper)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPropertyBindingPrivate17setStaticObserverEPFvP20QUntypedPropertyDataEPFb9QMetaTypeS1_N9QtPrivate24QPropertyBindingFunctionEE(
    QPropertyBindingPrivate *self,
    void *callback,
    void *bindingWrapper) {
  self->setStaticObserver(
      reinterpret_cast<QtPrivate::QPropertyObserverCallback>(callback),
      reinterpret_cast<QtPrivate::QPropertyBindingWrapper>(bindingWrapper));
}

//  void QPropertyBindingPrivate::prependObserver(QPropertyObserverPointer
//      observer)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPropertyBindingPrivate15prependObserverE24QPropertyObserverPointer(
    QPropertyBindingPrivate *self,
    const QPropertyObserverPointer *observer) {
  self->prependObserver(*observer);
}

//  QPropertyObserverPointer QPropertyBindingPrivate::takeObservers()
extern "C" Q_DECL_EXPORT
QPropertyObserverPointer *ritual_ZN23QPropertyBindingPrivate13takeObserversEv(
    QPropertyBindingPrivate *self) {
  return new QPropertyObserverPointer(self->takeObservers());
}

//  void QPropertyBindingPrivate::clearDependencyObservers()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPropertyBindingPrivate24clearDependencyObserversEv(
    QPropertyBindingPrivate *self) {
  self->clearDependencyObservers();
}

//  QPropertyObserverPointer
//      QPropertyBindingPrivate::allocateDependencyObserver()
extern "C" Q_DECL_EXPORT
QPropertyObserverPointer *ritual_ZN23QPropertyBindingPrivate26allocateDependencyObserverEv(
    QPropertyBindingPrivate *self) {
  return new QPropertyObserverPointer(self->allocateDependencyObserver());
}

//  QPropertyObserverPointer
//      QPropertyBindingPrivate::allocateDependencyObserver_slow()
extern "C" Q_DECL_EXPORT
QPropertyObserverPointer *ritual_ZN23QPropertyBindingPrivate31allocateDependencyObserver_slowEv(
    QPropertyBindingPrivate *self) {
  return new QPropertyObserverPointer(
      self->allocateDependencyObserver_slow());
}

//  QPropertyBindingSourceLocation QPropertyBindingPrivate::sourceLocation()
//      const
extern "C" Q_DECL_EXPORT
QPropertyBindingSourceLocation *ritual_ZNK23QPropertyBindingPrivate14sourceLocationEv(
    const QPropertyBindingPrivate *self) {
  return new QPropertyBindingSourceLocation(self->sourceLocation());
}

//  QPropertyBindingError QPropertyBindingPrivate::bindingError() const
extern "C" Q_DECL_EXPORT
QPropertyBindingError *ritual_ZNK23QPropertyBindingPrivate12bindingErrorEv(
    const QPropertyBindingPrivate *self) {
  return new QPropertyBindingError(self->bindingError());
}

//  QMetaType QPropertyBindingPrivate::valueMetaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK23QPropertyBindingPrivate13valueMetaTypeEv(
    const QPropertyBindingPrivate *self) {
  return new QMetaType(self->valueMetaType());
}

//  void QPropertyBindingPrivate::unlinkAndDeref()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPropertyBindingPrivate14unlinkAndDerefEv(
    QPropertyBindingPrivate *self) {
  self->unlinkAndDeref();
}

//  bool
//      QPropertyBindingPrivate::evaluateRecursive(PendingBindingObserverList
//      &bindingObservers, QBindingStatus *status)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QPropertyBindingPrivate17evaluateRecursiveER15QVarLengthArrayI26QPropertyBindingPrivatePtrLx256EEP14QBindingStatus(
    QPropertyBindingPrivate *self,
    PendingBindingObserverList *bindingObservers,
    QBindingStatus *status) {
  return self->evaluateRecursive(*bindingObservers, status);
}

#if !defined(QT_NO_DEBUG)
//  bool QPropertyBindingPrivate::evaluateRecursive_inline(PendingBindingObse
//      rverList &bindingObservers, QBindingStatus *status)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QPropertyBindingPrivate24evaluateRecursive_inlineER15QVarLengthArrayI26QPropertyBindingPrivatePtrLx256EEP14QBindingStatus(
    QPropertyBindingPrivate *self,
    PendingBindingObserverList *bindingObservers,
    QBindingStatus *status) {
  return self->evaluateRecursive_inline(*bindingObservers, status);
}
#endif  // !defined(QT_NO_DEBUG)

//  void QPropertyBindingPrivate::notifyNonRecursive(const
//      PendingBindingObserverList &bindingObservers)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPropertyBindingPrivate18notifyNonRecursiveERK15QVarLengthArrayI26QPropertyBindingPrivatePtrLx256EE(
    QPropertyBindingPrivate *self,
    const PendingBindingObserverList *bindingObservers) {
  self->notifyNonRecursive(*bindingObservers);
}

//  NotificationState QPropertyBindingPrivate::notifyNonRecursive()
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivate::NotificationState ritual_ZN23QPropertyBindingPrivate18notifyNonRecursiveEv(
    QPropertyBindingPrivate *self) {
  return self->notifyNonRecursive();
}

//  QPropertyBindingPrivate *QPropertyBindingPrivate::get(const
//      QUntypedPropertyBinding &binding)
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivate *ritual_ZN23QPropertyBindingPrivate3getERK23QUntypedPropertyBinding(
    const QUntypedPropertyBinding *binding) {
  return QPropertyBindingPrivate::get(*binding);
}

//  QUntypedPropertyBinding
//      QPropertyBindingPrivate::makeUntyped(QPropertyBindingPrivate *d)
extern "C" Q_DECL_EXPORT
QUntypedPropertyBinding *ritual_ZN23QPropertyBindingPrivate11makeUntypedEPS_(
    QPropertyBindingPrivate *d) {
  return new QUntypedPropertyBinding(
      QPropertyBindingPrivate::makeUntyped(
          d));
}

//  void QPropertyBindingPrivate::setError(QPropertyBindingError &&e)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPropertyBindingPrivate8setErrorEO21QPropertyBindingError(
    QPropertyBindingPrivate *self,
    QPropertyBindingError *e) {
  self->setError(std::move(*e));
}

//  void QPropertyBindingPrivate::detachFromProperty()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPropertyBindingPrivate18detachFromPropertyEv(
    QPropertyBindingPrivate *self) {
  self->detachFromProperty();
}

//  QPropertyBindingPrivate
//      *QPropertyBindingPrivate::currentlyEvaluatingBinding()
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivate *ritual_ZN23QPropertyBindingPrivate26currentlyEvaluatingBindingEv() {
  return QPropertyBindingPrivate::currentlyEvaluatingBinding();
}

//  bool QPropertyBindingPrivate::hasCustomVTable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QPropertyBindingPrivate15hasCustomVTableEv(
    const QPropertyBindingPrivate *self) {
  return self->hasCustomVTable();
}

//  bool QPropertyBindingPrivate::isQmlBinding() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QPropertyBindingPrivate12isQmlBindingEv(
    const QPropertyBindingPrivate *self) {
  return self->isQmlBinding();
}

//  void
//      QPropertyBindingPrivate::destroyAndFreeMemory(QPropertyBindingPrivate
//      *priv)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPropertyBindingPrivate20destroyAndFreeMemoryEPS_(
    QPropertyBindingPrivate *priv) {
  QPropertyBindingPrivate::destroyAndFreeMemory(priv);
}
