//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuagenericstructhandler.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuagenericstructhandler.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuagenericstructvalue.h>
#include <QtOpcUa/qopcuastructuredefinition.h>
#include <QtOpcUa/qopcuaenumdefinition.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QOpcUaGenericStructHandler that Python can take functions over in. Every QOpcUaGenericStructHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaGenericStructHandlerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaGenericStructHandlerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaGenericStructHandlerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaGenericStructHandlerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaGenericStructHandlerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaGenericStructHandlerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaGenericStructHandlerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpcUaGenericStructHandler : public QOpcUaGenericStructHandler {
public:
  using QOpcUaGenericStructHandler::QOpcUaGenericStructHandler;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpcUaGenericStructHandlerCall0 call = reinterpret_cast<CuteQOpcUaGenericStructHandlerCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpcUaGenericStructHandlerCall1 call = reinterpret_cast<CuteQOpcUaGenericStructHandlerCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQOpcUaGenericStructHandlerCall2 call = reinterpret_cast<CuteQOpcUaGenericStructHandlerCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQOpcUaGenericStructHandlerCall3 call = reinterpret_cast<CuteQOpcUaGenericStructHandlerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQOpcUaGenericStructHandlerCall4 call = reinterpret_cast<CuteQOpcUaGenericStructHandlerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQOpcUaGenericStructHandlerCall5 call = reinterpret_cast<CuteQOpcUaGenericStructHandlerCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQOpcUaGenericStructHandlerCall6 call = reinterpret_cast<CuteQOpcUaGenericStructHandlerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpcUaGenericStructHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QOpcUaGenericStructHandler10metaObjectEv(
    const QOpcUaGenericStructHandler *self) {
  return self->metaObject();
}

//  QString QOpcUaGenericStructHandler::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QOpcUaGenericStructHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpcUaGenericStructHandler::tr(s, c, n));
}

//  QOpcUaGenericStructHandlerPrivate *QOpcUaGenericStructHandler::d_func()
extern "C" Q_DECL_EXPORT
QOpcUaGenericStructHandlerPrivate *ritual_ZN26QOpcUaGenericStructHandler6d_funcEv(
    QOpcUaGenericStructHandler *self) {
  return self->d_func();
}

//  const QOpcUaGenericStructHandlerPrivate
//      *QOpcUaGenericStructHandler::d_func() const
extern "C" Q_DECL_EXPORT
const QOpcUaGenericStructHandlerPrivate *ritual_ZNK26QOpcUaGenericStructHandler6d_funcEv(
    const QOpcUaGenericStructHandler *self) {
  return self->d_func();
}

//  QOpcUaGenericStructHandler::QOpcUaGenericStructHandler(QOpcUaClient
//      *client, QObject *parent)
extern "C" Q_DECL_EXPORT
QOpcUaGenericStructHandler *ritual_ZN26QOpcUaGenericStructHandlerC1EP12QOpcUaClientP7QObject(
    QOpcUaClient *client,
    QObject *parent) {
  return new CuteQOpcUaGenericStructHandler(client, parent);
}

//  QOpcUaGenericStructHandler::~QOpcUaGenericStructHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaGenericStructHandlerD1Ev(
    QOpcUaGenericStructHandler *self) {
  delete self;
}

//  bool QOpcUaGenericStructHandler::initialize()
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QOpcUaGenericStructHandler10initializeEv(
    QOpcUaGenericStructHandler *self) {
  return self->initialize();
}

//  QOpcUaGenericStructValue
//      QOpcUaGenericStructHandler::createGenericStructValueForTypeId(const
//      QString &typeId)
extern "C" Q_DECL_EXPORT
QOpcUaGenericStructValue *ritual_ZN26QOpcUaGenericStructHandler33createGenericStructValueForTypeIdERK7QString(
    QOpcUaGenericStructHandler *self,
    const QString *typeId) {
  return new QOpcUaGenericStructValue(
      self->createGenericStructValueForTypeId(
          *typeId));
}

//  QOpcUaStructureDefinition
//      QOpcUaGenericStructHandler::structureDefinitionForBinaryEncodingId(co
//      nst QString &id) const
extern "C" Q_DECL_EXPORT
QOpcUaStructureDefinition *ritual_ZNK26QOpcUaGenericStructHandler38structureDefinitionForBinaryEncodingIdERK7QString(
    const QOpcUaGenericStructHandler *self,
    const QString *id) {
  return new QOpcUaStructureDefinition(
      self->structureDefinitionForBinaryEncodingId(
          *id));
}

//  QOpcUaStructureDefinition
//      QOpcUaGenericStructHandler::structureDefinitionForTypeId(const
//      QString &id) const
extern "C" Q_DECL_EXPORT
QOpcUaStructureDefinition *ritual_ZNK26QOpcUaGenericStructHandler28structureDefinitionForTypeIdERK7QString(
    const QOpcUaGenericStructHandler *self,
    const QString *id) {
  return new QOpcUaStructureDefinition(
      self->structureDefinitionForTypeId(
          *id));
}

//  QOpcUaEnumDefinition
//      QOpcUaGenericStructHandler::enumDefinitionForTypeId(const QString
//      &id) const
extern "C" Q_DECL_EXPORT
QOpcUaEnumDefinition *ritual_ZNK26QOpcUaGenericStructHandler23enumDefinitionForTypeIdERK7QString(
    const QOpcUaGenericStructHandler *self,
    const QString *id) {
  return new QOpcUaEnumDefinition(self->enumDefinitionForTypeId(*id));
}

//  QString QOpcUaGenericStructHandler::typeNameForBinaryEncodingId(const
//      QString &id) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QOpcUaGenericStructHandler27typeNameForBinaryEncodingIdERK7QString(
    const QOpcUaGenericStructHandler *self,
    const QString *id) {
  return new QString(self->typeNameForBinaryEncodingId(*id));
}

//  QString QOpcUaGenericStructHandler::typeNameForTypeId(const QString &id)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QOpcUaGenericStructHandler17typeNameForTypeIdERK7QString(
    const QOpcUaGenericStructHandler *self,
    const QString *id) {
  return new QString(self->typeNameForTypeId(*id));
}

//  bool QOpcUaGenericStructHandler::isAbstractTypeId(const QString &id)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QOpcUaGenericStructHandler16isAbstractTypeIdERK7QString(
    const QOpcUaGenericStructHandler *self,
    const QString *id) {
  return self->isAbstractTypeId(*id);
}

//  bool QOpcUaGenericStructHandler::addCustomStructureDefinition(const
//      QOpcUaStructureDefinition &definition, const QString &typeId, const
//      QString &name, QOpcUa::IsAbstract isAbstract)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QOpcUaGenericStructHandler28addCustomStructureDefinitionERK25QOpcUaStructureDefinitionRK7QStringS5_N6QOpcUa10IsAbstractE(
    QOpcUaGenericStructHandler *self,
    const QOpcUaStructureDefinition *definition,
    const QString *typeId,
    const QString *name,
    QOpcUa::IsAbstract isAbstract) {
  return self->addCustomStructureDefinition(
      *definition,
      *typeId,
      *name,
      isAbstract);
}

//  bool QOpcUaGenericStructHandler::addCustomEnumDefinition(const
//      QOpcUaEnumDefinition &definition, const QString &typeId, const
//      QString &name, QOpcUa::IsAbstract isAbstract)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QOpcUaGenericStructHandler23addCustomEnumDefinitionERK20QOpcUaEnumDefinitionRK7QStringS5_N6QOpcUa10IsAbstractE(
    QOpcUaGenericStructHandler *self,
    const QOpcUaEnumDefinition *definition,
    const QString *typeId,
    const QString *name,
    QOpcUa::IsAbstract isAbstract) {
  return self->addCustomEnumDefinition(
      *definition,
      *typeId,
      *name,
      isAbstract);
}

//  bool QOpcUaGenericStructHandler::initialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QOpcUaGenericStructHandler11initializedEv(
    const QOpcUaGenericStructHandler *self) {
  return self->initialized();
}

//  DataTypeKind QOpcUaGenericStructHandler::dataTypeKindForTypeId(const
//      QString &id) const
extern "C" Q_DECL_EXPORT
QOpcUaGenericStructHandler::DataTypeKind ritual_ZNK26QOpcUaGenericStructHandler21dataTypeKindForTypeIdERK7QString(
    const QOpcUaGenericStructHandler *self,
    const QString *id) {
  return self->dataTypeKindForTypeId(*id);
}

//  QString QOpcUaGenericStructHandler::typeIdForBinaryEncodingId(const
//      QString &id) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QOpcUaGenericStructHandler25typeIdForBinaryEncodingIdERK7QString(
    const QOpcUaGenericStructHandler *self,
    const QString *id) {
  return new QString(self->typeIdForBinaryEncodingId(*id));
}

//  a Python function taken by a CuteQOpcUaGenericStructHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpcUaGenericStructHandler(
    QOpcUaGenericStructHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpcUaGenericStructHandler *>(self)->take(key, call);
}
