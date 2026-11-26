//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/abstractintrospection_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/abstractintrospection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A QDesignerMetaPropertyInterface that Python can take functions over in. Every QDesignerMetaPropertyInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQDesignerMetaPropertyInterfaceCall0)(const void *, int *);
typedef int (*CuteQDesignerMetaPropertyInterfaceCall1)(const void *, int *);
typedef int (*CuteQDesignerMetaPropertyInterfaceCall2)(const void *, int *);
typedef int (*CuteQDesignerMetaPropertyInterfaceCall3)(const void *, int *);
typedef int (*CuteQDesignerMetaPropertyInterfaceCall4)(const void *, int *);
typedef QString * (*CuteQDesignerMetaPropertyInterfaceCall5)(const void *, int *);
typedef QString * (*CuteQDesignerMetaPropertyInterfaceCall6)(const void *, int *);
typedef int (*CuteQDesignerMetaPropertyInterfaceCall7)(const void *, int *);
typedef bool (*CuteQDesignerMetaPropertyInterfaceCall8)(const void *, int *);
typedef const QVariant * (*CuteQDesignerMetaPropertyInterfaceCall9)(const void *, const QObject *, int *);
typedef bool (*CuteQDesignerMetaPropertyInterfaceCall10)(const void *, QObject *, int *);
typedef bool (*CuteQDesignerMetaPropertyInterfaceCall11)(const void *, QObject *, const QVariant *, int *);
class CuteQDesignerMetaPropertyInterface : public QDesignerMetaPropertyInterface {
public:
  using QDesignerMetaPropertyInterface::QDesignerMetaPropertyInterface;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK30QDesignerMetaPropertyInterface10enumeratorEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerMetaPropertyInterface4kindEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerMetaPropertyInterface11accessFlagsEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerMetaPropertyInterface10attributesEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerMetaPropertyInterface4typeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerMetaPropertyInterface4nameEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerMetaPropertyInterface8typeNameEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerMetaPropertyInterface8userTypeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerMetaPropertyInterface9hasSetterEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerMetaPropertyInterface4readEPK7QObject")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerMetaPropertyInterface5resetEP7QObject")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QDesignerMetaPropertyInterface5writeEP7QObjectRK8QVariant")) {
      taken[11] = call;
      return true;
    }
    return false;
  }

  //  const QDesignerMetaEnumInterface
  //      *QDesignerMetaPropertyInterface::enumerator() const
  const QDesignerMetaEnumInterface *enumerator() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerMetaPropertyInterfaceCall0 call = reinterpret_cast<CuteQDesignerMetaPropertyInterfaceCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QDesignerMetaEnumInterface *>(given);
    }
    return {};
  }

  //  Kind QDesignerMetaPropertyInterface::kind() const
  QDesignerMetaPropertyInterface::Kind kind() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerMetaPropertyInterfaceCall1 call = reinterpret_cast<CuteQDesignerMetaPropertyInterfaceCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QDesignerMetaPropertyInterface::Kind>(given);
    }
    return {};
  }

  //  AccessFlags QDesignerMetaPropertyInterface::accessFlags() const
  QDesignerMetaPropertyInterface::AccessFlags accessFlags() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerMetaPropertyInterfaceCall2 call = reinterpret_cast<CuteQDesignerMetaPropertyInterfaceCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return QFlags<QDesignerMetaPropertyInterface::AccessFlag>::fromInt(given);
    }
    return {};
  }

  //  Attributes QDesignerMetaPropertyInterface::attributes() const
  QDesignerMetaPropertyInterface::Attributes attributes() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerMetaPropertyInterfaceCall3 call = reinterpret_cast<CuteQDesignerMetaPropertyInterfaceCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return QFlags<QDesignerMetaPropertyInterface::Attribute>::fromInt(given);
    }
    return {};
  }

  //  int QDesignerMetaPropertyInterface::type() const
  int type() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerMetaPropertyInterfaceCall4 call = reinterpret_cast<CuteQDesignerMetaPropertyInterfaceCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QDesignerMetaPropertyInterface::name() const
  QString name() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerMetaPropertyInterfaceCall5 call = reinterpret_cast<CuteQDesignerMetaPropertyInterfaceCall5>(taken[5]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QDesignerMetaPropertyInterface::typeName() const
  QString typeName() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerMetaPropertyInterfaceCall6 call = reinterpret_cast<CuteQDesignerMetaPropertyInterfaceCall6>(taken[6]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  int QDesignerMetaPropertyInterface::userType() const
  int userType() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerMetaPropertyInterfaceCall7 call = reinterpret_cast<CuteQDesignerMetaPropertyInterfaceCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QDesignerMetaPropertyInterface::hasSetter() const
  bool hasSetter() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerMetaPropertyInterfaceCall8 call = reinterpret_cast<CuteQDesignerMetaPropertyInterfaceCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QVariant QDesignerMetaPropertyInterface::read(const QObject *object)
  //      const
  QVariant read(const QObject *object) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerMetaPropertyInterfaceCall9 call = reinterpret_cast<CuteQDesignerMetaPropertyInterfaceCall9>(taken[9]);
      const QVariant * given = call(this, object, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QDesignerMetaPropertyInterface::reset(QObject *object) const
  bool reset(QObject *object) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerMetaPropertyInterfaceCall10 call = reinterpret_cast<CuteQDesignerMetaPropertyInterfaceCall10>(taken[10]);
      bool given = call(this, object, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QDesignerMetaPropertyInterface::write(QObject *object, const
  //      QVariant &value) const
  bool write(QObject *object, const QVariant &value) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerMetaPropertyInterfaceCall11 call = reinterpret_cast<CuteQDesignerMetaPropertyInterfaceCall11>(taken[11]);
      bool given = call(this, object, &value, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QDesignerMetaPropertyInterface::QDesignerMetaPropertyInterface()
extern "C" Q_DECL_EXPORT
QDesignerMetaPropertyInterface *ritual_ZN30QDesignerMetaPropertyInterfaceC1Ev() {
  return new CuteQDesignerMetaPropertyInterface();
}

//  QDesignerMetaPropertyInterface::~QDesignerMetaPropertyInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDesignerMetaPropertyInterfaceD1Ev(
    QDesignerMetaPropertyInterface *self) {
  delete self;
}

//  const QDesignerMetaEnumInterface
//      *QDesignerMetaPropertyInterface::enumerator() const
extern "C" Q_DECL_EXPORT
const QDesignerMetaEnumInterface *ritual_ZNK30QDesignerMetaPropertyInterface10enumeratorEv(
    const QDesignerMetaPropertyInterface *self) {
  return self->enumerator();
}

//  Kind QDesignerMetaPropertyInterface::kind() const
extern "C" Q_DECL_EXPORT
QDesignerMetaPropertyInterface::Kind ritual_ZNK30QDesignerMetaPropertyInterface4kindEv(
    const QDesignerMetaPropertyInterface *self) {
  return self->kind();
}

//  AccessFlags QDesignerMetaPropertyInterface::accessFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QDesignerMetaPropertyInterface11accessFlagsEv(
    const QDesignerMetaPropertyInterface *self) {
  return static_cast<int>(self->accessFlags().toInt());
}

//  Attributes QDesignerMetaPropertyInterface::attributes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QDesignerMetaPropertyInterface10attributesEv(
    const QDesignerMetaPropertyInterface *self) {
  return static_cast<int>(self->attributes().toInt());
}

//  int QDesignerMetaPropertyInterface::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QDesignerMetaPropertyInterface4typeEv(
    const QDesignerMetaPropertyInterface *self) {
  return self->type();
}

//  QString QDesignerMetaPropertyInterface::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30QDesignerMetaPropertyInterface4nameEv(
    const QDesignerMetaPropertyInterface *self) {
  return new QString(self->name());
}

//  QString QDesignerMetaPropertyInterface::typeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30QDesignerMetaPropertyInterface8typeNameEv(
    const QDesignerMetaPropertyInterface *self) {
  return new QString(self->typeName());
}

//  int QDesignerMetaPropertyInterface::userType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QDesignerMetaPropertyInterface8userTypeEv(
    const QDesignerMetaPropertyInterface *self) {
  return self->userType();
}

//  bool QDesignerMetaPropertyInterface::hasSetter() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QDesignerMetaPropertyInterface9hasSetterEv(
    const QDesignerMetaPropertyInterface *self) {
  return self->hasSetter();
}

//  QVariant QDesignerMetaPropertyInterface::read(const QObject *object)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK30QDesignerMetaPropertyInterface4readEPK7QObject(
    const QDesignerMetaPropertyInterface *self,
    const QObject *object) {
  return new QVariant(self->read(object));
}

//  bool QDesignerMetaPropertyInterface::reset(QObject *object) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QDesignerMetaPropertyInterface5resetEP7QObject(
    const QDesignerMetaPropertyInterface *self,
    QObject *object) {
  return self->reset(object);
}

//  bool QDesignerMetaPropertyInterface::write(QObject *object, const
//      QVariant &value) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QDesignerMetaPropertyInterface5writeEP7QObjectRK8QVariant(
    const QDesignerMetaPropertyInterface *self,
    QObject *object,
    const QVariant *value) {
  return self->write(object, *value);
}

//  a Python function taken by a CuteQDesignerMetaPropertyInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerMetaPropertyInterface(
    QDesignerMetaPropertyInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerMetaPropertyInterface *>(self)->take(key, call);
}
