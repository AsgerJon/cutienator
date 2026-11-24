//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistcompositor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmllistcompositor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlListCompositor::insert_iterator::insert_iterator()
extern "C" Q_DECL_EXPORT
QQmlListCompositor::insert_iterator *ritual_ZN18QQmlListCompositor15insert_iteratorC1Ev() {
  return new QQmlListCompositor::insert_iterator();
}

//  QQmlListCompositor::insert_iterator::insert_iterator(const iterator &it)
extern "C" Q_DECL_EXPORT
QQmlListCompositor::insert_iterator *ritual_ZN18QQmlListCompositor15insert_iteratorC1ERKNS_8iteratorE(
    const QQmlListCompositor::iterator *it) {
  return new QQmlListCompositor::insert_iterator(*it);
}

//  QQmlListCompositor::insert_iterator::insert_iterator(Range *a0, int a1,
//      Group a2, int a3)
extern "C" Q_DECL_EXPORT
QQmlListCompositor::insert_iterator *ritual_ZN18QQmlListCompositor15insert_iteratorC1EPNS_5RangeEiNS_5GroupEi(
    QQmlListCompositor::Range *a0,
    int a1,
    QQmlListCompositor::Group a2,
    int a3) {
  return new QQmlListCompositor::insert_iterator(a0, a1, a2, a3);
}

//  QQmlListCompositor::insert_iterator::~insert_iterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor15insert_iteratorD1Ev(
    QQmlListCompositor::insert_iterator *self) {
  delete self;
}
