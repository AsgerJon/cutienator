//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtGui/qeventpoint.h>
#include <cstring>

//  A QPointerEvent that Python can take functions over in. Every QPointerEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQPointerEventCall0)(const void *, int *);
typedef void (*CuteQPointerEventCall1)(const void *, quint64, int *);
typedef bool (*CuteQPointerEventCall2)(const void *, int *);
typedef bool (*CuteQPointerEventCall3)(const void *, int *);
typedef bool (*CuteQPointerEventCall4)(const void *, int *);
typedef void (*CuteQPointerEventCall5)(const void *, bool, int *);
class CuteQPointerEvent : public QPointerEvent {
public:
  using QPointerEvent::QPointerEvent;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QInputEvent12setTimestampEy")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPointerEvent12isBeginEventEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPointerEvent13isUpdateEventEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPointerEvent10isEndEventEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  QPointerEvent *QPointerEvent::clone() const
  QPointerEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPointerEventCall0 call = reinterpret_cast<CuteQPointerEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPointerEvent *>(given);
    }
    return QPointerEvent::clone();
  }

  //  void QPointerEvent::setTimestamp(quint64 timestamp)
  void setTimestamp(quint64 timestamp) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPointerEventCall1 call = reinterpret_cast<CuteQPointerEventCall1>(taken[1]);
      call(this, timestamp, &handled);
      if (handled) return;
    }
    QPointerEvent::setTimestamp(timestamp);
  }

  //  bool QPointerEvent::isBeginEvent() const
  bool isBeginEvent() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPointerEventCall2 call = reinterpret_cast<CuteQPointerEventCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPointerEvent::isBeginEvent();
  }

  //  bool QPointerEvent::isUpdateEvent() const
  bool isUpdateEvent() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPointerEventCall3 call = reinterpret_cast<CuteQPointerEventCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPointerEvent::isUpdateEvent();
  }

  //  bool QPointerEvent::isEndEvent() const
  bool isEndEvent() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPointerEventCall4 call = reinterpret_cast<CuteQPointerEventCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPointerEvent::isEndEvent();
  }

  //  void QPointerEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPointerEventCall5 call = reinterpret_cast<CuteQPointerEventCall5>(taken[5]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QPointerEvent::setAccepted(accepted);
  }
};

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

//  a Python function taken by a CuteQPointerEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPointerEvent(
    QPointerEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPointerEvent *>(self)->take(key, call);
}

//  QPointerEvent *QPointerEvent::clone() const
extern "C" Q_DECL_EXPORT
QPointerEvent *ritual_own_ZNK13QPointerEvent5cloneEv(
    const QPointerEvent *self) {
  return self->QPointerEvent::clone();
}

//  void QPointerEvent::setTimestamp(quint64 timestamp)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QPointerEvent12setTimestampEy(
    QPointerEvent *self,
    quint64 timestamp) {
  self->QPointerEvent::setTimestamp(timestamp);
}

//  bool QPointerEvent::isBeginEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QPointerEvent12isBeginEventEv(
    const QPointerEvent *self) {
  return self->QPointerEvent::isBeginEvent();
}

//  bool QPointerEvent::isUpdateEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QPointerEvent13isUpdateEventEv(
    const QPointerEvent *self) {
  return self->QPointerEvent::isUpdateEvent();
}

//  bool QPointerEvent::isEndEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QPointerEvent10isEndEventEv(const QPointerEvent *self) {
  return self->QPointerEvent::isEndEvent();
}

//  void QPointerEvent::setAccepted(bool accepted)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QPointerEvent11setAcceptedEb(
    QPointerEvent *self,
    bool accepted) {
  self->QPointerEvent::setAccepted(accepted);
}
