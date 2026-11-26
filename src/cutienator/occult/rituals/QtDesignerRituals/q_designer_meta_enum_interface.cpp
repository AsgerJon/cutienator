//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/abstractintrospection_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/abstractintrospection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  A QDesignerMetaEnumInterface that Python can take functions over in. Every QDesignerMetaEnumInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQDesignerMetaEnumInterfaceCall0)(const void *, int *);
typedef QString * (*CuteQDesignerMetaEnumInterfaceCall1)(const void *, int, int *);
typedef int (*CuteQDesignerMetaEnumInterfaceCall2)(const void *, int *);
typedef int (*CuteQDesignerMetaEnumInterfaceCall3)(const void *, const QString *, int *);
typedef int (*CuteQDesignerMetaEnumInterfaceCall4)(const void *, const QString *, int *);
typedef QString * (*CuteQDesignerMetaEnumInterfaceCall5)(const void *, int *);
typedef QString * (*CuteQDesignerMetaEnumInterfaceCall6)(const void *, int *);
typedef QString * (*CuteQDesignerMetaEnumInterfaceCall7)(const void *, int *);
typedef QString * (*CuteQDesignerMetaEnumInterfaceCall8)(const void *, int *);
typedef int (*CuteQDesignerMetaEnumInterfaceCall9)(const void *, int, int *);
typedef QString * (*CuteQDesignerMetaEnumInterfaceCall10)(const void *, int, int *);
typedef QString * (*CuteQDesignerMetaEnumInterfaceCall11)(const void *, int, int *);
class CuteQDesignerMetaEnumInterface : public QDesignerMetaEnumInterface {
public:
  using QDesignerMetaEnumInterface::QDesignerMetaEnumInterface;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK26QDesignerMetaEnumInterface6isFlagEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDesignerMetaEnumInterface3keyEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDesignerMetaEnumInterface8keyCountEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDesignerMetaEnumInterface10keyToValueERK7QString")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDesignerMetaEnumInterface11keysToValueERK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDesignerMetaEnumInterface4nameEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDesignerMetaEnumInterface8enumNameEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDesignerMetaEnumInterface5scopeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDesignerMetaEnumInterface9separatorEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDesignerMetaEnumInterface5valueEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDesignerMetaEnumInterface10valueToKeyEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QDesignerMetaEnumInterface11valueToKeysEi")) {
      taken[11] = call;
      return true;
    }
    return false;
  }

  //  bool QDesignerMetaEnumInterface::isFlag() const
  bool isFlag() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerMetaEnumInterfaceCall0 call = reinterpret_cast<CuteQDesignerMetaEnumInterfaceCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QDesignerMetaEnumInterface::key(int index) const
  QString key(int index) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerMetaEnumInterfaceCall1 call = reinterpret_cast<CuteQDesignerMetaEnumInterfaceCall1>(taken[1]);
      QString * given = call(this, index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  int QDesignerMetaEnumInterface::keyCount() const
  int keyCount() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerMetaEnumInterfaceCall2 call = reinterpret_cast<CuteQDesignerMetaEnumInterfaceCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QDesignerMetaEnumInterface::keyToValue(const QString &key) const
  int keyToValue(const QString &key) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerMetaEnumInterfaceCall3 call = reinterpret_cast<CuteQDesignerMetaEnumInterfaceCall3>(taken[3]);
      int given = call(this, &key, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QDesignerMetaEnumInterface::keysToValue(const QString &keys)
  //      const
  int keysToValue(const QString &keys) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerMetaEnumInterfaceCall4 call = reinterpret_cast<CuteQDesignerMetaEnumInterfaceCall4>(taken[4]);
      int given = call(this, &keys, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QDesignerMetaEnumInterface::name() const
  QString name() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerMetaEnumInterfaceCall5 call = reinterpret_cast<CuteQDesignerMetaEnumInterfaceCall5>(taken[5]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QDesignerMetaEnumInterface::enumName() const
  QString enumName() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerMetaEnumInterfaceCall6 call = reinterpret_cast<CuteQDesignerMetaEnumInterfaceCall6>(taken[6]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QDesignerMetaEnumInterface::scope() const
  QString scope() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerMetaEnumInterfaceCall7 call = reinterpret_cast<CuteQDesignerMetaEnumInterfaceCall7>(taken[7]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QDesignerMetaEnumInterface::separator() const
  QString separator() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerMetaEnumInterfaceCall8 call = reinterpret_cast<CuteQDesignerMetaEnumInterfaceCall8>(taken[8]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  int QDesignerMetaEnumInterface::value(int index) const
  int value(int index) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerMetaEnumInterfaceCall9 call = reinterpret_cast<CuteQDesignerMetaEnumInterfaceCall9>(taken[9]);
      int given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QDesignerMetaEnumInterface::valueToKey(int value) const
  QString valueToKey(int value) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerMetaEnumInterfaceCall10 call = reinterpret_cast<CuteQDesignerMetaEnumInterfaceCall10>(taken[10]);
      QString * given = call(this, value, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QDesignerMetaEnumInterface::valueToKeys(int value) const
  QString valueToKeys(int value) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerMetaEnumInterfaceCall11 call = reinterpret_cast<CuteQDesignerMetaEnumInterfaceCall11>(taken[11]);
      QString * given = call(this, value, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
};

//  QDesignerMetaEnumInterface::QDesignerMetaEnumInterface()
extern "C" Q_DECL_EXPORT
QDesignerMetaEnumInterface *ritual_ZN26QDesignerMetaEnumInterfaceC1Ev() {
  return new CuteQDesignerMetaEnumInterface();
}

//  QDesignerMetaEnumInterface::~QDesignerMetaEnumInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDesignerMetaEnumInterfaceD1Ev(
    QDesignerMetaEnumInterface *self) {
  delete self;
}

//  bool QDesignerMetaEnumInterface::isFlag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QDesignerMetaEnumInterface6isFlagEv(
    const QDesignerMetaEnumInterface *self) {
  return self->isFlag();
}

//  QString QDesignerMetaEnumInterface::key(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QDesignerMetaEnumInterface3keyEi(
    const QDesignerMetaEnumInterface *self,
    int index) {
  return new QString(self->key(index));
}

//  int QDesignerMetaEnumInterface::keyCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QDesignerMetaEnumInterface8keyCountEv(
    const QDesignerMetaEnumInterface *self) {
  return self->keyCount();
}

//  int QDesignerMetaEnumInterface::keyToValue(const QString &key) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QDesignerMetaEnumInterface10keyToValueERK7QString(
    const QDesignerMetaEnumInterface *self,
    const QString *key) {
  return self->keyToValue(*key);
}

//  int QDesignerMetaEnumInterface::keysToValue(const QString &keys) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QDesignerMetaEnumInterface11keysToValueERK7QString(
    const QDesignerMetaEnumInterface *self,
    const QString *keys) {
  return self->keysToValue(*keys);
}

//  QString QDesignerMetaEnumInterface::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QDesignerMetaEnumInterface4nameEv(
    const QDesignerMetaEnumInterface *self) {
  return new QString(self->name());
}

//  QString QDesignerMetaEnumInterface::enumName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QDesignerMetaEnumInterface8enumNameEv(
    const QDesignerMetaEnumInterface *self) {
  return new QString(self->enumName());
}

//  QString QDesignerMetaEnumInterface::scope() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QDesignerMetaEnumInterface5scopeEv(
    const QDesignerMetaEnumInterface *self) {
  return new QString(self->scope());
}

//  QString QDesignerMetaEnumInterface::separator() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QDesignerMetaEnumInterface9separatorEv(
    const QDesignerMetaEnumInterface *self) {
  return new QString(self->separator());
}

//  int QDesignerMetaEnumInterface::value(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QDesignerMetaEnumInterface5valueEi(
    const QDesignerMetaEnumInterface *self,
    int index) {
  return self->value(index);
}

//  QString QDesignerMetaEnumInterface::valueToKey(int value) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QDesignerMetaEnumInterface10valueToKeyEi(
    const QDesignerMetaEnumInterface *self,
    int value) {
  return new QString(self->valueToKey(value));
}

//  QString QDesignerMetaEnumInterface::valueToKeys(int value) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QDesignerMetaEnumInterface11valueToKeysEi(
    const QDesignerMetaEnumInterface *self,
    int value) {
  return new QString(self->valueToKeys(value));
}

//  a Python function taken by a CuteQDesignerMetaEnumInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerMetaEnumInterface(
    QDesignerMetaEnumInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerMetaEnumInterface *>(self)->take(key, call);
}
