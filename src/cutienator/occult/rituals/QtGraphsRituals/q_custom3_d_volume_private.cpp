//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qcustom3dvolume_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qcustom3dvolume.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qcustom3dvolume_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
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

//  from ../qtgraphs/src/graphs3d/data/qcustom3ditem.cpp, line 635, as _ZN20QCustom3DItemPrivateC2Ev
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

//  from ../qtgraphs/src/graphs3d/data/qcustom3ditem.cpp, line 666, as _ZN20QCustom3DItemPrivateD2Ev
inline QCustom3DItemPrivate::~QCustom3DItemPrivate() {}

//  from ../qtgraphs/src/graphs3d/data/qcustom3dvolume.cpp, line 1418, as _ZN22QCustom3DVolumePrivateD1Ev
inline QCustom3DVolumePrivate::~QCustom3DVolumePrivate()
{
    delete m_textureData;
}

//  from ../qtgraphs/src/graphs3d/data/qcustom3ditem.cpp, line 648, as _ZN20QCustom3DItemPrivateC2ERK7QString9QVector3DS3_RK11QQuaternion
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

//  from ../qtgraphs/src/graphs3d/data/qcustom3dvolume.cpp, line 1349, as _ZN22QCustom3DVolumePrivateC1Ev
inline QCustom3DVolumePrivate::QCustom3DVolumePrivate()
    : m_textureWidth(0)
    , m_textureHeight(0)
    , m_textureDepth(0)
    , m_sliceIndexX(-1)
    , m_sliceIndexY(-1)
    , m_sliceIndexZ(-1)
    , m_textureFormat(QImage::Format_ARGB32)
    , m_textureData(0)
    , m_alphaMultiplier(1.0f)
    , m_preserveOpacity(true)
    , m_useHighDefShader(true)
    , m_drawSlices(false)
    , m_drawSliceFrames(false)
    , m_sliceFrameColor(Qt::black)
    , m_sliceFrameWidths(QVector3D(0.01f, 0.01f, 0.01f))
    , m_sliceFrameGaps(QVector3D(0.01f, 0.01f, 0.01f))
    , m_sliceFrameThicknesses(QVector3D(0.01f, 0.01f, 0.01f))
{
    m_isVolumeItem = true;
    m_meshFile = QStringLiteral(":/defaultMeshes/barMeshFull");
}

//  from ../qtgraphs/src/graphs3d/data/qcustom3dvolume.cpp, line 1372, as _ZN22QCustom3DVolumePrivateC1E9QVector3DS0_RK11QQuaternioniiiP5QListIhEN6QImage6FormatERKS4_IjE
inline QCustom3DVolumePrivate::QCustom3DVolumePrivate(QVector3D position,
                                               QVector3D scaling,
                                               const QQuaternion &rotation,
                                               int textureWidth,
                                               int textureHeight,
                                               int textureDepth,
                                               QList<uchar> *textureData,
                                               QImage::Format textureFormat,
                                               const QList<QRgb> &colorTable)
    : QCustom3DItemPrivate(QStringLiteral(":/defaultMeshes/barMeshFull"),
                           position,
                           scaling,
                           rotation)
    , m_textureWidth(textureWidth)
    , m_textureHeight(textureHeight)
    , m_textureDepth(textureDepth)
    , m_sliceIndexX(-1)
    , m_sliceIndexY(-1)
    , m_sliceIndexZ(-1)
    , m_textureFormat(textureFormat)
    , m_colorTable(colorTable)
    , m_textureData(textureData)
    , m_alphaMultiplier(1.0f)
    , m_preserveOpacity(true)
    , m_useHighDefShader(true)
    , m_drawSlices(false)
    , m_drawSliceFrames(false)
    , m_sliceFrameColor(Qt::black)
    , m_sliceFrameWidths(QVector3D(0.01f, 0.01f, 0.01f))
    , m_sliceFrameGaps(QVector3D(0.01f, 0.01f, 0.01f))
    , m_sliceFrameThicknesses(QVector3D(0.01f, 0.01f, 0.01f))
{
    m_isVolumeItem = true;
    m_shadowCasting = false;

    if (m_textureWidth < 0)
        m_textureWidth = 0;
    if (m_textureHeight < 0)
        m_textureHeight = 0;
    if (m_textureDepth < 0)
        m_textureDepth = 0;

    if (m_textureFormat != QImage::Format_Indexed8)
        m_textureFormat = QImage::Format_ARGB32;
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

//  QCustom3DVolumePrivate::QCustom3DVolumePrivate()
extern "C" Q_DECL_EXPORT
QCustom3DVolumePrivate *ritual_ZN22QCustom3DVolumePrivateC1Ev() {
  return new QCustom3DVolumePrivate();
}

//  QCustom3DVolumePrivate::QCustom3DVolumePrivate(QVector3D position,
//      QVector3D scaling, const QQuaternion &rotation, int textureWidth, int
//      textureHeight, int textureDepth, QList<uchar> *textureData,
//      QImage::Format textureFormat, const QList<QRgb> &colorTable)
extern "C" Q_DECL_EXPORT
QCustom3DVolumePrivate *ritual_ZN22QCustom3DVolumePrivateC1E9QVector3DS0_RK11QQuaternioniiiP5QListIhEN6QImage6FormatERKS4_IjE(
    const QVector3D *position,
    const QVector3D *scaling,
    const QQuaternion *rotation,
    int textureWidth,
    int textureHeight,
    int textureDepth,
    QList<uchar> *textureData,
    QImage::Format textureFormat,
    const QList<QRgb> *colorTable) {
  return new QCustom3DVolumePrivate(
      *position,
      *scaling,
      *rotation,
      textureWidth,
      textureHeight,
      textureDepth,
      textureData,
      textureFormat,
      *colorTable);
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

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
