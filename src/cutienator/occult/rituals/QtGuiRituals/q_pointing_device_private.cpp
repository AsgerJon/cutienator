//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpointingdevice_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qpointingdevice.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpointingdevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qeventpoint.h>

//  QPointingDevice *QPointingDevicePrivate::q_func()
extern "C" Q_DECL_EXPORT
QPointingDevice *ritual_ZN22QPointingDevicePrivate6q_funcEv(
    QPointingDevicePrivate *self) {
  return self->q_func();
}

//  const QPointingDevice *QPointingDevicePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPointingDevice *ritual_ZNK22QPointingDevicePrivate6q_funcEv(
    const QPointingDevicePrivate *self) {
  return self->q_func();
}

//  QPointingDevicePrivate::QPointingDevicePrivate(const QString &name,
//      qint64 id, QInputDevice::DeviceType type,
//      QPointingDevice::PointerType pType, QPointingDevice::Capabilities
//      caps, int maxPoints, int buttonCount, const QString &seatName,
//      QPointingDeviceUniqueId uniqueId)
extern "C" Q_DECL_EXPORT
QPointingDevicePrivate *ritual_ZN22QPointingDevicePrivateC1ERK7QStringxN12QInputDevice10DeviceTypeEN15QPointingDevice11PointerTypeE6QFlagsINS3_10CapabilityEEiiS2_23QPointingDeviceUniqueId(
    const QString *name,
    qint64 id,
    QInputDevice::DeviceType type,
    QPointingDevice::PointerType pType,
    int caps,
    int maxPoints,
    int buttonCount,
    const QString *seatName,
    const QPointingDeviceUniqueId *uniqueId) {
  return new QPointingDevicePrivate(
      *name,
      id,
      type,
      pType,
      QFlags<QInputDevice::Capability>::fromInt(caps),
      maxPoints,
      buttonCount,
      *seatName,
      *uniqueId);
}

//  QPointingDevicePrivate::~QPointingDevicePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPointingDevicePrivateD1Ev(QPointingDevicePrivate *self) {
  delete self;
}

//  void QPointingDevicePrivate::sendTouchCancelEvent(QTouchEvent
//      *cancelEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPointingDevicePrivate20sendTouchCancelEventEP11QTouchEvent(
    QPointingDevicePrivate *self,
    QTouchEvent *cancelEvent) {
  self->sendTouchCancelEvent(cancelEvent);
}

//  EventPointData *QPointingDevicePrivate::queryPointById(int id) const
extern "C" Q_DECL_EXPORT
QPointingDevicePrivate::EventPointData *ritual_ZNK22QPointingDevicePrivate14queryPointByIdEi(
    const QPointingDevicePrivate *self,
    int id) {
  return self->queryPointById(id);
}

//  EventPointData *QPointingDevicePrivate::pointById(int id) const
extern "C" Q_DECL_EXPORT
QPointingDevicePrivate::EventPointData *ritual_ZNK22QPointingDevicePrivate9pointByIdEi(
    const QPointingDevicePrivate *self,
    int id) {
  return self->pointById(id);
}

//  void QPointingDevicePrivate::removePointById(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPointingDevicePrivate15removePointByIdEi(
    QPointingDevicePrivate *self,
    int id) {
  self->removePointById(id);
}

//  QObject *QPointingDevicePrivate::firstActiveTarget() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK22QPointingDevicePrivate17firstActiveTargetEv(
    const QPointingDevicePrivate *self) {
  return self->firstActiveTarget();
}

//  QWindow *QPointingDevicePrivate::firstActiveWindow() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK22QPointingDevicePrivate17firstActiveWindowEv(
    const QPointingDevicePrivate *self) {
  return self->firstActiveWindow();
}

//  QObject *QPointingDevicePrivate::firstPointExclusiveGrabber() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK22QPointingDevicePrivate26firstPointExclusiveGrabberEv(
    const QPointingDevicePrivate *self) {
  return self->firstPointExclusiveGrabber();
}

//  void QPointingDevicePrivate::setExclusiveGrabber(const QPointerEvent
//      *event, const QEventPoint &point, QObject *exclusiveGrabber)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPointingDevicePrivate19setExclusiveGrabberEPK13QPointerEventRK11QEventPointP7QObject(
    QPointingDevicePrivate *self,
    const QPointerEvent *event,
    const QEventPoint *point,
    QObject *exclusiveGrabber) {
  self->setExclusiveGrabber(event, *point, exclusiveGrabber);
}

//  bool QPointingDevicePrivate::removeExclusiveGrabber(const QPointerEvent
//      *event, const QObject *grabber)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QPointingDevicePrivate22removeExclusiveGrabberEPK13QPointerEventPK7QObject(
    QPointingDevicePrivate *self,
    const QPointerEvent *event,
    const QObject *grabber) {
  return self->removeExclusiveGrabber(event, grabber);
}

//  bool QPointingDevicePrivate::addPassiveGrabber(const QPointerEvent
//      *event, const QEventPoint &point, QObject *grabber)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QPointingDevicePrivate17addPassiveGrabberEPK13QPointerEventRK11QEventPointP7QObject(
    QPointingDevicePrivate *self,
    const QPointerEvent *event,
    const QEventPoint *point,
    QObject *grabber) {
  return self->addPassiveGrabber(event, *point, grabber);
}

//  bool QPointingDevicePrivate::setPassiveGrabberContext(EventPointData
//      *epd, QObject *grabber, QObject *context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QPointingDevicePrivate24setPassiveGrabberContextEPNS_14EventPointDataEP7QObjectS3_(
    QPointingDevicePrivate::EventPointData *epd,
    QObject *grabber,
    QObject *context) {
  return QPointingDevicePrivate::setPassiveGrabberContext(
      epd,
      grabber,
      context);
}

//  bool QPointingDevicePrivate::removePassiveGrabber(const QPointerEvent
//      *event, const QEventPoint &point, QObject *grabber)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QPointingDevicePrivate20removePassiveGrabberEPK13QPointerEventRK11QEventPointP7QObject(
    QPointingDevicePrivate *self,
    const QPointerEvent *event,
    const QEventPoint *point,
    QObject *grabber) {
  return self->removePassiveGrabber(event, *point, grabber);
}

//  void QPointingDevicePrivate::clearPassiveGrabbers(const QPointerEvent
//      *event, const QEventPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPointingDevicePrivate20clearPassiveGrabbersEPK13QPointerEventRK11QEventPoint(
    QPointingDevicePrivate *self,
    const QPointerEvent *event,
    const QEventPoint *point) {
  self->clearPassiveGrabbers(event, *point);
}

//  void QPointingDevicePrivate::removeGrabber(QObject *grabber, bool cancel)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPointingDevicePrivate13removeGrabberEP7QObjectb(
    QPointingDevicePrivate *self,
    QObject *grabber,
    bool cancel) {
  self->removeGrabber(grabber, cancel);
}

//  QPointingDevicePrivate *QPointingDevicePrivate::get(QPointingDevice *q)
extern "C" Q_DECL_EXPORT
QPointingDevicePrivate *ritual_ZN22QPointingDevicePrivate3getEP15QPointingDevice(
    QPointingDevice *q) {
  return QPointingDevicePrivate::get(q);
}

//  const QPointingDevicePrivate *QPointingDevicePrivate::get(const
//      QPointingDevice *q)
extern "C" Q_DECL_EXPORT
const QPointingDevicePrivate *ritual_ZN22QPointingDevicePrivate3getEPK15QPointingDevice(
    const QPointingDevice *q) {
  return QPointingDevicePrivate::get(q);
}

//  const QPointingDevice
//      *QPointingDevicePrivate::tabletDevice(QInputDevice::DeviceType
//      deviceType, QPointingDevice::PointerType pointerType,
//      QPointingDeviceUniqueId uniqueId)
extern "C" Q_DECL_EXPORT
const QPointingDevice *ritual_ZN22QPointingDevicePrivate12tabletDeviceEN12QInputDevice10DeviceTypeEN15QPointingDevice11PointerTypeE23QPointingDeviceUniqueId(
    QInputDevice::DeviceType deviceType,
    QPointingDevice::PointerType pointerType,
    const QPointingDeviceUniqueId *uniqueId) {
  return QPointingDevicePrivate::tabletDevice(
      deviceType,
      pointerType,
      *uniqueId);
}

//  const QPointingDevice
//      *QPointingDevicePrivate::queryTabletDevice(QInputDevice::DeviceType
//      deviceType, QPointingDevice::PointerType pointerType,
//      QPointingDeviceUniqueId uniqueId, QInputDevice::Capabilities
//      capabilities, qint64 systemId)
extern "C" Q_DECL_EXPORT
const QPointingDevice *ritual_ZN22QPointingDevicePrivate17queryTabletDeviceEN12QInputDevice10DeviceTypeEN15QPointingDevice11PointerTypeE23QPointingDeviceUniqueId6QFlagsINS0_10CapabilityEEx(
    QInputDevice::DeviceType deviceType,
    QPointingDevice::PointerType pointerType,
    const QPointingDeviceUniqueId *uniqueId,
    int capabilities,
    qint64 systemId) {
  return QPointingDevicePrivate::queryTabletDevice(
      deviceType,
      pointerType,
      *uniqueId,
      QFlags<QInputDevice::Capability>::fromInt(capabilities),
      systemId);
}

//  const QPointingDevice *QPointingDevicePrivate::pointingDeviceById(qint64
//      systemId)
extern "C" Q_DECL_EXPORT
const QPointingDevice *ritual_ZN22QPointingDevicePrivate18pointingDeviceByIdEx(
    qint64 systemId) {
  return QPointingDevicePrivate::pointingDeviceById(systemId);
}
