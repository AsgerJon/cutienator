//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QScxmlExecutableContent::StateTable::StateTable()
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::StateTable *ritual_ZN23QScxmlExecutableContent10StateTableC1Ev() {
  return new QScxmlExecutableContent::StateTable();
}

//  const State &QScxmlExecutableContent::StateTable::state(int idx) const
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::StateTable::State *ritual_ZNK23QScxmlExecutableContent10StateTable5stateEi(
    const QScxmlExecutableContent::StateTable *self,
    int idx) {
  return new QScxmlExecutableContent::StateTable::State(self->state(idx));
}

//  const Transition &QScxmlExecutableContent::StateTable::transition(int
//      idx) const
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::StateTable::Transition *ritual_ZNK23QScxmlExecutableContent10StateTable10transitionEi(
    const QScxmlExecutableContent::StateTable *self,
    int idx) {
  return new QScxmlExecutableContent::StateTable::Transition(
      self->transition(
          idx));
}

//  const Array QScxmlExecutableContent::StateTable::array(int idx) const
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::StateTable::Array *ritual_ZNK23QScxmlExecutableContent10StateTable5arrayEi(
    const QScxmlExecutableContent::StateTable *self,
    int idx) {
  return new QScxmlExecutableContent::StateTable::Array(self->array(idx));
}

//  QScxmlExecutableContent::StateTable::~StateTable()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScxmlExecutableContent10StateTableD1Ev(
    QScxmlExecutableContent::StateTable *self) {
  delete self;
}
