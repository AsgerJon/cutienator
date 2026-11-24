//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(gestures)
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QNativeGestureEvent that Python can take functions over in. Every QNativeGestureEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(gestures)
typedef void * (*CuteQNativeGestureEventCall0)(const void *, int *);
#endif  // QT_CONFIG(gestures)
typedef bool (*CuteQNativeGestureEventCall1)(const void *, int *);
typedef bool (*CuteQNativeGestureEventCall2)(const void *, int *);
typedef bool (*CuteQNativeGestureEventCall3)(const void *, int *);
typedef void (*CuteQNativeGestureEventCall4)(const void *, quint64, int *);
typedef void (*CuteQNativeGestureEventCall5)(const void *, bool, int *);
class CuteQNativeGestureEvent : public QNativeGestureEvent {
public:
  using QNativeGestureEvent::QNativeGestureEvent;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(gestures)
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(gestures)
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

#if QT_CONFIG(gestures)
  //  QNativeGestureEvent *QNativeGestureEvent::clone() const
  QNativeGestureEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNativeGestureEventCall0 call = reinterpret_cast<CuteQNativeGestureEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QNativeGestureEvent *>(given);
    }
    return QNativeGestureEvent::clone();
  }
#endif  // QT_CONFIG(gestures)

  //  bool QSinglePointEvent::isBeginEvent() const
  bool isBeginEvent() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNativeGestureEventCall1 call = reinterpret_cast<CuteQNativeGestureEventCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSinglePointEvent::isBeginEvent();
  }

  //  bool QSinglePointEvent::isUpdateEvent() const
  bool isUpdateEvent() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNativeGestureEventCall2 call = reinterpret_cast<CuteQNativeGestureEventCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSinglePointEvent::isUpdateEvent();
  }

  //  bool QSinglePointEvent::isEndEvent() const
  bool isEndEvent() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNativeGestureEventCall3 call = reinterpret_cast<CuteQNativeGestureEventCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSinglePointEvent::isEndEvent();
  }

  //  void QPointerEvent::setTimestamp(quint64 timestamp)
  void setTimestamp(quint64 timestamp) override {
    if (taken[4]) {
      int handled = 0;
      CuteQNativeGestureEventCall4 call = reinterpret_cast<CuteQNativeGestureEventCall4>(taken[4]);
      call(this, timestamp, &handled);
      if (handled) return;
    }
    QPointerEvent::setTimestamp(timestamp);
  }

  //  void QPointerEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNativeGestureEventCall5 call = reinterpret_cast<CuteQNativeGestureEventCall5>(taken[5]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QPointerEvent::setAccepted(accepted);
  }
};

//  QNativeGestureEvent *QNativeGestureEvent::clone() const
extern "C" Q_DECL_EXPORT
QNativeGestureEvent *ritual_ZNK19QNativeGestureEvent5cloneEv(
    const QNativeGestureEvent *self) {
  return self->clone();
}

//  QNativeGestureEvent::~QNativeGestureEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QNativeGestureEventD1Ev(QNativeGestureEvent *self) {
  delete self;
}

#if QT_DEPRECATED_SINCE(6, 2)
//  QNativeGestureEvent::QNativeGestureEvent(Qt::NativeGestureType type,
//      const QPointingDevice *dev, const QPointF &localPos, const QPointF
//      &scenePos, const QPointF &globalPos, qreal value, quint64 sequenceId,
//      quint64 intArgument)
extern "C" Q_DECL_EXPORT
QNativeGestureEvent *ritual_ZN19QNativeGestureEventC1EN2Qt17NativeGestureTypeEPK15QPointingDeviceRK7QPointFS7_S7_dyy(
    Qt::NativeGestureType type,
    const QPointingDevice *dev,
    const QPointF *localPos,
    const QPointF *scenePos,
    const QPointF *globalPos,
    qreal value,
    quint64 sequenceId,
    quint64 intArgument) {
  return new CuteQNativeGestureEvent(
      type,
      dev,
      *localPos,
      *scenePos,
      *globalPos,
      value,
      sequenceId,
      intArgument);
}
#endif  // QT_DEPRECATED_SINCE(6, 2)

//  QNativeGestureEvent::QNativeGestureEvent(Qt::NativeGestureType type,
//      const QPointingDevice *dev, int fingerCount, const QPointF &localPos,
//      const QPointF &scenePos, const QPointF &globalPos, qreal value, const
//      QPointF &delta, quint64 sequenceId)
extern "C" Q_DECL_EXPORT
QNativeGestureEvent *ritual_ZN19QNativeGestureEventC1EN2Qt17NativeGestureTypeEPK15QPointingDeviceiRK7QPointFS7_S7_dS7_y(
    Qt::NativeGestureType type,
    const QPointingDevice *dev,
    int fingerCount,
    const QPointF *localPos,
    const QPointF *scenePos,
    const QPointF *globalPos,
    qreal value,
    const QPointF *delta,
    quint64 sequenceId) {
  return new CuteQNativeGestureEvent(
      type,
      dev,
      fingerCount,
      *localPos,
      *scenePos,
      *globalPos,
      value,
      *delta,
      sequenceId);
}

//  Qt::NativeGestureType QNativeGestureEvent::gestureType() const
extern "C" Q_DECL_EXPORT
Qt::NativeGestureType ritual_ZNK19QNativeGestureEvent11gestureTypeEv(
    const QNativeGestureEvent *self) {
  return self->gestureType();
}

//  int QNativeGestureEvent::fingerCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QNativeGestureEvent11fingerCountEv(
    const QNativeGestureEvent *self) {
  return self->fingerCount();
}

//  qreal QNativeGestureEvent::value() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QNativeGestureEvent5valueEv(
    const QNativeGestureEvent *self) {
  return self->value();
}

//  QPointF QNativeGestureEvent::delta() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QNativeGestureEvent5deltaEv(
    const QNativeGestureEvent *self) {
  return new QPointF(self->delta());
}

#if QT_DEPRECATED_SINCE(6, 0)
#if !defined(QT_NO_INTEGER_EVENT_COORDINATES)
//  const QPoint QNativeGestureEvent::pos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK19QNativeGestureEvent3posEv(
    const QNativeGestureEvent *self) {
  return new QPoint(self->pos());
}
#endif  // !defined(QT_NO_INTEGER_EVENT_COORDINATES)
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
#if !defined(QT_NO_INTEGER_EVENT_COORDINATES)
//  const QPoint QNativeGestureEvent::globalPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK19QNativeGestureEvent9globalPosEv(
    const QNativeGestureEvent *self) {
  return new QPoint(self->globalPos());
}
#endif  // !defined(QT_NO_INTEGER_EVENT_COORDINATES)
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QPointF QNativeGestureEvent::localPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QNativeGestureEvent8localPosEv(
    const QNativeGestureEvent *self) {
  return new QPointF(self->localPos());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QPointF QNativeGestureEvent::windowPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QNativeGestureEvent9windowPosEv(
    const QNativeGestureEvent *self) {
  return new QPointF(self->windowPos());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QPointF QNativeGestureEvent::screenPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QNativeGestureEvent9screenPosEv(
    const QNativeGestureEvent *self) {
  return new QPointF(self->screenPos());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  a Python function taken by a CuteQNativeGestureEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNativeGestureEvent(
    QNativeGestureEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNativeGestureEvent *>(self)->take(key, call);
}

//  QNativeGestureEvent *QNativeGestureEvent::clone() const
extern "C" Q_DECL_EXPORT
QNativeGestureEvent *ritual_own_ZNK19QNativeGestureEvent5cloneEv(
    const QNativeGestureEvent *self) {
  return self->QNativeGestureEvent::clone();
}

#endif  // QT_CONFIG(gestures)
