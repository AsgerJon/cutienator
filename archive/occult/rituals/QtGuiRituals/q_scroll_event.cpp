//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QScrollEvent that Python can take functions over in. Every QScrollEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQScrollEventCall0)(const void *, int *);
typedef void (*CuteQScrollEventCall1)(const void *, bool, int *);
class CuteQScrollEvent : public QScrollEvent {
public:
  using QScrollEvent::QScrollEvent;
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

  //  QScrollEvent *QScrollEvent::clone() const
  QScrollEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQScrollEventCall0 call = reinterpret_cast<CuteQScrollEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QScrollEvent *>(given);
    }
    return QScrollEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQScrollEventCall1 call = reinterpret_cast<CuteQScrollEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QScrollEvent *QScrollEvent::clone() const
extern "C" Q_DECL_EXPORT
QScrollEvent *ritual_ZNK12QScrollEvent5cloneEv(const QScrollEvent *self) {
  return self->clone();
}

//  QScrollEvent::~QScrollEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QScrollEventD1Ev(QScrollEvent *self) {
  delete self;
}

//  QScrollEvent::QScrollEvent(const QPointF &contentPos, const QPointF
//      &overshoot, ScrollState scrollState)
extern "C" Q_DECL_EXPORT
QScrollEvent *ritual_ZN12QScrollEventC1ERK7QPointFS2_NS_11ScrollStateE(
    const QPointF *contentPos,
    const QPointF *overshoot,
    QScrollEvent::ScrollState scrollState) {
  return new CuteQScrollEvent(*contentPos, *overshoot, scrollState);
}

//  QPointF QScrollEvent::contentPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK12QScrollEvent10contentPosEv(const QScrollEvent *self) {
  return new QPointF(self->contentPos());
}

//  QPointF QScrollEvent::overshootDistance() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK12QScrollEvent17overshootDistanceEv(
    const QScrollEvent *self) {
  return new QPointF(self->overshootDistance());
}

//  ScrollState QScrollEvent::scrollState() const
extern "C" Q_DECL_EXPORT
QScrollEvent::ScrollState ritual_ZNK12QScrollEvent11scrollStateEv(
    const QScrollEvent *self) {
  return self->scrollState();
}

//  a Python function taken by a CuteQScrollEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScrollEvent(
    QScrollEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScrollEvent *>(self)->take(key, call);
}

//  QScrollEvent *QScrollEvent::clone() const
extern "C" Q_DECL_EXPORT
QScrollEvent *ritual_own_ZNK12QScrollEvent5cloneEv(
    const QScrollEvent *self) {
  return self->QScrollEvent::clone();
}
