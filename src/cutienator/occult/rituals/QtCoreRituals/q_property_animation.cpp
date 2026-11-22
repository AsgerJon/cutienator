//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpropertyanimation.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qpropertyanimation.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>

//  const QMetaObject *QPropertyAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QPropertyAnimation10metaObjectEv(
    const QPropertyAnimation *self) {
  return self->metaObject();
}

//  QString QPropertyAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QPropertyAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPropertyAnimation::tr(s, c, n));
}

//  QPropertyAnimation::QPropertyAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QPropertyAnimation *ritual_ZN18QPropertyAnimationC1EP7QObject(
    QObject *parent) {
  return new QPropertyAnimation(parent);
}

//  QPropertyAnimation::QPropertyAnimation(QObject *target, const QByteArray
//      &propertyName, QObject *parent)
extern "C" Q_DECL_EXPORT
QPropertyAnimation *ritual_ZN18QPropertyAnimationC1EP7QObjectRK10QByteArrayS1_(
    QObject *target,
    const QByteArray *propertyName,
    QObject *parent) {
  return new QPropertyAnimation(target, *propertyName, parent);
}

//  QPropertyAnimation::~QPropertyAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPropertyAnimationD1Ev(QPropertyAnimation *self) {
  delete self;
}

//  QObject *QPropertyAnimation::targetObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK18QPropertyAnimation12targetObjectEv(
    const QPropertyAnimation *self) {
  return self->targetObject();
}

//  void QPropertyAnimation::setTargetObject(QObject *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPropertyAnimation15setTargetObjectEP7QObject(
    QPropertyAnimation *self,
    QObject *target) {
  self->setTargetObject(target);
}

//  QByteArray QPropertyAnimation::propertyName() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QPropertyAnimation12propertyNameEv(
    const QPropertyAnimation *self) {
  return new QByteArray(self->propertyName());
}

//  void QPropertyAnimation::setPropertyName(const QByteArray &propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPropertyAnimation15setPropertyNameERK10QByteArray(
    QPropertyAnimation *self,
    const QByteArray *propertyName) {
  self->setPropertyName(*propertyName);
}
