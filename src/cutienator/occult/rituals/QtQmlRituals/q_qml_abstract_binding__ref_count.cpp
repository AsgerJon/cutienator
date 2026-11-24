//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlabstractbinding_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlabstractbinding_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlAbstractBinding::RefCount::RefCount()
extern "C" Q_DECL_EXPORT
QQmlAbstractBinding::RefCount *ritual_ZN19QQmlAbstractBinding8RefCountC1Ev() {
  return new QQmlAbstractBinding::RefCount();
}

//  void QQmlAbstractBinding::RefCount::ref()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlAbstractBinding8RefCount3refEv(
    QQmlAbstractBinding::RefCount *self) {
  self->ref();
}

//  int QQmlAbstractBinding::RefCount::deref()
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQmlAbstractBinding8RefCount5derefEv(
    QQmlAbstractBinding::RefCount *self) {
  return self->deref();
}

//  int QQmlAbstractBinding::RefCount::operator int() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQmlAbstractBinding8RefCountcviEv(
    const QQmlAbstractBinding::RefCount *self) {
  return self->operator int();
}

//  QQmlAbstractBinding::RefCount::~RefCount()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlAbstractBinding8RefCountD1Ev(
    QQmlAbstractBinding::RefCount *self) {
  delete self;
}
