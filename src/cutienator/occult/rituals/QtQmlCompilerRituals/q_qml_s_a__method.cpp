//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
#include <QtQmlCompiler/qqmlsa.h>
#include <QtCore/qstring.h>
#include <QtQmlCompiler/qqmlsasourcelocation.h>

//  MethodPrivate *QQmlSA::Method::d_func()
extern "C" Q_DECL_EXPORT
QQmlSA::MethodPrivate *ritual_ZN6QQmlSA6Method6d_funcEv(
    QQmlSA::Method *self) {
  return self->d_func();
}

//  const MethodPrivate *QQmlSA::Method::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlSA::MethodPrivate *ritual_ZNK6QQmlSA6Method6d_funcEv(
    const QQmlSA::Method *self) {
  return self->d_func();
}

//  QQmlSA::Method::Method()
extern "C" Q_DECL_EXPORT
QQmlSA::Method *ritual_ZN6QQmlSA6MethodC1Ev() {
  return new QQmlSA::Method();
}

//  QQmlSA::Method::Method(const Method &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Method *ritual_ZN6QQmlSA6MethodC1ERKS0_(const QQmlSA::Method *a0) {
  return new QQmlSA::Method(*a0);
}

//  QQmlSA::Method::Method(Method &&a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Method *ritual_ZN6QQmlSA6MethodC1EOS0_(QQmlSA::Method *a0) {
  return new QQmlSA::Method(std::move(*a0));
}

//  Method &QQmlSA::Method::operator=(const Method &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Method *ritual_ZN6QQmlSA6MethodaSERKS0_(
    QQmlSA::Method *self,
    const QQmlSA::Method *a0) {
  return &(self->operator=(*a0));
}

//  Method &QQmlSA::Method::operator=(Method &&a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Method *ritual_ZN6QQmlSA6MethodaSEOS0_(
    QQmlSA::Method *self,
    QQmlSA::Method *a0) {
  return &(self->operator=(std::move(*a0)));
}

//  QQmlSA::Method::~Method()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA6MethodD1Ev(QQmlSA::Method *self) {
  delete self;
}

//  QString QQmlSA::Method::methodName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA6Method10methodNameEv(const QQmlSA::Method *self) {
  return new QString(self->methodName());
}

//  QQmlSA::SourceLocation QQmlSA::Method::sourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlSA::SourceLocation *ritual_ZNK6QQmlSA6Method14sourceLocationEv(
    const QQmlSA::Method *self) {
  return new QQmlSA::SourceLocation(self->sourceLocation());
}

//  MethodType QQmlSA::Method::methodType() const
extern "C" Q_DECL_EXPORT
QQmlSA::MethodType ritual_ZNK6QQmlSA6Method10methodTypeEv(
    const QQmlSA::Method *self) {
  return self->methodType();
}

//  bool operator==(const Method &lhs, const Method &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAeqERKNS_6MethodES2_(
    const QQmlSA::Method *lhs,
    const QQmlSA::Method *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const Method &lhs, const Method &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAneERKNS_6MethodES2_(
    const QQmlSA::Method *lhs,
    const QQmlSA::Method *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool QQmlSA::Method::operatorEqualsImpl(const Method &a0, const Method
//      &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSA6Method18operatorEqualsImplERKS0_S2_(
    const QQmlSA::Method *a0,
    const QQmlSA::Method *a1) {
  return QQmlSA::Method::operatorEqualsImpl(*a0, *a1);
}
