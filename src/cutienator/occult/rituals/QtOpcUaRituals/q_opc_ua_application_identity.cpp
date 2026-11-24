//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaapplicationidentity.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuaapplicationidentity.h>
#include <QtCore/qstring.h>

//  QOpcUaApplicationIdentity::QOpcUaApplicationIdentity()
extern "C" Q_DECL_EXPORT
QOpcUaApplicationIdentity *ritual_ZN25QOpcUaApplicationIdentityC1Ev() {
  return new QOpcUaApplicationIdentity();
}

//  QOpcUaApplicationIdentity::~QOpcUaApplicationIdentity()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaApplicationIdentityD1Ev(
    QOpcUaApplicationIdentity *self) {
  delete self;
}

//  QOpcUaApplicationIdentity::QOpcUaApplicationIdentity(const
//      QOpcUaApplicationIdentity &other)
extern "C" Q_DECL_EXPORT
QOpcUaApplicationIdentity *ritual_ZN25QOpcUaApplicationIdentityC1ERKS_(
    const QOpcUaApplicationIdentity *other) {
  return new QOpcUaApplicationIdentity(*other);
}

//  QString QOpcUaApplicationIdentity::applicationUri() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QOpcUaApplicationIdentity14applicationUriEv(
    const QOpcUaApplicationIdentity *self) {
  return new QString(self->applicationUri());
}

//  void QOpcUaApplicationIdentity::setApplicationUri(const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaApplicationIdentity17setApplicationUriERK7QString(
    QOpcUaApplicationIdentity *self,
    const QString *value) {
  self->setApplicationUri(*value);
}

//  QString QOpcUaApplicationIdentity::applicationName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QOpcUaApplicationIdentity15applicationNameEv(
    const QOpcUaApplicationIdentity *self) {
  return new QString(self->applicationName());
}

//  void QOpcUaApplicationIdentity::setApplicationName(const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaApplicationIdentity18setApplicationNameERK7QString(
    QOpcUaApplicationIdentity *self,
    const QString *value) {
  self->setApplicationName(*value);
}

//  QString QOpcUaApplicationIdentity::productUri() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QOpcUaApplicationIdentity10productUriEv(
    const QOpcUaApplicationIdentity *self) {
  return new QString(self->productUri());
}

//  void QOpcUaApplicationIdentity::setProductUri(const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaApplicationIdentity13setProductUriERK7QString(
    QOpcUaApplicationIdentity *self,
    const QString *value) {
  self->setProductUri(*value);
}

//  QOpcUaApplicationDescription::ApplicationType
//      QOpcUaApplicationIdentity::applicationType() const
extern "C" Q_DECL_EXPORT
QOpcUaApplicationDescription::ApplicationType ritual_ZNK25QOpcUaApplicationIdentity15applicationTypeEv(
    const QOpcUaApplicationIdentity *self) {
  return self->applicationType();
}

//  void QOpcUaApplicationIdentity::setApplicationType(QOpcUaApplicationDescr
//      iption::ApplicationType value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaApplicationIdentity18setApplicationTypeEN28QOpcUaApplicationDescription15ApplicationTypeE(
    QOpcUaApplicationIdentity *self,
    QOpcUaApplicationDescription::ApplicationType value) {
  self->setApplicationType(value);
}

//  bool QOpcUaApplicationIdentity::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QOpcUaApplicationIdentity7isValidEv(
    const QOpcUaApplicationIdentity *self) {
  return self->isValid();
}
