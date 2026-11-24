//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
#include <QtQmlCompiler/qqmlsa.h>

//  MethodsPrivate *QQmlSA::Method::Methods::d_func()
extern "C" Q_DECL_EXPORT
QQmlSA::MethodsPrivate *ritual_ZN6QQmlSA6Method7Methods6d_funcEv(
    QQmlSA::Method::Methods *self) {
  return self->d_func();
}

//  const MethodsPrivate *QQmlSA::Method::Methods::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlSA::MethodsPrivate *ritual_ZNK6QQmlSA6Method7Methods6d_funcEv(
    const QQmlSA::Method::Methods *self) {
  return self->d_func();
}

//  QQmlSA::Method::Methods::Methods()
extern "C" Q_DECL_EXPORT
QQmlSA::Method::Methods *ritual_ZN6QQmlSA6Method7MethodsC1Ev() {
  return new QQmlSA::Method::Methods();
}

//  QQmlSA::Method::Methods::Methods(const Methods &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Method::Methods *ritual_ZN6QQmlSA6Method7MethodsC1ERKS1_(
    const QQmlSA::Method::Methods *a0) {
  return new QQmlSA::Method::Methods(*a0);
}

//  QQmlSA::Method::Methods::~Methods()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA6Method7MethodsD1Ev(QQmlSA::Method::Methods *self) {
  delete self;
}
