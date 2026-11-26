//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
#include <QtQmlCompiler/qqmlsa.h>
#include <QtCore/QMultiHash>
#include <QtCore/QString>

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

//  QMultiHash<QString, Method>::const_iterator
//      QQmlSA::Method::Methods::begin() const
extern "C" Q_DECL_EXPORT
QMultiHash<QString, QQmlSA::Method>::const_iterator *ritual_ZNK6QQmlSA6Method7Methods5beginEv(
    const QQmlSA::Method::Methods *self) {
  return new QMultiHash<QString, QQmlSA::Method>::const_iterator(
      self->begin());
}

//  QMultiHash<QString, Method>::const_iterator
//      QQmlSA::Method::Methods::end() const
extern "C" Q_DECL_EXPORT
QMultiHash<QString, QQmlSA::Method>::const_iterator *ritual_ZNK6QQmlSA6Method7Methods3endEv(
    const QQmlSA::Method::Methods *self) {
  return new QMultiHash<QString, QQmlSA::Method>::const_iterator(
      self->end());
}

//  QMultiHash<QString, Method>::const_iterator
//      QQmlSA::Method::Methods::constBegin() const
extern "C" Q_DECL_EXPORT
QMultiHash<QString, QQmlSA::Method>::const_iterator *ritual_ZNK6QQmlSA6Method7Methods10constBeginEv(
    const QQmlSA::Method::Methods *self) {
  return new QMultiHash<QString, QQmlSA::Method>::const_iterator(
      self->constBegin());
}

//  QMultiHash<QString, Method>::const_iterator
//      QQmlSA::Method::Methods::constEnd() const
extern "C" Q_DECL_EXPORT
QMultiHash<QString, QQmlSA::Method>::const_iterator *ritual_ZNK6QQmlSA6Method7Methods8constEndEv(
    const QQmlSA::Method::Methods *self) {
  return new QMultiHash<QString, QQmlSA::Method>::const_iterator(
      self->constEnd());
}

//  a QMultiHash<QString, QQmlSA::Method>::const_iterator a ritual of
//      QQmlSA::Method::Methods gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlSA_Method_Methods__QMultiHash_QString_QQmlSA_Method_const_iterator(
    QMultiHash<QString, QQmlSA::Method>::const_iterator *self) {
  delete self;
}
