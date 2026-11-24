//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QWindowSystemEventHandler that Python can take functions over in. Every QWindowSystemEventHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQWindowSystemEventHandlerCall0)(const void *, QWindowSystemInterfacePrivate::WindowSystemEvent *, int *);
class CuteQWindowSystemEventHandler : public QWindowSystemEventHandler {
public:
  using QWindowSystemEventHandler::QWindowSystemEventHandler;
  CuteQWindowSystemEventHandler(const QWindowSystemEventHandler &other) : QWindowSystemEventHandler(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QWindowSystemEventHandler9sendEventEPN29QWindowSystemInterfacePrivate17WindowSystemEventE")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  bool QWindowSystemEventHandler::sendEvent(QWindowSystemInterfacePriva
  //      te::WindowSystemEvent *event)
  bool sendEvent(
      QWindowSystemInterfacePrivate::WindowSystemEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWindowSystemEventHandlerCall0 call = reinterpret_cast<CuteQWindowSystemEventHandlerCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWindowSystemEventHandler::sendEvent(event);
  }
};

//  QWindowSystemEventHandler::~QWindowSystemEventHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWindowSystemEventHandlerD1Ev(
    QWindowSystemEventHandler *self) {
  delete self;
}

//  bool QWindowSystemEventHandler::sendEvent(QWindowSystemInterfacePrivate::
//      WindowSystemEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QWindowSystemEventHandler9sendEventEPN29QWindowSystemInterfacePrivate17WindowSystemEventE(
    QWindowSystemEventHandler *self,
    QWindowSystemInterfacePrivate::WindowSystemEvent *event) {
  return self->sendEvent(event);
}

//  a Python function taken by a CuteQWindowSystemEventHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowSystemEventHandler(
    QWindowSystemEventHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowSystemEventHandler *>(self)->take(key, call);
}

//  bool QWindowSystemEventHandler::sendEvent(QWindowSystemInterfacePrivate::
//      WindowSystemEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN25QWindowSystemEventHandler9sendEventEPN29QWindowSystemInterfacePrivate17WindowSystemEventE(
    QWindowSystemEventHandler *self,
    QWindowSystemInterfacePrivate::WindowSystemEvent *event) {
  return self->QWindowSystemEventHandler::sendEvent(event);
}
