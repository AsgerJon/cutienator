//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qevent_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qevent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qeventpoint.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QMutableTouchEvent that Python can take functions over in. Every QMutableTouchEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQMutableTouchEventCall0)(const void *, int *);
typedef bool (*CuteQMutableTouchEventCall1)(const void *, int *);
typedef bool (*CuteQMutableTouchEventCall2)(const void *, int *);
typedef bool (*CuteQMutableTouchEventCall3)(const void *, int *);
typedef void (*CuteQMutableTouchEventCall4)(const void *, quint64, int *);
typedef void (*CuteQMutableTouchEventCall5)(const void *, bool, int *);
class CuteQMutableTouchEvent : public QMutableTouchEvent {
public:
  using QMutableTouchEvent::QMutableTouchEvent;
  CuteQMutableTouchEvent(const QMutableTouchEvent &other) : QMutableTouchEvent(other) {}
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPointerEvent12isBeginEventEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPointerEvent13isUpdateEventEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPointerEvent10isEndEventEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QInputEvent12setTimestampEy")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  QTouchEvent *QTouchEvent::clone() const
  QTouchEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQMutableTouchEventCall0 call = reinterpret_cast<CuteQMutableTouchEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QTouchEvent *>(given);
    }
    return QTouchEvent::clone();
  }

  //  bool QTouchEvent::isBeginEvent() const
  bool isBeginEvent() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQMutableTouchEventCall1 call = reinterpret_cast<CuteQMutableTouchEventCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QTouchEvent::isBeginEvent();
  }

  //  bool QTouchEvent::isUpdateEvent() const
  bool isUpdateEvent() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQMutableTouchEventCall2 call = reinterpret_cast<CuteQMutableTouchEventCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QTouchEvent::isUpdateEvent();
  }

  //  bool QTouchEvent::isEndEvent() const
  bool isEndEvent() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQMutableTouchEventCall3 call = reinterpret_cast<CuteQMutableTouchEventCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QTouchEvent::isEndEvent();
  }

  //  void QPointerEvent::setTimestamp(quint64 timestamp)
  void setTimestamp(quint64 timestamp) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMutableTouchEventCall4 call = reinterpret_cast<CuteQMutableTouchEventCall4>(taken[4]);
      call(this, timestamp, &handled);
      if (handled) return;
    }
    QPointerEvent::setTimestamp(timestamp);
  }

  //  void QPointerEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[5]) {
      int handled = 0;
      CuteQMutableTouchEventCall5 call = reinterpret_cast<CuteQMutableTouchEventCall5>(taken[5]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QPointerEvent::setAccepted(accepted);
  }
};

//  QMutableTouchEvent::QMutableTouchEvent(QEvent::Type eventType, const
//      QPointingDevice *device, Qt::KeyboardModifiers modifiers, const
//      QList<QEventPoint> &touchPoints)
extern "C" Q_DECL_EXPORT
QMutableTouchEvent *ritual_ZN18QMutableTouchEventC1EN6QEvent4TypeEPK15QPointingDevice6QFlagsIN2Qt16KeyboardModifierEERK5QListI11QEventPointE(
    QEvent::Type eventType,
    const QPointingDevice *device,
    int modifiers,
    const QList<QEventPoint> *touchPoints) {
  return new CuteQMutableTouchEvent(
      eventType,
      device,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      *touchPoints);
}

//  QMutableTouchEvent::~QMutableTouchEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableTouchEventD1Ev(QMutableTouchEvent *self) {
  delete self;
}

//  void QMutableTouchEvent::setTarget(QObject *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableTouchEvent9setTargetEP7QObject(
    QMutableTouchEvent *self,
    QObject *target) {
  self->setTarget(target);
}

//  void QMutableTouchEvent::addPoint(const QEventPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableTouchEvent8addPointERK11QEventPoint(
    QMutableTouchEvent *self,
    const QEventPoint *point) {
  self->addPoint(*point);
}

//  void QMutableTouchEvent::setTarget(QTouchEvent *e, QObject *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableTouchEvent9setTargetEP11QTouchEventP7QObject(
    QTouchEvent *e,
    QObject *target) {
  QMutableTouchEvent::setTarget(e, target);
}

//  void QMutableTouchEvent::addPoint(QTouchEvent *e, const QEventPoint
//      &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableTouchEvent8addPointEP11QTouchEventRK11QEventPoint(
    QTouchEvent *e,
    const QEventPoint *point) {
  QMutableTouchEvent::addPoint(e, *point);
}

//  a Python function taken by a CuteQMutableTouchEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMutableTouchEvent(
    QMutableTouchEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMutableTouchEvent *>(self)->take(key, call);
}
