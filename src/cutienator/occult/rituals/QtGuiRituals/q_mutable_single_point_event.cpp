//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qevent_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qevent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qeventpoint.h>
#include <cstring>

//  A QMutableSinglePointEvent that Python can take functions over in. Every QMutableSinglePointEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQMutableSinglePointEventCall0)(const void *, int *);
typedef bool (*CuteQMutableSinglePointEventCall1)(const void *, int *);
typedef bool (*CuteQMutableSinglePointEventCall2)(const void *, int *);
typedef bool (*CuteQMutableSinglePointEventCall3)(const void *, int *);
typedef void (*CuteQMutableSinglePointEventCall4)(const void *, quint64, int *);
typedef void (*CuteQMutableSinglePointEventCall5)(const void *, bool, int *);
class CuteQMutableSinglePointEvent : public QMutableSinglePointEvent {
public:
  using QMutableSinglePointEvent::QMutableSinglePointEvent;
  CuteQMutableSinglePointEvent(const QMutableSinglePointEvent & other) : QMutableSinglePointEvent(other) {}
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
      CuteQMutableSinglePointEventCall0 call = reinterpret_cast<CuteQMutableSinglePointEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSinglePointEvent *>(given);
    }
    return QSinglePointEvent::clone();
  }

  //  bool QSinglePointEvent::isBeginEvent() const
  bool isBeginEvent() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQMutableSinglePointEventCall1 call = reinterpret_cast<CuteQMutableSinglePointEventCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSinglePointEvent::isBeginEvent();
  }

  //  bool QSinglePointEvent::isUpdateEvent() const
  bool isUpdateEvent() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQMutableSinglePointEventCall2 call = reinterpret_cast<CuteQMutableSinglePointEventCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSinglePointEvent::isUpdateEvent();
  }

  //  bool QSinglePointEvent::isEndEvent() const
  bool isEndEvent() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQMutableSinglePointEventCall3 call = reinterpret_cast<CuteQMutableSinglePointEventCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSinglePointEvent::isEndEvent();
  }

  //  void QPointerEvent::setTimestamp(quint64 timestamp)
  void setTimestamp(quint64 timestamp) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMutableSinglePointEventCall4 call = reinterpret_cast<CuteQMutableSinglePointEventCall4>(taken[4]);
      call(this, timestamp, &handled);
      if (handled) return;
    }
    QPointerEvent::setTimestamp(timestamp);
  }

  //  void QPointerEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[5]) {
      int handled = 0;
      CuteQMutableSinglePointEventCall5 call = reinterpret_cast<CuteQMutableSinglePointEventCall5>(taken[5]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QPointerEvent::setAccepted(accepted);
  }
};

//  QMutableSinglePointEvent::QMutableSinglePointEvent(const
//      QSinglePointEvent &other)
extern "C" Q_DECL_EXPORT
QMutableSinglePointEvent *ritual_ZN24QMutableSinglePointEventC1ERK17QSinglePointEvent(
    const QSinglePointEvent *other) {
  return new CuteQMutableSinglePointEvent(*other);
}

//  QMutableSinglePointEvent::QMutableSinglePointEvent(Type type, const
//      QPointingDevice *device, const QEventPoint &point, Qt::MouseButton
//      button, Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers,
//      Qt::MouseEventSource source)
extern "C" Q_DECL_EXPORT
QMutableSinglePointEvent *ritual_ZN24QMutableSinglePointEventC1EN6QEvent4TypeEPK15QPointingDeviceRK11QEventPointN2Qt11MouseButtonE6QFlagsIS9_ESA_INS8_16KeyboardModifierEENS8_16MouseEventSourceE(
    QEvent::Type type,
    const QPointingDevice *device,
    const QEventPoint *point,
    Qt::MouseButton button,
    int buttons,
    int modifiers,
    Qt::MouseEventSource source) {
  return new CuteQMutableSinglePointEvent(
      type,
      device,
      *point,
      button,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      source);
}

//  QMutableSinglePointEvent::~QMutableSinglePointEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QMutableSinglePointEventD1Ev(
    QMutableSinglePointEvent *self) {
  delete self;
}

//  void QMutableSinglePointEvent::setSource(Qt::MouseEventSource s)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QMutableSinglePointEvent9setSourceEN2Qt16MouseEventSourceE(
    QMutableSinglePointEvent *self,
    Qt::MouseEventSource s) {
  self->setSource(s);
}

//  bool QMutableSinglePointEvent::isDoubleClick()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QMutableSinglePointEvent13isDoubleClickEv(
    QMutableSinglePointEvent *self) {
  return self->isDoubleClick();
}

//  void QMutableSinglePointEvent::setDoubleClick(bool d)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QMutableSinglePointEvent14setDoubleClickEb(
    QMutableSinglePointEvent *self,
    bool d) {
  self->setDoubleClick(d);
}

//  bool QMutableSinglePointEvent::isDoubleClick(const QSinglePointEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QMutableSinglePointEvent13isDoubleClickEPK17QSinglePointEvent(
    const QSinglePointEvent *ev) {
  return QMutableSinglePointEvent::isDoubleClick(ev);
}

//  void QMutableSinglePointEvent::setDoubleClick(QSinglePointEvent *ev, bool
//      d)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QMutableSinglePointEvent14setDoubleClickEP17QSinglePointEventb(
    QSinglePointEvent *ev,
    bool d) {
  QMutableSinglePointEvent::setDoubleClick(ev, d);
}

//  a Python function taken by a CuteQMutableSinglePointEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMutableSinglePointEvent(
    QMutableSinglePointEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMutableSinglePointEvent *>(self)->take(key, call);
}
