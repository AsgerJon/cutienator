//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
#include <QtQmlCompiler/qqmlsa.h>
#include <QtCore/QMultiHash>
#include <QtCore/QString>

//  BindingsPrivate *QQmlSA::Binding::Bindings::d_func()
extern "C" Q_DECL_EXPORT
QQmlSA::BindingsPrivate *ritual_ZN6QQmlSA7Binding8Bindings6d_funcEv(
    QQmlSA::Binding::Bindings *self) {
  return self->d_func();
}

//  const BindingsPrivate *QQmlSA::Binding::Bindings::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlSA::BindingsPrivate *ritual_ZNK6QQmlSA7Binding8Bindings6d_funcEv(
    const QQmlSA::Binding::Bindings *self) {
  return self->d_func();
}

//  QQmlSA::Binding::Bindings::Bindings()
extern "C" Q_DECL_EXPORT
QQmlSA::Binding::Bindings *ritual_ZN6QQmlSA7Binding8BindingsC1Ev() {
  return new QQmlSA::Binding::Bindings();
}

//  QQmlSA::Binding::Bindings::Bindings(const Bindings &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Binding::Bindings *ritual_ZN6QQmlSA7Binding8BindingsC1ERKS1_(
    const QQmlSA::Binding::Bindings *a0) {
  return new QQmlSA::Binding::Bindings(*a0);
}

//  QQmlSA::Binding::Bindings::~Bindings()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA7Binding8BindingsD1Ev(QQmlSA::Binding::Bindings *self) {
  delete self;
}

//  QMultiHash<QString, Binding>::const_iterator
//      QQmlSA::Binding::Bindings::begin() const
extern "C" Q_DECL_EXPORT
QMultiHash<QString, QQmlSA::Binding>::const_iterator *ritual_ZNK6QQmlSA7Binding8Bindings5beginEv(
    const QQmlSA::Binding::Bindings *self) {
  return new QMultiHash<QString, QQmlSA::Binding>::const_iterator(
      self->begin());
}

//  QMultiHash<QString, Binding>::const_iterator
//      QQmlSA::Binding::Bindings::end() const
extern "C" Q_DECL_EXPORT
QMultiHash<QString, QQmlSA::Binding>::const_iterator *ritual_ZNK6QQmlSA7Binding8Bindings3endEv(
    const QQmlSA::Binding::Bindings *self) {
  return new QMultiHash<QString, QQmlSA::Binding>::const_iterator(
      self->end());
}

//  QMultiHash<QString, Binding>::const_iterator
//      QQmlSA::Binding::Bindings::constBegin() const
extern "C" Q_DECL_EXPORT
QMultiHash<QString, QQmlSA::Binding>::const_iterator *ritual_ZNK6QQmlSA7Binding8Bindings10constBeginEv(
    const QQmlSA::Binding::Bindings *self) {
  return new QMultiHash<QString, QQmlSA::Binding>::const_iterator(
      self->constBegin());
}

//  QMultiHash<QString, Binding>::const_iterator
//      QQmlSA::Binding::Bindings::constEnd() const
extern "C" Q_DECL_EXPORT
QMultiHash<QString, QQmlSA::Binding>::const_iterator *ritual_ZNK6QQmlSA7Binding8Bindings8constEndEv(
    const QQmlSA::Binding::Bindings *self) {
  return new QMultiHash<QString, QQmlSA::Binding>::const_iterator(
      self->constEnd());
}

//  a QMultiHash<QString, QQmlSA::Binding>::const_iterator a ritual of
//      QQmlSA::Binding::Bindings gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlSA_Binding_Bindings__QMultiHash_QString_QQmlSA_Binding_const_iterator(
    QMultiHash<QString, QQmlSA::Binding>::const_iterator *self) {
  delete self;
}
