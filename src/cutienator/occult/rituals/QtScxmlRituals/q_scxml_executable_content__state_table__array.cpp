//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  int QScxmlExecutableContent::StateTable::Array::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QScxmlExecutableContent10StateTable5Array4sizeEv(
    const QScxmlExecutableContent::StateTable::Array *self) {
  return self->size();
}

//  bool QScxmlExecutableContent::StateTable::Array::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QScxmlExecutableContent10StateTable5Array7isValidEv(
    const QScxmlExecutableContent::StateTable::Array *self) {
  return self->isValid();
}

//  int QScxmlExecutableContent::StateTable::Array::operator[](int idx) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QScxmlExecutableContent10StateTable5ArrayixEi(
    const QScxmlExecutableContent::StateTable::Array *self,
    int idx) {
  return self->operator[](idx);
}

//  const_iterator QScxmlExecutableContent::StateTable::Array::begin() const
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::StateTable::Array::const_iterator *ritual_ZNK23QScxmlExecutableContent10StateTable5Array5beginEv(
    const QScxmlExecutableContent::StateTable::Array *self) {
  return new QScxmlExecutableContent::StateTable::Array::const_iterator(
      self->begin());
}

//  const_iterator QScxmlExecutableContent::StateTable::Array::end() const
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::StateTable::Array::const_iterator *ritual_ZNK23QScxmlExecutableContent10StateTable5Array3endEv(
    const QScxmlExecutableContent::StateTable::Array *self) {
  return new QScxmlExecutableContent::StateTable::Array::const_iterator(
      self->end());
}

//  QScxmlExecutableContent::StateTable::Array::~Array()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScxmlExecutableContent10StateTable5ArrayD1Ev(
    QScxmlExecutableContent::StateTable::Array *self) {
  delete self;
}
