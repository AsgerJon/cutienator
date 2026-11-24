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
