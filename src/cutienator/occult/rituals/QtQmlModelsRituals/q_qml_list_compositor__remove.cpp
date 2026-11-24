//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistcompositor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmllistcompositor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlListCompositor::Remove::Remove()
extern "C" Q_DECL_EXPORT
QQmlListCompositor::Remove *ritual_ZN18QQmlListCompositor6RemoveC1Ev() {
  return new QQmlListCompositor::Remove();
}

//  QQmlListCompositor::Remove::Remove(const iterator &it, int count, uint
//      flags, int moveId)
extern "C" Q_DECL_EXPORT
QQmlListCompositor::Remove *ritual_ZN18QQmlListCompositor6RemoveC1ERKNS_8iteratorEiji(
    const QQmlListCompositor::iterator *it,
    int count,
    uint flags,
    int moveId) {
  return new QQmlListCompositor::Remove(*it, count, flags, moveId);
}

//  QQmlListCompositor::Remove::~Remove()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor6RemoveD1Ev(
    QQmlListCompositor::Remove *self) {
  delete self;
}
