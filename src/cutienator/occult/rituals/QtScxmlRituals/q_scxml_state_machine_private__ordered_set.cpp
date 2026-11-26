//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <vector>

//  QScxmlStateMachinePrivate::OrderedSet::OrderedSet()
extern "C" Q_DECL_EXPORT
QScxmlStateMachinePrivate::OrderedSet *ritual_ZN25QScxmlStateMachinePrivate10OrderedSetC1Ev() {
  return new QScxmlStateMachinePrivate::OrderedSet();
}

//  QScxmlStateMachinePrivate::OrderedSet::OrderedSet(std::initializer_list<i
//      nt> l)
extern "C" Q_DECL_EXPORT
QScxmlStateMachinePrivate::OrderedSet *ritual_ZN25QScxmlStateMachinePrivate10OrderedSetC1ESt16initializer_listIiE(
    const std::initializer_list<int> *l) {
  return new QScxmlStateMachinePrivate::OrderedSet(*l);
}

//  std::vector<int> QScxmlStateMachinePrivate::OrderedSet::takeList() const
extern "C" Q_DECL_EXPORT
std::vector<int> *ritual_ZNK25QScxmlStateMachinePrivate10OrderedSet8takeListEv(
    const QScxmlStateMachinePrivate::OrderedSet *self) {
  return new std::vector<int>(self->takeList());
}

//  const std::vector<int> &QScxmlStateMachinePrivate::OrderedSet::list()
//      const
extern "C" Q_DECL_EXPORT
const std::vector<int> *ritual_ZNK25QScxmlStateMachinePrivate10OrderedSet4listEv(
    const QScxmlStateMachinePrivate::OrderedSet *self) {
  return &(self->list());
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

//  const_iterator QScxmlStateMachinePrivate::OrderedSet::begin() const
extern "C" Q_DECL_EXPORT
QScxmlStateMachinePrivate::OrderedSet::const_iterator *ritual_ZNK25QScxmlStateMachinePrivate10OrderedSet5beginEv(
    const QScxmlStateMachinePrivate::OrderedSet *self) {
  return new QScxmlStateMachinePrivate::OrderedSet::const_iterator(
      self->begin());
}

//  const_iterator QScxmlStateMachinePrivate::OrderedSet::end() const
extern "C" Q_DECL_EXPORT
QScxmlStateMachinePrivate::OrderedSet::const_iterator *ritual_ZNK25QScxmlStateMachinePrivate10OrderedSet3endEv(
    const QScxmlStateMachinePrivate::OrderedSet *self) {
  return new QScxmlStateMachinePrivate::OrderedSet::const_iterator(
      self->end());
}

//  QScxmlStateMachinePrivate::OrderedSet::~OrderedSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate10OrderedSetD1Ev(
    QScxmlStateMachinePrivate::OrderedSet *self) {
  delete self;
}

//  a std::vector<int> a ritual of QScxmlStateMachinePrivate::OrderedSet gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QScxmlStateMachinePrivate_OrderedSet__std_vector_int(
    std::vector<int> *self) {
  delete self;
}

//  a QScxmlStateMachinePrivate::OrderedSet::const_iterator a ritual of
//      QScxmlStateMachinePrivate::OrderedSet gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QScxmlStateMachinePrivate_OrderedSet__QScxmlStateMachinePrivate_OrderedSet_const_iterator(
    QScxmlStateMachinePrivate::OrderedSet::const_iterator *self) {
  delete self;
}
