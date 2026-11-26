//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QScxmlExecutableContent::StateTable::Array::const_iterator::const_iterato
//      r(const Array &a, int pos)
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::StateTable::Array::const_iterator *ritual_ZN23QScxmlExecutableContent10StateTable5Array14const_iteratorC1ERKS1_i(
    const QScxmlExecutableContent::StateTable::Array *a,
    int pos) {
  return new QScxmlExecutableContent::StateTable::Array::const_iterator(
      *a,
      pos);
}

//  const_iterator
//      &QScxmlExecutableContent::StateTable::Array::const_iterator::operator
//      ++()
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::StateTable::Array::const_iterator *ritual_ZN23QScxmlExecutableContent10StateTable5Array14const_iteratorppEv(
    QScxmlExecutableContent::StateTable::Array::const_iterator *self) {
  return &(self->operator++());
}

//  bool QScxmlExecutableContent::StateTable::Array::const_iterator::operator
//      ==(const const_iterator &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QScxmlExecutableContent10StateTable5Array14const_iteratoreqERKS2_(
    const QScxmlExecutableContent::StateTable::Array::const_iterator *self,
    const QScxmlExecutableContent::StateTable::Array::const_iterator *other) {
  return self->operator==(*other);
}

//  bool QScxmlExecutableContent::StateTable::Array::const_iterator::operator
//      !=(const StateTable::Array::const_iterator &other)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QScxmlExecutableContent10StateTable5Array14const_iteratorneERKS2_(
    QScxmlExecutableContent::StateTable::Array::const_iterator *self,
    const QScxmlExecutableContent::StateTable::Array::const_iterator *other) {
  return self->operator!=(*other);
}

//  int
//      QScxmlExecutableContent::StateTable::Array::const_iterator::operator*
//      () const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QScxmlExecutableContent10StateTable5Array14const_iteratordeEv(
    const QScxmlExecutableContent::StateTable::Array::const_iterator *self) {
  return self->operator*();
}

//  QScxmlExecutableContent::StateTable::Array::const_iterator::~const_iterat
//      or()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScxmlExecutableContent10StateTable5Array14const_iteratorD1Ev(
    QScxmlExecutableContent::StateTable::Array::const_iterator *self) {
  delete self;
}
