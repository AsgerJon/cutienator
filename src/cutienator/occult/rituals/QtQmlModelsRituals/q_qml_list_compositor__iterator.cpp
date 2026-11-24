//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistcompositor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmllistcompositor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlListCompositor::iterator::iterator()
extern "C" Q_DECL_EXPORT
QQmlListCompositor::iterator *ritual_ZN18QQmlListCompositor8iteratorC1Ev() {
  return new QQmlListCompositor::iterator();
}

//  QQmlListCompositor::iterator::iterator(Range *range, int offset, Group
//      group, int groupCount)
extern "C" Q_DECL_EXPORT
QQmlListCompositor::iterator *ritual_ZN18QQmlListCompositor8iteratorC1EPNS_5RangeEiNS_5GroupEi(
    QQmlListCompositor::Range *range,
    int offset,
    QQmlListCompositor::Group group,
    int groupCount) {
  return new QQmlListCompositor::iterator(range, offset, group, groupCount);
}

//  bool QQmlListCompositor::iterator::operator==(const iterator &it) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlListCompositor8iteratoreqERKS0_(
    const QQmlListCompositor::iterator *self,
    const QQmlListCompositor::iterator *it) {
  return self->operator==(*it);
}

//  bool QQmlListCompositor::iterator::operator!=(const iterator &it) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlListCompositor8iteratorneERKS0_(
    const QQmlListCompositor::iterator *self,
    const QQmlListCompositor::iterator *it) {
  return self->operator!=(*it);
}

//  bool QQmlListCompositor::iterator::operator==(Group group) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlListCompositor8iteratoreqENS_5GroupE(
    const QQmlListCompositor::iterator *self,
    QQmlListCompositor::Group group) {
  return self->operator==(group);
}

//  bool QQmlListCompositor::iterator::operator!=(Group group) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlListCompositor8iteratorneENS_5GroupE(
    const QQmlListCompositor::iterator *self,
    QQmlListCompositor::Group group) {
  return self->operator!=(group);
}

//  Range *QQmlListCompositor::iterator::operator->()
extern "C" Q_DECL_EXPORT
QQmlListCompositor::Range *ritual_ZN18QQmlListCompositor8iteratorptEv(
    QQmlListCompositor::iterator *self) {
  return self->operator->();
}

//  const Range *QQmlListCompositor::iterator::operator->() const
extern "C" Q_DECL_EXPORT
const QQmlListCompositor::Range *ritual_ZNK18QQmlListCompositor8iteratorptEv(
    const QQmlListCompositor::iterator *self) {
  return self->operator->();
}

//  int QQmlListCompositor::iterator::modelIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQmlListCompositor8iterator10modelIndexEv(
    const QQmlListCompositor::iterator *self) {
  return self->modelIndex();
}

//  void QQmlListCompositor::iterator::incrementIndexes(int difference)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor8iterator16incrementIndexesEi(
    QQmlListCompositor::iterator *self,
    int difference) {
  self->incrementIndexes(difference);
}

//  void QQmlListCompositor::iterator::decrementIndexes(int difference)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor8iterator16decrementIndexesEi(
    QQmlListCompositor::iterator *self,
    int difference) {
  self->decrementIndexes(difference);
}

//  void QQmlListCompositor::iterator::incrementIndexes(int difference, uint
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor8iterator16incrementIndexesEij(
    QQmlListCompositor::iterator *self,
    int difference,
    uint flags) {
  self->incrementIndexes(difference, flags);
}

//  void QQmlListCompositor::iterator::decrementIndexes(int difference, uint
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor8iterator16decrementIndexesEij(
    QQmlListCompositor::iterator *self,
    int difference,
    uint flags) {
  self->decrementIndexes(difference, flags);
}

//  void QQmlListCompositor::iterator::setGroup(Group g)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor8iterator8setGroupENS_5GroupE(
    QQmlListCompositor::iterator *self,
    QQmlListCompositor::Group g) {
  self->setGroup(g);
}

//  int QQmlListCompositor::iterator::cacheIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQmlListCompositor8iterator10cacheIndexEv(
    const QQmlListCompositor::iterator *self) {
  return self->cacheIndex();
}

//  void QQmlListCompositor::iterator::setCacheIndex(int cacheIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor8iterator13setCacheIndexEi(
    QQmlListCompositor::iterator *self,
    int cacheIndex) {
  self->setCacheIndex(cacheIndex);
}

//  QQmlListCompositor::iterator::~iterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor8iteratorD1Ev(
    QQmlListCompositor::iterator *self) {
  delete self;
}
