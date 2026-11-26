//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbusmessage.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS) && !defined(QT_BOOTSTRAPPED)
#include <QtDBus/qdbusmessage.h>
#include <QtCore/qstring.h>
#include <QtDBus/qdbuserror.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  QDBusMessage::QDBusMessage()
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZN12QDBusMessageC1Ev() {
  return new QDBusMessage();
}

//  QDBusMessage::QDBusMessage(const QDBusMessage &other)
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZN12QDBusMessageC1ERKS_(const QDBusMessage *other) {
  return new QDBusMessage(*other);
}

//  QDBusMessage::QDBusMessage(QDBusMessage &&other)
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZN12QDBusMessageC1EOS_(QDBusMessage *other) {
  return new QDBusMessage(std::move(*other));
}

//  QDBusMessage &QDBusMessage::operator=(QDBusMessage &&other)
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZN12QDBusMessageaSEOS_(
    QDBusMessage *self,
    QDBusMessage *other) {
  return &(self->operator=(std::move(*other)));
}

//  QDBusMessage &QDBusMessage::operator=(const QDBusMessage &other)
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZN12QDBusMessageaSERKS_(
    QDBusMessage *self,
    const QDBusMessage *other) {
  return &(self->operator=(*other));
}

//  QDBusMessage::~QDBusMessage()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDBusMessageD1Ev(QDBusMessage *self) {
  delete self;
}

//  void QDBusMessage::swap(QDBusMessage &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDBusMessage4swapERS_(
    QDBusMessage *self,
    QDBusMessage *other) {
  self->swap(*other);
}

//  QDBusMessage QDBusMessage::createSignal(const QString &path, const
//      QString &interface, const QString &name)
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZN12QDBusMessage12createSignalERK7QStringS2_S2_(
    const QString *path,
    const QString *interface,
    const QString *name) {
  return new QDBusMessage(
      QDBusMessage::createSignal(
          *path,
          *interface,
          *name));
}

//  QDBusMessage QDBusMessage::createTargetedSignal(const QString &service,
//      const QString &path, const QString &interface, const QString &name)
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZN12QDBusMessage20createTargetedSignalERK7QStringS2_S2_S2_(
    const QString *service,
    const QString *path,
    const QString *interface,
    const QString *name) {
  return new QDBusMessage(
      QDBusMessage::createTargetedSignal(
          *service,
          *path,
          *interface,
          *name));
}

//  QDBusMessage QDBusMessage::createMethodCall(const QString &destination,
//      const QString &path, const QString &interface, const QString &method)
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZN12QDBusMessage16createMethodCallERK7QStringS2_S2_S2_(
    const QString *destination,
    const QString *path,
    const QString *interface,
    const QString *method) {
  return new QDBusMessage(
      QDBusMessage::createMethodCall(
          *destination,
          *path,
          *interface,
          *method));
}

//  QDBusMessage QDBusMessage::createError(const QString &name, const QString
//      &msg)
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZN12QDBusMessage11createErrorERK7QStringS2_(
    const QString *name,
    const QString *msg) {
  return new QDBusMessage(QDBusMessage::createError(*name, *msg));
}

//  QDBusMessage QDBusMessage::createError(const QDBusError &err)
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZN12QDBusMessage11createErrorERK10QDBusError(
    const QDBusError *err) {
  return new QDBusMessage(QDBusMessage::createError(*err));
}

//  QDBusMessage QDBusMessage::createError(QDBusError::ErrorType type, const
//      QString &msg)
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZN12QDBusMessage11createErrorEN10QDBusError9ErrorTypeERK7QString(
    QDBusError::ErrorType type,
    const QString *msg) {
  return new QDBusMessage(QDBusMessage::createError(type, *msg));
}

//  QDBusMessage QDBusMessage::createReply(const QList<QVariant> &arguments)
//      const
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZNK12QDBusMessage11createReplyERK5QListI8QVariantE(
    const QDBusMessage *self,
    const QList<QVariant> *arguments) {
  return new QDBusMessage(self->createReply(*arguments));
}

//  QDBusMessage QDBusMessage::createReply(const QVariant &argument) const
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZNK12QDBusMessage11createReplyERK8QVariant(
    const QDBusMessage *self,
    const QVariant *argument) {
  return new QDBusMessage(self->createReply(*argument));
}

//  QDBusMessage QDBusMessage::createErrorReply(const QString &name, const
//      QString &msg) const
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZNK12QDBusMessage16createErrorReplyERK7QStringS2_(
    const QDBusMessage *self,
    const QString *name,
    const QString *msg) {
  return new QDBusMessage(self->createErrorReply(*name, *msg));
}

//  QDBusMessage QDBusMessage::createErrorReply(const QDBusError &err) const
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZNK12QDBusMessage16createErrorReplyERK10QDBusError(
    const QDBusMessage *self,
    const QDBusError *err) {
  return new QDBusMessage(self->createErrorReply(*err));
}

//  QDBusMessage QDBusMessage::createErrorReply(QDBusError::ErrorType type,
//      const QString &msg) const
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZNK12QDBusMessage16createErrorReplyEN10QDBusError9ErrorTypeERK7QString(
    const QDBusMessage *self,
    QDBusError::ErrorType type,
    const QString *msg) {
  return new QDBusMessage(self->createErrorReply(type, *msg));
}

//  QString QDBusMessage::service() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QDBusMessage7serviceEv(const QDBusMessage *self) {
  return new QString(self->service());
}

//  QString QDBusMessage::path() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QDBusMessage4pathEv(const QDBusMessage *self) {
  return new QString(self->path());
}

//  QString QDBusMessage::interface() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QDBusMessage9interfaceEv(const QDBusMessage *self) {
  return new QString(self->interface());
}

//  QString QDBusMessage::member() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QDBusMessage6memberEv(const QDBusMessage *self) {
  return new QString(self->member());
}

//  QString QDBusMessage::errorName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QDBusMessage9errorNameEv(const QDBusMessage *self) {
  return new QString(self->errorName());
}

//  QString QDBusMessage::errorMessage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QDBusMessage12errorMessageEv(const QDBusMessage *self) {
  return new QString(self->errorMessage());
}

//  MessageType QDBusMessage::type() const
extern "C" Q_DECL_EXPORT
QDBusMessage::MessageType ritual_ZNK12QDBusMessage4typeEv(
    const QDBusMessage *self) {
  return self->type();
}

//  QString QDBusMessage::signature() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QDBusMessage9signatureEv(const QDBusMessage *self) {
  return new QString(self->signature());
}

//  bool QDBusMessage::isReplyRequired() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QDBusMessage15isReplyRequiredEv(const QDBusMessage *self) {
  return self->isReplyRequired();
}

//  void QDBusMessage::setDelayedReply(bool enable) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QDBusMessage15setDelayedReplyEb(
    const QDBusMessage *self,
    bool enable) {
  self->setDelayedReply(enable);
}

//  bool QDBusMessage::isDelayedReply() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QDBusMessage14isDelayedReplyEv(const QDBusMessage *self) {
  return self->isDelayedReply();
}

//  void QDBusMessage::setAutoStartService(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDBusMessage19setAutoStartServiceEb(
    QDBusMessage *self,
    bool enable) {
  self->setAutoStartService(enable);
}

//  bool QDBusMessage::autoStartService() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QDBusMessage16autoStartServiceEv(const QDBusMessage *self) {
  return self->autoStartService();
}

//  void QDBusMessage::setInteractiveAuthorizationAllowed(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDBusMessage34setInteractiveAuthorizationAllowedEb(
    QDBusMessage *self,
    bool enable) {
  self->setInteractiveAuthorizationAllowed(enable);
}

//  bool QDBusMessage::isInteractiveAuthorizationAllowed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QDBusMessage33isInteractiveAuthorizationAllowedEv(
    const QDBusMessage *self) {
  return self->isInteractiveAuthorizationAllowed();
}

//  void QDBusMessage::setArguments(const QList<QVariant> &arguments)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDBusMessage12setArgumentsERK5QListI8QVariantE(
    QDBusMessage *self,
    const QList<QVariant> *arguments) {
  self->setArguments(*arguments);
}

//  QList<QVariant> QDBusMessage::arguments() const
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZNK12QDBusMessage9argumentsEv(
    const QDBusMessage *self) {
  return new QList<QVariant>(self->arguments());
}

//  QDBusMessage &QDBusMessage::operator<<(const QVariant &arg)
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZN12QDBusMessagelsERK8QVariant(
    QDBusMessage *self,
    const QVariant *arg) {
  return &(self->operator<<(*arg));
}

//  QDBusMessage::QDBusMessage(QDBusMessagePrivate &dd)
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZN12QDBusMessageC1ER19QDBusMessagePrivate(
    QDBusMessagePrivate *dd) {
  return new QDBusMessage(*dd);
}

#endif  // !defined(QT_NO_DBUS) && !defined(QT_BOOTSTRAPPED)
