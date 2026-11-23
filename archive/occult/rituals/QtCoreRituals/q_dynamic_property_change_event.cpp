//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcoreevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcoreevent.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QDynamicPropertyChangeEvent that Python can take functions over in. Every QDynamicPropertyChangeEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQDynamicPropertyChangeEventCall0)(const void *, int *);
typedef void (*CuteQDynamicPropertyChangeEventCall1)(const void *, bool, int *);
class CuteQDynamicPropertyChangeEvent : public QDynamicPropertyChangeEvent {
public:
  using QDynamicPropertyChangeEvent::QDynamicPropertyChangeEvent;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QDynamicPropertyChangeEvent *QDynamicPropertyChangeEvent::clone()
  //      const
  QDynamicPropertyChangeEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDynamicPropertyChangeEventCall0 call = reinterpret_cast<CuteQDynamicPropertyChangeEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDynamicPropertyChangeEvent *>(given);
    }
    return QDynamicPropertyChangeEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDynamicPropertyChangeEventCall1 call = reinterpret_cast<CuteQDynamicPropertyChangeEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QDynamicPropertyChangeEvent *QDynamicPropertyChangeEvent::clone() const
extern "C" Q_DECL_EXPORT
QDynamicPropertyChangeEvent *ritual_ZNK27QDynamicPropertyChangeEvent5cloneEv(
    const QDynamicPropertyChangeEvent *self) {
  return self->clone();
}

//  QDynamicPropertyChangeEvent::~QDynamicPropertyChangeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDynamicPropertyChangeEventD1Ev(
    QDynamicPropertyChangeEvent *self) {
  delete self;
}

//  QDynamicPropertyChangeEvent::QDynamicPropertyChangeEvent(const QByteArray
//      &name)
extern "C" Q_DECL_EXPORT
QDynamicPropertyChangeEvent *ritual_ZN27QDynamicPropertyChangeEventC1ERK10QByteArray(
    const QByteArray *name) {
  return new CuteQDynamicPropertyChangeEvent(*name);
}

//  QByteArray QDynamicPropertyChangeEvent::propertyName() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK27QDynamicPropertyChangeEvent12propertyNameEv(
    const QDynamicPropertyChangeEvent *self) {
  return new QByteArray(self->propertyName());
}

//  a Python function taken by a CuteQDynamicPropertyChangeEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDynamicPropertyChangeEvent(
    QDynamicPropertyChangeEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDynamicPropertyChangeEvent *>(self)->take(key, call);
}

//  QDynamicPropertyChangeEvent *QDynamicPropertyChangeEvent::clone() const
extern "C" Q_DECL_EXPORT
QDynamicPropertyChangeEvent *ritual_own_ZNK27QDynamicPropertyChangeEvent5cloneEv(
    const QDynamicPropertyChangeEvent *self) {
  return self->QDynamicPropertyChangeEvent::clone();
}
