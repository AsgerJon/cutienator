//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbusextratypes.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbusextratypes.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qstring.h>

//  QDBusSignature::QDBusSignature()
extern "C" Q_DECL_EXPORT
QDBusSignature *ritual_ZN14QDBusSignatureC1Ev() {
  return new QDBusSignature();
}

//  QDBusSignature::QDBusSignature(const char *signature)
extern "C" Q_DECL_EXPORT
QDBusSignature *ritual_ZN14QDBusSignatureC1EPKc(const char *signature) {
  return new QDBusSignature(signature);
}

//  QDBusSignature::QDBusSignature(QLatin1StringView signature)
extern "C" Q_DECL_EXPORT
QDBusSignature *ritual_ZN14QDBusSignatureC1E13QLatin1String(
    const QLatin1String *signature) {
  return new QDBusSignature(*signature);
}

//  QDBusSignature::QDBusSignature(const QString &signature)
extern "C" Q_DECL_EXPORT
QDBusSignature *ritual_ZN14QDBusSignatureC1ERK7QString(
    const QString *signature) {
  return new QDBusSignature(*signature);
}

//  void QDBusSignature::setSignature(const QString &signature)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDBusSignature12setSignatureERK7QString(
    QDBusSignature *self,
    const QString *signature) {
  self->setSignature(*signature);
}

//  QString QDBusSignature::signature() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QDBusSignature9signatureEv(const QDBusSignature *self) {
  return new QString(self->signature());
}

//  void QDBusSignature::doCheck()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDBusSignature7doCheckEv(QDBusSignature *self) {
  self->doCheck();
}

//  QDBusSignature::~QDBusSignature()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDBusSignatureD1Ev(QDBusSignature *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
