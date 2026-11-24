//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistcompositor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmllistcompositor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlListCompositor::Range::Range()
extern "C" Q_DECL_EXPORT
QQmlListCompositor::Range *ritual_ZN18QQmlListCompositor5RangeC1Ev() {
  return new QQmlListCompositor::Range();
}

//  int QQmlListCompositor::Range::start() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQmlListCompositor5Range5startEv(
    const QQmlListCompositor::Range *self) {
  return self->start();
}

//  int QQmlListCompositor::Range::end() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQmlListCompositor5Range3endEv(
    const QQmlListCompositor::Range *self) {
  return self->end();
}

//  int QQmlListCompositor::Range::groups() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQmlListCompositor5Range6groupsEv(
    const QQmlListCompositor::Range *self) {
  return self->groups();
}

//  bool QQmlListCompositor::Range::inGroup() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlListCompositor5Range7inGroupEv(
    const QQmlListCompositor::Range *self) {
  return self->inGroup();
}

//  bool QQmlListCompositor::Range::inCache() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlListCompositor5Range7inCacheEv(
    const QQmlListCompositor::Range *self) {
  return self->inCache();
}

//  bool QQmlListCompositor::Range::inGroup(int group) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlListCompositor5Range7inGroupEi(
    const QQmlListCompositor::Range *self,
    int group) {
  return self->inGroup(group);
}

//  bool QQmlListCompositor::Range::isUnresolved() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlListCompositor5Range12isUnresolvedEv(
    const QQmlListCompositor::Range *self) {
  return self->isUnresolved();
}

//  bool QQmlListCompositor::Range::prepend() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlListCompositor5Range7prependEv(
    const QQmlListCompositor::Range *self) {
  return self->prepend();
}

//  bool QQmlListCompositor::Range::append() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlListCompositor5Range6appendEv(
    const QQmlListCompositor::Range *self) {
  return self->append();
}

//  QQmlListCompositor::Range::~Range()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlListCompositor5RangeD1Ev(
    QQmlListCompositor::Range *self) {
  delete self;
}
