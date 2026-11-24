//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbusmetatype.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbusmetatype.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qbytearray.h>

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
