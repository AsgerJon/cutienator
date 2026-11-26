//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QMoveEvent that Python can take functions over in. Every QMoveEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQMoveEventCall0)(const void *, int *);
typedef void (*CuteQMoveEventCall1)(const void *, bool, int *);
class CuteQMoveEvent : public QMoveEvent {
public:
  using QMoveEvent::QMoveEvent;
  CuteQMoveEvent(const QMoveEvent & other) : QMoveEvent(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QMoveEvent *QMoveEvent::clone() const
  QMoveEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQMoveEventCall0 call = reinterpret_cast<CuteQMoveEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QMoveEvent *>(given);
    }
    return QMoveEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMoveEventCall1 call = reinterpret_cast<CuteQMoveEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QMoveEvent::QMoveEvent(const QMoveEvent &a0)
extern "C" Q_DECL_EXPORT
QMoveEvent *ritual_ZN10QMoveEventC1ERKS_(const QMoveEvent *a0) {
  return new CuteQMoveEvent(*a0);
}

//  QMoveEvent &QMoveEvent::operator=(const QMoveEvent &other)
extern "C" Q_DECL_EXPORT
QMoveEvent *ritual_ZN10QMoveEventaSERKS_(
    QMoveEvent *self,
    const QMoveEvent *other) {
  return &(self->operator=(*other));
}

//  QMoveEvent *QMoveEvent::clone() const
extern "C" Q_DECL_EXPORT
QMoveEvent *ritual_ZNK10QMoveEvent5cloneEv(const QMoveEvent *self) {
  return self->clone();
}

//  QMoveEvent::~QMoveEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMoveEventD1Ev(QMoveEvent *self) {
  delete self;
}

//  QMoveEvent::QMoveEvent(const QPoint &pos, const QPoint &oldPos)
extern "C" Q_DECL_EXPORT
QMoveEvent *ritual_ZN10QMoveEventC1ERK6QPointS2_(
    const QPoint *pos,
    const QPoint *oldPos) {
  return new CuteQMoveEvent(*pos, *oldPos);
}

//  const QPoint &QMoveEvent::pos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK10QMoveEvent3posEv(const QMoveEvent *self) {
  return new QPoint(self->pos());
}

//  const QPoint &QMoveEvent::oldPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK10QMoveEvent6oldPosEv(const QMoveEvent *self) {
  return new QPoint(self->oldPos());
}

//  a Python function taken by a CuteQMoveEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMoveEvent(QMoveEvent *self, const char *key, void *call) {
  return static_cast<CuteQMoveEvent *>(self)->take(key, call);
}

//  QMoveEvent *QMoveEvent::clone() const
extern "C" Q_DECL_EXPORT
QMoveEvent *ritual_own_ZNK10QMoveEvent5cloneEv(const QMoveEvent *self) {
  return self->QMoveEvent::clone();
}
