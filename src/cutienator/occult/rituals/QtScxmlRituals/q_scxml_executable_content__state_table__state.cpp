//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlexecutablecontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QScxmlExecutableContent::StateTable::State::State()
extern "C" Q_DECL_EXPORT
QScxmlExecutableContent::StateTable::State *ritual_ZN23QScxmlExecutableContent10StateTable5StateC1Ev() {
  return new QScxmlExecutableContent::StateTable::State();
}

//  bool QScxmlExecutableContent::StateTable::State::isAtomic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QScxmlExecutableContent10StateTable5State8isAtomicEv(
    const QScxmlExecutableContent::StateTable::State *self) {
  return self->isAtomic();
}

//  bool QScxmlExecutableContent::StateTable::State::isCompound() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QScxmlExecutableContent10StateTable5State10isCompoundEv(
    const QScxmlExecutableContent::StateTable::State *self) {
  return self->isCompound();
}

//  bool QScxmlExecutableContent::StateTable::State::parentIsScxmlElement()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QScxmlExecutableContent10StateTable5State20parentIsScxmlElementEv(
    const QScxmlExecutableContent::StateTable::State *self) {
  return self->parentIsScxmlElement();
}

//  bool QScxmlExecutableContent::StateTable::State::isHistoryState() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QScxmlExecutableContent10StateTable5State14isHistoryStateEv(
    const QScxmlExecutableContent::StateTable::State *self) {
  return self->isHistoryState();
}

//  bool QScxmlExecutableContent::StateTable::State::isParallel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QScxmlExecutableContent10StateTable5State10isParallelEv(
    const QScxmlExecutableContent::StateTable::State *self) {
  return self->isParallel();
}

//  QScxmlExecutableContent::StateTable::State::~State()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScxmlExecutableContent10StateTable5StateD1Ev(
    QScxmlExecutableContent::StateTable::State *self) {
  delete self;
}
