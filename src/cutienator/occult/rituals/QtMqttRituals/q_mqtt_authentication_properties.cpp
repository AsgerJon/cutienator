//  Written by dev_tooling.RitualGenerator from the records of
//  QtMqtt/qmqttauthenticationproperties.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtMqtt/qmqttauthenticationproperties.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtMqtt/qmqtttype.h>

//  QMqttAuthenticationProperties::QMqttAuthenticationProperties()
extern "C" Q_DECL_EXPORT
QMqttAuthenticationProperties *ritual_ZN29QMqttAuthenticationPropertiesC1Ev() {
  return new QMqttAuthenticationProperties();
}

//  QMqttAuthenticationProperties::QMqttAuthenticationProperties(const
//      QMqttAuthenticationProperties &a0)
extern "C" Q_DECL_EXPORT
QMqttAuthenticationProperties *ritual_ZN29QMqttAuthenticationPropertiesC1ERKS_(
    const QMqttAuthenticationProperties *a0) {
  return new QMqttAuthenticationProperties(*a0);
}

//  QMqttAuthenticationProperties::~QMqttAuthenticationProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QMqttAuthenticationPropertiesD1Ev(
    QMqttAuthenticationProperties *self) {
  delete self;
}

//  QString QMqttAuthenticationProperties::authenticationMethod() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QMqttAuthenticationProperties20authenticationMethodEv(
    const QMqttAuthenticationProperties *self) {
  return new QString(self->authenticationMethod());
}

//  void QMqttAuthenticationProperties::setAuthenticationMethod(const QString
//      &method)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QMqttAuthenticationProperties23setAuthenticationMethodERK7QString(
    QMqttAuthenticationProperties *self,
    const QString *method) {
  self->setAuthenticationMethod(*method);
}

//  QByteArray QMqttAuthenticationProperties::authenticationData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK29QMqttAuthenticationProperties18authenticationDataEv(
    const QMqttAuthenticationProperties *self) {
  return new QByteArray(self->authenticationData());
}

//  void QMqttAuthenticationProperties::setAuthenticationData(const
//      QByteArray &adata)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QMqttAuthenticationProperties21setAuthenticationDataERK10QByteArray(
    QMqttAuthenticationProperties *self,
    const QByteArray *adata) {
  self->setAuthenticationData(*adata);
}

//  QString QMqttAuthenticationProperties::reason() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QMqttAuthenticationProperties6reasonEv(
    const QMqttAuthenticationProperties *self) {
  return new QString(self->reason());
}

//  void QMqttAuthenticationProperties::setReason(const QString &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QMqttAuthenticationProperties9setReasonERK7QString(
    QMqttAuthenticationProperties *self,
    const QString *r) {
  self->setReason(*r);
}

//  QMqttUserProperties QMqttAuthenticationProperties::userProperties() const
extern "C" Q_DECL_EXPORT
QMqttUserProperties *ritual_ZNK29QMqttAuthenticationProperties14userPropertiesEv(
    const QMqttAuthenticationProperties *self) {
  return new QMqttUserProperties(self->userProperties());
}

//  void QMqttAuthenticationProperties::setUserProperties(const
//      QMqttUserProperties &user)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QMqttAuthenticationProperties17setUserPropertiesERK19QMqttUserProperties(
    QMqttAuthenticationProperties *self,
    const QMqttUserProperties *user) {
  self->setUserProperties(*user);
}
