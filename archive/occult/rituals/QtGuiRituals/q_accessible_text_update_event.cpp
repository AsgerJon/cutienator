//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QAccessibleTextUpdateEvent that Python can take functions over in. Every QAccessibleTextUpdateEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQAccessibleTextUpdateEventCall0)(const void *, int *);
class CuteQAccessibleTextUpdateEvent : public QAccessibleTextUpdateEvent {
public:
  using QAccessibleTextUpdateEvent::QAccessibleTextUpdateEvent;
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
      CuteQAccessibleTextUpdateEventCall0 call = reinterpret_cast<CuteQAccessibleTextUpdateEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleEvent::accessibleInterface();
  }
};

//  QAccessibleTextUpdateEvent::QAccessibleTextUpdateEvent(QObject *obj, int
//      position, const QString &oldText, const QString &text)
extern "C" Q_DECL_EXPORT
QAccessibleTextUpdateEvent *ritual_ZN26QAccessibleTextUpdateEventC1EP7QObjectiRK7QStringS4_(
    QObject *obj,
    int position,
    const QString *oldText,
    const QString *text) {
  return new CuteQAccessibleTextUpdateEvent(obj, position, *oldText, *text);
}

//  QAccessibleTextUpdateEvent::QAccessibleTextUpdateEvent(QAccessibleInterfa
//      ce *iface, int position, const QString &oldText, const QString &text)
extern "C" Q_DECL_EXPORT
QAccessibleTextUpdateEvent *ritual_ZN26QAccessibleTextUpdateEventC1EP20QAccessibleInterfaceiRK7QStringS4_(
    QAccessibleInterface *iface,
    int position,
    const QString *oldText,
    const QString *text) {
  return new CuteQAccessibleTextUpdateEvent(
      iface,
      position,
      *oldText,
      *text);
}

//  QAccessibleTextUpdateEvent::~QAccessibleTextUpdateEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleTextUpdateEventD1Ev(
    QAccessibleTextUpdateEvent *self) {
  delete self;
}

//  QString QAccessibleTextUpdateEvent::textRemoved() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QAccessibleTextUpdateEvent11textRemovedEv(
    const QAccessibleTextUpdateEvent *self) {
  return new QString(self->textRemoved());
}

//  QString QAccessibleTextUpdateEvent::textInserted() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QAccessibleTextUpdateEvent12textInsertedEv(
    const QAccessibleTextUpdateEvent *self) {
  return new QString(self->textInserted());
}

//  int QAccessibleTextUpdateEvent::changePosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QAccessibleTextUpdateEvent14changePositionEv(
    const QAccessibleTextUpdateEvent *self) {
  return self->changePosition();
}

//  a Python function taken by a CuteQAccessibleTextUpdateEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleTextUpdateEvent(
    QAccessibleTextUpdateEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleTextUpdateEvent *>(self)->take(key, call);
}
