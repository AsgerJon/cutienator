//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlinstantiator_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_object_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlinstantiator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlinstantiator_p_p.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlInstantiator *QQmlInstantiatorPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQmlInstantiator *ritual_ZN23QQmlInstantiatorPrivate6q_funcEv(
    QQmlInstantiatorPrivate *self) {
  return self->q_func();
}

//  const QQmlInstantiator *QQmlInstantiatorPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQmlInstantiator *ritual_ZNK23QQmlInstantiatorPrivate6q_funcEv(
    const QQmlInstantiatorPrivate *self) {
  return self->q_func();
}

//  QQmlInstantiatorPrivate::QQmlInstantiatorPrivate()
extern "C" Q_DECL_EXPORT
QQmlInstantiatorPrivate *ritual_ZN23QQmlInstantiatorPrivateC1Ev() {
  return new QQmlInstantiatorPrivate();
}

//  void QQmlInstantiatorPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlInstantiatorPrivate5clearEv(
    QQmlInstantiatorPrivate *self) {
  self->clear();
}

//  void QQmlInstantiatorPrivate::regenerate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlInstantiatorPrivate10regenerateEv(
    QQmlInstantiatorPrivate *self) {
  self->regenerate();
}

//  void QQmlInstantiatorPrivate::_q_createdItem(int a0, QObject *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlInstantiatorPrivate14_q_createdItemEiP7QObject(
    QQmlInstantiatorPrivate *self,
    int a0,
    QObject *a1) {
  self->_q_createdItem(a0, a1);
}

//  void QQmlInstantiatorPrivate::_q_modelUpdated(const QQmlChangeSet &a0,
//      bool a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlInstantiatorPrivate15_q_modelUpdatedERK13QQmlChangeSetb(
    QQmlInstantiatorPrivate *self,
    const QQmlChangeSet *a0,
    bool a1) {
  self->_q_modelUpdated(*a0, a1);
}

//  QObject *QQmlInstantiatorPrivate::modelObject(int index, bool async)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN23QQmlInstantiatorPrivate11modelObjectEib(
    QQmlInstantiatorPrivate *self,
    int index,
    bool async) {
  return self->modelObject(index, async);
}

//  QQmlInstantiatorPrivate *QQmlInstantiatorPrivate::get(QQmlInstantiator
//      *instantiator)
extern "C" Q_DECL_EXPORT
QQmlInstantiatorPrivate *ritual_ZN23QQmlInstantiatorPrivate3getEP16QQmlInstantiator(
    QQmlInstantiator *instantiator) {
  return QQmlInstantiatorPrivate::get(instantiator);
}

//  const QQmlInstantiatorPrivate *QQmlInstantiatorPrivate::get(const
//      QQmlInstantiator *instantiator)
extern "C" Q_DECL_EXPORT
const QQmlInstantiatorPrivate *ritual_ZN23QQmlInstantiatorPrivate3getEPK16QQmlInstantiator(
    const QQmlInstantiator *instantiator) {
  return QQmlInstantiatorPrivate::get(instantiator);
}

//  void QQmlInstantiatorPrivate::connectModel(QQmlInstantiator *q,
//      QQmlDelegateModelPointer *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlInstantiatorPrivate12connectModelEP16QQmlInstantiatorP24QQmlDelegateModelPointer(
    QQmlInstantiatorPrivate *self,
    QQmlInstantiator *q,
    QQmlDelegateModelPointer *model) {
  self->connectModel(q, model);
}

//  void QQmlInstantiatorPrivate::disconnectModel(QQmlInstantiator *q,
//      QQmlDelegateModelPointer *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlInstantiatorPrivate15disconnectModelEP16QQmlInstantiatorP24QQmlDelegateModelPointer(
    QQmlInstantiatorPrivate *self,
    QQmlInstantiator *q,
    QQmlDelegateModelPointer *model) {
  self->disconnectModel(q, model);
}

#endif  // QT_CONFIG(qml_object_model)
#endif  // QT_CONFIG(qml_delegate_model)
