//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QHoverEvent that Python can take functions over in. Every QHoverEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQHoverEventCall0)(const void *, int *);
typedef bool (*CuteQHoverEventCall1)(const void *, int *);
typedef bool (*CuteQHoverEventCall2)(const void *, int *);
typedef bool (*CuteQHoverEventCall3)(const void *, int *);
typedef void (*CuteQHoverEventCall4)(const void *, quint64, int *);
typedef void (*CuteQHoverEventCall5)(const void *, bool, int *);
class CuteQHoverEvent : public QHoverEvent {
public:
  using QHoverEvent::QHoverEvent;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPointerEvent13isUpdateEventEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPointerEvent12isBeginEventEv")) {
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

  //  QHoverEvent *QHoverEvent::clone() const
  QHoverEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQHoverEventCall0 call = reinterpret_cast<CuteQHoverEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QHoverEvent *>(given);
    }
    return QHoverEvent::clone();
  }

  //  bool QHoverEvent::isUpdateEvent() const
  bool isUpdateEvent() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQHoverEventCall1 call = reinterpret_cast<CuteQHoverEventCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QHoverEvent::isUpdateEvent();
  }

  //  bool QSinglePointEvent::isBeginEvent() const
  bool isBeginEvent() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQHoverEventCall2 call = reinterpret_cast<CuteQHoverEventCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSinglePointEvent::isBeginEvent();
  }

  //  bool QSinglePointEvent::isEndEvent() const
  bool isEndEvent() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQHoverEventCall3 call = reinterpret_cast<CuteQHoverEventCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSinglePointEvent::isEndEvent();
  }

  //  void QPointerEvent::setTimestamp(quint64 timestamp)
  void setTimestamp(quint64 timestamp) override {
    if (taken[4]) {
      int handled = 0;
      CuteQHoverEventCall4 call = reinterpret_cast<CuteQHoverEventCall4>(taken[4]);
      call(this, timestamp, &handled);
      if (handled) return;
    }
    QPointerEvent::setTimestamp(timestamp);
  }

  //  void QPointerEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[5]) {
      int handled = 0;
      CuteQHoverEventCall5 call = reinterpret_cast<CuteQHoverEventCall5>(taken[5]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QPointerEvent::setAccepted(accepted);
  }
};

//  QHoverEvent *QHoverEvent::clone() const
extern "C" Q_DECL_EXPORT
QHoverEvent *ritual_ZNK11QHoverEvent5cloneEv(const QHoverEvent *self) {
  return self->clone();
}

//  QHoverEvent::~QHoverEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHoverEventD1Ev(QHoverEvent *self) {
  delete self;
}

//  QHoverEvent::QHoverEvent(Type type, const QPointF &scenePos, const
//      QPointF &globalPos, const QPointF &oldPos, Qt::KeyboardModifiers
//      modifiers, const QPointingDevice *device)
extern "C" Q_DECL_EXPORT
QHoverEvent *ritual_ZN11QHoverEventC1EN6QEvent4TypeERK7QPointFS4_S4_6QFlagsIN2Qt16KeyboardModifierEEPK15QPointingDevice(
    QEvent::Type type,
    const QPointF *scenePos,
    const QPointF *globalPos,
    const QPointF *oldPos,
    int modifiers,
    const QPointingDevice *device) {
  return new CuteQHoverEvent(
      type,
      *scenePos,
      *globalPos,
      *oldPos,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      device);
}

//  QHoverEvent::QHoverEvent(Type type, const QPointF &pos, const QPointF
//      &oldPos, Qt::KeyboardModifiers modifiers, const QPointingDevice
//      *device)
extern "C" Q_DECL_EXPORT
QHoverEvent *ritual_ZN11QHoverEventC1EN6QEvent4TypeERK7QPointFS4_6QFlagsIN2Qt16KeyboardModifierEEPK15QPointingDevice(
    QEvent::Type type,
    const QPointF *pos,
    const QPointF *oldPos,
    int modifiers,
    const QPointingDevice *device) {
  return new CuteQHoverEvent(
      type,
      *pos,
      *oldPos,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      device);
}

//  QPoint QHoverEvent::pos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK11QHoverEvent3posEv(const QHoverEvent *self) {
  return new QPoint(self->pos());
}

//  QPointF QHoverEvent::posF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QHoverEvent4posFEv(const QHoverEvent *self) {
  return new QPointF(self->posF());
}

//  bool QHoverEvent::isUpdateEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHoverEvent13isUpdateEventEv(const QHoverEvent *self) {
  return self->isUpdateEvent();
}

//  QPoint QHoverEvent::oldPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK11QHoverEvent6oldPosEv(const QHoverEvent *self) {
  return new QPoint(self->oldPos());
}

//  QPointF QHoverEvent::oldPosF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QHoverEvent7oldPosFEv(const QHoverEvent *self) {
  return new QPointF(self->oldPosF());
}

//  a Python function taken by a CuteQHoverEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHoverEvent(
    QHoverEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHoverEvent *>(self)->take(key, call);
}

//  QHoverEvent *QHoverEvent::clone() const
extern "C" Q_DECL_EXPORT
QHoverEvent *ritual_own_ZNK11QHoverEvent5cloneEv(const QHoverEvent *self) {
  return self->QHoverEvent::clone();
}

//  bool QHoverEvent::isUpdateEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QHoverEvent13isUpdateEventEv(const QHoverEvent *self) {
  return self->QHoverEvent::isUpdateEvent();
}
