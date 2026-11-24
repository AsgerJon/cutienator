//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QMouseEvent that Python can take functions over in. Every QMouseEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQMouseEventCall0)(const void *, int *);
typedef bool (*CuteQMouseEventCall1)(const void *, int *);
typedef bool (*CuteQMouseEventCall2)(const void *, int *);
typedef bool (*CuteQMouseEventCall3)(const void *, int *);
typedef void (*CuteQMouseEventCall4)(const void *, quint64, int *);
typedef void (*CuteQMouseEventCall5)(const void *, bool, int *);
class CuteQMouseEvent : public QMouseEvent {
public:
  using QMouseEvent::QMouseEvent;
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

  //  QMouseEvent *QMouseEvent::clone() const
  QMouseEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQMouseEventCall0 call = reinterpret_cast<CuteQMouseEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QMouseEvent *>(given);
    }
    return QMouseEvent::clone();
  }

  //  bool QSinglePointEvent::isBeginEvent() const
  bool isBeginEvent() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQMouseEventCall1 call = reinterpret_cast<CuteQMouseEventCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSinglePointEvent::isBeginEvent();
  }

  //  bool QSinglePointEvent::isUpdateEvent() const
  bool isUpdateEvent() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQMouseEventCall2 call = reinterpret_cast<CuteQMouseEventCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSinglePointEvent::isUpdateEvent();
  }

  //  bool QSinglePointEvent::isEndEvent() const
  bool isEndEvent() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQMouseEventCall3 call = reinterpret_cast<CuteQMouseEventCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSinglePointEvent::isEndEvent();
  }

  //  void QPointerEvent::setTimestamp(quint64 timestamp)
  void setTimestamp(quint64 timestamp) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMouseEventCall4 call = reinterpret_cast<CuteQMouseEventCall4>(taken[4]);
      call(this, timestamp, &handled);
      if (handled) return;
    }
    QPointerEvent::setTimestamp(timestamp);
  }

  //  void QPointerEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[5]) {
      int handled = 0;
      CuteQMouseEventCall5 call = reinterpret_cast<CuteQMouseEventCall5>(taken[5]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QPointerEvent::setAccepted(accepted);
  }
};

//  QMouseEvent *QMouseEvent::clone() const
extern "C" Q_DECL_EXPORT
QMouseEvent *ritual_ZNK11QMouseEvent5cloneEv(const QMouseEvent *self) {
  return self->clone();
}

//  QMouseEvent::~QMouseEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMouseEventD1Ev(QMouseEvent *self) {
  delete self;
}

#if QT_DEPRECATED_SINCE(6, 4)
//  QMouseEvent::QMouseEvent(Type type, const QPointF &localPos,
//      Qt::MouseButton button, Qt::MouseButtons buttons,
//      Qt::KeyboardModifiers modifiers, const QPointingDevice *device)
extern "C" Q_DECL_EXPORT
QMouseEvent *ritual_ZN11QMouseEventC1EN6QEvent4TypeERK7QPointFN2Qt11MouseButtonE6QFlagsIS6_ES7_INS5_16KeyboardModifierEEPK15QPointingDevice(
    QEvent::Type type,
    const QPointF *localPos,
    Qt::MouseButton button,
    int buttons,
    int modifiers,
    const QPointingDevice *device) {
  return new CuteQMouseEvent(
      type,
      *localPos,
      button,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      device);
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  QMouseEvent::QMouseEvent(Type type, const QPointF &localPos, const
//      QPointF &globalPos, Qt::MouseButton button, Qt::MouseButtons buttons,
//      Qt::KeyboardModifiers modifiers, const QPointingDevice *device)
extern "C" Q_DECL_EXPORT
QMouseEvent *ritual_ZN11QMouseEventC1EN6QEvent4TypeERK7QPointFS4_N2Qt11MouseButtonE6QFlagsIS6_ES7_INS5_16KeyboardModifierEEPK15QPointingDevice(
    QEvent::Type type,
    const QPointF *localPos,
    const QPointF *globalPos,
    Qt::MouseButton button,
    int buttons,
    int modifiers,
    const QPointingDevice *device) {
  return new CuteQMouseEvent(
      type,
      *localPos,
      *globalPos,
      button,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      device);
}

//  QMouseEvent::QMouseEvent(Type type, const QPointF &localPos, const
//      QPointF &scenePos, const QPointF &globalPos, Qt::MouseButton button,
//      Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers, const
//      QPointingDevice *device)
extern "C" Q_DECL_EXPORT
QMouseEvent *ritual_ZN11QMouseEventC1EN6QEvent4TypeERK7QPointFS4_S4_N2Qt11MouseButtonE6QFlagsIS6_ES7_INS5_16KeyboardModifierEEPK15QPointingDevice(
    QEvent::Type type,
    const QPointF *localPos,
    const QPointF *scenePos,
    const QPointF *globalPos,
    Qt::MouseButton button,
    int buttons,
    int modifiers,
    const QPointingDevice *device) {
  return new CuteQMouseEvent(
      type,
      *localPos,
      *scenePos,
      *globalPos,
      button,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      device);
}

//  QMouseEvent::QMouseEvent(Type type, const QPointF &localPos, const
//      QPointF &scenePos, const QPointF &globalPos, Qt::MouseButton button,
//      Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers,
//      Qt::MouseEventSource source, const QPointingDevice *device)
extern "C" Q_DECL_EXPORT
QMouseEvent *ritual_ZN11QMouseEventC1EN6QEvent4TypeERK7QPointFS4_S4_N2Qt11MouseButtonE6QFlagsIS6_ES7_INS5_16KeyboardModifierEENS5_16MouseEventSourceEPK15QPointingDevice(
    QEvent::Type type,
    const QPointF *localPos,
    const QPointF *scenePos,
    const QPointF *globalPos,
    Qt::MouseButton button,
    int buttons,
    int modifiers,
    Qt::MouseEventSource source,
    const QPointingDevice *device) {
  return new CuteQMouseEvent(
      type,
      *localPos,
      *scenePos,
      *globalPos,
      button,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      source,
      device);
}

#if !defined(QT_NO_INTEGER_EVENT_COORDINATES)
//  QPoint QMouseEvent::pos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK11QMouseEvent3posEv(const QMouseEvent *self) {
  return new QPoint(self->pos());
}
#endif  // !defined(QT_NO_INTEGER_EVENT_COORDINATES)

#if QT_DEPRECATED_SINCE(6, 0)
#if !defined(QT_NO_INTEGER_EVENT_COORDINATES)
//  QPoint QMouseEvent::globalPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK11QMouseEvent9globalPosEv(const QMouseEvent *self) {
  return new QPoint(self->globalPos());
}
#endif  // !defined(QT_NO_INTEGER_EVENT_COORDINATES)
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
#if !defined(QT_NO_INTEGER_EVENT_COORDINATES)
//  int QMouseEvent::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMouseEvent1xEv(const QMouseEvent *self) {
  return self->x();
}
#endif  // !defined(QT_NO_INTEGER_EVENT_COORDINATES)
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
#if !defined(QT_NO_INTEGER_EVENT_COORDINATES)
//  int QMouseEvent::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMouseEvent1yEv(const QMouseEvent *self) {
  return self->y();
}
#endif  // !defined(QT_NO_INTEGER_EVENT_COORDINATES)
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
#if !defined(QT_NO_INTEGER_EVENT_COORDINATES)
//  int QMouseEvent::globalX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMouseEvent7globalXEv(const QMouseEvent *self) {
  return self->globalX();
}
#endif  // !defined(QT_NO_INTEGER_EVENT_COORDINATES)
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
#if !defined(QT_NO_INTEGER_EVENT_COORDINATES)
//  int QMouseEvent::globalY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMouseEvent7globalYEv(const QMouseEvent *self) {
  return self->globalY();
}
#endif  // !defined(QT_NO_INTEGER_EVENT_COORDINATES)
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QPointF QMouseEvent::localPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QMouseEvent8localPosEv(const QMouseEvent *self) {
  return new QPointF(self->localPos());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QPointF QMouseEvent::windowPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QMouseEvent9windowPosEv(const QMouseEvent *self) {
  return new QPointF(self->windowPos());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QPointF QMouseEvent::screenPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QMouseEvent9screenPosEv(const QMouseEvent *self) {
  return new QPointF(self->screenPos());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  Qt::MouseEventSource QMouseEvent::source() const
extern "C" Q_DECL_EXPORT
Qt::MouseEventSource ritual_ZNK11QMouseEvent6sourceEv(
    const QMouseEvent *self) {
  return self->source();
}

//  Qt::MouseEventFlags QMouseEvent::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMouseEvent5flagsEv(const QMouseEvent *self) {
  return static_cast<int>(self->flags().toInt());
}

//  a Python function taken by a CuteQMouseEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMouseEvent(
    QMouseEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMouseEvent *>(self)->take(key, call);
}

//  QMouseEvent *QMouseEvent::clone() const
extern "C" Q_DECL_EXPORT
QMouseEvent *ritual_own_ZNK11QMouseEvent5cloneEv(const QMouseEvent *self) {
  return self->QMouseEvent::clone();
}
