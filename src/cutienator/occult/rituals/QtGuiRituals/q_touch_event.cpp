//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtGui/qeventpoint.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QTouchEvent that Python can take functions over in. Every QTouchEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQTouchEventCall0)(const void *, int *);
typedef bool (*CuteQTouchEventCall1)(const void *, int *);
typedef bool (*CuteQTouchEventCall2)(const void *, int *);
typedef bool (*CuteQTouchEventCall3)(const void *, int *);
typedef void (*CuteQTouchEventCall4)(const void *, quint64, int *);
typedef void (*CuteQTouchEventCall5)(const void *, bool, int *);
class CuteQTouchEvent : public QTouchEvent {
public:
  using QTouchEvent::QTouchEvent;
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
      CuteQTouchEventCall0 call = reinterpret_cast<CuteQTouchEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QTouchEvent *>(given);
    }
    return QTouchEvent::clone();
  }

  //  bool QTouchEvent::isBeginEvent() const
  bool isBeginEvent() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTouchEventCall1 call = reinterpret_cast<CuteQTouchEventCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QTouchEvent::isBeginEvent();
  }

  //  bool QTouchEvent::isUpdateEvent() const
  bool isUpdateEvent() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQTouchEventCall2 call = reinterpret_cast<CuteQTouchEventCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QTouchEvent::isUpdateEvent();
  }

  //  bool QTouchEvent::isEndEvent() const
  bool isEndEvent() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQTouchEventCall3 call = reinterpret_cast<CuteQTouchEventCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QTouchEvent::isEndEvent();
  }

  //  void QPointerEvent::setTimestamp(quint64 timestamp)
  void setTimestamp(quint64 timestamp) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTouchEventCall4 call = reinterpret_cast<CuteQTouchEventCall4>(taken[4]);
      call(this, timestamp, &handled);
      if (handled) return;
    }
    QPointerEvent::setTimestamp(timestamp);
  }

  //  void QPointerEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTouchEventCall5 call = reinterpret_cast<CuteQTouchEventCall5>(taken[5]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QPointerEvent::setAccepted(accepted);
  }
};

//  QTouchEvent *QTouchEvent::clone() const
extern "C" Q_DECL_EXPORT
QTouchEvent *ritual_ZNK11QTouchEvent5cloneEv(const QTouchEvent *self) {
  return self->clone();
}

//  QTouchEvent::~QTouchEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTouchEventD1Ev(QTouchEvent *self) {
  delete self;
}

//  QTouchEvent::QTouchEvent(QEvent::Type eventType, const QPointingDevice
//      *device, Qt::KeyboardModifiers modifiers, const QList<QEventPoint>
//      &touchPoints)
extern "C" Q_DECL_EXPORT
QTouchEvent *ritual_ZN11QTouchEventC1EN6QEvent4TypeEPK15QPointingDevice6QFlagsIN2Qt16KeyboardModifierEERK5QListI11QEventPointE(
    QEvent::Type eventType,
    const QPointingDevice *device,
    int modifiers,
    const QList<QEventPoint> *touchPoints) {
  return new CuteQTouchEvent(
      eventType,
      device,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      *touchPoints);
}

#if QT_DEPRECATED_SINCE(6, 0)
//  QTouchEvent::QTouchEvent(QEvent::Type eventType, const QPointingDevice
//      *device, Qt::KeyboardModifiers modifiers, QEventPoint::States
//      touchPointStates, const QList<QEventPoint> &touchPoints)
extern "C" Q_DECL_EXPORT
QTouchEvent *ritual_ZN11QTouchEventC1EN6QEvent4TypeEPK15QPointingDevice6QFlagsIN2Qt16KeyboardModifierEES5_IN11QEventPoint5StateEERK5QListIS9_E(
    QEvent::Type eventType,
    const QPointingDevice *device,
    int modifiers,
    int touchPointStates,
    const QList<QEventPoint> *touchPoints) {
  return new CuteQTouchEvent(
      eventType,
      device,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      QFlags<QEventPoint::State>::fromInt(touchPointStates),
      *touchPoints);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  QObject *QTouchEvent::target() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK11QTouchEvent6targetEv(const QTouchEvent *self) {
  return self->target();
}

//  QEventPoint::States QTouchEvent::touchPointStates() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTouchEvent16touchPointStatesEv(const QTouchEvent *self) {
  return static_cast<int>(self->touchPointStates().toInt());
}

#if QT_DEPRECATED_SINCE(6, 0)
//  const QList<QEventPoint> &QTouchEvent::touchPoints() const
extern "C" Q_DECL_EXPORT
QList<QEventPoint> *ritual_ZNK11QTouchEvent11touchPointsEv(
    const QTouchEvent *self) {
  return new QList<QEventPoint>(self->touchPoints());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  bool QTouchEvent::isBeginEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTouchEvent12isBeginEventEv(const QTouchEvent *self) {
  return self->isBeginEvent();
}

//  bool QTouchEvent::isUpdateEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTouchEvent13isUpdateEventEv(const QTouchEvent *self) {
  return self->isUpdateEvent();
}

//  bool QTouchEvent::isEndEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTouchEvent10isEndEventEv(const QTouchEvent *self) {
  return self->isEndEvent();
}

//  a Python function taken by a CuteQTouchEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTouchEvent(
    QTouchEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTouchEvent *>(self)->take(key, call);
}

//  QTouchEvent *QTouchEvent::clone() const
extern "C" Q_DECL_EXPORT
QTouchEvent *ritual_own_ZNK11QTouchEvent5cloneEv(const QTouchEvent *self) {
  return self->QTouchEvent::clone();
}

//  bool QTouchEvent::isBeginEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QTouchEvent12isBeginEventEv(const QTouchEvent *self) {
  return self->QTouchEvent::isBeginEvent();
}

//  bool QTouchEvent::isUpdateEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QTouchEvent13isUpdateEventEv(const QTouchEvent *self) {
  return self->QTouchEvent::isUpdateEvent();
}

//  bool QTouchEvent::isEndEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QTouchEvent10isEndEventEv(const QTouchEvent *self) {
  return self->QTouchEvent::isEndEvent();
}
