//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qaccessiblecache_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(accessibility)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qaccessiblecache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QAccessibleObjectDestroyedEvent that Python can take functions over in. Every QAccessibleObjectDestroyedEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleObjectDestroyedEventCall0)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleObjectDestroyedEvent : public QAccessibleObjectDestroyedEvent {
public:
  using QAccessibleObjectDestroyedEvent::QAccessibleObjectDestroyedEvent;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK16QAccessibleEvent19accessibleInterfaceEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleEvent::accessibleInterface() const
  QAccessibleInterface *accessibleInterface() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleObjectDestroyedEventCall0 call = reinterpret_cast<CuteQAccessibleObjectDestroyedEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleEvent::accessibleInterface();
  }
#endif  // QT_CONFIG(accessibility)
};

//  QAccessibleObjectDestroyedEvent::QAccessibleObjectDestroyedEvent(QObject
//      *obj)
extern "C" Q_DECL_EXPORT
QAccessibleObjectDestroyedEvent *ritual_ZN31QAccessibleObjectDestroyedEventC1EP7QObject(
    QObject *obj) {
  return new CuteQAccessibleObjectDestroyedEvent(obj);
}

//  QAccessibleObjectDestroyedEvent::QAccessibleObjectDestroyedEvent(QAccessi
//      bleInterface *iface)
extern "C" Q_DECL_EXPORT
QAccessibleObjectDestroyedEvent *ritual_ZN31QAccessibleObjectDestroyedEventC1EP20QAccessibleInterface(
    QAccessibleInterface *iface) {
  return new CuteQAccessibleObjectDestroyedEvent(iface);
}

//  QAccessibleObjectDestroyedEvent::QAccessibleObjectDestroyedEvent(QAccessi
//      ble::Id uniqueId)
extern "C" Q_DECL_EXPORT
QAccessibleObjectDestroyedEvent *ritual_ZN31QAccessibleObjectDestroyedEventC1Ej(
    QAccessible::Id uniqueId) {
  return new CuteQAccessibleObjectDestroyedEvent(uniqueId);
}

//  QAccessibleObjectDestroyedEvent::~QAccessibleObjectDestroyedEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QAccessibleObjectDestroyedEventD1Ev(
    QAccessibleObjectDestroyedEvent *self) {
  delete self;
}

//  a Python function taken by a CuteQAccessibleObjectDestroyedEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleObjectDestroyedEvent(
    QAccessibleObjectDestroyedEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleObjectDestroyedEvent *>(self)->take(key, call);
}

#endif  // QT_CONFIG(accessibility)
