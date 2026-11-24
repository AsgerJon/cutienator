//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistcompositor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmllistcompositor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlListCompositor::Change::Change()
extern "C" Q_DECL_EXPORT
QQmlListCompositor::Change *ritual_ZN18QQmlListCompositor6ChangeC1Ev() {
  return new QQmlListCompositor::Change();
}

//  QQmlListCompositor::Change::Change(const iterator &it, int count, uint
//      flags, int moveId)
extern "C" Q_DECL_EXPORT
QQmlListCompositor::Change *ritual_ZN18QQmlListCompositor6ChangeC1ERKNS_8iteratorEiji(
    const QQmlListCompositor::iterator *it,
    int count,
    uint flags,
    int moveId) {
  return new QQmlListCompositor::Change(*it, count, flags, moveId);
}

//  int QQmlListCompositor::Change::cacheIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQmlListCompositor6Change10cacheIndexEv(
    const QQmlListCompositor::Change *self) {
  return self->cacheIndex();
}

//  void QQmlListCompositor::Change::setCacheIndex(int cacheIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor6Change13setCacheIndexEi(
    QQmlListCompositor::Change *self,
    int cacheIndex) {
  self->setCacheIndex(cacheIndex);
}

//  bool QQmlListCompositor::Change::isMove() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlListCompositor6Change6isMoveEv(
    const QQmlListCompositor::Change *self) {
  return self->isMove();
}

//  bool QQmlListCompositor::Change::inCache() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlListCompositor6Change7inCacheEv(
    const QQmlListCompositor::Change *self) {
  return self->inCache();
}

//  bool QQmlListCompositor::Change::inGroup() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlListCompositor6Change7inGroupEv(
    const QQmlListCompositor::Change *self) {
  return self->inGroup();
}

//  bool QQmlListCompositor::Change::inGroup(int group) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlListCompositor6Change7inGroupEi(
    const QQmlListCompositor::Change *self,
    int group) {
  return self->inGroup(group);
}

//  int QQmlListCompositor::Change::groups() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQmlListCompositor6Change6groupsEv(
    const QQmlListCompositor::Change *self) {
  return self->groups();
}

//  QQmlListCompositor::Change::~Change()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor6ChangeD1Ev(
    QQmlListCompositor::Change *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_delegate_model)
