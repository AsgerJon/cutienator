//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickmultipointtoucharea_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickmultipointtoucharea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qpointingdevice.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QQuickTouchPoint::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickTouchPoint10metaObjectEv(
    const QQuickTouchPoint *self) {
  return self->metaObject();
}

//  QString QQuickTouchPoint::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickTouchPoint2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTouchPoint::tr(s, c, n));
}

//  QQuickTouchPoint::QQuickTouchPoint(bool qmlDefined)
extern "C" Q_DECL_EXPORT
QQuickTouchPoint *ritual_ZN16QQuickTouchPointC1Eb(bool qmlDefined) {
  return new QQuickTouchPoint(qmlDefined);
}

//  int QQuickTouchPoint::pointId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickTouchPoint7pointIdEv(const QQuickTouchPoint *self) {
  return self->pointId();
}

//  void QQuickTouchPoint::setPointId(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTouchPoint10setPointIdEi(
    QQuickTouchPoint *self,
    int id) {
  self->setPointId(id);
}

//  QPointingDeviceUniqueId QQuickTouchPoint::uniqueId() const
extern "C" Q_DECL_EXPORT
QPointingDeviceUniqueId *ritual_ZNK16QQuickTouchPoint8uniqueIdEv(
    const QQuickTouchPoint *self) {
  return new QPointingDeviceUniqueId(self->uniqueId());
}

//  void QQuickTouchPoint::setUniqueId(const QPointingDeviceUniqueId &id)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTouchPoint11setUniqueIdERK23QPointingDeviceUniqueId(
    QQuickTouchPoint *self,
    const QPointingDeviceUniqueId *id) {
  self->setUniqueId(*id);
}

//  qreal QQuickTouchPoint::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickTouchPoint1xEv(const QQuickTouchPoint *self) {
  return self->x();
}

//  qreal QQuickTouchPoint::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickTouchPoint1yEv(const QQuickTouchPoint *self) {
  return self->y();
}

//  void QQuickTouchPoint::setPosition(QPointF pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTouchPoint11setPositionE7QPointF(
    QQuickTouchPoint *self,
    const QPointF *pos) {
  self->setPosition(*pos);
}

//  QSizeF QQuickTouchPoint::ellipseDiameters() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK16QQuickTouchPoint16ellipseDiametersEv(
    const QQuickTouchPoint *self) {
  return new QSizeF(self->ellipseDiameters());
}

//  void QQuickTouchPoint::setEllipseDiameters(const QSizeF &d)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTouchPoint19setEllipseDiametersERK6QSizeF(
    QQuickTouchPoint *self,
    const QSizeF *d) {
  self->setEllipseDiameters(*d);
}

//  qreal QQuickTouchPoint::pressure() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickTouchPoint8pressureEv(const QQuickTouchPoint *self) {
  return self->pressure();
}

//  void QQuickTouchPoint::setPressure(qreal pressure)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTouchPoint11setPressureEd(
    QQuickTouchPoint *self,
    qreal pressure) {
  self->setPressure(pressure);
}

//  qreal QQuickTouchPoint::rotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickTouchPoint8rotationEv(const QQuickTouchPoint *self) {
  return self->rotation();
}

//  void QQuickTouchPoint::setRotation(qreal r)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTouchPoint11setRotationEd(
    QQuickTouchPoint *self,
    qreal r) {
  self->setRotation(r);
}

//  QVector2D QQuickTouchPoint::velocity() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK16QQuickTouchPoint8velocityEv(
    const QQuickTouchPoint *self) {
  return new QVector2D(self->velocity());
}

//  void QQuickTouchPoint::setVelocity(const QVector2D &velocity)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTouchPoint11setVelocityERK9QVector2D(
    QQuickTouchPoint *self,
    const QVector2D *velocity) {
  self->setVelocity(*velocity);
}

//  QRectF QQuickTouchPoint::area() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK16QQuickTouchPoint4areaEv(const QQuickTouchPoint *self) {
  return new QRectF(self->area());
}

//  void QQuickTouchPoint::setArea(const QRectF &area)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTouchPoint7setAreaERK6QRectF(
    QQuickTouchPoint *self,
    const QRectF *area) {
  self->setArea(*area);
}

//  bool QQuickTouchPoint::isQmlDefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickTouchPoint12isQmlDefinedEv(
    const QQuickTouchPoint *self) {
  return self->isQmlDefined();
}

//  bool QQuickTouchPoint::inUse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickTouchPoint5inUseEv(const QQuickTouchPoint *self) {
  return self->inUse();
}

//  void QQuickTouchPoint::setInUse(bool inUse)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTouchPoint8setInUseEb(
    QQuickTouchPoint *self,
    bool inUse) {
  self->setInUse(inUse);
}

//  bool QQuickTouchPoint::pressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickTouchPoint7pressedEv(const QQuickTouchPoint *self) {
  return self->pressed();
}

//  void QQuickTouchPoint::setPressed(bool pressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTouchPoint10setPressedEb(
    QQuickTouchPoint *self,
    bool pressed) {
  self->setPressed(pressed);
}

//  qreal QQuickTouchPoint::startX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickTouchPoint6startXEv(const QQuickTouchPoint *self) {
  return self->startX();
}

//  void QQuickTouchPoint::setStartX(qreal startX)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTouchPoint9setStartXEd(
    QQuickTouchPoint *self,
    qreal startX) {
  self->setStartX(startX);
}

//  qreal QQuickTouchPoint::startY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickTouchPoint6startYEv(const QQuickTouchPoint *self) {
  return self->startY();
}

//  void QQuickTouchPoint::setStartY(qreal startY)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTouchPoint9setStartYEd(
    QQuickTouchPoint *self,
    qreal startY) {
  self->setStartY(startY);
}

//  qreal QQuickTouchPoint::previousX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickTouchPoint9previousXEv(
    const QQuickTouchPoint *self) {
  return self->previousX();
}

//  void QQuickTouchPoint::setPreviousX(qreal previousX)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTouchPoint12setPreviousXEd(
    QQuickTouchPoint *self,
    qreal previousX) {
  self->setPreviousX(previousX);
}

//  qreal QQuickTouchPoint::previousY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickTouchPoint9previousYEv(
    const QQuickTouchPoint *self) {
  return self->previousY();
}

//  void QQuickTouchPoint::setPreviousY(qreal previousY)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTouchPoint12setPreviousYEd(
    QQuickTouchPoint *self,
    qreal previousY) {
  self->setPreviousY(previousY);
}

//  qreal QQuickTouchPoint::sceneX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickTouchPoint6sceneXEv(const QQuickTouchPoint *self) {
  return self->sceneX();
}

//  void QQuickTouchPoint::setSceneX(qreal sceneX)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTouchPoint9setSceneXEd(
    QQuickTouchPoint *self,
    qreal sceneX) {
  self->setSceneX(sceneX);
}

//  qreal QQuickTouchPoint::sceneY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickTouchPoint6sceneYEv(const QQuickTouchPoint *self) {
  return self->sceneY();
}

//  void QQuickTouchPoint::setSceneY(qreal sceneY)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTouchPoint9setSceneYEd(
    QQuickTouchPoint *self,
    qreal sceneY) {
  self->setSceneY(sceneY);
}
