//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qauthenticator.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qauthenticator.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QAuthenticator::QAuthenticator()
extern "C" Q_DECL_EXPORT
QAuthenticator *ritual_ZN14QAuthenticatorC1Ev() {
  return new QAuthenticator();
}

//  QAuthenticator::~QAuthenticator()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAuthenticatorD1Ev(QAuthenticator *self) {
  delete self;
}

//  QAuthenticator::QAuthenticator(const QAuthenticator &other)
extern "C" Q_DECL_EXPORT
QAuthenticator *ritual_ZN14QAuthenticatorC1ERKS_(
    const QAuthenticator *other) {
  return new QAuthenticator(*other);
}

//  bool QAuthenticator::operator==(const QAuthenticator &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QAuthenticatoreqERKS_(
    const QAuthenticator *self,
    const QAuthenticator *other) {
  return self->operator==(*other);
}

//  bool QAuthenticator::operator!=(const QAuthenticator &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QAuthenticatorneERKS_(
    const QAuthenticator *self,
    const QAuthenticator *other) {
  return self->operator!=(*other);
}

//  QString QAuthenticator::user() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QAuthenticator4userEv(const QAuthenticator *self) {
  return new QString(self->user());
}

//  void QAuthenticator::setUser(const QString &user)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAuthenticator7setUserERK7QString(
    QAuthenticator *self,
    const QString *user) {
  self->setUser(*user);
}

//  QString QAuthenticator::password() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QAuthenticator8passwordEv(const QAuthenticator *self) {
  return new QString(self->password());
}

//  void QAuthenticator::setPassword(const QString &password)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAuthenticator11setPasswordERK7QString(
    QAuthenticator *self,
    const QString *password) {
  self->setPassword(*password);
}

//  QString QAuthenticator::realm() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QAuthenticator5realmEv(const QAuthenticator *self) {
  return new QString(self->realm());
}

//  void QAuthenticator::setRealm(const QString &realm)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAuthenticator8setRealmERK7QString(
    QAuthenticator *self,
    const QString *realm) {
  self->setRealm(*realm);
}

//  QVariant QAuthenticator::option(const QString &opt) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QAuthenticator6optionERK7QString(
    const QAuthenticator *self,
    const QString *opt) {
  return new QVariant(self->option(*opt));
}

//  QVariantHash QAuthenticator::options() const
extern "C" Q_DECL_EXPORT
QHash<QString, QVariant> *ritual_ZNK14QAuthenticator7optionsEv(
    const QAuthenticator *self) {
  return new QHash<QString, QVariant>(self->options());
}

//  void QAuthenticator::setOption(const QString &opt, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAuthenticator9setOptionERK7QStringRK8QVariant(
    QAuthenticator *self,
    const QString *opt,
    const QVariant *value) {
  self->setOption(*opt, *value);
}

//  bool QAuthenticator::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QAuthenticator6isNullEv(const QAuthenticator *self) {
  return self->isNull();
}

//  void QAuthenticator::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAuthenticator6detachEv(QAuthenticator *self) {
  self->detach();
}

//  void QAuthenticator::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAuthenticator5clearEv(QAuthenticator *self) {
  self->clear();
}
