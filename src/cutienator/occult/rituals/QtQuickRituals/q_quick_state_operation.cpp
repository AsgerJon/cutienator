//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickstate_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickstate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QQuickStateOperation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickStateOperation10metaObjectEv(
    const QQuickStateOperation *self) {
  return self->metaObject();
}

//  QString QQuickStateOperation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickStateOperation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickStateOperation::tr(s, c, n));
}

//  void QQuickStateOperation::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickStateOperation22qt_qmlMarker_anonymousEv(
    QQuickStateOperation *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickStateOperation::QQuickStateOperation(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickStateOperation *ritual_ZN20QQuickStateOperationC1EP7QObject(
    QObject *parent) {
  return new QQuickStateOperation(parent);
}

//  ActionList QQuickStateOperation::actions()
extern "C" Q_DECL_EXPORT
QList<QQuickStateAction> *ritual_ZN20QQuickStateOperation7actionsEv(
    QQuickStateOperation *self) {
  return new QList<QQuickStateAction>(self->actions());
}

//  QQuickState *QQuickStateOperation::state() const
extern "C" Q_DECL_EXPORT
QQuickState *ritual_ZNK20QQuickStateOperation5stateEv(
    const QQuickStateOperation *self) {
  return self->state();
}

//  void QQuickStateOperation::setState(QQuickState *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickStateOperation8setStateEP11QQuickState(
    QQuickStateOperation *self,
    QQuickState *state) {
  self->setState(state);
}

//  QQuickStateOperationPrivate *QQuickStateOperation::d_func()
extern "C" Q_DECL_EXPORT
QQuickStateOperationPrivate *ritual_ZN20QQuickStateOperation6d_funcEv(
    QQuickStateOperation *self) {
  return self->d_func();
}

//  const QQuickStateOperationPrivate *QQuickStateOperation::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickStateOperationPrivate *ritual_ZNK20QQuickStateOperation6d_funcEv(
    const QQuickStateOperation *self) {
  return self->d_func();
}
