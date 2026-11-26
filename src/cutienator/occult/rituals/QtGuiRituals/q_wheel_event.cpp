//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(wheelevent)
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QWheelEvent that Python can take functions over in. Every QWheelEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(wheelevent)
typedef void * (*CuteQWheelEventCall0)(const void *, int *);
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(wheelevent)
typedef bool (*CuteQWheelEventCall1)(const void *, int *);
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(wheelevent)
typedef bool (*CuteQWheelEventCall2)(const void *, int *);
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(wheelevent)
typedef bool (*CuteQWheelEventCall3)(const void *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQWheelEventCall4)(const void *, quint64, int *);
typedef void (*CuteQWheelEventCall5)(const void *, bool, int *);
class CuteQWheelEvent : public QWheelEvent {
public:
  using QWheelEvent::QWheelEvent;
  CuteQWheelEvent(const QWheelEvent & other) : QWheelEvent(other) {}
  void *taken[6] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZNK13QPointerEvent12isBeginEventEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZNK13QPointerEvent13isUpdateEventEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZNK13QPointerEvent10isEndEventEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
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

#if QT_CONFIG(wheelevent)
  //  QWheelEvent *QWheelEvent::clone() const
  QWheelEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQWheelEventCall0 call = reinterpret_cast<CuteQWheelEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWheelEvent *>(given);
    }
    return QWheelEvent::clone();
  }
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(wheelevent)
  //  bool QWheelEvent::isBeginEvent() const
  bool isBeginEvent() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWheelEventCall1 call = reinterpret_cast<CuteQWheelEventCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWheelEvent::isBeginEvent();
  }
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(wheelevent)
  //  bool QWheelEvent::isUpdateEvent() const
  bool isUpdateEvent() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQWheelEventCall2 call = reinterpret_cast<CuteQWheelEventCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWheelEvent::isUpdateEvent();
  }
#endif  // QT_CONFIG(wheelevent)

#if QT_CONFIG(wheelevent)
  //  bool QWheelEvent::isEndEvent() const
  bool isEndEvent() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQWheelEventCall3 call = reinterpret_cast<CuteQWheelEventCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWheelEvent::isEndEvent();
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QPointerEvent::setTimestamp(quint64 timestamp)
  void setTimestamp(quint64 timestamp) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWheelEventCall4 call = reinterpret_cast<CuteQWheelEventCall4>(taken[4]);
      call(this, timestamp, &handled);
      if (handled) return;
    }
    QPointerEvent::setTimestamp(timestamp);
  }

  //  void QPointerEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWheelEventCall5 call = reinterpret_cast<CuteQWheelEventCall5>(taken[5]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QPointerEvent::setAccepted(accepted);
  }
};

//  QWheelEvent::QWheelEvent(const QWheelEvent &a0)
extern "C" Q_DECL_EXPORT
QWheelEvent *ritual_ZN11QWheelEventC1ERKS_(const QWheelEvent *a0) {
  return new CuteQWheelEvent(*a0);
}

//  QWheelEvent &QWheelEvent::operator=(const QWheelEvent &other)
extern "C" Q_DECL_EXPORT
QWheelEvent *ritual_ZN11QWheelEventaSERKS_(
    QWheelEvent *self,
    const QWheelEvent *other) {
  return &(self->operator=(*other));
}

//  QWheelEvent *QWheelEvent::clone() const
extern "C" Q_DECL_EXPORT
QWheelEvent *ritual_ZNK11QWheelEvent5cloneEv(const QWheelEvent *self) {
  return self->clone();
}

//  QWheelEvent::~QWheelEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWheelEventD1Ev(QWheelEvent *self) {
  delete self;
}

//  QWheelEvent::QWheelEvent(const QPointF &pos, const QPointF &globalPos,
//      QPoint pixelDelta, QPoint angleDelta, Qt::MouseButtons buttons,
//      Qt::KeyboardModifiers modifiers, Qt::ScrollPhase phase, bool
//      inverted, Qt::MouseEventSource source, const QPointingDevice *device)
extern "C" Q_DECL_EXPORT
QWheelEvent *ritual_ZN11QWheelEventC1ERK7QPointFS2_6QPointS3_6QFlagsIN2Qt11MouseButtonEES4_INS5_16KeyboardModifierEENS5_11ScrollPhaseEbNS5_16MouseEventSourceEPK15QPointingDevice(
    const QPointF *pos,
    const QPointF *globalPos,
    const QPoint *pixelDelta,
    const QPoint *angleDelta,
    int buttons,
    int modifiers,
    Qt::ScrollPhase phase,
    bool inverted,
    Qt::MouseEventSource source,
    const QPointingDevice *device) {
  return new CuteQWheelEvent(
      *pos,
      *globalPos,
      *pixelDelta,
      *angleDelta,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      phase,
      inverted,
      source,
      device);
}

//  QPoint QWheelEvent::pixelDelta() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK11QWheelEvent10pixelDeltaEv(const QWheelEvent *self) {
  return new QPoint(self->pixelDelta());
}

//  QPoint QWheelEvent::angleDelta() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK11QWheelEvent10angleDeltaEv(const QWheelEvent *self) {
  return new QPoint(self->angleDelta());
}

//  Qt::ScrollPhase QWheelEvent::phase() const
extern "C" Q_DECL_EXPORT
Qt::ScrollPhase ritual_ZNK11QWheelEvent5phaseEv(const QWheelEvent *self) {
  return self->phase();
}

//  bool QWheelEvent::inverted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWheelEvent8invertedEv(const QWheelEvent *self) {
  return self->inverted();
}

//  bool QWheelEvent::isInverted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWheelEvent10isInvertedEv(const QWheelEvent *self) {
  return self->isInverted();
}

//  bool QWheelEvent::hasPixelDelta() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWheelEvent13hasPixelDeltaEv(const QWheelEvent *self) {
  return self->hasPixelDelta();
}

//  bool QWheelEvent::isBeginEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWheelEvent12isBeginEventEv(const QWheelEvent *self) {
  return self->isBeginEvent();
}

//  bool QWheelEvent::isUpdateEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWheelEvent13isUpdateEventEv(const QWheelEvent *self) {
  return self->isUpdateEvent();
}

//  bool QWheelEvent::isEndEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWheelEvent10isEndEventEv(const QWheelEvent *self) {
  return self->isEndEvent();
}

//  Qt::MouseEventSource QWheelEvent::source() const
extern "C" Q_DECL_EXPORT
Qt::MouseEventSource ritual_ZNK11QWheelEvent6sourceEv(
    const QWheelEvent *self) {
  return self->source();
}

//  a Python function taken by a CuteQWheelEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWheelEvent(
    QWheelEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWheelEvent *>(self)->take(key, call);
}

//  QWheelEvent *QWheelEvent::clone() const
extern "C" Q_DECL_EXPORT
QWheelEvent *ritual_own_ZNK11QWheelEvent5cloneEv(const QWheelEvent *self) {
  return self->QWheelEvent::clone();
}

//  bool QWheelEvent::isBeginEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QWheelEvent12isBeginEventEv(const QWheelEvent *self) {
  return self->QWheelEvent::isBeginEvent();
}

//  bool QWheelEvent::isUpdateEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QWheelEvent13isUpdateEventEv(const QWheelEvent *self) {
  return self->QWheelEvent::isUpdateEvent();
}

//  bool QWheelEvent::isEndEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QWheelEvent10isEndEventEv(const QWheelEvent *self) {
  return self->QWheelEvent::isEndEvent();
}

#endif  // QT_CONFIG(wheelevent)
