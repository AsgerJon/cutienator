//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QAbstractMetaCallEvent that Python can take functions over in. Every QAbstractMetaCallEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractMetaCallEventCall0)(const void *, QObject *, int *);
typedef void (*CuteQAbstractMetaCallEventCall1)(const void *, bool, int *);
typedef void * (*CuteQAbstractMetaCallEventCall2)(const void *, int *);
class CuteQAbstractMetaCallEvent : public QAbstractMetaCallEvent {
public:
  using QAbstractMetaCallEvent::QAbstractMetaCallEvent;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QAbstractMetaCallEvent13placeMetaCallEP7QObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QAbstractMetaCallEvent::placeMetaCall(QObject *object)
  void placeMetaCall(QObject *object) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractMetaCallEventCall0 call = reinterpret_cast<CuteQAbstractMetaCallEventCall0>(taken[0]);
      call(this, object, &handled);
      if (handled) return;
    }
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractMetaCallEventCall1 call = reinterpret_cast<CuteQAbstractMetaCallEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractMetaCallEventCall2 call = reinterpret_cast<CuteQAbstractMetaCallEventCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  QAbstractMetaCallEvent::QAbstractMetaCallEvent(const QObject *sender, int
//      signalId, QLatch *latch)
extern "C" Q_DECL_EXPORT
QAbstractMetaCallEvent *ritual_ZN22QAbstractMetaCallEventC1EPK7QObjectiP6QLatch(
    const QObject *sender,
    int signalId,
    QLatch *latch) {
  return new CuteQAbstractMetaCallEvent(sender, signalId, latch);
}

//  QAbstractMetaCallEvent::~QAbstractMetaCallEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractMetaCallEventD1Ev(QAbstractMetaCallEvent *self) {
  delete self;
}

//  void QAbstractMetaCallEvent::placeMetaCall(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractMetaCallEvent13placeMetaCallEP7QObject(
    QAbstractMetaCallEvent *self,
    QObject *object) {
  self->placeMetaCall(object);
}

//  const QObject *QAbstractMetaCallEvent::sender() const
extern "C" Q_DECL_EXPORT
const QObject *ritual_ZNK22QAbstractMetaCallEvent6senderEv(
    const QAbstractMetaCallEvent *self) {
  return self->sender();
}

//  int QAbstractMetaCallEvent::signalId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QAbstractMetaCallEvent8signalIdEv(
    const QAbstractMetaCallEvent *self) {
  return self->signalId();
}

//  a Python function taken by a CuteQAbstractMetaCallEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractMetaCallEvent(
    QAbstractMetaCallEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractMetaCallEvent *>(self)->take(key, call);
}
