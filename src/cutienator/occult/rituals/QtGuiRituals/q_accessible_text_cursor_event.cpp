//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <cstring>

//  A QAccessibleTextCursorEvent that Python can take functions over in. Every QAccessibleTextCursorEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQAccessibleTextCursorEventCall0)(const void *, int *);
class CuteQAccessibleTextCursorEvent : public QAccessibleTextCursorEvent {
public:
  using QAccessibleTextCursorEvent::QAccessibleTextCursorEvent;
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
      CuteQAccessibleTextCursorEventCall0 call = reinterpret_cast<CuteQAccessibleTextCursorEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleEvent::accessibleInterface();
  }
};

//  QAccessibleTextCursorEvent::QAccessibleTextCursorEvent(QObject *obj, int
//      cursorPos)
extern "C" Q_DECL_EXPORT
QAccessibleTextCursorEvent *ritual_ZN26QAccessibleTextCursorEventC1EP7QObjecti(
    QObject *obj,
    int cursorPos) {
  return new CuteQAccessibleTextCursorEvent(obj, cursorPos);
}

//  QAccessibleTextCursorEvent::QAccessibleTextCursorEvent(QAccessibleInterfa
//      ce *iface, int cursorPos)
extern "C" Q_DECL_EXPORT
QAccessibleTextCursorEvent *ritual_ZN26QAccessibleTextCursorEventC1EP20QAccessibleInterfacei(
    QAccessibleInterface *iface,
    int cursorPos) {
  return new CuteQAccessibleTextCursorEvent(iface, cursorPos);
}

//  QAccessibleTextCursorEvent::~QAccessibleTextCursorEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleTextCursorEventD1Ev(
    QAccessibleTextCursorEvent *self) {
  delete self;
}

//  void QAccessibleTextCursorEvent::setCursorPosition(int position)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleTextCursorEvent17setCursorPositionEi(
    QAccessibleTextCursorEvent *self,
    int position) {
  self->setCursorPosition(position);
}

//  int QAccessibleTextCursorEvent::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QAccessibleTextCursorEvent14cursorPositionEv(
    const QAccessibleTextCursorEvent *self) {
  return self->cursorPosition();
}

//  a Python function taken by a CuteQAccessibleTextCursorEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleTextCursorEvent(
    QAccessibleTextCursorEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleTextCursorEvent *>(self)->take(key, call);
}
