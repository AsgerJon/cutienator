//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickhandlerpoint_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickhandlerpoint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qsize.h>
#include <QtGui/qpointingdevice.h>
#include <QtGui/qeventpoint.h>
#include <QtCore/qlist.h>

//  void QQuickHandlerPoint::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickHandlerPoint22qt_qmlMarker_anonymousEv(
    QQuickHandlerPoint *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickHandlerPoint::QQuickHandlerPoint()
extern "C" Q_DECL_EXPORT
QQuickHandlerPoint *ritual_ZN18QQuickHandlerPointC1Ev() {
  return new QQuickHandlerPoint();
}

//  int QQuickHandlerPoint::id() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickHandlerPoint2idEv(const QQuickHandlerPoint *self) {
  return self->id();
}

//  Qt::MouseButtons QQuickHandlerPoint::pressedButtons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickHandlerPoint14pressedButtonsEv(
    const QQuickHandlerPoint *self) {
  return static_cast<int>(self->pressedButtons().toInt());
}

//  Qt::KeyboardModifiers QQuickHandlerPoint::modifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickHandlerPoint9modifiersEv(
    const QQuickHandlerPoint *self) {
  return static_cast<int>(self->modifiers().toInt());
}

//  QPointF QQuickHandlerPoint::pressPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK18QQuickHandlerPoint13pressPositionEv(
    const QQuickHandlerPoint *self) {
  return new QPointF(self->pressPosition());
}

//  QPointF QQuickHandlerPoint::scenePressPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK18QQuickHandlerPoint18scenePressPositionEv(
    const QQuickHandlerPoint *self) {
  return new QPointF(self->scenePressPosition());
}

//  QPointF QQuickHandlerPoint::sceneGrabPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK18QQuickHandlerPoint17sceneGrabPositionEv(
    const QQuickHandlerPoint *self) {
  return new QPointF(self->sceneGrabPosition());
}

//  QPointF QQuickHandlerPoint::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK18QQuickHandlerPoint8positionEv(
    const QQuickHandlerPoint *self) {
  return new QPointF(self->position());
}

//  QPointF QQuickHandlerPoint::scenePosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK18QQuickHandlerPoint13scenePositionEv(
    const QQuickHandlerPoint *self) {
  return new QPointF(self->scenePosition());
}

//  QVector2D QQuickHandlerPoint::velocity() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK18QQuickHandlerPoint8velocityEv(
    const QQuickHandlerPoint *self) {
  return new QVector2D(self->velocity());
}

//  qreal QQuickHandlerPoint::rotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickHandlerPoint8rotationEv(
    const QQuickHandlerPoint *self) {
  return self->rotation();
}

//  qreal QQuickHandlerPoint::pressure() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickHandlerPoint8pressureEv(
    const QQuickHandlerPoint *self) {
  return self->pressure();
}

//  QSizeF QQuickHandlerPoint::ellipseDiameters() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK18QQuickHandlerPoint16ellipseDiametersEv(
    const QQuickHandlerPoint *self) {
  return new QSizeF(self->ellipseDiameters());
}

//  QPointingDeviceUniqueId QQuickHandlerPoint::uniqueId() const
extern "C" Q_DECL_EXPORT
QPointingDeviceUniqueId *ritual_ZNK18QQuickHandlerPoint8uniqueIdEv(
    const QQuickHandlerPoint *self) {
  return new QPointingDeviceUniqueId(self->uniqueId());
}

//  QPointingDevice *QQuickHandlerPoint::device() const
extern "C" Q_DECL_EXPORT
QPointingDevice *ritual_ZNK18QQuickHandlerPoint6deviceEv(
    const QQuickHandlerPoint *self) {
  return self->device();
}

//  void QQuickHandlerPoint::localize(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickHandlerPoint8localizeEP10QQuickItem(
    QQuickHandlerPoint *self,
    QQuickItem *item) {
  self->localize(item);
}

//  void QQuickHandlerPoint::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickHandlerPoint5resetEv(QQuickHandlerPoint *self) {
  self->reset();
}

//  void QQuickHandlerPoint::reset(const QPointerEvent *event, const
//      QEventPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickHandlerPoint5resetEPK13QPointerEventRK11QEventPoint(
    QQuickHandlerPoint *self,
    const QPointerEvent *event,
    const QEventPoint *point) {
  self->reset(event, *point);
}

//  void QQuickHandlerPoint::reset(const QList<QQuickHandlerPoint> &points)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickHandlerPoint5resetERK5QListIS_E(
    QQuickHandlerPoint *self,
    const QList<QQuickHandlerPoint> *points) {
  self->reset(*points);
}

//  QQuickHandlerPoint::~QQuickHandlerPoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickHandlerPointD1Ev(QQuickHandlerPoint *self) {
  delete self;
}

//  QList<QQuickHandlerPoint>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuickHandlerPoint> *ritual_list_make_QQuickHandlerPoint() {
  return new QList<QQuickHandlerPoint>();
}

//  void QList<QQuickHandlerPoint>::append(const QQuickHandlerPoint &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuickHandlerPoint(
    QList<QQuickHandlerPoint> *self,
    const QQuickHandlerPoint *element) {
  self->append(*element);
}

//  qsizetype QList<QQuickHandlerPoint>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuickHandlerPoint(
    const QList<QQuickHandlerPoint> *self) {
  return self->size();
}

//  const QQuickHandlerPoint &QList<QQuickHandlerPoint>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QQuickHandlerPoint *ritual_list_at_QQuickHandlerPoint(
    const QList<QQuickHandlerPoint> *self,
    long long index) {
  return new QQuickHandlerPoint(self->at(index));
}

//  QList<QQuickHandlerPoint>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuickHandlerPoint(QList<QQuickHandlerPoint> *self) {
  delete self;
}
