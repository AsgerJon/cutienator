//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractsettings.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/abstractsettings.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A QDesignerSettingsInterface that Python can take functions over in. Every QDesignerSettingsInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDesignerSettingsInterfaceCall0)(const void *, const QString *, int *);
typedef void (*CuteQDesignerSettingsInterfaceCall1)(const void *, int *);
typedef bool (*CuteQDesignerSettingsInterfaceCall2)(const void *, const QString *, int *);
typedef void (*CuteQDesignerSettingsInterfaceCall3)(const void *, const QString *, const QVariant *, int *);
typedef const QVariant * (*CuteQDesignerSettingsInterfaceCall4)(const void *, const QString *, const QVariant *, int *);
typedef void (*CuteQDesignerSettingsInterfaceCall5)(const void *, const QString *, int *);
class CuteQDesignerSettingsInterface : public QDesignerSettingsInterface {
public:
  using QDesignerSettingsInterface::QDesignerSettingsInterface;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QDesignerSettingsInterface10beginGroupERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDesignerSettingsInterface8endGroupEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDesignerSettingsInterface8containsERK7QString")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDesignerSettingsInterface8setValueERK7QStringRK8QVariant")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDesignerSettingsInterface5valueERK7QStringRK8QVariant")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QDesignerSettingsInterface6removeERK7QString")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  void QDesignerSettingsInterface::beginGroup(const QString &prefix)
  void beginGroup(const QString &prefix) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerSettingsInterfaceCall0 call = reinterpret_cast<CuteQDesignerSettingsInterfaceCall0>(taken[0]);
      call(this, &prefix, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerSettingsInterface::endGroup()
  void endGroup() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerSettingsInterfaceCall1 call = reinterpret_cast<CuteQDesignerSettingsInterfaceCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  bool QDesignerSettingsInterface::contains(const QString &key) const
  bool contains(const QString &key) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerSettingsInterfaceCall2 call = reinterpret_cast<CuteQDesignerSettingsInterfaceCall2>(taken[2]);
      bool given = call(this, &key, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerSettingsInterface::setValue(const QString &key, const
  //      QVariant &value)
  void setValue(const QString &key, const QVariant &value) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerSettingsInterfaceCall3 call = reinterpret_cast<CuteQDesignerSettingsInterfaceCall3>(taken[3]);
      call(this, &key, &value, &handled);
      if (handled) return;
    }
  }

  //  QVariant QDesignerSettingsInterface::value(const QString &key, const
  //      QVariant &defaultValue) const
  QVariant value(
      const QString &key,
      const QVariant &defaultValue) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerSettingsInterfaceCall4 call = reinterpret_cast<CuteQDesignerSettingsInterfaceCall4>(taken[4]);
      const QVariant * given = call(this, &key, &defaultValue, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QDesignerSettingsInterface::remove(const QString &key)
  void remove(const QString &key) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerSettingsInterfaceCall5 call = reinterpret_cast<CuteQDesignerSettingsInterfaceCall5>(taken[5]);
      call(this, &key, &handled);
      if (handled) return;
    }
  }
};

//  QDesignerSettingsInterface::~QDesignerSettingsInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDesignerSettingsInterfaceD1Ev(
    QDesignerSettingsInterface *self) {
  delete self;
}

//  void QDesignerSettingsInterface::beginGroup(const QString &prefix)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDesignerSettingsInterface10beginGroupERK7QString(
    QDesignerSettingsInterface *self,
    const QString *prefix) {
  self->beginGroup(*prefix);
}

//  void QDesignerSettingsInterface::endGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDesignerSettingsInterface8endGroupEv(
    QDesignerSettingsInterface *self) {
  self->endGroup();
}

//  bool QDesignerSettingsInterface::contains(const QString &key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QDesignerSettingsInterface8containsERK7QString(
    const QDesignerSettingsInterface *self,
    const QString *key) {
  return self->contains(*key);
}

//  void QDesignerSettingsInterface::setValue(const QString &key, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDesignerSettingsInterface8setValueERK7QStringRK8QVariant(
    QDesignerSettingsInterface *self,
    const QString *key,
    const QVariant *value) {
  self->setValue(*key, *value);
}

//  QVariant QDesignerSettingsInterface::value(const QString &key, const
//      QVariant &defaultValue) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK26QDesignerSettingsInterface5valueERK7QStringRK8QVariant(
    const QDesignerSettingsInterface *self,
    const QString *key,
    const QVariant *defaultValue) {
  return new QVariant(self->value(*key, *defaultValue));
}

//  void QDesignerSettingsInterface::remove(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDesignerSettingsInterface6removeERK7QString(
    QDesignerSettingsInterface *self,
    const QString *key) {
  self->remove(*key);
}

//  a Python function taken by a CuteQDesignerSettingsInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerSettingsInterface(
    QDesignerSettingsInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerSettingsInterface *>(self)->take(key, call);
}
