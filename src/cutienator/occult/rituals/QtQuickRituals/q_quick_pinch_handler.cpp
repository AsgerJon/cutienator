//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpinchhandler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpinchhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qpoint.h>

//  Only a class built on QQuickPinchHandler may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickPinchHandler : QQuickPinchHandler {
  using QQuickPinchHandler::wantsPointerEvent;
  using QQuickPinchHandler::onActiveChanged;
  using QQuickPinchHandler::handlePointerEventImpl;
};

//  const QMetaObject *QQuickPinchHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickPinchHandler10metaObjectEv(
    const QQuickPinchHandler *self) {
  return self->metaObject();
}

//  void *QQuickPinchHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuickPinchHandler11qt_metacastEPKc(
    QQuickPinchHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPinchHandler::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickPinchHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPinchHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPinchHandler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickPinchHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPinchHandler::tr(s, c, n));
}

//  QQuickPinchHandler::QQuickPinchHandler(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickPinchHandler *ritual_ZN18QQuickPinchHandlerC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickPinchHandler(parent);
}

//  QQuickDragAxis *QQuickPinchHandler::xAxis()
extern "C" Q_DECL_EXPORT
QQuickDragAxis *ritual_ZN18QQuickPinchHandler5xAxisEv(
    QQuickPinchHandler *self) {
  return self->xAxis();
}

//  QQuickDragAxis *QQuickPinchHandler::yAxis()
extern "C" Q_DECL_EXPORT
QQuickDragAxis *ritual_ZN18QQuickPinchHandler5yAxisEv(
    QQuickPinchHandler *self) {
  return self->yAxis();
}

#if QT_DEPRECATED_SINCE(6, 5)
//  QVector2D QQuickPinchHandler::translation() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK18QQuickPinchHandler11translationEv(
    const QQuickPinchHandler *self) {
  return new QVector2D(self->translation());
}
#endif  // QT_DEPRECATED_SINCE(6, 5)

//  QPointF QQuickPinchHandler::activeTranslation() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK18QQuickPinchHandler17activeTranslationEv(
    const QQuickPinchHandler *self) {
  return new QPointF(self->activeTranslation());
}

//  QPointF QQuickPinchHandler::persistentTranslation() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK18QQuickPinchHandler21persistentTranslationEv(
    const QQuickPinchHandler *self) {
  return new QPointF(self->persistentTranslation());
}

//  void QQuickPinchHandler::setPersistentTranslation(const QPointF &trans)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPinchHandler24setPersistentTranslationERK7QPointF(
    QQuickPinchHandler *self,
    const QPointF *trans) {
  self->setPersistentTranslation(*trans);
}

//  QQuickDragAxis *QQuickPinchHandler::scaleAxis()
extern "C" Q_DECL_EXPORT
QQuickDragAxis *ritual_ZN18QQuickPinchHandler9scaleAxisEv(
    QQuickPinchHandler *self) {
  return self->scaleAxis();
}

#if QT_DEPRECATED_SINCE(6, 5)
//  qreal QQuickPinchHandler::minimumScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickPinchHandler12minimumScaleEv(
    const QQuickPinchHandler *self) {
  return self->minimumScale();
}
#endif  // QT_DEPRECATED_SINCE(6, 5)

#if QT_DEPRECATED_SINCE(6, 5)
//  void QQuickPinchHandler::setMinimumScale(qreal minimumScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPinchHandler15setMinimumScaleEd(
    QQuickPinchHandler *self,
    qreal minimumScale) {
  self->setMinimumScale(minimumScale);
}
#endif  // QT_DEPRECATED_SINCE(6, 5)

#if QT_DEPRECATED_SINCE(6, 5)
//  qreal QQuickPinchHandler::maximumScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickPinchHandler12maximumScaleEv(
    const QQuickPinchHandler *self) {
  return self->maximumScale();
}
#endif  // QT_DEPRECATED_SINCE(6, 5)

#if QT_DEPRECATED_SINCE(6, 5)
//  void QQuickPinchHandler::setMaximumScale(qreal maximumScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPinchHandler15setMaximumScaleEd(
    QQuickPinchHandler *self,
    qreal maximumScale) {
  self->setMaximumScale(maximumScale);
}
#endif  // QT_DEPRECATED_SINCE(6, 5)

#if QT_DEPRECATED_SINCE(6, 5)
//  qreal QQuickPinchHandler::scale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickPinchHandler5scaleEv(
    const QQuickPinchHandler *self) {
  return self->scale();
}
#endif  // QT_DEPRECATED_SINCE(6, 5)

//  qreal QQuickPinchHandler::activeScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickPinchHandler11activeScaleEv(
    const QQuickPinchHandler *self) {
  return self->activeScale();
}

//  void QQuickPinchHandler::setActiveScale(qreal scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPinchHandler14setActiveScaleEd(
    QQuickPinchHandler *self,
    qreal scale) {
  self->setActiveScale(scale);
}

//  qreal QQuickPinchHandler::persistentScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickPinchHandler15persistentScaleEv(
    const QQuickPinchHandler *self) {
  return self->persistentScale();
}

//  void QQuickPinchHandler::setPersistentScale(qreal scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPinchHandler18setPersistentScaleEd(
    QQuickPinchHandler *self,
    qreal scale) {
  self->setPersistentScale(scale);
}

//  QQuickDragAxis *QQuickPinchHandler::rotationAxis()
extern "C" Q_DECL_EXPORT
QQuickDragAxis *ritual_ZN18QQuickPinchHandler12rotationAxisEv(
    QQuickPinchHandler *self) {
  return self->rotationAxis();
}

#if QT_DEPRECATED_SINCE(6, 5)
//  qreal QQuickPinchHandler::minimumRotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickPinchHandler15minimumRotationEv(
    const QQuickPinchHandler *self) {
  return self->minimumRotation();
}
#endif  // QT_DEPRECATED_SINCE(6, 5)

#if QT_DEPRECATED_SINCE(6, 5)
//  void QQuickPinchHandler::setMinimumRotation(qreal minimumRotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPinchHandler18setMinimumRotationEd(
    QQuickPinchHandler *self,
    qreal minimumRotation) {
  self->setMinimumRotation(minimumRotation);
}
#endif  // QT_DEPRECATED_SINCE(6, 5)

#if QT_DEPRECATED_SINCE(6, 5)
//  qreal QQuickPinchHandler::maximumRotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickPinchHandler15maximumRotationEv(
    const QQuickPinchHandler *self) {
  return self->maximumRotation();
}
#endif  // QT_DEPRECATED_SINCE(6, 5)

#if QT_DEPRECATED_SINCE(6, 5)
//  void QQuickPinchHandler::setMaximumRotation(qreal maximumRotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPinchHandler18setMaximumRotationEd(
    QQuickPinchHandler *self,
    qreal maximumRotation) {
  self->setMaximumRotation(maximumRotation);
}
#endif  // QT_DEPRECATED_SINCE(6, 5)

#if QT_DEPRECATED_SINCE(6, 5)
//  qreal QQuickPinchHandler::rotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickPinchHandler8rotationEv(
    const QQuickPinchHandler *self) {
  return self->rotation();
}
#endif  // QT_DEPRECATED_SINCE(6, 5)

//  qreal QQuickPinchHandler::activeRotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickPinchHandler14activeRotationEv(
    const QQuickPinchHandler *self) {
  return self->activeRotation();
}

//  void QQuickPinchHandler::setActiveRotation(qreal rot)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPinchHandler17setActiveRotationEd(
    QQuickPinchHandler *self,
    qreal rot) {
  self->setActiveRotation(rot);
}

//  qreal QQuickPinchHandler::persistentRotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickPinchHandler18persistentRotationEv(
    const QQuickPinchHandler *self) {
  return self->persistentRotation();
}

//  void QQuickPinchHandler::setPersistentRotation(qreal rot)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPinchHandler21setPersistentRotationEd(
    QQuickPinchHandler *self,
    qreal rot) {
  self->setPersistentRotation(rot);
}

//  void QQuickPinchHandler::minimumScaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPinchHandler19minimumScaleChangedEv(
    QQuickPinchHandler *self) {
  self->minimumScaleChanged();
}

//  void QQuickPinchHandler::maximumScaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPinchHandler19maximumScaleChangedEv(
    QQuickPinchHandler *self) {
  self->maximumScaleChanged();
}

//  void QQuickPinchHandler::minimumRotationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPinchHandler22minimumRotationChangedEv(
    QQuickPinchHandler *self) {
  self->minimumRotationChanged();
}

//  void QQuickPinchHandler::maximumRotationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPinchHandler22maximumRotationChangedEv(
    QQuickPinchHandler *self) {
  self->maximumRotationChanged();
}

//  void QQuickPinchHandler::updated()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPinchHandler7updatedEv(QQuickPinchHandler *self) {
  self->updated();
}

//  void QQuickPinchHandler::scaleChanged(qreal delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPinchHandler12scaleChangedEd(
    QQuickPinchHandler *self,
    qreal delta) {
  self->scaleChanged(delta);
}

//  void QQuickPinchHandler::rotationChanged(qreal delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPinchHandler15rotationChangedEd(
    QQuickPinchHandler *self,
    qreal delta) {
  self->rotationChanged(delta);
}

//  void QQuickPinchHandler::translationChanged(QVector2D delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPinchHandler18translationChangedE9QVector2D(
    QQuickPinchHandler *self,
    const QVector2D *delta) {
  self->translationChanged(*delta);
}

//  bool QQuickPinchHandler::wantsPointerEvent(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickPinchHandler17wantsPointerEventEP13QPointerEvent(
    QQuickPinchHandler *self,
    QPointerEvent *event) {
  return self->wantsPointerEvent(event);
}

//  void QQuickPinchHandler::onActiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPinchHandler15onActiveChangedEv(
    QQuickPinchHandler *self) {
  self->onActiveChanged();
}

//  void QQuickPinchHandler::handlePointerEventImpl(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPinchHandler22handlePointerEventImplEP13QPointerEvent(
    QQuickPinchHandler *self,
    QPointerEvent *event) {
  self->handlePointerEventImpl(event);
}

//  bool QQuickPinchHandler::wantsPointerEvent(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQuickPinchHandler17wantsPointerEventEP13QPointerEvent(
    QQuickPinchHandler *self,
    QPointerEvent *event) {
  return static_cast<OwnQQuickPinchHandler *>(self)->OwnQQuickPinchHandler::wantsPointerEvent(
      event);
}

//  void QQuickPinchHandler::onActiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickPinchHandler15onActiveChangedEv(
    QQuickPinchHandler *self) {
  static_cast<OwnQQuickPinchHandler *>(self)->OwnQQuickPinchHandler::onActiveChanged();
}

//  void QQuickPinchHandler::handlePointerEventImpl(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickPinchHandler22handlePointerEventImplEP13QPointerEvent(
    QQuickPinchHandler *self,
    QPointerEvent *event) {
  static_cast<OwnQQuickPinchHandler *>(self)->OwnQQuickPinchHandler::handlePointerEventImpl(
      event);
}
