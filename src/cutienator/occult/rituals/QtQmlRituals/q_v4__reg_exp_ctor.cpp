//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4regexpobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4regexpobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::RegExpCtor::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV410RegExpCtor10__dataTestEv(QV4::RegExpCtor *self) {
  self->__dataTest();
}

//  QV4::Heap::RegExpCtor *QV4::RegExpCtor::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::RegExpCtor *ritual_ZNK3QV410RegExpCtor11d_uncheckedEv(
    const QV4::RegExpCtor *self) {
  return self->d_unchecked();
}

//  QV4::Heap::RegExpCtor *QV4::RegExpCtor::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::RegExpCtor *ritual_ZNK3QV410RegExpCtor1dEv(
    const QV4::RegExpCtor *self) {
  return self->d();
}

//  Value QV4::RegExpCtor::lastMatch()
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV410RegExpCtor9lastMatchEv(QV4::RegExpCtor *self) {
  return new QV4::Value(self->lastMatch());
}

//  Heap::String *QV4::RegExpCtor::lastInput()
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZN3QV410RegExpCtor9lastInputEv(
    QV4::RegExpCtor *self) {
  return self->lastInput();
}

//  int QV4::RegExpCtor::lastMatchStart()
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV410RegExpCtor14lastMatchStartEv(QV4::RegExpCtor *self) {
  return self->lastMatchStart();
}

//  int QV4::RegExpCtor::lastMatchEnd()
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV410RegExpCtor12lastMatchEndEv(QV4::RegExpCtor *self) {
  return self->lastMatchEnd();
}
