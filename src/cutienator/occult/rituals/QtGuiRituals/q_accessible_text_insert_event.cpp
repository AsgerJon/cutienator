//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QAccessibleTextInsertEvent that Python can take functions over in. Every QAccessibleTextInsertEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTextInsertEventCall0)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleTextInsertEvent : public QAccessibleTextInsertEvent {
public:
  using QAccessibleTextInsertEvent::QAccessibleTextInsertEvent;
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
      CuteQAccessibleTextInsertEventCall0 call = reinterpret_cast<CuteQAccessibleTextInsertEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleEvent::accessibleInterface();
  }
#endif  // QT_CONFIG(accessibility)
};

//  QAccessibleTextInsertEvent::QAccessibleTextInsertEvent(QObject *obj, int
//      position, const QString &text)
extern "C" Q_DECL_EXPORT
QAccessibleTextInsertEvent *ritual_ZN26QAccessibleTextInsertEventC1EP7QObjectiRK7QString(
    QObject *obj,
    int position,
    const QString *text) {
  return new CuteQAccessibleTextInsertEvent(obj, position, *text);
}

//  QAccessibleTextInsertEvent::QAccessibleTextInsertEvent(QAccessibleInterfa
//      ce *iface, int position, const QString &text)
extern "C" Q_DECL_EXPORT
QAccessibleTextInsertEvent *ritual_ZN26QAccessibleTextInsertEventC1EP20QAccessibleInterfaceiRK7QString(
    QAccessibleInterface *iface,
    int position,
    const QString *text) {
  return new CuteQAccessibleTextInsertEvent(iface, position, *text);
}

//  QAccessibleTextInsertEvent::~QAccessibleTextInsertEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleTextInsertEventD1Ev(
    QAccessibleTextInsertEvent *self) {
  delete self;
}

//  QString QAccessibleTextInsertEvent::textInserted() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QAccessibleTextInsertEvent12textInsertedEv(
    const QAccessibleTextInsertEvent *self) {
  return new QString(self->textInserted());
}

//  int QAccessibleTextInsertEvent::changePosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QAccessibleTextInsertEvent14changePositionEv(
    const QAccessibleTextInsertEvent *self) {
  return self->changePosition();
}

//  a Python function taken by a CuteQAccessibleTextInsertEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleTextInsertEvent(
    QAccessibleTextInsertEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleTextInsertEvent *>(self)->take(key, call);
}

#endif  // QT_CONFIG(accessibility)
