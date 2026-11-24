//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdraghandler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdraghandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qpoint.h>

//  Only a class built on QQuickDragHandler may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickDragHandler : QQuickDragHandler {
  using QQuickDragHandler::wantsPointerEvent;
  using QQuickDragHandler::onActiveChanged;
};

//  const QMetaObject *QQuickDragHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickDragHandler10metaObjectEv(
    const QQuickDragHandler *self) {
  return self->metaObject();
}

//  QString QQuickDragHandler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickDragHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickDragHandler::tr(s, c, n));
}

//  QQuickDragHandler::QQuickDragHandler(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickDragHandler *ritual_ZN17QQuickDragHandlerC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickDragHandler(parent);
}

//  void QQuickDragHandler::handlePointerEventImpl(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDragHandler22handlePointerEventImplEP13QPointerEvent(
    QQuickDragHandler *self,
    QPointerEvent *event) {
  self->handlePointerEventImpl(event);
}

//  QQuickDragAxis *QQuickDragHandler::xAxis()
extern "C" Q_DECL_EXPORT
QQuickDragAxis *ritual_ZN17QQuickDragHandler5xAxisEv(
    QQuickDragHandler *self) {
  return self->xAxis();
}

//  QQuickDragAxis *QQuickDragHandler::yAxis()
extern "C" Q_DECL_EXPORT
QQuickDragAxis *ritual_ZN17QQuickDragHandler5yAxisEv(
    QQuickDragHandler *self) {
  return self->yAxis();
}

#if QT_DEPRECATED_SINCE(6, 2)
//  QVector2D QQuickDragHandler::translation() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK17QQuickDragHandler11translationEv(
    const QQuickDragHandler *self) {
  return new QVector2D(self->translation());
}
#endif  // QT_DEPRECATED_SINCE(6, 2)

//  QVector2D QQuickDragHandler::activeTranslation() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK17QQuickDragHandler17activeTranslationEv(
    const QQuickDragHandler *self) {
  return new QVector2D(self->activeTranslation());
}

//  void QQuickDragHandler::setActiveTranslation(const QVector2D &trans)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDragHandler20setActiveTranslationERK9QVector2D(
    QQuickDragHandler *self,
    const QVector2D *trans) {
  self->setActiveTranslation(*trans);
}

//  QVector2D QQuickDragHandler::persistentTranslation() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK17QQuickDragHandler21persistentTranslationEv(
    const QQuickDragHandler *self) {
  return new QVector2D(self->persistentTranslation());
}

//  void QQuickDragHandler::setPersistentTranslation(const QVector2D &trans)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDragHandler24setPersistentTranslationERK9QVector2D(
    QQuickDragHandler *self,
    const QVector2D *trans) {
  self->setPersistentTranslation(*trans);
}

//  QQuickDragHandler::SnapMode QQuickDragHandler::snapMode() const
extern "C" Q_DECL_EXPORT
QQuickDragHandler::SnapMode ritual_ZNK17QQuickDragHandler8snapModeEv(
    const QQuickDragHandler *self) {
  return self->snapMode();
}

//  void QQuickDragHandler::setSnapMode(QQuickDragHandler::SnapMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDragHandler11setSnapModeENS_8SnapModeE(
    QQuickDragHandler *self,
    QQuickDragHandler::SnapMode mode) {
  self->setSnapMode(mode);
}

//  bool QQuickDragHandler::wantsPointerEvent(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickDragHandler17wantsPointerEventEP13QPointerEvent(
    QQuickDragHandler *self,
    QPointerEvent *event) {
  return self->wantsPointerEvent(event);
}

//  void QQuickDragHandler::onActiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDragHandler15onActiveChangedEv(
    QQuickDragHandler *self) {
  self->onActiveChanged();
}

//  void QQuickDragHandler::enforceAxisConstraints(QPointF *localPos)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickDragHandler22enforceAxisConstraintsEP7QPointF(
    QQuickDragHandler *self,
    QPointF *localPos) {
  self->enforceAxisConstraints(localPos);
}

//  QPointF QQuickDragHandler::targetCentroidPosition()
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN17QQuickDragHandler22targetCentroidPositionEv(
    QQuickDragHandler *self) {
  return new QPointF(self->targetCentroidPosition());
}

//  void QQuickDragHandler::handlePointerEventImpl(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickDragHandler22handlePointerEventImplEP13QPointerEvent(
    QQuickDragHandler *self,
    QPointerEvent *event) {
  self->QQuickDragHandler::handlePointerEventImpl(event);
}

//  bool QQuickDragHandler::wantsPointerEvent(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QQuickDragHandler17wantsPointerEventEP13QPointerEvent(
    QQuickDragHandler *self,
    QPointerEvent *event) {
  return static_cast<OwnQQuickDragHandler *>(self)->OwnQQuickDragHandler::wantsPointerEvent(
      event);
}

//  void QQuickDragHandler::onActiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickDragHandler15onActiveChangedEv(
    QQuickDragHandler *self) {
  static_cast<OwnQQuickDragHandler *>(self)->OwnQQuickDragHandler::onActiveChanged();
}
