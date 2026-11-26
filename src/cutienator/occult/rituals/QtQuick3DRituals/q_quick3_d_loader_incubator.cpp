//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dloader_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/private/qquick3dloader_p.h>
#include <QtQuick3D/private/qquick3dobject_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlcomponent_p.h>
#include <QtQml/private/qqmlincubator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/quick3d/qquick3dloader.cpp, line 20, as _ZN23QQuick3DLoaderIncubator13statusChangedEN13QQmlIncubator6StatusE
inline void QQuick3DLoaderIncubator::statusChanged(QQmlIncubator::Status status)
{
    m_loader->incubatorStateChanged(status);
}

//  from ../qtquick3d/src/quick3d/qquick3dloader.cpp, line 25, as _ZN23QQuick3DLoaderIncubator15setInitialStateEP7QObject
inline void QQuick3DLoaderIncubator::setInitialState(QObject *o)
{
    m_loader->setInitialState(o);
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuick3DLoaderIncubator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DLoaderIncubator : QQuick3DLoaderIncubator {
  using QQuick3DLoaderIncubator::statusChanged;
  using QQuick3DLoaderIncubator::setInitialState;
};

//  QQuick3DLoaderIncubator::QQuick3DLoaderIncubator(QQuick3DLoader *l,
//      IncubationMode mode)
extern "C" Q_DECL_EXPORT
QQuick3DLoaderIncubator *ritual_ZN23QQuick3DLoaderIncubatorC1EP14QQuick3DLoaderN13QQmlIncubator14IncubationModeE(
    QQuick3DLoader *l,
    QQmlIncubator::IncubationMode mode) {
  return new QQuick3DLoaderIncubator(l, mode);
}

//  void QQuick3DLoaderIncubator::statusChanged(Status a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DLoaderIncubator13statusChangedEN13QQmlIncubator6StatusE(
    QQuick3DLoaderIncubator *self,
    QQmlIncubator::Status a0) {
  self->statusChanged(a0);
}

//  void QQuick3DLoaderIncubator::setInitialState(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DLoaderIncubator15setInitialStateEP7QObject(
    QQuick3DLoaderIncubator *self,
    QObject *a0) {
  self->setInitialState(a0);
}

//  void QQuick3DLoaderIncubator::statusChanged(Status a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuick3DLoaderIncubator13statusChangedEN13QQmlIncubator6StatusE(
    QQuick3DLoaderIncubator *self,
    QQmlIncubator::Status a0) {
  static_cast<OwnQQuick3DLoaderIncubator *>(self)->OwnQQuick3DLoaderIncubator::statusChanged(
      a0);
}

//  void QQuick3DLoaderIncubator::setInitialState(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuick3DLoaderIncubator15setInitialStateEP7QObject(
    QQuick3DLoaderIncubator *self,
    QObject *a0) {
  static_cast<OwnQQuick3DLoaderIncubator *>(self)->OwnQQuick3DLoaderIncubator::setInitialState(
      a0);
}
