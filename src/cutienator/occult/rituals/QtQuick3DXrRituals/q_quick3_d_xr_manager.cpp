//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrmanager_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquick3dxrmanager_p.h"
#include <QtCore/QCoreApplication>
#include <QtCore/QDebug>
#include <QtCore/qjsonobject.h>
#include <QtCore/qjsonarray.h>
#include <rhi/qrhi.h>
#include <QtQuick/private/qquickwindow_p.h>
#include <QtQuick/QQuickRenderControl>
#include <QtQuick/QQuickRenderTarget>
#include <QtQuick/QQuickItem>
#include <QtQuick3D/private/qquick3dnode_p.h>
#include <QtQuick3D/private/qquick3dviewport_p.h>
#include "qquick3dxranimationdriver_p.h"
#if defined(Q_OS_VISIONOS)
# include <QtQuick3DXr/private/qquick3dxrmanager_visionos_p.h>
#else
#endif
#include "qquick3dxrorigin_p.h"
#include "qquick3dxrinputmanager_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrmanager.cpp, line 121, as _ZNK17QQuick3DXrManager29isMultiViewRenderingSupportedEv
inline bool QQuick3DXrManager::isMultiViewRenderingSupported() const
{
    QRhi *rhi = m_renderControl->rhi();
    return rhi ? rhi->isFeatureSupported(QRhi::MultiView) : false;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrmanager.cpp, line 221, as _ZN17QQuick3DXrManager28isMultiviewRenderingDisabledEv
inline bool QQuick3DXrManager::isMultiviewRenderingDisabled()
{
    const bool disabled = qEnvironmentVariableIntValue("QT_QUICK3D_XR_DISABLE_MULTIVIEW") != 0;
    return disabled;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrmanager.cpp, line 274, as _ZN17QQuick3DXrManager18preSetupQuickSceneEv
inline void QQuick3DXrManager::preSetupQuickScene()
{
    if (!m_renderControl)
        m_renderControl = new QQuickRenderControl;
    if (!m_quickWindow)
        m_quickWindow = new QQuickWindow(m_renderControl);
}
//  -----------------------------------------------------------------------

//  A QQuick3DXrManager that Python can take functions over in. Every QQuick3DXrManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DXrManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DXrManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DXrManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DXrManager : public QQuick3DXrManager {
public:
  using QQuick3DXrManager::QQuick3DXrManager;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuick3DXrManager::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DXrManagerCall0 call = reinterpret_cast<CuteQQuick3DXrManagerCall0>(taken[0]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QQuick3DXrManager::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DXrManagerCall1 call = reinterpret_cast<CuteQQuick3DXrManagerCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DXrManagerCall2 call = reinterpret_cast<CuteQQuick3DXrManagerCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DXrManagerCall3 call = reinterpret_cast<CuteQQuick3DXrManagerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DXrManagerCall4 call = reinterpret_cast<CuteQQuick3DXrManagerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DXrManagerCall5 call = reinterpret_cast<CuteQQuick3DXrManagerCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DXrManagerCall6 call = reinterpret_cast<CuteQQuick3DXrManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DXrManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuick3DXrManager10metaObjectEv(
    const QQuick3DXrManager *self) {
  return self->metaObject();
}

//  bool QQuick3DXrManager::isMultiViewRenderingSupported() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuick3DXrManager29isMultiViewRenderingSupportedEv(
    const QQuick3DXrManager *self) {
  return self->isMultiViewRenderingSupported();
}

//  bool QQuick3DXrManager::isMultiviewRenderingDisabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuick3DXrManager28isMultiviewRenderingDisabledEv() {
  return QQuick3DXrManager::isMultiviewRenderingDisabled();
}

//  void QQuick3DXrManager::preSetupQuickScene()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuick3DXrManager18preSetupQuickSceneEv(
    QQuick3DXrManager *self) {
  self->preSetupQuickScene();
}

//  a Python function taken by a CuteQQuick3DXrManager, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DXrManager(
    QQuick3DXrManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DXrManager *>(self)->take(key, call);
}
