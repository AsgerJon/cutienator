//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(tabletevent)
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QTabletEvent that Python can take functions over in. Every QTabletEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(tabletevent)
typedef void * (*CuteQTabletEventCall0)(const void *, int *);
#endif  // QT_CONFIG(tabletevent)
typedef bool (*CuteQTabletEventCall1)(const void *, int *);
typedef bool (*CuteQTabletEventCall2)(const void *, int *);
typedef bool (*CuteQTabletEventCall3)(const void *, int *);
typedef void (*CuteQTabletEventCall4)(const void *, quint64, int *);
typedef void (*CuteQTabletEventCall5)(const void *, bool, int *);
class CuteQTabletEvent : public QTabletEvent {
public:
  using QTabletEvent::QTabletEvent;
  CuteQTabletEvent(const QTabletEvent & other) : QTabletEvent(other) {}
  void *taken[6] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
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

#if QT_CONFIG(tabletevent)
  //  QTabletEvent *QTabletEvent::clone() const
  QTabletEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTabletEventCall0 call = reinterpret_cast<CuteQTabletEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QTabletEvent *>(given);
    }
    return QTabletEvent::clone();
  }
#endif  // QT_CONFIG(tabletevent)

  //  bool QSinglePointEvent::isBeginEvent() const
  bool isBeginEvent() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTabletEventCall1 call = reinterpret_cast<CuteQTabletEventCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSinglePointEvent::isBeginEvent();
  }

  //  bool QSinglePointEvent::isUpdateEvent() const
  bool isUpdateEvent() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQTabletEventCall2 call = reinterpret_cast<CuteQTabletEventCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSinglePointEvent::isUpdateEvent();
  }

  //  bool QSinglePointEvent::isEndEvent() const
  bool isEndEvent() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQTabletEventCall3 call = reinterpret_cast<CuteQTabletEventCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSinglePointEvent::isEndEvent();
  }

  //  void QPointerEvent::setTimestamp(quint64 timestamp)
  void setTimestamp(quint64 timestamp) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTabletEventCall4 call = reinterpret_cast<CuteQTabletEventCall4>(taken[4]);
      call(this, timestamp, &handled);
      if (handled) return;
    }
    QPointerEvent::setTimestamp(timestamp);
  }

  //  void QPointerEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTabletEventCall5 call = reinterpret_cast<CuteQTabletEventCall5>(taken[5]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QPointerEvent::setAccepted(accepted);
  }
};

//  QTabletEvent::QTabletEvent(const QTabletEvent &a0)
extern "C" Q_DECL_EXPORT
QTabletEvent *ritual_ZN12QTabletEventC1ERKS_(const QTabletEvent *a0) {
  return new CuteQTabletEvent(*a0);
}

//  QTabletEvent &QTabletEvent::operator=(const QTabletEvent &other)
extern "C" Q_DECL_EXPORT
QTabletEvent *ritual_ZN12QTabletEventaSERKS_(
    QTabletEvent *self,
    const QTabletEvent *other) {
  return &(self->operator=(*other));
}

//  QTabletEvent *QTabletEvent::clone() const
extern "C" Q_DECL_EXPORT
QTabletEvent *ritual_ZNK12QTabletEvent5cloneEv(const QTabletEvent *self) {
  return self->clone();
}

//  QTabletEvent::~QTabletEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTabletEventD1Ev(QTabletEvent *self) {
  delete self;
}

//  QTabletEvent::QTabletEvent(Type t, const QPointingDevice *device, const
//      QPointF &pos, const QPointF &globalPos, qreal pressure, float xTilt,
//      float yTilt, float tangentialPressure, qreal rotation, float z,
//      Qt::KeyboardModifiers keyState, Qt::MouseButton button,
//      Qt::MouseButtons buttons)
extern "C" Q_DECL_EXPORT
QTabletEvent *ritual_ZN12QTabletEventC1EN6QEvent4TypeEPK15QPointingDeviceRK7QPointFS7_dfffdf6QFlagsIN2Qt16KeyboardModifierEENS9_11MouseButtonES8_ISC_E(
    QEvent::Type t,
    const QPointingDevice *device,
    const QPointF *pos,
    const QPointF *globalPos,
    qreal pressure,
    float xTilt,
    float yTilt,
    float tangentialPressure,
    qreal rotation,
    float z,
    int keyState,
    Qt::MouseButton button,
    int buttons) {
  return new CuteQTabletEvent(
      t,
      device,
      *pos,
      *globalPos,
      pressure,
      xTilt,
      yTilt,
      tangentialPressure,
      rotation,
      z,
      QFlags<Qt::KeyboardModifier>::fromInt(keyState),
      button,
      QFlags<Qt::MouseButton>::fromInt(buttons));
}

#if QT_DEPRECATED_SINCE(6, 0)
//  QPoint QTabletEvent::pos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK12QTabletEvent3posEv(const QTabletEvent *self) {
  return new QPoint(self->pos());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QPoint QTabletEvent::globalPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK12QTabletEvent9globalPosEv(const QTabletEvent *self) {
  return new QPoint(self->globalPos());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  const QPointF QTabletEvent::posF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK12QTabletEvent4posFEv(const QTabletEvent *self) {
  return new QPointF(self->posF());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  const QPointF QTabletEvent::globalPosF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK12QTabletEvent10globalPosFEv(const QTabletEvent *self) {
  return new QPointF(self->globalPosF());
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  int QTabletEvent::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTabletEvent1xEv(const QTabletEvent *self) {
  return self->x();
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  int QTabletEvent::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTabletEvent1yEv(const QTabletEvent *self) {
  return self->y();
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  int QTabletEvent::globalX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTabletEvent7globalXEv(const QTabletEvent *self) {
  return self->globalX();
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  int QTabletEvent::globalY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTabletEvent7globalYEv(const QTabletEvent *self) {
  return self->globalY();
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  qreal QTabletEvent::hiResGlobalX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QTabletEvent12hiResGlobalXEv(const QTabletEvent *self) {
  return self->hiResGlobalX();
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  qreal QTabletEvent::hiResGlobalY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QTabletEvent12hiResGlobalYEv(const QTabletEvent *self) {
  return self->hiResGlobalY();
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  qint64 QTabletEvent::uniqueId() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QTabletEvent8uniqueIdEv(const QTabletEvent *self) {
  return self->uniqueId();
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  qreal QTabletEvent::pressure() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QTabletEvent8pressureEv(const QTabletEvent *self) {
  return self->pressure();
}

//  qreal QTabletEvent::rotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QTabletEvent8rotationEv(const QTabletEvent *self) {
  return self->rotation();
}

//  qreal QTabletEvent::z() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QTabletEvent1zEv(const QTabletEvent *self) {
  return self->z();
}

//  qreal QTabletEvent::tangentialPressure() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QTabletEvent18tangentialPressureEv(
    const QTabletEvent *self) {
  return self->tangentialPressure();
}

//  qreal QTabletEvent::xTilt() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QTabletEvent5xTiltEv(const QTabletEvent *self) {
  return self->xTilt();
}

//  qreal QTabletEvent::yTilt() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QTabletEvent5yTiltEv(const QTabletEvent *self) {
  return self->yTilt();
}

//  a Python function taken by a CuteQTabletEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTabletEvent(
    QTabletEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTabletEvent *>(self)->take(key, call);
}

//  QTabletEvent *QTabletEvent::clone() const
extern "C" Q_DECL_EXPORT
QTabletEvent *ritual_own_ZNK12QTabletEvent5cloneEv(
    const QTabletEvent *self) {
  return self->QTabletEvent::clone();
}

#endif  // QT_CONFIG(tabletevent)
