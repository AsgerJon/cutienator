//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbusmetatype.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbusmetatype.h>
#include <QtCore/qmetatype.h>
#include <QtDBus/qdbusargument.h>
#include <QtCore/qbytearray.h>

//  void QDBusMetaType::registerMarshallOperators(QMetaType typeId,
//      MarshallFunction a1, DemarshallFunction a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusMetaType25registerMarshallOperatorsE9QMetaTypePFvR13QDBusArgumentPKvEPFvRKS1_PvE(
    const QMetaType *typeId,
    void *a1,
    void *a2) {
  QDBusMetaType::registerMarshallOperators(
      *typeId,
      reinterpret_cast<QDBusMetaType::MarshallFunction>(a1),
      reinterpret_cast<QDBusMetaType::DemarshallFunction>(a2));
}

//  bool QDBusMetaType::marshall(QDBusArgument &a0, QMetaType id, const void
//      *data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QDBusMetaType8marshallER13QDBusArgument9QMetaTypePKv(
    QDBusArgument *a0,
    const QMetaType *id,
    const void *data) {
  return QDBusMetaType::marshall(*a0, *id, data);
}

//  bool QDBusMetaType::demarshall(const QDBusArgument &a0, QMetaType id,
//      void *data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QDBusMetaType10demarshallERK13QDBusArgument9QMetaTypePv(
    const QDBusArgument *a0,
    const QMetaType *id,
    void *data) {
  return QDBusMetaType::demarshall(*a0, *id, data);
}

//  void QDBusMetaType::registerCustomType(QMetaType type, const QByteArray
//      &signature)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusMetaType18registerCustomTypeE9QMetaTypeRK10QByteArray(
    const QMetaType *type,
    const QByteArray *signature) {
  QDBusMetaType::registerCustomType(*type, *signature);
}

//  QMetaType QDBusMetaType::signatureToMetaType(const char *signature)
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZN13QDBusMetaType19signatureToMetaTypeEPKc(
    const char *signature) {
  return new QMetaType(QDBusMetaType::signatureToMetaType(signature));
}

//  const char *QDBusMetaType::typeToSignature(QMetaType type)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN13QDBusMetaType15typeToSignatureE9QMetaType(
    const QMetaType *type) {
  return QDBusMetaType::typeToSignature(*type);
}

//  QDBusMetaType::~QDBusMetaType()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusMetaTypeD1Ev(QDBusMetaType *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
