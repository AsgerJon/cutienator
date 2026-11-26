//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>
#include <QtGui/qeventpoint.h>
#include <cstring>

//  A QSinglePointEvent that Python can take functions over in. Every QSinglePointEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSinglePointEventCall0)(const void *, int *);
typedef bool (*CuteQSinglePointEventCall1)(const void *, int *);
typedef bool (*CuteQSinglePointEventCall2)(const void *, int *);
typedef bool (*CuteQSinglePointEventCall3)(const void *, int *);
typedef void (*CuteQSinglePointEventCall4)(const void *, quint64, int *);
typedef void (*CuteQSinglePointEventCall5)(const void *, bool, int *);
class CuteQSinglePointEvent : public QSinglePointEvent {
public:
  using QSinglePointEvent::QSinglePointEvent;
  CuteQSinglePointEvent(const QSinglePointEvent & other) : QSinglePointEvent(other) {}
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

  //  QSinglePointEvent *QSinglePointEvent::clone() const
  QSinglePointEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSinglePointEventCall0 call = reinterpret_cast<CuteQSinglePointEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSinglePointEvent *>(given);
    }
    return QSinglePointEvent::clone();
  }

  //  bool QSinglePointEvent::isBeginEvent() const
  bool isBeginEvent() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSinglePointEventCall1 call = reinterpret_cast<CuteQSinglePointEventCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSinglePointEvent::isBeginEvent();
  }

  //  bool QSinglePointEvent::isUpdateEvent() const
  bool isUpdateEvent() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSinglePointEventCall2 call = reinterpret_cast<CuteQSinglePointEventCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSinglePointEvent::isUpdateEvent();
  }

  //  bool QSinglePointEvent::isEndEvent() const
  bool isEndEvent() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSinglePointEventCall3 call = reinterpret_cast<CuteQSinglePointEventCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSinglePointEvent::isEndEvent();
  }

  //  void QPointerEvent::setTimestamp(quint64 timestamp)
  void setTimestamp(quint64 timestamp) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSinglePointEventCall4 call = reinterpret_cast<CuteQSinglePointEventCall4>(taken[4]);
      call(this, timestamp, &handled);
      if (handled) return;
    }
    QPointerEvent::setTimestamp(timestamp);
  }

  //  void QPointerEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSinglePointEventCall5 call = reinterpret_cast<CuteQSinglePointEventCall5>(taken[5]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QPointerEvent::setAccepted(accepted);
  }
};

//  QSinglePointEvent::QSinglePointEvent(const QSinglePointEvent &a0)
extern "C" Q_DECL_EXPORT
QSinglePointEvent *ritual_ZN17QSinglePointEventC1ERKS_(
    const QSinglePointEvent *a0) {
  return new CuteQSinglePointEvent(*a0);
}

//  QSinglePointEvent &QSinglePointEvent::operator=(const QSinglePointEvent
//      &other)
extern "C" Q_DECL_EXPORT
QSinglePointEvent *ritual_ZN17QSinglePointEventaSERKS_(
    QSinglePointEvent *self,
    const QSinglePointEvent *other) {
  return &(self->operator=(*other));
}

//  QSinglePointEvent *QSinglePointEvent::clone() const
extern "C" Q_DECL_EXPORT
QSinglePointEvent *ritual_ZNK17QSinglePointEvent5cloneEv(
    const QSinglePointEvent *self) {
  return self->clone();
}

//  QSinglePointEvent::~QSinglePointEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSinglePointEventD1Ev(QSinglePointEvent *self) {
  delete self;
}

//  Qt::MouseButton QSinglePointEvent::button() const
extern "C" Q_DECL_EXPORT
Qt::MouseButton ritual_ZNK17QSinglePointEvent6buttonEv(
    const QSinglePointEvent *self) {
  return self->button();
}

//  Qt::MouseButtons QSinglePointEvent::buttons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QSinglePointEvent7buttonsEv(const QSinglePointEvent *self) {
  return static_cast<int>(self->buttons().toInt());
}

//  QPointF QSinglePointEvent::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK17QSinglePointEvent8positionEv(
    const QSinglePointEvent *self) {
  return new QPointF(self->position());
}

//  QPointF QSinglePointEvent::scenePosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK17QSinglePointEvent13scenePositionEv(
    const QSinglePointEvent *self) {
  return new QPointF(self->scenePosition());
}

//  QPointF QSinglePointEvent::globalPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK17QSinglePointEvent14globalPositionEv(
    const QSinglePointEvent *self) {
  return new QPointF(self->globalPosition());
}

//  bool QSinglePointEvent::isBeginEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSinglePointEvent12isBeginEventEv(
    const QSinglePointEvent *self) {
  return self->isBeginEvent();
}

//  bool QSinglePointEvent::isUpdateEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSinglePointEvent13isUpdateEventEv(
    const QSinglePointEvent *self) {
  return self->isUpdateEvent();
}

//  bool QSinglePointEvent::isEndEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSinglePointEvent10isEndEventEv(
    const QSinglePointEvent *self) {
  return self->isEndEvent();
}

//  QObject *QSinglePointEvent::exclusivePointGrabber() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK17QSinglePointEvent21exclusivePointGrabberEv(
    const QSinglePointEvent *self) {
  return self->exclusivePointGrabber();
}

//  void QSinglePointEvent::setExclusivePointGrabber(QObject
//      *exclusiveGrabber)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSinglePointEvent24setExclusivePointGrabberEP7QObject(
    QSinglePointEvent *self,
    QObject *exclusiveGrabber) {
  self->setExclusivePointGrabber(exclusiveGrabber);
}

//  QSinglePointEvent::QSinglePointEvent(Type type, const QPointingDevice
//      *dev, const QEventPoint &point, Qt::MouseButton button,
//      Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers,
//      Qt::MouseEventSource source)
extern "C" Q_DECL_EXPORT
QSinglePointEvent *ritual_ZN17QSinglePointEventC1EN6QEvent4TypeEPK15QPointingDeviceRK11QEventPointN2Qt11MouseButtonE6QFlagsIS9_ESA_INS8_16KeyboardModifierEENS8_16MouseEventSourceE(
    QEvent::Type type,
    const QPointingDevice *dev,
    const QEventPoint *point,
    Qt::MouseButton button,
    int buttons,
    int modifiers,
    Qt::MouseEventSource source) {
  return new CuteQSinglePointEvent(
      type,
      dev,
      *point,
      button,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      source);
}

//  QSinglePointEvent::QSinglePointEvent(Type type, const QPointingDevice
//      *dev, const QPointF &localPos, const QPointF &scenePos, const QPointF
//      &globalPos, Qt::MouseButton button, Qt::MouseButtons buttons,
//      Qt::KeyboardModifiers modifiers, Qt::MouseEventSource source)
extern "C" Q_DECL_EXPORT
QSinglePointEvent *ritual_ZN17QSinglePointEventC1EN6QEvent4TypeEPK15QPointingDeviceRK7QPointFS7_S7_N2Qt11MouseButtonE6QFlagsIS9_ESA_INS8_16KeyboardModifierEENS8_16MouseEventSourceE(
    QEvent::Type type,
    const QPointingDevice *dev,
    const QPointF *localPos,
    const QPointF *scenePos,
    const QPointF *globalPos,
    Qt::MouseButton button,
    int buttons,
    int modifiers,
    Qt::MouseEventSource source) {
  return new CuteQSinglePointEvent(
      type,
      dev,
      *localPos,
      *scenePos,
      *globalPos,
      button,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      source);
}

//  a Python function taken by a CuteQSinglePointEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSinglePointEvent(
    QSinglePointEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSinglePointEvent *>(self)->take(key, call);
}

//  QSinglePointEvent *QSinglePointEvent::clone() const
extern "C" Q_DECL_EXPORT
QSinglePointEvent *ritual_own_ZNK17QSinglePointEvent5cloneEv(
    const QSinglePointEvent *self) {
  return self->QSinglePointEvent::clone();
}

//  bool QSinglePointEvent::isBeginEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QSinglePointEvent12isBeginEventEv(
    const QSinglePointEvent *self) {
  return self->QSinglePointEvent::isBeginEvent();
}

//  bool QSinglePointEvent::isUpdateEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QSinglePointEvent13isUpdateEventEv(
    const QSinglePointEvent *self) {
  return self->QSinglePointEvent::isUpdateEvent();
}

//  bool QSinglePointEvent::isEndEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QSinglePointEvent10isEndEventEv(
    const QSinglePointEvent *self) {
  return self->QSinglePointEvent::isEndEvent();
}
