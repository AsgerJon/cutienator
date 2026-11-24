//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/abstractintrospection_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/abstractintrospection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDesignerMetaMethodInterface that Python can take functions over in. Every QDesignerMetaMethodInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQDesignerMetaMethodInterfaceCall0)(const void *, int *);
typedef int (*CuteQDesignerMetaMethodInterfaceCall1)(const void *, int *);
typedef QString * (*CuteQDesignerMetaMethodInterfaceCall2)(const void *, int *);
typedef QString * (*CuteQDesignerMetaMethodInterfaceCall3)(const void *, int *);
typedef QString * (*CuteQDesignerMetaMethodInterfaceCall4)(const void *, int *);
typedef QString * (*CuteQDesignerMetaMethodInterfaceCall5)(const void *, int *);
class CuteQDesignerMetaMethodInterface : public QDesignerMetaMethodInterface {
public:
  using QDesignerMetaMethodInterface::QDesignerMetaMethodInterface;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK28QDesignerMetaMethodInterface6accessEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaMethodInterface10methodTypeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaMethodInterface9signatureEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaMethodInterface19normalizedSignatureEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaMethodInterface3tagEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QDesignerMetaMethodInterface8typeNameEv")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  Access QDesignerMetaMethodInterface::access() const
  QDesignerMetaMethodInterface::Access access() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerMetaMethodInterfaceCall0 call = reinterpret_cast<CuteQDesignerMetaMethodInterfaceCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QDesignerMetaMethodInterface::Access>(given);
    }
    return {};
  }

  //  MethodType QDesignerMetaMethodInterface::methodType() const
  QDesignerMetaMethodInterface::MethodType methodType() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerMetaMethodInterfaceCall1 call = reinterpret_cast<CuteQDesignerMetaMethodInterfaceCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QDesignerMetaMethodInterface::MethodType>(given);
    }
    return {};
  }

  //  QString QDesignerMetaMethodInterface::signature() const
  QString signature() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerMetaMethodInterfaceCall2 call = reinterpret_cast<CuteQDesignerMetaMethodInterfaceCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QDesignerMetaMethodInterface::normalizedSignature() const
  QString normalizedSignature() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerMetaMethodInterfaceCall3 call = reinterpret_cast<CuteQDesignerMetaMethodInterfaceCall3>(taken[3]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QDesignerMetaMethodInterface::tag() const
  QString tag() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerMetaMethodInterfaceCall4 call = reinterpret_cast<CuteQDesignerMetaMethodInterfaceCall4>(taken[4]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QDesignerMetaMethodInterface::typeName() const
  QString typeName() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerMetaMethodInterfaceCall5 call = reinterpret_cast<CuteQDesignerMetaMethodInterfaceCall5>(taken[5]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
};

//  QDesignerMetaMethodInterface::~QDesignerMetaMethodInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QDesignerMetaMethodInterfaceD1Ev(
    QDesignerMetaMethodInterface *self) {
  delete self;
}

//  Access QDesignerMetaMethodInterface::access() const
extern "C" Q_DECL_EXPORT
QDesignerMetaMethodInterface::Access ritual_ZNK28QDesignerMetaMethodInterface6accessEv(
    const QDesignerMetaMethodInterface *self) {
  return self->access();
}

//  MethodType QDesignerMetaMethodInterface::methodType() const
extern "C" Q_DECL_EXPORT
QDesignerMetaMethodInterface::MethodType ritual_ZNK28QDesignerMetaMethodInterface10methodTypeEv(
    const QDesignerMetaMethodInterface *self) {
  return self->methodType();
}

//  QStringList QDesignerMetaMethodInterface::parameterNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK28QDesignerMetaMethodInterface14parameterNamesEv(
    const QDesignerMetaMethodInterface *self) {
  return new QList<QString>(self->parameterNames());
}

//  QStringList QDesignerMetaMethodInterface::parameterTypes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK28QDesignerMetaMethodInterface14parameterTypesEv(
    const QDesignerMetaMethodInterface *self) {
  return new QList<QString>(self->parameterTypes());
}

//  QString QDesignerMetaMethodInterface::signature() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QDesignerMetaMethodInterface9signatureEv(
    const QDesignerMetaMethodInterface *self) {
  return new QString(self->signature());
}

//  QString QDesignerMetaMethodInterface::normalizedSignature() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QDesignerMetaMethodInterface19normalizedSignatureEv(
    const QDesignerMetaMethodInterface *self) {
  return new QString(self->normalizedSignature());
}

//  QString QDesignerMetaMethodInterface::tag() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QDesignerMetaMethodInterface3tagEv(
    const QDesignerMetaMethodInterface *self) {
  return new QString(self->tag());
}

//  QString QDesignerMetaMethodInterface::typeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QDesignerMetaMethodInterface8typeNameEv(
    const QDesignerMetaMethodInterface *self) {
  return new QString(self->typeName());
}

//  a Python function taken by a CuteQDesignerMetaMethodInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerMetaMethodInterface(
    QDesignerMetaMethodInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerMetaMethodInterface *>(self)->take(key, call);
}
