//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QQmlChangeSet::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlChangeSet22qt_qmlMarker_anonymousEv(
    QQmlChangeSet *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQmlChangeSet::QQmlChangeSet()
extern "C" Q_DECL_EXPORT
QQmlChangeSet *ritual_ZN13QQmlChangeSetC1Ev() {
  return new QQmlChangeSet();
}

//  QQmlChangeSet::QQmlChangeSet(const QQmlChangeSet &changeSet)
extern "C" Q_DECL_EXPORT
QQmlChangeSet *ritual_ZN13QQmlChangeSetC1ERKS_(
    const QQmlChangeSet *changeSet) {
  return new QQmlChangeSet(*changeSet);
}

//  QQmlChangeSet::~QQmlChangeSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlChangeSetD1Ev(QQmlChangeSet *self) {
  delete self;
}

//  void QQmlChangeSet::insert(int index, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlChangeSet6insertEii(
    QQmlChangeSet *self,
    int index,
    int count) {
  self->insert(index, count);
}

//  void QQmlChangeSet::remove(int index, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlChangeSet6removeEii(
    QQmlChangeSet *self,
    int index,
    int count) {
  self->remove(index, count);
}

//  void QQmlChangeSet::move(int from, int to, int count, int moveId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlChangeSet4moveEiiii(
    QQmlChangeSet *self,
    int from,
    int to,
    int count,
    int moveId) {
  self->move(from, to, count, moveId);
}

//  void QQmlChangeSet::change(int index, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlChangeSet6changeEii(
    QQmlChangeSet *self,
    int index,
    int count) {
  self->change(index, count);
}

//  void QQmlChangeSet::apply(const QQmlChangeSet &changeSet)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlChangeSet5applyERKS_(
    QQmlChangeSet *self,
    const QQmlChangeSet *changeSet) {
  self->apply(*changeSet);
}

//  bool QQmlChangeSet::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQmlChangeSet7isEmptyEv(const QQmlChangeSet *self) {
  return self->isEmpty();
}

//  void QQmlChangeSet::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlChangeSet5clearEv(QQmlChangeSet *self) {
  self->clear();
}

//  int QQmlChangeSet::difference() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QQmlChangeSet10differenceEv(const QQmlChangeSet *self) {
  return self->difference();
}
