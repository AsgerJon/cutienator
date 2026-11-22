//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A QAccessibleValueInterface that Python can take functions over in. Every QAccessibleValueInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQAccessibleValueInterfaceCall0)(const void *, int *);
typedef void (*CuteQAccessibleValueInterfaceCall1)(const void *, const QVariant *, int *);
typedef const QVariant * (*CuteQAccessibleValueInterfaceCall2)(const void *, int *);
typedef const QVariant * (*CuteQAccessibleValueInterfaceCall3)(const void *, int *);
typedef const QVariant * (*CuteQAccessibleValueInterfaceCall4)(const void *, int *);
class CuteQAccessibleValueInterface : public QAccessibleValueInterface {
public:
  using QAccessibleValueInterface::QAccessibleValueInterface;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12currentValueEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QAccessibleValueInterface15setCurrentValueERK8QVariant")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12maximumValueEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12minimumValueEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface15minimumStepSizeEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  QVariant QAccessibleValueInterface::currentValue() const
  QVariant currentValue() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleValueInterfaceCall0 call = reinterpret_cast<CuteQAccessibleValueInterfaceCall0>(taken[0]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QAccessibleValueInterface::setCurrentValue(const QVariant
  //      &value)
  void setCurrentValue(const QVariant &value) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleValueInterfaceCall1 call = reinterpret_cast<CuteQAccessibleValueInterfaceCall1>(taken[1]);
      call(this, &value, &handled);
      if (handled) return;
    }
  }

  //  QVariant QAccessibleValueInterface::maximumValue() const
  QVariant maximumValue() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleValueInterfaceCall2 call = reinterpret_cast<CuteQAccessibleValueInterfaceCall2>(taken[2]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QVariant QAccessibleValueInterface::minimumValue() const
  QVariant minimumValue() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleValueInterfaceCall3 call = reinterpret_cast<CuteQAccessibleValueInterfaceCall3>(taken[3]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QVariant QAccessibleValueInterface::minimumStepSize() const
  QVariant minimumStepSize() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleValueInterfaceCall4 call = reinterpret_cast<CuteQAccessibleValueInterfaceCall4>(taken[4]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QAccessibleValueInterface::~QAccessibleValueInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAccessibleValueInterfaceD1Ev(
    QAccessibleValueInterface *self) {
  delete self;
}

//  QVariant QAccessibleValueInterface::currentValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAccessibleValueInterface12currentValueEv(
    const QAccessibleValueInterface *self) {
  return new QVariant(self->currentValue());
}

//  void QAccessibleValueInterface::setCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAccessibleValueInterface15setCurrentValueERK8QVariant(
    QAccessibleValueInterface *self,
    const QVariant *value) {
  self->setCurrentValue(*value);
}

//  QVariant QAccessibleValueInterface::maximumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAccessibleValueInterface12maximumValueEv(
    const QAccessibleValueInterface *self) {
  return new QVariant(self->maximumValue());
}

//  QVariant QAccessibleValueInterface::minimumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAccessibleValueInterface12minimumValueEv(
    const QAccessibleValueInterface *self) {
  return new QVariant(self->minimumValue());
}

//  QVariant QAccessibleValueInterface::minimumStepSize() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAccessibleValueInterface15minimumStepSizeEv(
    const QAccessibleValueInterface *self) {
  return new QVariant(self->minimumStepSize());
}

//  a Python function taken by a CuteQAccessibleValueInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleValueInterface(
    QAccessibleValueInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleValueInterface *>(self)->take(key, call);
}
