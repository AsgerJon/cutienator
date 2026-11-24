//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistcompositor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmllistcompositor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlListCompositor::Insert::Insert()
extern "C" Q_DECL_EXPORT
QQmlListCompositor::Insert *ritual_ZN18QQmlListCompositor6InsertC1Ev() {
  return new QQmlListCompositor::Insert();
}

//  QQmlListCompositor::Insert::Insert(const iterator &it, int count, uint
//      flags, int moveId)
extern "C" Q_DECL_EXPORT
QQmlListCompositor::Insert *ritual_ZN18QQmlListCompositor6InsertC1ERKNS_8iteratorEiji(
    const QQmlListCompositor::iterator *it,
    int count,
    uint flags,
    int moveId) {
  return new QQmlListCompositor::Insert(*it, count, flags, moveId);
}

//  QQmlListCompositor::Insert::~Insert()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor6InsertD1Ev(
    QQmlListCompositor::Insert *self) {
  delete self;
}
