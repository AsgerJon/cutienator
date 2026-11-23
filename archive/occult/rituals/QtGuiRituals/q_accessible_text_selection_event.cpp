//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <cstring>

//  A QAccessibleTextSelectionEvent that Python can take functions over in. Every QAccessibleTextSelectionEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQAccessibleTextSelectionEventCall0)(const void *, int *);
class CuteQAccessibleTextSelectionEvent : public QAccessibleTextSelectionEvent {
public:
  using QAccessibleTextSelectionEvent::QAccessibleTextSelectionEvent;
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
      CuteQAccessibleTextSelectionEventCall0 call = reinterpret_cast<CuteQAccessibleTextSelectionEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleEvent::accessibleInterface();
  }
};

//  QAccessibleTextSelectionEvent::QAccessibleTextSelectionEvent(QObject
//      *obj, int start, int end)
extern "C" Q_DECL_EXPORT
QAccessibleTextSelectionEvent *ritual_ZN29QAccessibleTextSelectionEventC1EP7QObjectii(
    QObject *obj,
    int start,
    int end) {
  return new CuteQAccessibleTextSelectionEvent(obj, start, end);
}

//  QAccessibleTextSelectionEvent::QAccessibleTextSelectionEvent(QAccessibleI
//      nterface *iface, int start, int end)
extern "C" Q_DECL_EXPORT
QAccessibleTextSelectionEvent *ritual_ZN29QAccessibleTextSelectionEventC1EP20QAccessibleInterfaceii(
    QAccessibleInterface *iface,
    int start,
    int end) {
  return new CuteQAccessibleTextSelectionEvent(iface, start, end);
}

//  QAccessibleTextSelectionEvent::~QAccessibleTextSelectionEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QAccessibleTextSelectionEventD1Ev(
    QAccessibleTextSelectionEvent *self) {
  delete self;
}

//  void QAccessibleTextSelectionEvent::setSelection(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QAccessibleTextSelectionEvent12setSelectionEii(
    QAccessibleTextSelectionEvent *self,
    int start,
    int end) {
  self->setSelection(start, end);
}

//  int QAccessibleTextSelectionEvent::selectionStart() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QAccessibleTextSelectionEvent14selectionStartEv(
    const QAccessibleTextSelectionEvent *self) {
  return self->selectionStart();
}

//  int QAccessibleTextSelectionEvent::selectionEnd() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QAccessibleTextSelectionEvent12selectionEndEv(
    const QAccessibleTextSelectionEvent *self) {
  return self->selectionEnd();
}

//  a Python function taken by a CuteQAccessibleTextSelectionEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleTextSelectionEvent(
    QAccessibleTextSelectionEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleTextSelectionEvent *>(self)->take(key, call);
}
