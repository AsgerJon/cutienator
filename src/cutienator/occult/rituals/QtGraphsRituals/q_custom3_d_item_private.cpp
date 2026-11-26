//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qcustom3ditem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qcustom3ditem.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qcustom3ditem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtGui/qimage.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qfileinfo.h>
#include <QtGraphs/private/qcustom3ditem_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs3d/data/qcustom3ditem.cpp, line 666, as _ZN20QCustom3DItemPrivateD1Ev
inline QCustom3DItemPrivate::~QCustom3DItemPrivate() {}

//  from ../qtgraphs/src/graphs3d/data/qcustom3ditem.cpp, line 635, as _ZN20QCustom3DItemPrivateC1Ev
inline QCustom3DItemPrivate::QCustom3DItemPrivate()
    : m_textureImage(QImage(1, 1, QImage::Format_ARGB32))
    , m_position(QVector3D(0.0f, 0.0f, 0.0f))
    , m_positionAbsolute(false)
    , m_scaling(QVector3D(0.1f, 0.1f, 0.1f))
    , m_scalingAbsolute(true)
    , m_rotation(QQuaternion())
    , m_visible(true)
    , m_shadowCasting(true)
    , m_isLabelItem(false)
    , m_isVolumeItem(false)
{}

//  from ../qtgraphs/src/graphs3d/data/qcustom3ditem.cpp, line 648, as _ZN20QCustom3DItemPrivateC1ERK7QString9QVector3DS3_RK11QQuaternion
inline QCustom3DItemPrivate::QCustom3DItemPrivate(const QString &meshFile,
                                           QVector3D position,
                                           QVector3D scaling,
                                           const QQuaternion &rotation)
    : m_textureImage(QImage(1, 1, QImage::Format_ARGB32))
    , m_meshFile(meshFile)
    , m_position(position)
    , m_positionAbsolute(false)
    , m_scaling(scaling)
    , m_scalingAbsolute(true)
    , m_rotation(rotation)
    , m_rotationAbsolute(true)
    , m_visible(true)
    , m_shadowCasting(true)
    , m_isLabelItem(false)
    , m_isVolumeItem(false)
{}

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

//  QCustom3DItemPrivate::QCustom3DItemPrivate()
extern "C" Q_DECL_EXPORT
QCustom3DItemPrivate *ritual_ZN20QCustom3DItemPrivateC1Ev() {
  return new QCustom3DItemPrivate();
}

//  QCustom3DItemPrivate::QCustom3DItemPrivate(const QString &meshFile,
//      QVector3D position, QVector3D scaling, const QQuaternion &rotation)
extern "C" Q_DECL_EXPORT
QCustom3DItemPrivate *ritual_ZN20QCustom3DItemPrivateC1ERK7QString9QVector3DS3_RK11QQuaternion(
    const QString *meshFile,
    const QVector3D *position,
    const QVector3D *scaling,
    const QQuaternion *rotation) {
  return new QCustom3DItemPrivate(*meshFile, *position, *scaling, *rotation);
}

//  QCustom3DItemPrivate::~QCustom3DItemPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCustom3DItemPrivateD1Ev(QCustom3DItemPrivate *self) {
  delete self;
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

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
