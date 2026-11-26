//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfutureinterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(future)
#if QT_CONFIG(future)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfutureinterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QFutureCallOutInterface that Python can take functions over in. Every QFutureCallOutInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(future)
typedef void (*CuteQFutureCallOutInterfaceCall0)(const void *, int *);
#endif  // QT_CONFIG(future)
class CuteQFutureCallOutInterface : public QFutureCallOutInterface {
public:
  using QFutureCallOutInterface::QFutureCallOutInterface;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(future)
    if (!std::strcmp(key, "_ZN23QFutureCallOutInterface28callOutInterfaceDisconnectedEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(future)
    return false;
  }

#if QT_CONFIG(future)
  //  void QFutureCallOutInterface::callOutInterfaceDisconnected()
  void callOutInterfaceDisconnected() override {
    if (taken[0]) {
      int handled = 0;
      CuteQFutureCallOutInterfaceCall0 call = reinterpret_cast<CuteQFutureCallOutInterfaceCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(future)
};

//  QFutureCallOutInterface::~QFutureCallOutInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QFutureCallOutInterfaceD1Ev(QFutureCallOutInterface *self) {
  delete self;
}

//  void QFutureCallOutInterface::postCallOutEvent(const QFutureCallOutEvent
//      &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QFutureCallOutInterface16postCallOutEventERK19QFutureCallOutEvent(
    QFutureCallOutInterface *self,
    const QFutureCallOutEvent *a0) {
  self->postCallOutEvent(*a0);
}

//  void QFutureCallOutInterface::callOutInterfaceDisconnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QFutureCallOutInterface28callOutInterfaceDisconnectedEv(
    QFutureCallOutInterface *self) {
  self->callOutInterfaceDisconnected();
}

//  a Python function taken by a CuteQFutureCallOutInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFutureCallOutInterface(
    QFutureCallOutInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFutureCallOutInterface *>(self)->take(key, call);
}

#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(future)
