//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QEnterEvent that Python can take functions over in. Every QEnterEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQEnterEventCall0)(const void *, int *);
typedef bool (*CuteQEnterEventCall1)(const void *, int *);
typedef bool (*CuteQEnterEventCall2)(const void *, int *);
typedef bool (*CuteQEnterEventCall3)(const void *, int *);
typedef void (*CuteQEnterEventCall4)(const void *, quint64, int *);
typedef void (*CuteQEnterEventCall5)(const void *, bool, int *);
class CuteQEnterEvent : public QEnterEvent {
public:
  using QEnterEvent::QEnterEvent;
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

  //  QEnterEvent *QEnterEvent::clone() const
  QEnterEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQEnterEventCall0 call = reinterpret_cast<CuteQEnterEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEnterEvent *>(given);
    }
    return QEnterEvent::clone();
  }

  //  bool QSinglePointEvent::isBeginEvent() const
  bool isBeginEvent() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQEnterEventCall1 call = reinterpret_cast<CuteQEnterEventCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSinglePointEvent::isBeginEvent();
  }

  //  bool QSinglePointEvent::isUpdateEvent() const
  bool isUpdateEvent() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQEnterEventCall2 call = reinterpret_cast<CuteQEnterEventCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSinglePointEvent::isUpdateEvent();
  }

  //  bool QSinglePointEvent::isEndEvent() const
  bool isEndEvent() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQEnterEventCall3 call = reinterpret_cast<CuteQEnterEventCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSinglePointEvent::isEndEvent();
  }

  //  void QPointerEvent::setTimestamp(quint64 timestamp)
  void setTimestamp(quint64 timestamp) override {
    if (taken[4]) {
      int handled = 0;
      CuteQEnterEventCall4 call = reinterpret_cast<CuteQEnterEventCall4>(taken[4]);
      call(this, timestamp, &handled);
      if (handled) return;
    }
    QPointerEvent::setTimestamp(timestamp);
  }

  //  void QPointerEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[5]) {
      int handled = 0;
      CuteQEnterEventCall5 call = reinterpret_cast<CuteQEnterEventCall5>(taken[5]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QPointerEvent::setAccepted(accepted);
  }
};

//  QEnterEvent *QEnterEvent::clone() const
extern "C" Q_DECL_EXPORT
QEnterEvent *ritual_ZNK11QEnterEvent5cloneEv(const QEnterEvent *self) {
  return self->clone();
}

//  QEnterEvent::~QEnterEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QEnterEventD1Ev(QEnterEvent *self) {
  delete self;
}

//  QEnterEvent::QEnterEvent(const QPointF &localPos, const QPointF
//      &scenePos, const QPointF &globalPos, const QPointingDevice *device)
extern "C" Q_DECL_EXPORT
QEnterEvent *ritual_ZN11QEnterEventC1ERK7QPointFS2_S2_PK15QPointingDevice(
    const QPointF *localPos,
    const QPointF *scenePos,
    const QPointF *globalPos,
    const QPointingDevice *device) {
  return new CuteQEnterEvent(*localPos, *scenePos, *globalPos, device);
}

//  QPoint QEnterEvent::pos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK11QEnterEvent3posEv(const QEnterEvent *self) {
  return new QPoint(self->pos());
}

//  QPoint QEnterEvent::globalPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK11QEnterEvent9globalPosEv(const QEnterEvent *self) {
  return new QPoint(self->globalPos());
}

//  int QEnterEvent::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QEnterEvent1xEv(const QEnterEvent *self) {
  return self->x();
}

//  int QEnterEvent::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QEnterEvent1yEv(const QEnterEvent *self) {
  return self->y();
}

//  int QEnterEvent::globalX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QEnterEvent7globalXEv(const QEnterEvent *self) {
  return self->globalX();
}

//  int QEnterEvent::globalY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QEnterEvent7globalYEv(const QEnterEvent *self) {
  return self->globalY();
}

//  QPointF QEnterEvent::localPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEnterEvent8localPosEv(const QEnterEvent *self) {
  return new QPointF(self->localPos());
}

//  QPointF QEnterEvent::windowPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEnterEvent9windowPosEv(const QEnterEvent *self) {
  return new QPointF(self->windowPos());
}

//  QPointF QEnterEvent::screenPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEnterEvent9screenPosEv(const QEnterEvent *self) {
  return new QPointF(self->screenPos());
}

//  a Python function taken by a CuteQEnterEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QEnterEvent(
    QEnterEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQEnterEvent *>(self)->take(key, call);
}

//  QEnterEvent *QEnterEvent::clone() const
extern "C" Q_DECL_EXPORT
QEnterEvent *ritual_own_ZNK11QEnterEvent5cloneEv(const QEnterEvent *self) {
  return self->QEnterEvent::clone();
}
