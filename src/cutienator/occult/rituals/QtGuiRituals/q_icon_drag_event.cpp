//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <cstring>

//  A QIconDragEvent that Python can take functions over in. Every QIconDragEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQIconDragEventCall0)(const void *, int *);
typedef void (*CuteQIconDragEventCall1)(const void *, bool, int *);
class CuteQIconDragEvent : public QIconDragEvent {
public:
  using QIconDragEvent::QIconDragEvent;
  CuteQIconDragEvent(const QIconDragEvent & other) : QIconDragEvent(other) {}
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

  //  QIconDragEvent *QIconDragEvent::clone() const
  QIconDragEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQIconDragEventCall0 call = reinterpret_cast<CuteQIconDragEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIconDragEvent *>(given);
    }
    return QIconDragEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQIconDragEventCall1 call = reinterpret_cast<CuteQIconDragEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QIconDragEvent::QIconDragEvent(const QIconDragEvent &a0)
extern "C" Q_DECL_EXPORT
QIconDragEvent *ritual_ZN14QIconDragEventC1ERKS_(const QIconDragEvent *a0) {
  return new CuteQIconDragEvent(*a0);
}

//  QIconDragEvent &QIconDragEvent::operator=(const QIconDragEvent &other)
extern "C" Q_DECL_EXPORT
QIconDragEvent *ritual_ZN14QIconDragEventaSERKS_(
    QIconDragEvent *self,
    const QIconDragEvent *other) {
  return &(self->operator=(*other));
}

//  QIconDragEvent *QIconDragEvent::clone() const
extern "C" Q_DECL_EXPORT
QIconDragEvent *ritual_ZNK14QIconDragEvent5cloneEv(
    const QIconDragEvent *self) {
  return self->clone();
}

//  QIconDragEvent::~QIconDragEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QIconDragEventD1Ev(QIconDragEvent *self) {
  delete self;
}

//  QIconDragEvent::QIconDragEvent()
extern "C" Q_DECL_EXPORT
QIconDragEvent *ritual_ZN14QIconDragEventC1Ev() {
  return new CuteQIconDragEvent();
}

//  a Python function taken by a CuteQIconDragEvent, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QIconDragEvent(
    QIconDragEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQIconDragEvent *>(self)->take(key, call);
}

//  QIconDragEvent *QIconDragEvent::clone() const
extern "C" Q_DECL_EXPORT
QIconDragEvent *ritual_own_ZNK14QIconDragEvent5cloneEv(
    const QIconDragEvent *self) {
  return self->QIconDragEvent::clone();
}
