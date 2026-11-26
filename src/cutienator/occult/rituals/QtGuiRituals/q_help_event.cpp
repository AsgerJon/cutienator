//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QHelpEvent that Python can take functions over in. Every QHelpEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQHelpEventCall0)(const void *, int *);
typedef void (*CuteQHelpEventCall1)(const void *, bool, int *);
class CuteQHelpEvent : public QHelpEvent {
public:
  using QHelpEvent::QHelpEvent;
  CuteQHelpEvent(const QHelpEvent & other) : QHelpEvent(other) {}
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

  //  QHelpEvent *QHelpEvent::clone() const
  QHelpEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQHelpEventCall0 call = reinterpret_cast<CuteQHelpEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QHelpEvent *>(given);
    }
    return QHelpEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHelpEventCall1 call = reinterpret_cast<CuteQHelpEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QHelpEvent::QHelpEvent(const QHelpEvent &a0)
extern "C" Q_DECL_EXPORT
QHelpEvent *ritual_ZN10QHelpEventC1ERKS_(const QHelpEvent *a0) {
  return new CuteQHelpEvent(*a0);
}

//  QHelpEvent &QHelpEvent::operator=(const QHelpEvent &other)
extern "C" Q_DECL_EXPORT
QHelpEvent *ritual_ZN10QHelpEventaSERKS_(
    QHelpEvent *self,
    const QHelpEvent *other) {
  return &(self->operator=(*other));
}

//  QHelpEvent *QHelpEvent::clone() const
extern "C" Q_DECL_EXPORT
QHelpEvent *ritual_ZNK10QHelpEvent5cloneEv(const QHelpEvent *self) {
  return self->clone();
}

//  QHelpEvent::~QHelpEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QHelpEventD1Ev(QHelpEvent *self) {
  delete self;
}

//  QHelpEvent::QHelpEvent(Type type, const QPoint &pos, const QPoint
//      &globalPos)
extern "C" Q_DECL_EXPORT
QHelpEvent *ritual_ZN10QHelpEventC1EN6QEvent4TypeERK6QPointS4_(
    QEvent::Type type,
    const QPoint *pos,
    const QPoint *globalPos) {
  return new CuteQHelpEvent(type, *pos, *globalPos);
}

//  int QHelpEvent::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QHelpEvent1xEv(const QHelpEvent *self) {
  return self->x();
}

//  int QHelpEvent::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QHelpEvent1yEv(const QHelpEvent *self) {
  return self->y();
}

//  int QHelpEvent::globalX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QHelpEvent7globalXEv(const QHelpEvent *self) {
  return self->globalX();
}

//  int QHelpEvent::globalY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QHelpEvent7globalYEv(const QHelpEvent *self) {
  return self->globalY();
}

//  const QPoint &QHelpEvent::pos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK10QHelpEvent3posEv(const QHelpEvent *self) {
  return new QPoint(self->pos());
}

//  const QPoint &QHelpEvent::globalPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK10QHelpEvent9globalPosEv(const QHelpEvent *self) {
  return new QPoint(self->globalPos());
}

//  a Python function taken by a CuteQHelpEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHelpEvent(QHelpEvent *self, const char *key, void *call) {
  return static_cast<CuteQHelpEvent *>(self)->take(key, call);
}

//  QHelpEvent *QHelpEvent::clone() const
extern "C" Q_DECL_EXPORT
QHelpEvent *ritual_own_ZNK10QHelpEvent5cloneEv(const QHelpEvent *self) {
  return self->QHelpEvent::clone();
}
