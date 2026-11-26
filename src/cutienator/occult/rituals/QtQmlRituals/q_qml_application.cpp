//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlglobal_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlglobal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QQmlApplication::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQmlApplication10metaObjectEv(
    const QQmlApplication *self) {
  return self->metaObject();
}

//  void *QQmlApplication::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQmlApplication11qt_metacastEPKc(
    QQmlApplication *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlApplication::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQmlApplication11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlApplication *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlApplication::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQmlApplication2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlApplication::tr(s, c, n));
}

//  void QQmlApplication::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlApplication22qt_qmlMarker_anonymousEv(
    QQmlApplication *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQmlApplication::QQmlApplication(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlApplication *ritual_ZN15QQmlApplicationC1EP7QObject(QObject *parent) {
  return new QQmlApplication(parent);
}

//  QStringList QQmlApplication::args()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN15QQmlApplication4argsEv(QQmlApplication *self) {
  return new QList<QString>(self->args());
}

//  QString QQmlApplication::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQmlApplication4nameEv(const QQmlApplication *self) {
  return new QString(self->name());
}

//  QString QQmlApplication::version() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQmlApplication7versionEv(const QQmlApplication *self) {
  return new QString(self->version());
}

//  QString QQmlApplication::organization() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQmlApplication12organizationEv(
    const QQmlApplication *self) {
  return new QString(self->organization());
}

//  QString QQmlApplication::domain() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQmlApplication6domainEv(const QQmlApplication *self) {
  return new QString(self->domain());
}

//  void QQmlApplication::setName(const QString &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlApplication7setNameERK7QString(
    QQmlApplication *self,
    const QString *arg) {
  self->setName(*arg);
}

//  void QQmlApplication::setVersion(const QString &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlApplication10setVersionERK7QString(
    QQmlApplication *self,
    const QString *arg) {
  self->setVersion(*arg);
}

//  void QQmlApplication::setOrganization(const QString &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlApplication15setOrganizationERK7QString(
    QQmlApplication *self,
    const QString *arg) {
  self->setOrganization(*arg);
}

//  void QQmlApplication::setDomain(const QString &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlApplication9setDomainERK7QString(
    QQmlApplication *self,
    const QString *arg) {
  self->setDomain(*arg);
}

//  void QQmlApplication::aboutToQuit()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlApplication11aboutToQuitEv(QQmlApplication *self) {
  self->aboutToQuit();
}

//  void QQmlApplication::nameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlApplication11nameChangedEv(QQmlApplication *self) {
  self->nameChanged();
}

//  void QQmlApplication::versionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlApplication14versionChangedEv(QQmlApplication *self) {
  self->versionChanged();
}

//  void QQmlApplication::organizationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlApplication19organizationChangedEv(
    QQmlApplication *self) {
  self->organizationChanged();
}

//  void QQmlApplication::domainChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlApplication13domainChangedEv(QQmlApplication *self) {
  self->domainChanged();
}

//  QQmlApplication::QQmlApplication(QQmlApplicationPrivate &dd, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQmlApplication *ritual_ZN15QQmlApplicationC1ER22QQmlApplicationPrivateP7QObject(
    QQmlApplicationPrivate *dd,
    QObject *parent) {
  return new QQmlApplication(*dd, parent);
}

//  QQmlApplicationPrivate *QQmlApplication::d_func()
extern "C" Q_DECL_EXPORT
QQmlApplicationPrivate *ritual_ZN15QQmlApplication6d_funcEv(
    QQmlApplication *self) {
  return self->d_func();
}

//  const QQmlApplicationPrivate *QQmlApplication::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlApplicationPrivate *ritual_ZNK15QQmlApplication6d_funcEv(
    const QQmlApplication *self) {
  return self->d_func();
}
