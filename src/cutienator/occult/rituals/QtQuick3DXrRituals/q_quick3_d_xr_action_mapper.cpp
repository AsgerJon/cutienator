//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxractionmapper_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxractionmapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>
#include <QtCore/QPointer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/private/qquick3dxractionmapper_p.h>
#include <QtQuick3DXr/private/qquick3dxrabstracthapticeffect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 15, as local:qquick3dxractionmapper.cpp:actionIntKey
static inline quint32 actionIntKey(const QQuick3DXrInputAction::Action id, const QtQuick3DXr::Controller controller)
{
    return quint16(id) | (quint32(controller) << 16);
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 20, as local:qquick3dxractionmapper.cpp:actionStringKey
static inline QString actionStringKey(const QString &name, const QtQuick3DXr::Controller controller)
{
    return QString::number(uint(controller)) + name;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 163, as _ZN21QQuick3DXrInputAction10setPressedEb
inline void QQuick3DXrInputAction::setPressed(bool newPressed)
{
    if (m_pressed == newPressed)
        return;
    m_pressed = newPressed;
    emit pressedChanged();
    if (newPressed)
        emit triggered();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 142, as _ZN21QQuick3DXrInputAction8setValueEf
inline void QQuick3DXrInputAction::setValue(float newValue)
{
    if (qFuzzyCompare(m_value, newValue))
        return;
    m_value = newValue;
    emit valueChanged();
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 353, as _ZNK21QQuick3DXrInputAction7enabledEv
inline bool QQuick3DXrInputAction::enabled() const
{
    return m_enabled;
}

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxractionmapper.cpp, line 432, as _ZNK24QQuick3DXrHapticFeedback10controllerEv
inline QQuick3DXrHapticFeedback::Controller QQuick3DXrHapticFeedback::controller() const
{
    return m_controller;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuick3DXrActionMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuick3DXrActionMapper10metaObjectEv(
    const QQuick3DXrActionMapper *self) {
  return self->metaObject();
}

//  void *QQuick3DXrActionMapper::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuick3DXrActionMapper11qt_metacastEPKc(
    QQuick3DXrActionMapper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DXrActionMapper::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuick3DXrActionMapper11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DXrActionMapper *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  a QList<QPointer<QQuick3DXrHapticFeedback>> a ritual of
//      QQuick3DXrActionMapper gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DXrActionMapper__QList_QPointer_QQuick3DXrHapticFeedback(
    QList<QPointer<QQuick3DXrHapticFeedback>> *self) {
  delete self;
}
