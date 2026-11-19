//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtGui/qeventpoint.h>

//  QPointerEvent *QPointerEvent::clone() const
extern "C" Q_DECL_EXPORT
QPointerEvent *ritual_ZNK13QPointerEvent5cloneEv(const QPointerEvent *self) {
  return self->clone();
}

//  QPointerEvent::~QPointerEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPointerEventD1Ev(QPointerEvent *self) {
  delete self;
}

//  const QPointingDevice *QPointerEvent::pointingDevice() const
extern "C" Q_DECL_EXPORT
const QPointingDevice *ritual_ZNK13QPointerEvent14pointingDeviceEv(
    const QPointerEvent *self) {
  return self->pointingDevice();
}

//  QPointingDevice::PointerType QPointerEvent::pointerType() const
extern "C" Q_DECL_EXPORT
QPointingDevice::PointerType ritual_ZNK13QPointerEvent11pointerTypeEv(
    const QPointerEvent *self) {
  return self->pointerType();
}

//  void QPointerEvent::setTimestamp(quint64 timestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPointerEvent12setTimestampEy(
    QPointerEvent *self,
    quint64 timestamp) {
  self->setTimestamp(timestamp);
}

//  qsizetype QPointerEvent::pointCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QPointerEvent10pointCountEv(
    const QPointerEvent *self) {
  return self->pointCount();
}

//  QEventPoint *QPointerEvent::pointById(int id)
extern "C" Q_DECL_EXPORT
QEventPoint *ritual_ZN13QPointerEvent9pointByIdEi(
    QPointerEvent *self,
    int id) {
  return self->pointById(id);
}

//  bool QPointerEvent::allPointsGrabbed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPointerEvent16allPointsGrabbedEv(
    const QPointerEvent *self) {
  return self->allPointsGrabbed();
}

//  bool QPointerEvent::isBeginEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPointerEvent12isBeginEventEv(const QPointerEvent *self) {
  return self->isBeginEvent();
}

//  bool QPointerEvent::isUpdateEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPointerEvent13isUpdateEventEv(const QPointerEvent *self) {
  return self->isUpdateEvent();
}

//  bool QPointerEvent::isEndEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPointerEvent10isEndEventEv(const QPointerEvent *self) {
  return self->isEndEvent();
}

//  bool QPointerEvent::allPointsAccepted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPointerEvent17allPointsAcceptedEv(
    const QPointerEvent *self) {
  return self->allPointsAccepted();
}

//  void QPointerEvent::setAccepted(bool accepted)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPointerEvent11setAcceptedEb(
    QPointerEvent *self,
    bool accepted) {
  self->setAccepted(accepted);
}

//  QObject *QPointerEvent::exclusiveGrabber(const QEventPoint &point) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK13QPointerEvent16exclusiveGrabberERK11QEventPoint(
    const QPointerEvent *self,
    const QEventPoint *point) {
  return self->exclusiveGrabber(*point);
}

//  void QPointerEvent::setExclusiveGrabber(const QEventPoint &point, QObject
//      *exclusiveGrabber)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPointerEvent19setExclusiveGrabberERK11QEventPointP7QObject(
    QPointerEvent *self,
    const QEventPoint *point,
    QObject *exclusiveGrabber) {
  self->setExclusiveGrabber(*point, exclusiveGrabber);
}

//  void QPointerEvent::clearPassiveGrabbers(const QEventPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPointerEvent20clearPassiveGrabbersERK11QEventPoint(
    QPointerEvent *self,
    const QEventPoint *point) {
  self->clearPassiveGrabbers(*point);
}

//  bool QPointerEvent::addPassiveGrabber(const QEventPoint &point, QObject
//      *grabber)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QPointerEvent17addPassiveGrabberERK11QEventPointP7QObject(
    QPointerEvent *self,
    const QEventPoint *point,
    QObject *grabber) {
  return self->addPassiveGrabber(*point, grabber);
}

//  bool QPointerEvent::removePassiveGrabber(const QEventPoint &point,
//      QObject *grabber)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QPointerEvent20removePassiveGrabberERK11QEventPointP7QObject(
    QPointerEvent *self,
    const QEventPoint *point,
    QObject *grabber) {
  return self->removePassiveGrabber(*point, grabber);
}
