//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <cstring>

//  A QAccessibleEvent that Python can take functions over in. Every QAccessibleEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQAccessibleEventCall0)(const void *, int *);
class CuteQAccessibleEvent : public QAccessibleEvent {
public:
  using QAccessibleEvent::QAccessibleEvent;
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
      CuteQAccessibleEventCall0 call = reinterpret_cast<CuteQAccessibleEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleEvent::accessibleInterface();
  }
};

//  QAccessibleEvent::QAccessibleEvent(QObject *obj, QAccessible::Event typ)
extern "C" Q_DECL_EXPORT
QAccessibleEvent *ritual_ZN16QAccessibleEventC1EP7QObjectN11QAccessible5EventE(
    QObject *obj,
    QAccessible::Event typ) {
  return new CuteQAccessibleEvent(obj, typ);
}

//  QAccessibleEvent::QAccessibleEvent(QAccessibleInterface *iface,
//      QAccessible::Event typ)
extern "C" Q_DECL_EXPORT
QAccessibleEvent *ritual_ZN16QAccessibleEventC1EP20QAccessibleInterfaceN11QAccessible5EventE(
    QAccessibleInterface *iface,
    QAccessible::Event typ) {
  return new CuteQAccessibleEvent(iface, typ);
}

//  QAccessibleEvent::~QAccessibleEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAccessibleEventD1Ev(QAccessibleEvent *self) {
  delete self;
}

//  QAccessible::Event QAccessibleEvent::type() const
extern "C" Q_DECL_EXPORT
QAccessible::Event ritual_ZNK16QAccessibleEvent4typeEv(
    const QAccessibleEvent *self) {
  return self->type();
}

//  QObject *QAccessibleEvent::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK16QAccessibleEvent6objectEv(
    const QAccessibleEvent *self) {
  return self->object();
}

//  QAccessible::Id QAccessibleEvent::uniqueId() const
extern "C" Q_DECL_EXPORT
QAccessible::Id ritual_ZNK16QAccessibleEvent8uniqueIdEv(
    const QAccessibleEvent *self) {
  return self->uniqueId();
}

//  void QAccessibleEvent::setChild(int chld)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAccessibleEvent8setChildEi(
    QAccessibleEvent *self,
    int chld) {
  self->setChild(chld);
}

//  int QAccessibleEvent::child() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QAccessibleEvent5childEv(const QAccessibleEvent *self) {
  return self->child();
}

//  QAccessibleInterface *QAccessibleEvent::accessibleInterface() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK16QAccessibleEvent19accessibleInterfaceEv(
    const QAccessibleEvent *self) {
  return self->accessibleInterface();
}

//  a Python function taken by a CuteQAccessibleEvent, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleEvent(
    QAccessibleEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleEvent *>(self)->take(key, call);
}

//  QAccessibleInterface *QAccessibleEvent::accessibleInterface() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK16QAccessibleEvent19accessibleInterfaceEv(
    const QAccessibleEvent *self) {
  return self->QAccessibleEvent::accessibleInterface();
}
