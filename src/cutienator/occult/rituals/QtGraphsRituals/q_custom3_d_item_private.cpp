//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qcustom3ditem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if !(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qcustom3ditem.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qcustom3ditem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qfileinfo.h>
#include "qcustom3ditem_p.h"
#include "qgraphs3dlogging_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs3d/data/qcustom3ditem.cpp, line 668, as _ZN20QCustom3DItemPrivate12textureImageEv
inline QImage QCustom3DItemPrivate::textureImage()
{
    return m_textureImage;
}

//  from ../qtgraphs/src/graphs3d/data/qcustom3ditem.cpp, line 673, as _ZN20QCustom3DItemPrivate17clearTextureImageEv
inline void QCustom3DItemPrivate::clearTextureImage()
{
    m_textureImage = QImage();
    m_textureFile.clear();
}

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
//  -----------------------------------------------------------------------

//  QCustom3DItem *QCustom3DItemPrivate::q_func()
extern "C" Q_DECL_EXPORT
QCustom3DItem *ritual_ZN20QCustom3DItemPrivate6q_funcEv(
    QCustom3DItemPrivate *self) {
  return self->q_func();
}

//  const QCustom3DItem *QCustom3DItemPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCustom3DItem *ritual_ZNK20QCustom3DItemPrivate6q_funcEv(
    const QCustom3DItemPrivate *self) {
  return self->q_func();
}

//  QImage QCustom3DItemPrivate::textureImage()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN20QCustom3DItemPrivate12textureImageEv(
    QCustom3DItemPrivate *self) {
  return new QImage(self->textureImage());
}

//  void QCustom3DItemPrivate::clearTextureImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCustom3DItemPrivate17clearTextureImageEv(
    QCustom3DItemPrivate *self) {
  self->clearTextureImage();
}

//  void QCustom3DItemPrivate::resetDirtyBits()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCustom3DItemPrivate14resetDirtyBitsEv(
    QCustom3DItemPrivate *self) {
  self->resetDirtyBits();
}

#endif  // !(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))
