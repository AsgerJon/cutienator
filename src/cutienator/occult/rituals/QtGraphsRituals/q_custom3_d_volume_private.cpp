//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qcustom3dvolume_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if !(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qcustom3dvolume.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qcustom3dvolume_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qfileinfo.h>
#include <QtGraphs/private/qcustom3ditem_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#include <QtGraphs/private/qcustom3dvolume_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#include <QtGui/qquaternion.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs3d/data/qcustom3ditem.cpp, line 679, as _ZN20QCustom3DItemPrivate14resetDirtyBitsEv
inline void QCustom3DItemPrivate::resetDirtyBits()
{
    m_dirtyBits.textureDirty = false;
    m_dirtyBits.meshDirty = false;
    m_dirtyBits.positionDirty = false;
    m_dirtyBits.scalingDirty = false;
    m_dirtyBits.rotationDirty = false;
    m_dirtyBits.visibleDirty = false;
    m_dirtyBits.shadowCastingDirty = false;
}

//  from ../qtgraphs/src/graphs3d/data/qcustom3dvolume.cpp, line 1418, as _ZN22QCustom3DVolumePrivateD1Ev
inline QCustom3DVolumePrivate::~QCustom3DVolumePrivate()
{
    delete m_textureData;
}

//  from ../qtgraphs/src/graphs3d/data/qcustom3dvolume.cpp, line 1423, as _ZN22QCustom3DVolumePrivate14resetDirtyBitsEv
inline void QCustom3DVolumePrivate::resetDirtyBits()
{
    QCustom3DItemPrivate::resetDirtyBits();

    m_dirtyBitsVolume.textureDimensionsDirty = false;
    m_dirtyBitsVolume.slicesDirty = false;
    m_dirtyBitsVolume.colorTableDirty = false;
    m_dirtyBitsVolume.textureDataDirty = false;
    m_dirtyBitsVolume.textureFormatDirty = false;
    m_dirtyBitsVolume.alphaDirty = false;
    m_dirtyBitsVolume.shaderDirty = false;
}

//  from ../qtgraphs/src/graphs3d/data/qcustom3dvolume.cpp, line 1523, as _ZN22QCustom3DVolumePrivate20multipliedAlphaValueEi
inline int QCustom3DVolumePrivate::multipliedAlphaValue(int alpha)
{
    int modifiedAlpha = alpha;
    if (!m_preserveOpacity || alpha != 255) {
        modifiedAlpha = int(m_alphaMultiplier * float(alpha));
        modifiedAlpha = qMin(modifiedAlpha, 255);
    }
    return modifiedAlpha;
}
//  -----------------------------------------------------------------------

//  QCustom3DVolume *QCustom3DVolumePrivate::q_func()
extern "C" Q_DECL_EXPORT
QCustom3DVolume *ritual_ZN22QCustom3DVolumePrivate6q_funcEv(
    QCustom3DVolumePrivate *self) {
  return self->q_func();
}

//  const QCustom3DVolume *QCustom3DVolumePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCustom3DVolume *ritual_ZNK22QCustom3DVolumePrivate6q_funcEv(
    const QCustom3DVolumePrivate *self) {
  return self->q_func();
}

//  QCustom3DVolumePrivate::~QCustom3DVolumePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCustom3DVolumePrivateD1Ev(QCustom3DVolumePrivate *self) {
  delete self;
}

//  void QCustom3DVolumePrivate::resetDirtyBits()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCustom3DVolumePrivate14resetDirtyBitsEv(
    QCustom3DVolumePrivate *self) {
  self->resetDirtyBits();
}

//  int QCustom3DVolumePrivate::multipliedAlphaValue(int alpha)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QCustom3DVolumePrivate20multipliedAlphaValueEi(
    QCustom3DVolumePrivate *self,
    int alpha) {
  return self->multipliedAlphaValue(alpha);
}

#endif  // !(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))
