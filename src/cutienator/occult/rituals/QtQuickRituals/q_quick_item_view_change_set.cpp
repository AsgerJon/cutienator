//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemview_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_itemview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemview_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuickItemViewChangeSet::QQuickItemViewChangeSet()
extern "C" Q_DECL_EXPORT
QQuickItemViewChangeSet *ritual_ZN23QQuickItemViewChangeSetC1Ev() {
  return new QQuickItemViewChangeSet();
}

//  bool QQuickItemViewChangeSet::hasPendingChanges() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickItemViewChangeSet17hasPendingChangesEv(
    const QQuickItemViewChangeSet *self) {
  return self->hasPendingChanges();
}

//  void QQuickItemViewChangeSet::prepare(int currentIndex, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickItemViewChangeSet7prepareEii(
    QQuickItemViewChangeSet *self,
    int currentIndex,
    int count) {
  self->prepare(currentIndex, count);
}

//  void QQuickItemViewChangeSet::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickItemViewChangeSet5resetEv(
    QQuickItemViewChangeSet *self) {
  self->reset();
}

//  void QQuickItemViewChangeSet::applyChanges(const QQmlChangeSet
//      &changeSet)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickItemViewChangeSet12applyChangesERK13QQmlChangeSet(
    QQuickItemViewChangeSet *self,
    const QQmlChangeSet *changeSet) {
  self->applyChanges(*changeSet);
}

//  void QQuickItemViewChangeSet::applyBufferedChanges(const
//      QQuickItemViewChangeSet &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickItemViewChangeSet20applyBufferedChangesERKS_(
    QQuickItemViewChangeSet *self,
    const QQuickItemViewChangeSet *other) {
  self->applyBufferedChanges(*other);
}

//  QQuickItemViewChangeSet::~QQuickItemViewChangeSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickItemViewChangeSetD1Ev(QQuickItemViewChangeSet *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_itemview)
