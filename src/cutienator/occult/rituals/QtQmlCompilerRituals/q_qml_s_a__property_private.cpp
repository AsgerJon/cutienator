//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/qqmlsa.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlSA::Property *QQmlSA::PropertyPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQmlSA::Property *ritual_ZN6QQmlSA15PropertyPrivate6q_funcEv(
    QQmlSA::PropertyPrivate *self) {
  return self->q_func();
}

//  const QQmlSA::Property *QQmlSA::PropertyPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQmlSA::Property *ritual_ZNK6QQmlSA15PropertyPrivate6q_funcEv(
    const QQmlSA::PropertyPrivate *self) {
  return self->q_func();
}

//  QQmlSA::PropertyPrivate::PropertyPrivate(Property *a0)
extern "C" Q_DECL_EXPORT
QQmlSA::PropertyPrivate *ritual_ZN6QQmlSA15PropertyPrivateC1EPNS_8PropertyE(
    QQmlSA::Property *a0) {
  return new QQmlSA::PropertyPrivate(a0);
}

//  QQmlSA::PropertyPrivate::PropertyPrivate(Property *a0, const
//      PropertyPrivate &a1)
extern "C" Q_DECL_EXPORT
QQmlSA::PropertyPrivate *ritual_ZN6QQmlSA15PropertyPrivateC1EPNS_8PropertyERKS0_(
    QQmlSA::Property *a0,
    const QQmlSA::PropertyPrivate *a1) {
  return new QQmlSA::PropertyPrivate(a0, *a1);
}

//  QQmlSA::PropertyPrivate::PropertyPrivate(Property *a0, PropertyPrivate
//      &&a1)
extern "C" Q_DECL_EXPORT
QQmlSA::PropertyPrivate *ritual_ZN6QQmlSA15PropertyPrivateC1EPNS_8PropertyEOS0_(
    QQmlSA::Property *a0,
    QQmlSA::PropertyPrivate *a1) {
  return new QQmlSA::PropertyPrivate(a0, std::move(*a1));
}

//  QQmlSA::PropertyPrivate::~PropertyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA15PropertyPrivateD1Ev(QQmlSA::PropertyPrivate *self) {
  delete self;
}

//  QString QQmlSA::PropertyPrivate::typeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA15PropertyPrivate8typeNameEv(
    const QQmlSA::PropertyPrivate *self) {
  return new QString(self->typeName());
}

//  bool QQmlSA::PropertyPrivate::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA15PropertyPrivate7isValidEv(
    const QQmlSA::PropertyPrivate *self) {
  return self->isValid();
}

//  bool QQmlSA::PropertyPrivate::isReadonly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA15PropertyPrivate10isReadonlyEv(
    const QQmlSA::PropertyPrivate *self) {
  return self->isReadonly();
}

//  QQmlSA::Element QQmlSA::PropertyPrivate::type() const
extern "C" Q_DECL_EXPORT
QQmlSA::Element *ritual_ZNK6QQmlSA15PropertyPrivate4typeEv(
    const QQmlSA::PropertyPrivate *self) {
  return new QQmlSA::Element(self->type());
}

//  QQmlJSMetaProperty QQmlSA::PropertyPrivate::property(const
//      QQmlSA::Property &property)
extern "C" Q_DECL_EXPORT
QQmlJSMetaProperty *ritual_ZN6QQmlSA15PropertyPrivate8propertyERKNS_8PropertyE(
    const QQmlSA::Property *property) {
  return new QQmlJSMetaProperty(
      QQmlSA::PropertyPrivate::property(
          *property));
}

//  QQmlSA::Property QQmlSA::PropertyPrivate::createProperty(const
//      QQmlJSMetaProperty &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Property *ritual_ZN6QQmlSA15PropertyPrivate14createPropertyERK18QQmlJSMetaProperty(
    const QQmlJSMetaProperty *a0) {
  return new QQmlSA::Property(QQmlSA::PropertyPrivate::createProperty(*a0));
}
