//  Written by dev_tooling.RitualGenerator from the records of QtLocation/6.1
//  2.0/QtLocation/private/qdeclarativegeomapitemtransitionmanager_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitemtransitionmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qdeclarativegeomapitemtransitionmanager_p.h"
#include "qdeclarativegeomapitemview_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/quickmapitems/qdeclarativegeomapitemtransitionmanager.cpp, line 10, as _ZN39QDeclarativeGeoMapItemTransitionManagerC1EP7QObject
inline QDeclarativeGeoMapItemTransitionManager::QDeclarativeGeoMapItemTransitionManager(QObject *mapItem)
    : QQuickTransitionManager(), m_mapItem(mapItem)
{
}

//  from ../qtlocation/src/location/quickmapitems/qdeclarativegeomapitemtransitionmanager.cpp, line 15, as _ZN39QDeclarativeGeoMapItemTransitionManager15transitionEnterEv
inline void QDeclarativeGeoMapItemTransitionManager::transitionEnter()
{
    if (m_transitionState == ExitTransition)
        cancel();

    if (!prepareEnterTransition())
        return;

    if (m_view && m_view->m_enter)
        transition(enterActions, m_view->m_enter, m_mapItem);
    else
        finished();
}

//  from ../qtlocation/src/location/quickmapitems/qdeclarativegeomapitemtransitionmanager.cpp, line 29, as _ZN39QDeclarativeGeoMapItemTransitionManager14transitionExitEv
inline void QDeclarativeGeoMapItemTransitionManager::transitionExit()
{
    if (!prepareExitTransition())
        return;

    if (m_view && m_view->m_exit)
        transition(exitActions, m_view->m_exit, m_mapItem);
    else
        finished();
}

//  from ../qtlocation/src/location/quickmapitems/qdeclarativegeomapitemtransitionmanager.cpp, line 40, as _ZN39QDeclarativeGeoMapItemTransitionManager8finishedEv
inline void QDeclarativeGeoMapItemTransitionManager::finished()
{
    if (m_transitionState == EnterTransition)
        finalizeEnterTransition();
    else if (m_transitionState == ExitTransition)
        finalizeExitTransition();
}
//  -----------------------------------------------------------------------

//  Only a class built on QDeclarativeGeoMapItemTransitionManager may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDeclarativeGeoMapItemTransitionManager : QDeclarativeGeoMapItemTransitionManager {
  using QDeclarativeGeoMapItemTransitionManager::finished;
};

//  A QDeclarativeGeoMapItemTransitionManager that Python can take functions over in. Every QDeclarativeGeoMapItemTransitionManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativeGeoMapItemTransitionManagerCall0)(const void *, int *);
class CuteQDeclarativeGeoMapItemTransitionManager : public QDeclarativeGeoMapItemTransitionManager {
public:
  using QDeclarativeGeoMapItemTransitionManager::QDeclarativeGeoMapItemTransitionManager;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QQuickTransitionManager8finishedEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QDeclarativeGeoMapItemTransitionManager::finished()
  void finished() override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeGeoMapItemTransitionManagerCall0 call = reinterpret_cast<CuteQDeclarativeGeoMapItemTransitionManagerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeGeoMapItemTransitionManager::finished();
  }
};

//  QDeclarativeGeoMapItemTransitionManager::QDeclarativeGeoMapItemTransition
//      Manager(QObject *mapItem)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoMapItemTransitionManager *ritual_ZN39QDeclarativeGeoMapItemTransitionManagerC1EP7QObject(
    QObject *mapItem) {
  return new CuteQDeclarativeGeoMapItemTransitionManager(mapItem);
}

//  void QDeclarativeGeoMapItemTransitionManager::transitionEnter()
extern "C" Q_DECL_EXPORT
void ritual_ZN39QDeclarativeGeoMapItemTransitionManager15transitionEnterEv(
    QDeclarativeGeoMapItemTransitionManager *self) {
  self->transitionEnter();
}

//  void QDeclarativeGeoMapItemTransitionManager::transitionExit()
extern "C" Q_DECL_EXPORT
void ritual_ZN39QDeclarativeGeoMapItemTransitionManager14transitionExitEv(
    QDeclarativeGeoMapItemTransitionManager *self) {
  self->transitionExit();
}

//  bool QDeclarativeGeoMapItemTransitionManager::prepareEnterTransition()
extern "C" Q_DECL_EXPORT
bool ritual_ZN39QDeclarativeGeoMapItemTransitionManager22prepareEnterTransitionEv(
    QDeclarativeGeoMapItemTransitionManager *self) {
  return self->prepareEnterTransition();
}

//  bool QDeclarativeGeoMapItemTransitionManager::prepareExitTransition()
extern "C" Q_DECL_EXPORT
bool ritual_ZN39QDeclarativeGeoMapItemTransitionManager21prepareExitTransitionEv(
    QDeclarativeGeoMapItemTransitionManager *self) {
  return self->prepareExitTransition();
}

//  void QDeclarativeGeoMapItemTransitionManager::finalizeEnterTransition()
extern "C" Q_DECL_EXPORT
void ritual_ZN39QDeclarativeGeoMapItemTransitionManager23finalizeEnterTransitionEv(
    QDeclarativeGeoMapItemTransitionManager *self) {
  self->finalizeEnterTransition();
}

//  void QDeclarativeGeoMapItemTransitionManager::finalizeExitTransition()
extern "C" Q_DECL_EXPORT
void ritual_ZN39QDeclarativeGeoMapItemTransitionManager22finalizeExitTransitionEv(
    QDeclarativeGeoMapItemTransitionManager *self) {
  self->finalizeExitTransition();
}

//  void QDeclarativeGeoMapItemTransitionManager::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN39QDeclarativeGeoMapItemTransitionManager8finishedEv(
    QDeclarativeGeoMapItemTransitionManager *self) {
  self->finished();
}

//  a Python function taken by a CuteQDeclarativeGeoMapItemTransitionManager,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeGeoMapItemTransitionManager(
    QDeclarativeGeoMapItemTransitionManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeGeoMapItemTransitionManager *>(self)->take(key, call);
}

//  void QDeclarativeGeoMapItemTransitionManager::finished()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN39QDeclarativeGeoMapItemTransitionManager8finishedEv(
    QDeclarativeGeoMapItemTransitionManager *self) {
  static_cast<OwnQDeclarativeGeoMapItemTransitionManager *>(self)->OwnQDeclarativeGeoMapItemTransitionManager::finished();
}
