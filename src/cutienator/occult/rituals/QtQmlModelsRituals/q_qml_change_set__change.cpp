//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlChangeSet::Change::Change()
extern "C" Q_DECL_EXPORT
QQmlChangeSet::Change *ritual_ZN13QQmlChangeSet6ChangeC1Ev() {
  return new QQmlChangeSet::Change();
}

//  QQmlChangeSet::Change::Change(int index, int count, int moveId, int
//      offset)
extern "C" Q_DECL_EXPORT
QQmlChangeSet::Change *ritual_ZN13QQmlChangeSet6ChangeC1Eiiii(
    int index,
    int count,
    int moveId,
    int offset) {
  return new QQmlChangeSet::Change(index, count, moveId, offset);
}

//  bool QQmlChangeSet::Change::isMove() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQmlChangeSet6Change6isMoveEv(
    const QQmlChangeSet::Change *self) {
  return self->isMove();
}

//  MoveKey QQmlChangeSet::Change::moveKey(int index) const
extern "C" Q_DECL_EXPORT
QQmlChangeSet::MoveKey *ritual_ZNK13QQmlChangeSet6Change7moveKeyEi(
    const QQmlChangeSet::Change *self,
    int index) {
  return new QQmlChangeSet::MoveKey(self->moveKey(index));
}

//  int QQmlChangeSet::Change::start() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QQmlChangeSet6Change5startEv(
    const QQmlChangeSet::Change *self) {
  return self->start();
}

//  int QQmlChangeSet::Change::end() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QQmlChangeSet6Change3endEv(
    const QQmlChangeSet::Change *self) {
  return self->end();
}

//  QQmlChangeSet::Change::~Change()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlChangeSet6ChangeD1Ev(QQmlChangeSet::Change *self) {
  delete self;
}
