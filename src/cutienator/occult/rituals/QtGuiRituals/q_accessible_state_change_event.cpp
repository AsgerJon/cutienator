//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtGui/QtGui>
#include <QtGui/qtestsupport_gui.h>
#include <QtGui/qvulkanfunctions.h>
#include <QtGui/qvulkaninstance.h>
#include <QtGui/qvulkanwindow.h>
#include <cstring>

//  A QAccessibleStateChangeEvent that Python can take functions over in. Every QAccessibleStateChangeEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQAccessibleStateChangeEventCall0)(const void *, int *);
class CuteQAccessibleStateChangeEvent : public QAccessibleStateChangeEvent {
public:
  using QAccessibleStateChangeEvent::QAccessibleStateChangeEvent;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QAccessibleEvent19accessibleInterfaceEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QAccessibleInterface *QAccessibleEvent::accessibleInterface() const
  QAccessibleInterface *accessibleInterface() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleStateChangeEventCall0 call = reinterpret_cast<CuteQAccessibleStateChangeEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleEvent::accessibleInterface();
  }
};

//  QAccessibleStateChangeEvent::QAccessibleStateChangeEvent(QObject *obj,
//      QAccessible::State state)
extern "C" Q_DECL_EXPORT
QAccessibleStateChangeEvent *ritual_ZN27QAccessibleStateChangeEventC1EP7QObjectN11QAccessible5StateE(
    QObject *obj,
    const QAccessible::State *state) {
  return new CuteQAccessibleStateChangeEvent(obj, *state);
}

//  QAccessibleStateChangeEvent::QAccessibleStateChangeEvent(QAccessibleInter
//      face *iface, QAccessible::State state)
extern "C" Q_DECL_EXPORT
QAccessibleStateChangeEvent *ritual_ZN27QAccessibleStateChangeEventC1EP20QAccessibleInterfaceN11QAccessible5StateE(
    QAccessibleInterface *iface,
    const QAccessible::State *state) {
  return new CuteQAccessibleStateChangeEvent(iface, *state);
}

//  QAccessibleStateChangeEvent::~QAccessibleStateChangeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAccessibleStateChangeEventD1Ev(
    QAccessibleStateChangeEvent *self) {
  delete self;
}

//  QAccessible::State QAccessibleStateChangeEvent::changedStates() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK27QAccessibleStateChangeEvent13changedStatesEv(
    const QAccessibleStateChangeEvent *self) {
  return new QAccessible::State(self->changedStates());
}

//  a Python function taken by a CuteQAccessibleStateChangeEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleStateChangeEvent(
    QAccessibleStateChangeEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleStateChangeEvent *>(self)->take(key, call);
}
