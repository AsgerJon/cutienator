//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QMetaCallEvent that Python can take functions over in. Every QMetaCallEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQMetaCallEventCall0)(const void *, QObject *, int *);
typedef void (*CuteQMetaCallEventCall1)(const void *, bool, int *);
typedef void * (*CuteQMetaCallEventCall2)(const void *, int *);
class CuteQMetaCallEvent : public QMetaCallEvent {
public:
  using QMetaCallEvent::QMetaCallEvent;
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

  //  void QMetaCallEvent::placeMetaCall(QObject *object)
  void placeMetaCall(QObject *object) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMetaCallEventCall0 call = reinterpret_cast<CuteQMetaCallEventCall0>(taken[0]);
      call(this, object, &handled);
      if (handled) return;
    }
    QMetaCallEvent::placeMetaCall(object);
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMetaCallEventCall1 call = reinterpret_cast<CuteQMetaCallEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQMetaCallEventCall2 call = reinterpret_cast<CuteQMetaCallEventCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  void QMetaCallEvent::placeMetaCall(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMetaCallEvent13placeMetaCallEP7QObject(
    QMetaCallEvent *self,
    QObject *object) {
  self->placeMetaCall(object);
}

//  int QMetaCallEvent::id() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QMetaCallEvent2idEv(const QMetaCallEvent *self) {
  return self->id();
}

//  a Python function taken by a CuteQMetaCallEvent, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMetaCallEvent(
    QMetaCallEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMetaCallEvent *>(self)->take(key, call);
}

//  void QMetaCallEvent::placeMetaCall(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QMetaCallEvent13placeMetaCallEP7QObject(
    QMetaCallEvent *self,
    QObject *object) {
  self->QMetaCallEvent::placeMetaCall(object);
}
