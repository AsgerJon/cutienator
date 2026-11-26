//  Written by dev_tooling.RitualGenerator from the records of
//  QtMqtt/qmqtttype.h, Qt 6.12.0. Changes made here are lost.
#include <QtMqtt/qmqtttype.h>
#include <QtCore/qstring.h>

//  QMqttStringPair::QMqttStringPair()
extern "C" Q_DECL_EXPORT
QMqttStringPair *ritual_ZN15QMqttStringPairC1Ev() {
  return new QMqttStringPair();
}

//  QMqttStringPair::QMqttStringPair(const QString &name, const QString
//      &value)
extern "C" Q_DECL_EXPORT
QMqttStringPair *ritual_ZN15QMqttStringPairC1ERK7QStringS2_(
    const QString *name,
    const QString *value) {
  return new QMqttStringPair(*name, *value);
}

//  QMqttStringPair::QMqttStringPair(const QMqttStringPair &a0)
extern "C" Q_DECL_EXPORT
QMqttStringPair *ritual_ZN15QMqttStringPairC1ERKS_(
    const QMqttStringPair *a0) {
  return new QMqttStringPair(*a0);
}

//  QMqttStringPair::~QMqttStringPair()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMqttStringPairD1Ev(QMqttStringPair *self) {
  delete self;
}

//  QString QMqttStringPair::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QMqttStringPair4nameEv(const QMqttStringPair *self) {
  return new QString(self->name());
}

//  void QMqttStringPair::setName(const QString &n)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMqttStringPair7setNameERK7QString(
    QMqttStringPair *self,
    const QString *n) {
  self->setName(*n);
}

//  QString QMqttStringPair::value() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QMqttStringPair5valueEv(const QMqttStringPair *self) {
  return new QString(self->value());
}

//  void QMqttStringPair::setValue(const QString &v)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMqttStringPair8setValueERK7QString(
    QMqttStringPair *self,
    const QString *v) {
  self->setValue(*v);
}

//  bool QMqttStringPair::operator==(const QMqttStringPair &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QMqttStringPaireqERKS_(
    const QMqttStringPair *self,
    const QMqttStringPair *other) {
  return self->operator==(*other);
}

//  bool QMqttStringPair::operator!=(const QMqttStringPair &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QMqttStringPairneERKS_(
    const QMqttStringPair *self,
    const QMqttStringPair *other) {
  return self->operator!=(*other);
}

//  QMqttStringPair &QMqttStringPair::operator=(const QMqttStringPair &a0)
extern "C" Q_DECL_EXPORT
QMqttStringPair *ritual_ZN15QMqttStringPairaSERKS_(
    QMqttStringPair *self,
    const QMqttStringPair *a0) {
  return &(self->operator=(*a0));
}
