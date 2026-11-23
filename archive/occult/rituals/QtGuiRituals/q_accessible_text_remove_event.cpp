//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QAccessibleTextRemoveEvent that Python can take functions over in. Every QAccessibleTextRemoveEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQAccessibleTextRemoveEventCall0)(const void *, int *);
class CuteQAccessibleTextRemoveEvent : public QAccessibleTextRemoveEvent {
public:
  using QAccessibleTextRemoveEvent::QAccessibleTextRemoveEvent;
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
      CuteQAccessibleTextRemoveEventCall0 call = reinterpret_cast<CuteQAccessibleTextRemoveEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleEvent::accessibleInterface();
  }
};

//  QAccessibleTextRemoveEvent::QAccessibleTextRemoveEvent(QObject *obj, int
//      position, const QString &text)
extern "C" Q_DECL_EXPORT
QAccessibleTextRemoveEvent *ritual_ZN26QAccessibleTextRemoveEventC1EP7QObjectiRK7QString(
    QObject *obj,
    int position,
    const QString *text) {
  return new CuteQAccessibleTextRemoveEvent(obj, position, *text);
}

//  QAccessibleTextRemoveEvent::QAccessibleTextRemoveEvent(QAccessibleInterfa
//      ce *iface, int position, const QString &text)
extern "C" Q_DECL_EXPORT
QAccessibleTextRemoveEvent *ritual_ZN26QAccessibleTextRemoveEventC1EP20QAccessibleInterfaceiRK7QString(
    QAccessibleInterface *iface,
    int position,
    const QString *text) {
  return new CuteQAccessibleTextRemoveEvent(iface, position, *text);
}

//  QAccessibleTextRemoveEvent::~QAccessibleTextRemoveEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleTextRemoveEventD1Ev(
    QAccessibleTextRemoveEvent *self) {
  delete self;
}

//  QString QAccessibleTextRemoveEvent::textRemoved() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QAccessibleTextRemoveEvent11textRemovedEv(
    const QAccessibleTextRemoveEvent *self) {
  return new QString(self->textRemoved());
}

//  int QAccessibleTextRemoveEvent::changePosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QAccessibleTextRemoveEvent14changePositionEv(
    const QAccessibleTextRemoveEvent *self) {
  return self->changePosition();
}

//  a Python function taken by a CuteQAccessibleTextRemoveEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleTextRemoveEvent(
    QAccessibleTextRemoveEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleTextRemoveEvent *>(self)->take(key, call);
}
