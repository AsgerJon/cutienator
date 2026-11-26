//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcoreevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcoreevent.h>
#include <cstring>

//  A QChildEvent that Python can take functions over in. Every QChildEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQChildEventCall0)(const void *, int *);
typedef void (*CuteQChildEventCall1)(const void *, bool, int *);
class CuteQChildEvent : public QChildEvent {
public:
  using QChildEvent::QChildEvent;
  CuteQChildEvent(const QChildEvent & other) : QChildEvent(other) {}
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

  //  QChildEvent *QChildEvent::clone() const
  QChildEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQChildEventCall0 call = reinterpret_cast<CuteQChildEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QChildEvent *>(given);
    }
    return QChildEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQChildEventCall1 call = reinterpret_cast<CuteQChildEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QChildEvent::QChildEvent(const QChildEvent &a0)
extern "C" Q_DECL_EXPORT
QChildEvent *ritual_ZN11QChildEventC1ERKS_(const QChildEvent *a0) {
  return new CuteQChildEvent(*a0);
}

//  QChildEvent &QChildEvent::operator=(const QChildEvent &other)
extern "C" Q_DECL_EXPORT
QChildEvent *ritual_ZN11QChildEventaSERKS_(
    QChildEvent *self,
    const QChildEvent *other) {
  return &(self->operator=(*other));
}

//  QChildEvent *QChildEvent::clone() const
extern "C" Q_DECL_EXPORT
QChildEvent *ritual_ZNK11QChildEvent5cloneEv(const QChildEvent *self) {
  return self->clone();
}

//  QChildEvent::~QChildEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QChildEventD1Ev(QChildEvent *self) {
  delete self;
}

//  QChildEvent::QChildEvent(Type type, QObject *child)
extern "C" Q_DECL_EXPORT
QChildEvent *ritual_ZN11QChildEventC1EN6QEvent4TypeEP7QObject(
    QEvent::Type type,
    QObject *child) {
  return new CuteQChildEvent(type, child);
}

//  QObject *QChildEvent::child() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK11QChildEvent5childEv(const QChildEvent *self) {
  return self->child();
}

//  bool QChildEvent::added() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QChildEvent5addedEv(const QChildEvent *self) {
  return self->added();
}

//  bool QChildEvent::polished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QChildEvent8polishedEv(const QChildEvent *self) {
  return self->polished();
}

//  bool QChildEvent::removed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QChildEvent7removedEv(const QChildEvent *self) {
  return self->removed();
}

//  a Python function taken by a CuteQChildEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QChildEvent(
    QChildEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQChildEvent *>(self)->take(key, call);
}

//  QChildEvent *QChildEvent::clone() const
extern "C" Q_DECL_EXPORT
QChildEvent *ritual_own_ZNK11QChildEvent5cloneEv(const QChildEvent *self) {
  return self->QChildEvent::clone();
}
