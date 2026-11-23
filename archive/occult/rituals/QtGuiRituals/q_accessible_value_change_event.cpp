//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A QAccessibleValueChangeEvent that Python can take functions over in. Every QAccessibleValueChangeEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQAccessibleValueChangeEventCall0)(const void *, int *);
class CuteQAccessibleValueChangeEvent : public QAccessibleValueChangeEvent {
public:
  using QAccessibleValueChangeEvent::QAccessibleValueChangeEvent;
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
      CuteQAccessibleValueChangeEventCall0 call = reinterpret_cast<CuteQAccessibleValueChangeEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleEvent::accessibleInterface();
  }
};

//  QAccessibleValueChangeEvent::QAccessibleValueChangeEvent(QObject *obj,
//      const QVariant &val)
extern "C" Q_DECL_EXPORT
QAccessibleValueChangeEvent *ritual_ZN27QAccessibleValueChangeEventC1EP7QObjectRK8QVariant(
    QObject *obj,
    const QVariant *val) {
  return new CuteQAccessibleValueChangeEvent(obj, *val);
}

//  QAccessibleValueChangeEvent::QAccessibleValueChangeEvent(QAccessibleInter
//      face *iface, const QVariant &val)
extern "C" Q_DECL_EXPORT
QAccessibleValueChangeEvent *ritual_ZN27QAccessibleValueChangeEventC1EP20QAccessibleInterfaceRK8QVariant(
    QAccessibleInterface *iface,
    const QVariant *val) {
  return new CuteQAccessibleValueChangeEvent(iface, *val);
}

//  QAccessibleValueChangeEvent::~QAccessibleValueChangeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAccessibleValueChangeEventD1Ev(
    QAccessibleValueChangeEvent *self) {
  delete self;
}

//  void QAccessibleValueChangeEvent::setValue(const QVariant &val)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAccessibleValueChangeEvent8setValueERK8QVariant(
    QAccessibleValueChangeEvent *self,
    const QVariant *val) {
  self->setValue(*val);
}

//  QVariant QAccessibleValueChangeEvent::value() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK27QAccessibleValueChangeEvent5valueEv(
    const QAccessibleValueChangeEvent *self) {
  return new QVariant(self->value());
}

//  a Python function taken by a CuteQAccessibleValueChangeEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleValueChangeEvent(
    QAccessibleValueChangeEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleValueChangeEvent *>(self)->take(key, call);
}
