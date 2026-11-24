//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbuserror.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbuserror.h>
#include <QtDBus/qdbusmessage.h>
#include <QtCore/qstring.h>

//  QDBusError::QDBusError()
extern "C" Q_DECL_EXPORT
QDBusError *ritual_ZN10QDBusErrorC1Ev() {
  return new QDBusError();
}

#if !defined(QT_BOOTSTRAPPED)
//  QDBusError::QDBusError(const QDBusMessage &msg)
extern "C" Q_DECL_EXPORT
QDBusError *ritual_ZN10QDBusErrorC1ERK12QDBusMessage(
    const QDBusMessage *msg) {
  return new QDBusError(*msg);
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  QDBusError::QDBusError(ErrorType error, const QString &message)
extern "C" Q_DECL_EXPORT
QDBusError *ritual_ZN10QDBusErrorC1ENS_9ErrorTypeERK7QString(
    QDBusError::ErrorType error,
    const QString *message) {
  return new QDBusError(error, *message);
}

//  QDBusError::QDBusError(const QDBusError &other)
extern "C" Q_DECL_EXPORT
QDBusError *ritual_ZN10QDBusErrorC1ERKS_(const QDBusError *other) {
  return new QDBusError(*other);
}

//  ErrorType QDBusError::type() const
extern "C" Q_DECL_EXPORT
QDBusError::ErrorType ritual_ZNK10QDBusError4typeEv(const QDBusError *self) {
  return self->type();
}

//  QString QDBusError::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QDBusError4nameEv(const QDBusError *self) {
  return new QString(self->name());
}

//  QString QDBusError::message() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QDBusError7messageEv(const QDBusError *self) {
  return new QString(self->message());
}

//  bool QDBusError::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QDBusError7isValidEv(const QDBusError *self) {
  return self->isValid();
}

//  QString QDBusError::errorString(ErrorType error)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QDBusError11errorStringENS_9ErrorTypeE(
    QDBusError::ErrorType error) {
  return new QString(QDBusError::errorString(error));
}

//  QDBusError::~QDBusError()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDBusErrorD1Ev(QDBusError *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
