//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QScxmlStateMachinePrivate::OrderedSet::OrderedSet()
extern "C" Q_DECL_EXPORT
QScxmlStateMachinePrivate::OrderedSet *ritual_ZN25QScxmlStateMachinePrivate10OrderedSetC1Ev() {
  return new QScxmlStateMachinePrivate::OrderedSet();
}

//  bool QScxmlStateMachinePrivate::OrderedSet::contains(int i) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QScxmlStateMachinePrivate10OrderedSet8containsEi(
    const QScxmlStateMachinePrivate::OrderedSet *self,
    int i) {
  return self->contains(i);
}

//  bool QScxmlStateMachinePrivate::OrderedSet::remove(int i)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QScxmlStateMachinePrivate10OrderedSet6removeEi(
    QScxmlStateMachinePrivate::OrderedSet *self,
    int i) {
  return self->remove(i);
}

//  void QScxmlStateMachinePrivate::OrderedSet::removeHead()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate10OrderedSet10removeHeadEv(
    QScxmlStateMachinePrivate::OrderedSet *self) {
  self->removeHead();
}

//  bool QScxmlStateMachinePrivate::OrderedSet::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QScxmlStateMachinePrivate10OrderedSet7isEmptyEv(
    const QScxmlStateMachinePrivate::OrderedSet *self) {
  return self->isEmpty();
}

//  void QScxmlStateMachinePrivate::OrderedSet::add(int i)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate10OrderedSet3addEi(
    QScxmlStateMachinePrivate::OrderedSet *self,
    int i) {
  self->add(i);
}

//  bool QScxmlStateMachinePrivate::OrderedSet::intersectsWith(const
//      OrderedSet &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QScxmlStateMachinePrivate10OrderedSet14intersectsWithERKS0_(
    const QScxmlStateMachinePrivate::OrderedSet *self,
    const QScxmlStateMachinePrivate::OrderedSet *other) {
  return self->intersectsWith(*other);
}

//  void QScxmlStateMachinePrivate::OrderedSet::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate10OrderedSet5clearEv(
    QScxmlStateMachinePrivate::OrderedSet *self) {
  self->clear();
}

//  QScxmlStateMachinePrivate::OrderedSet::~OrderedSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate10OrderedSetD1Ev(
    QScxmlStateMachinePrivate::OrderedSet *self) {
  delete self;
}
