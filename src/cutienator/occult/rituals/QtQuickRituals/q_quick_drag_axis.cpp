//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdragaxis_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdragaxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickDragAxis::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickDragAxis10metaObjectEv(
    const QQuickDragAxis *self) {
  return self->metaObject();
}

//  QString QQuickDragAxis::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickDragAxis2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickDragAxis::tr(s, c, n));
}

//  void QQuickDragAxis::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickDragAxis24qt_qmlMarker_uncreatableEv(
    QQuickDragAxis *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickDragAxis::QQuickDragAxis(QQuickPointerHandler *handler, const
//      QString &propertyName, qreal initValue)
extern "C" Q_DECL_EXPORT
QQuickDragAxis *ritual_ZN14QQuickDragAxisC1EP20QQuickPointerHandlerRK7QStringd(
    QQuickPointerHandler *handler,
    const QString *propertyName,
    qreal initValue) {
  return new QQuickDragAxis(handler, *propertyName, initValue);
}

//  qreal QQuickDragAxis::minimum() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickDragAxis7minimumEv(const QQuickDragAxis *self) {
  return self->minimum();
}

//  void QQuickDragAxis::setMinimum(qreal minimum)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickDragAxis10setMinimumEd(
    QQuickDragAxis *self,
    qreal minimum) {
  self->setMinimum(minimum);
}

//  qreal QQuickDragAxis::maximum() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickDragAxis7maximumEv(const QQuickDragAxis *self) {
  return self->maximum();
}

//  void QQuickDragAxis::setMaximum(qreal maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickDragAxis10setMaximumEd(
    QQuickDragAxis *self,
    qreal maximum) {
  self->setMaximum(maximum);
}

//  bool QQuickDragAxis::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickDragAxis7enabledEv(const QQuickDragAxis *self) {
  return self->enabled();
}

//  void QQuickDragAxis::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickDragAxis10setEnabledEb(
    QQuickDragAxis *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  qreal QQuickDragAxis::activeValue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickDragAxis11activeValueEv(const QQuickDragAxis *self) {
  return self->activeValue();
}

//  qreal QQuickDragAxis::persistentValue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickDragAxis15persistentValueEv(
    const QQuickDragAxis *self) {
  return self->persistentValue();
}

//  void QQuickDragAxis::onActiveChanged(bool active, qreal initActiveValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickDragAxis15onActiveChangedEbd(
    QQuickDragAxis *self,
    bool active,
    qreal initActiveValue) {
  self->onActiveChanged(active, initActiveValue);
}

//  void QQuickDragAxis::updateValue(qreal activeValue, qreal
//      accumulatedValue, qreal delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickDragAxis11updateValueEddd(
    QQuickDragAxis *self,
    qreal activeValue,
    qreal accumulatedValue,
    qreal delta) {
  self->updateValue(activeValue, accumulatedValue, delta);
}
