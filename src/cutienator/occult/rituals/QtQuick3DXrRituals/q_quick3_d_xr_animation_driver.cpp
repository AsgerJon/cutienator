//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxranimationdriver_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxranimationdriver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquick3dxranimationdriver_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxranimationdriver.cpp, line 10, as _ZN25QQuick3DXrAnimationDriverC1Ev
inline QQuick3DXrAnimationDriver::QQuick3DXrAnimationDriver()
{
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxranimationdriver.cpp, line 14, as _ZN25QQuick3DXrAnimationDriver7advanceEv
inline void QQuick3DXrAnimationDriver::advance()
{
    m_elapsed += m_step;
    advanceAnimation();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxranimationdriver.cpp, line 20, as _ZNK25QQuick3DXrAnimationDriver7elapsedEv
inline qint64 QQuick3DXrAnimationDriver::elapsed() const
{
    return m_elapsed;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxranimationdriver.cpp, line 25, as _ZN25QQuick3DXrAnimationDriver7setStepEi
inline void QQuick3DXrAnimationDriver::setStep(int stepSize)
{
    m_step = stepSize;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxranimationdriver.cpp, line 30, as _ZN25QQuick3DXrAnimationDriver5startEv
inline void QQuick3DXrAnimationDriver::start()
{
    m_elapsed = 0;
    QAnimationDriver::start();
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuick3DXrAnimationDriver may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DXrAnimationDriver : QQuick3DXrAnimationDriver {
  using QQuick3DXrAnimationDriver::start;
};

//  QQuick3DXrAnimationDriver::QQuick3DXrAnimationDriver()
extern "C" Q_DECL_EXPORT
QQuick3DXrAnimationDriver *ritual_ZN25QQuick3DXrAnimationDriverC1Ev() {
  return new QQuick3DXrAnimationDriver();
}

//  void QQuick3DXrAnimationDriver::advance()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DXrAnimationDriver7advanceEv(
    QQuick3DXrAnimationDriver *self) {
  self->advance();
}

//  qint64 QQuick3DXrAnimationDriver::elapsed() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK25QQuick3DXrAnimationDriver7elapsedEv(
    const QQuick3DXrAnimationDriver *self) {
  return self->elapsed();
}

//  void QQuick3DXrAnimationDriver::setStep(int stepSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DXrAnimationDriver7setStepEi(
    QQuick3DXrAnimationDriver *self,
    int stepSize) {
  self->setStep(stepSize);
}

//  void QQuick3DXrAnimationDriver::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DXrAnimationDriver5startEv(
    QQuick3DXrAnimationDriver *self) {
  self->start();
}

//  void QQuick3DXrAnimationDriver::advance()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuick3DXrAnimationDriver7advanceEv(
    QQuick3DXrAnimationDriver *self) {
  self->QQuick3DXrAnimationDriver::advance();
}

//  qint64 QQuick3DXrAnimationDriver::elapsed() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK25QQuick3DXrAnimationDriver7elapsedEv(
    const QQuick3DXrAnimationDriver *self) {
  return self->QQuick3DXrAnimationDriver::elapsed();
}

//  void QQuick3DXrAnimationDriver::start()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuick3DXrAnimationDriver5startEv(
    QQuick3DXrAnimationDriver *self) {
  static_cast<OwnQQuick3DXrAnimationDriver *>(self)->OwnQQuick3DXrAnimationDriver::start();
}
