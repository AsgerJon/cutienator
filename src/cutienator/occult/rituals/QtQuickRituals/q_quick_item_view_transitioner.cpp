//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemviewtransition_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_viewtransitions)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemviewtransition_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qobject.h>
#include <QtCore/qlist.h>

//  QQuickItemViewTransitioner::QQuickItemViewTransitioner()
extern "C" Q_DECL_EXPORT
QQuickItemViewTransitioner *ritual_ZN26QQuickItemViewTransitionerC1Ev() {
  return new QQuickItemViewTransitioner();
}

//  QQuickItemViewTransitioner::~QQuickItemViewTransitioner()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickItemViewTransitionerD1Ev(
    QQuickItemViewTransitioner *self) {
  delete self;
}

//  bool QQuickItemViewTransitioner::canTransition(QQuickItemViewTransitioner
//      ::TransitionType type, bool asTarget) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuickItemViewTransitioner13canTransitionENS_14TransitionTypeEb(
    const QQuickItemViewTransitioner *self,
    QQuickItemViewTransitioner::TransitionType type,
    bool asTarget) {
  return self->canTransition(type, asTarget);
}

//  void QQuickItemViewTransitioner::transitionNextReposition(QQuickItemViewT
//      ransitionableItem *item, QQuickItemViewTransitioner::TransitionType
//      type, bool isTarget)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickItemViewTransitioner24transitionNextRepositionEP32QQuickItemViewTransitionableItemNS_14TransitionTypeEb(
    QQuickItemViewTransitioner *self,
    QQuickItemViewTransitionableItem *item,
    QQuickItemViewTransitioner::TransitionType type,
    bool isTarget) {
  self->transitionNextReposition(item, type, isTarget);
}

//  void QQuickItemViewTransitioner::addToTargetLists(QQuickItemViewTransitio
//      ner::TransitionType type, QQuickItemViewTransitionableItem *item, int
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickItemViewTransitioner16addToTargetListsENS_14TransitionTypeEP32QQuickItemViewTransitionableItemi(
    QQuickItemViewTransitioner *self,
    QQuickItemViewTransitioner::TransitionType type,
    QQuickItemViewTransitionableItem *item,
    int index) {
  self->addToTargetLists(type, item, index);
}

//  void QQuickItemViewTransitioner::resetTargetLists()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickItemViewTransitioner16resetTargetListsEv(
    QQuickItemViewTransitioner *self) {
  self->resetTargetLists();
}

//  QQuickTransition *QQuickItemViewTransitioner::transitionObject(QQuickItem
//      ViewTransitioner::TransitionType type, bool asTarget) const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK26QQuickItemViewTransitioner16transitionObjectENS_14TransitionTypeEb(
    const QQuickItemViewTransitioner *self,
    QQuickItemViewTransitioner::TransitionType type,
    bool asTarget) {
  return self->transitionObject(type, asTarget);
}

//  const QList<QObject *> &QQuickItemViewTransitioner::targetItems(QQuickIte
//      mViewTransitioner::TransitionType type) const
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_ZNK26QQuickItemViewTransitioner11targetItemsENS_14TransitionTypeE(
    const QQuickItemViewTransitioner *self,
    QQuickItemViewTransitioner::TransitionType type) {
  return new QList<QObject *>(self->targetItems(type));
}

//  void QQuickItemViewTransitioner::setPopulateTransitionEnabled(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickItemViewTransitioner28setPopulateTransitionEnabledEb(
    QQuickItemViewTransitioner *self,
    bool b) {
  self->setPopulateTransitionEnabled(b);
}

//  bool QQuickItemViewTransitioner::populateTransitionEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuickItemViewTransitioner25populateTransitionEnabledEv(
    const QQuickItemViewTransitioner *self) {
  return self->populateTransitionEnabled();
}

//  void QQuickItemViewTransitioner::setChangeListener(QQuickItemViewTransiti
//      onChangeListener *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickItemViewTransitioner17setChangeListenerEP38QQuickItemViewTransitionChangeListener(
    QQuickItemViewTransitioner *self,
    QQuickItemViewTransitionChangeListener *obj) {
  self->setChangeListener(obj);
}

#endif  // QT_CONFIG(quick_viewtransitions)
