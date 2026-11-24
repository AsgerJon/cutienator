//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopup_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopup_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Only a class built on QQuickPopupTransitionManager may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickPopupTransitionManager : QQuickPopupTransitionManager {
  using QQuickPopupTransitionManager::finished;
};

//  QQuickPopupTransitionManager::QQuickPopupTransitionManager(QQuickPopupPri
//      vate *popup)
extern "C" Q_DECL_EXPORT
QQuickPopupTransitionManager *ritual_ZN28QQuickPopupTransitionManagerC1EP18QQuickPopupPrivate(
    QQuickPopupPrivate *popup) {
  return new QQuickPopupTransitionManager(popup);
}

//  void QQuickPopupTransitionManager::transitionEnter()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickPopupTransitionManager15transitionEnterEv(
    QQuickPopupTransitionManager *self) {
  self->transitionEnter();
}

//  void QQuickPopupTransitionManager::transitionExit()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickPopupTransitionManager14transitionExitEv(
    QQuickPopupTransitionManager *self) {
  self->transitionExit();
}

//  void QQuickPopupTransitionManager::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickPopupTransitionManager8finishedEv(
    QQuickPopupTransitionManager *self) {
  self->finished();
}

//  void QQuickPopupTransitionManager::finished()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuickPopupTransitionManager8finishedEv(
    QQuickPopupTransitionManager *self) {
  static_cast<OwnQQuickPopupTransitionManager *>(self)->OwnQQuickPopupTransitionManager::finished();
}
