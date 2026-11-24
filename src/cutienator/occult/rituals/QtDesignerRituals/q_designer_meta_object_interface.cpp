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

//  A QDesignerMetaObjectInterface that Python can take functions over in. Every QDesignerMetaObjectInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQDesignerMetaObjectInterfaceCall0)(const void *, int *);
typedef void * (*CuteQDesignerMetaObjectInterfaceCall1)(const void *, int, int *);
typedef int (*CuteQDesignerMetaObjectInterfaceCall2)(const void *, int *);
typedef int (*CuteQDesignerMetaObjectInterfaceCall3)(const void *, int *);
typedef int (*CuteQDesignerMetaObjectInterfaceCall4)(const void *, const QString *, int *);
typedef int (*CuteQDesignerMetaObjectInterfaceCall5)(const void *, const QString *, int *);
typedef int (*CuteQDesignerMetaObjectInterfaceCall6)(const void *, const QString *, int *);
typedef int (*CuteQDesignerMetaObjectInterfaceCall7)(const void *, const QString *, int *);
typedef int (*CuteQDesignerMetaObjectInterfaceCall8)(const void *, const QString *, int *);
typedef void * (*CuteQDesignerMetaObjectInterfaceCall9)(const void *, int, int *);
typedef int (*CuteQDesignerMetaObjectInterfaceCall10)(const void *, int *);
typedef int (*CuteQDesignerMetaObjectInterfaceCall11)(const void *, int *);
typedef void * (*CuteQDesignerMetaObjectInterfaceCall12)(const void *, int, int *);
typedef int (*CuteQDesignerMetaObjectInterfaceCall13)(const void *, int *);
typedef int (*CuteQDesignerMetaObjectInterfaceCall14)(const void *, int *);
typedef void * (*CuteQDesignerMetaObjectInterfaceCall15)(const void *, int *);
typedef void * (*CuteQDesignerMetaObjectInterfaceCall16)(const void *, int *);
class CuteQDesignerMetaObjectInterface : public QDesignerMetaObjectInterface {
public:
  using QDesignerMetaObjectInterface::QDesignerMetaObjectInterface;
  void *taken[17] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK28QDesignerMetaObjectInterface9classNameEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaObjectInterface10enumeratorEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaObjectInterface15enumeratorCountEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaObjectInterface16enumeratorOffsetEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaObjectInterface17indexOfEnumeratorERK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaObjectInterface13indexOfMethodERK7QString")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaObjectInterface15indexOfPropertyERK7QString")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaObjectInterface13indexOfSignalERK7QString")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaObjectInterface11indexOfSlotERK7QString")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaObjectInterface6methodEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaObjectInterface11methodCountEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaObjectInterface12methodOffsetEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaObjectInterface8propertyEi")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaObjectInterface13propertyCountEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaObjectInterface14propertyOffsetEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaObjectInterface10superClassEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaObjectInterface12userPropertyEv")) {
      taken[16] = call;
      return true;
    }
    return false;
  }

  //  QString QDesignerMetaObjectInterface::className() const
  QString className() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerMetaObjectInterfaceCall0 call = reinterpret_cast<CuteQDesignerMetaObjectInterfaceCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  const QDesignerMetaEnumInterface
  //      *QDesignerMetaObjectInterface::enumerator(int index) const
  const QDesignerMetaEnumInterface *enumerator(int index) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerMetaObjectInterfaceCall1 call = reinterpret_cast<CuteQDesignerMetaObjectInterfaceCall1>(taken[1]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<const QDesignerMetaEnumInterface *>(given);
    }
    return {};
  }

  //  int QDesignerMetaObjectInterface::enumeratorCount() const
  int enumeratorCount() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerMetaObjectInterfaceCall2 call = reinterpret_cast<CuteQDesignerMetaObjectInterfaceCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QDesignerMetaObjectInterface::enumeratorOffset() const
  int enumeratorOffset() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerMetaObjectInterfaceCall3 call = reinterpret_cast<CuteQDesignerMetaObjectInterfaceCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QDesignerMetaObjectInterface::indexOfEnumerator(const QString
  //      &name) const
  int indexOfEnumerator(const QString &name) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerMetaObjectInterfaceCall4 call = reinterpret_cast<CuteQDesignerMetaObjectInterfaceCall4>(taken[4]);
      int given = call(this, &name, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QDesignerMetaObjectInterface::indexOfMethod(const QString
  //      &method) const
  int indexOfMethod(const QString &method) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerMetaObjectInterfaceCall5 call = reinterpret_cast<CuteQDesignerMetaObjectInterfaceCall5>(taken[5]);
      int given = call(this, &method, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QDesignerMetaObjectInterface::indexOfProperty(const QString
  //      &name) const
  int indexOfProperty(const QString &name) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerMetaObjectInterfaceCall6 call = reinterpret_cast<CuteQDesignerMetaObjectInterfaceCall6>(taken[6]);
      int given = call(this, &name, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QDesignerMetaObjectInterface::indexOfSignal(const QString
  //      &signal) const
  int indexOfSignal(const QString &signal) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerMetaObjectInterfaceCall7 call = reinterpret_cast<CuteQDesignerMetaObjectInterfaceCall7>(taken[7]);
      int given = call(this, &signal, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QDesignerMetaObjectInterface::indexOfSlot(const QString &slot)
  //      const
  int indexOfSlot(const QString &slot) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerMetaObjectInterfaceCall8 call = reinterpret_cast<CuteQDesignerMetaObjectInterfaceCall8>(taken[8]);
      int given = call(this, &slot, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  const QDesignerMetaMethodInterface
  //      *QDesignerMetaObjectInterface::method(int index) const
  const QDesignerMetaMethodInterface *method(int index) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerMetaObjectInterfaceCall9 call = reinterpret_cast<CuteQDesignerMetaObjectInterfaceCall9>(taken[9]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<const QDesignerMetaMethodInterface *>(given);
    }
    return {};
  }

  //  int QDesignerMetaObjectInterface::methodCount() const
  int methodCount() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerMetaObjectInterfaceCall10 call = reinterpret_cast<CuteQDesignerMetaObjectInterfaceCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QDesignerMetaObjectInterface::methodOffset() const
  int methodOffset() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerMetaObjectInterfaceCall11 call = reinterpret_cast<CuteQDesignerMetaObjectInterfaceCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  const QDesignerMetaPropertyInterface
  //      *QDesignerMetaObjectInterface::property(int index) const
  const QDesignerMetaPropertyInterface *property(int index) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQDesignerMetaObjectInterfaceCall12 call = reinterpret_cast<CuteQDesignerMetaObjectInterfaceCall12>(taken[12]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<const QDesignerMetaPropertyInterface *>(given);
    }
    return {};
  }

  //  int QDesignerMetaObjectInterface::propertyCount() const
  int propertyCount() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQDesignerMetaObjectInterfaceCall13 call = reinterpret_cast<CuteQDesignerMetaObjectInterfaceCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QDesignerMetaObjectInterface::propertyOffset() const
  int propertyOffset() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQDesignerMetaObjectInterfaceCall14 call = reinterpret_cast<CuteQDesignerMetaObjectInterfaceCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  const QDesignerMetaObjectInterface
  //      *QDesignerMetaObjectInterface::superClass() const
  const QDesignerMetaObjectInterface *superClass() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQDesignerMetaObjectInterfaceCall15 call = reinterpret_cast<CuteQDesignerMetaObjectInterfaceCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QDesignerMetaObjectInterface *>(given);
    }
    return {};
  }

  //  const QDesignerMetaPropertyInterface
  //      *QDesignerMetaObjectInterface::userProperty() const
  const QDesignerMetaPropertyInterface *userProperty() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQDesignerMetaObjectInterfaceCall16 call = reinterpret_cast<CuteQDesignerMetaObjectInterfaceCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QDesignerMetaPropertyInterface *>(given);
    }
    return {};
  }
};

//  QDesignerMetaObjectInterface::~QDesignerMetaObjectInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerMetaObjectInterfaceD1Ev(
    QDesignerMetaObjectInterface *self) {
  delete self;
}

//  QString QDesignerMetaObjectInterface::className() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QDesignerMetaObjectInterface9classNameEv(
    const QDesignerMetaObjectInterface *self) {
  return new QString(self->className());
}

//  const QDesignerMetaEnumInterface
//      *QDesignerMetaObjectInterface::enumerator(int index) const
extern "C" Q_DECL_EXPORT
const QDesignerMetaEnumInterface *ritual_ZNK28QDesignerMetaObjectInterface10enumeratorEi(
    const QDesignerMetaObjectInterface *self,
    int index) {
  return self->enumerator(index);
}

//  int QDesignerMetaObjectInterface::enumeratorCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QDesignerMetaObjectInterface15enumeratorCountEv(
    const QDesignerMetaObjectInterface *self) {
  return self->enumeratorCount();
}

//  int QDesignerMetaObjectInterface::enumeratorOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QDesignerMetaObjectInterface16enumeratorOffsetEv(
    const QDesignerMetaObjectInterface *self) {
  return self->enumeratorOffset();
}

//  int QDesignerMetaObjectInterface::indexOfEnumerator(const QString &name)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QDesignerMetaObjectInterface17indexOfEnumeratorERK7QString(
    const QDesignerMetaObjectInterface *self,
    const QString *name) {
  return self->indexOfEnumerator(*name);
}

//  int QDesignerMetaObjectInterface::indexOfMethod(const QString &method)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QDesignerMetaObjectInterface13indexOfMethodERK7QString(
    const QDesignerMetaObjectInterface *self,
    const QString *method) {
  return self->indexOfMethod(*method);
}

//  int QDesignerMetaObjectInterface::indexOfProperty(const QString &name)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QDesignerMetaObjectInterface15indexOfPropertyERK7QString(
    const QDesignerMetaObjectInterface *self,
    const QString *name) {
  return self->indexOfProperty(*name);
}

//  int QDesignerMetaObjectInterface::indexOfSignal(const QString &signal)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QDesignerMetaObjectInterface13indexOfSignalERK7QString(
    const QDesignerMetaObjectInterface *self,
    const QString *signal) {
  return self->indexOfSignal(*signal);
}

//  int QDesignerMetaObjectInterface::indexOfSlot(const QString &slot) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QDesignerMetaObjectInterface11indexOfSlotERK7QString(
    const QDesignerMetaObjectInterface *self,
    const QString *slot) {
  return self->indexOfSlot(*slot);
}

//  const QDesignerMetaMethodInterface
//      *QDesignerMetaObjectInterface::method(int index) const
extern "C" Q_DECL_EXPORT
const QDesignerMetaMethodInterface *ritual_ZNK28QDesignerMetaObjectInterface6methodEi(
    const QDesignerMetaObjectInterface *self,
    int index) {
  return self->method(index);
}

//  int QDesignerMetaObjectInterface::methodCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QDesignerMetaObjectInterface11methodCountEv(
    const QDesignerMetaObjectInterface *self) {
  return self->methodCount();
}

//  int QDesignerMetaObjectInterface::methodOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QDesignerMetaObjectInterface12methodOffsetEv(
    const QDesignerMetaObjectInterface *self) {
  return self->methodOffset();
}

//  const QDesignerMetaPropertyInterface
//      *QDesignerMetaObjectInterface::property(int index) const
extern "C" Q_DECL_EXPORT
const QDesignerMetaPropertyInterface *ritual_ZNK28QDesignerMetaObjectInterface8propertyEi(
    const QDesignerMetaObjectInterface *self,
    int index) {
  return self->property(index);
}

//  int QDesignerMetaObjectInterface::propertyCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QDesignerMetaObjectInterface13propertyCountEv(
    const QDesignerMetaObjectInterface *self) {
  return self->propertyCount();
}

//  int QDesignerMetaObjectInterface::propertyOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QDesignerMetaObjectInterface14propertyOffsetEv(
    const QDesignerMetaObjectInterface *self) {
  return self->propertyOffset();
}

//  const QDesignerMetaObjectInterface
//      *QDesignerMetaObjectInterface::superClass() const
extern "C" Q_DECL_EXPORT
const QDesignerMetaObjectInterface *ritual_ZNK28QDesignerMetaObjectInterface10superClassEv(
    const QDesignerMetaObjectInterface *self) {
  return self->superClass();
}

//  const QDesignerMetaPropertyInterface
//      *QDesignerMetaObjectInterface::userProperty() const
extern "C" Q_DECL_EXPORT
const QDesignerMetaPropertyInterface *ritual_ZNK28QDesignerMetaObjectInterface12userPropertyEv(
    const QDesignerMetaObjectInterface *self) {
  return self->userProperty();
}

//  a Python function taken by a CuteQDesignerMetaObjectInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerMetaObjectInterface(
    QDesignerMetaObjectInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerMetaObjectInterface *>(self)->take(key, call);
}
