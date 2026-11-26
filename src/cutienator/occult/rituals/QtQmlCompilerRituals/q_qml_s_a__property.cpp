//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
#include <QtQmlCompiler/qqmlsa.h>
#include <QtCore/qstring.h>

//  PropertyPrivate *QQmlSA::Property::d_func()
extern "C" Q_DECL_EXPORT
QQmlSA::PropertyPrivate *ritual_ZN6QQmlSA8Property6d_funcEv(
    QQmlSA::Property *self) {
  return self->d_func();
}

//  const PropertyPrivate *QQmlSA::Property::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlSA::PropertyPrivate *ritual_ZNK6QQmlSA8Property6d_funcEv(
    const QQmlSA::Property *self) {
  return self->d_func();
}

//  QQmlSA::Property::Property()
extern "C" Q_DECL_EXPORT
QQmlSA::Property *ritual_ZN6QQmlSA8PropertyC1Ev() {
  return new QQmlSA::Property();
}

//  QQmlSA::Property::Property(const Property &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Property *ritual_ZN6QQmlSA8PropertyC1ERKS0_(
    const QQmlSA::Property *a0) {
  return new QQmlSA::Property(*a0);
}

//  QQmlSA::Property::Property(Property &&a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Property *ritual_ZN6QQmlSA8PropertyC1EOS0_(QQmlSA::Property *a0) {
  return new QQmlSA::Property(std::move(*a0));
}

//  Property &QQmlSA::Property::operator=(const Property &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Property *ritual_ZN6QQmlSA8PropertyaSERKS0_(
    QQmlSA::Property *self,
    const QQmlSA::Property *a0) {
  return &(self->operator=(*a0));
}

//  Property &QQmlSA::Property::operator=(Property &&a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Property *ritual_ZN6QQmlSA8PropertyaSEOS0_(
    QQmlSA::Property *self,
    QQmlSA::Property *a0) {
  return &(self->operator=(std::move(*a0)));
}

//  QQmlSA::Property::~Property()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA8PropertyD1Ev(QQmlSA::Property *self) {
  delete self;
}

//  QString QQmlSA::Property::typeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA8Property8typeNameEv(
    const QQmlSA::Property *self) {
  return new QString(self->typeName());
}

//  bool QQmlSA::Property::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA8Property7isValidEv(const QQmlSA::Property *self) {
  return self->isValid();
}

//  bool QQmlSA::Property::isReadonly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA8Property10isReadonlyEv(const QQmlSA::Property *self) {
  return self->isReadonly();
}

//  QQmlSA::Element QQmlSA::Property::type() const
extern "C" Q_DECL_EXPORT
QQmlSA::Element *ritual_ZNK6QQmlSA8Property4typeEv(
    const QQmlSA::Property *self) {
  return new QQmlSA::Element(self->type());
}

//  bool operator==(const Property &lhs, const Property &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAeqERKNS_8PropertyES2_(
    const QQmlSA::Property *lhs,
    const QQmlSA::Property *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const Property &lhs, const Property &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAneERKNS_8PropertyES2_(
    const QQmlSA::Property *lhs,
    const QQmlSA::Property *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool QQmlSA::Property::operatorEqualsImpl(const Property &a0, const
//      Property &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSA8Property18operatorEqualsImplERKS0_S2_(
    const QQmlSA::Property *a0,
    const QQmlSA::Property *a1) {
  return QQmlSA::Property::operatorEqualsImpl(*a0, *a1);
}
