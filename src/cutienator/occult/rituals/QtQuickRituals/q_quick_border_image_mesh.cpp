//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickshadereffectmesh_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickshadereffectmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickborderimage_p.h>
#include <QtQuick/private/qquickborderimage_p_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlfile.h>
#include <QtQml/qqmlengine.h>
#if QT_CONFIG(qml_network)
#include <QtNetwork/qnetworkreply.h>
#endif
#include <QtCore/qfile.h>
#include <QtCore/qmath.h>
#include <QtGui/qguiapplication.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQuick/private/qsgadaptationlayer_p.h>
#include <QtQuick/private/qquickshadereffectmesh_p.h>
#include <QtQuick/qsggeometry.h>
#include <QtQuick/private/qquickshadereffect_p.h>
#include <QtQuick/private/qquickscalegrid_p_p.h>
#include <QtQuick/private/qquickborderimage_p_p.h>
#include <QtQuick/private/qsgbasicinternalimagenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickborderimage.cpp, line 465, as _ZN24QQuickBorderImagePrivate14calculateRectsEPK15QQuickScaleGridRK5QSizeRK6QSizeFiidP6QRectFSA_SA_SA_
inline void QQuickBorderImagePrivate::calculateRects(const QQuickScaleGrid *border,
                                              const QSize &sourceSize,
                                              const QSizeF &targetSize,
                                              int horizontalTileMode,
                                              int verticalTileMode,
                                              qreal devicePixelRatio,
                                              QRectF *targetRect,
                                              QRectF *innerTargetRect,
                                              QRectF *innerSourceRect,
                                              QRectF *subSourceRect)
{
    *innerSourceRect = QRectF(0, 0, 1, 1);
    *targetRect = QRectF(0, 0, targetSize.width(), targetSize.height());
    *innerTargetRect = *targetRect;

    if (border) {
        qreal borderLeft = border->left() * devicePixelRatio;
        qreal borderRight = border->right() * devicePixelRatio;
        qreal borderTop = border->top() * devicePixelRatio;
        qreal borderBottom = border->bottom() * devicePixelRatio;
        if (borderLeft + borderRight > sourceSize.width() && borderLeft < sourceSize.width())
            borderRight = sourceSize.width() - borderLeft;
        if (borderTop + borderBottom > sourceSize.height() && borderTop < sourceSize.height())
            borderBottom = sourceSize.height() - borderTop;
        *innerSourceRect = QRectF(QPointF(borderLeft / qreal(sourceSize.width()),
                                          borderTop / qreal(sourceSize.height())),
                                  QPointF((sourceSize.width() - borderRight) / qreal(sourceSize.width()),
                                          (sourceSize.height() - borderBottom) / qreal(sourceSize.height()))),
        *innerTargetRect = QRectF(border->left(),
                                  border->top(),
                                  qMax<qreal>(0, targetSize.width() - (border->right() + border->left())),
                                  qMax<qreal>(0, targetSize.height() - (border->bottom() + border->top())));
    }

    qreal hTiles = 1;
    qreal vTiles = 1;
    const QSizeF innerTargetSize = innerTargetRect->size() * devicePixelRatio;
    if (innerSourceRect->width() <= 0)
        hTiles = 0;
    else if (horizontalTileMode != QQuickBorderImage::Stretch) {
        hTiles = innerTargetSize.width() / qreal(innerSourceRect->width() * sourceSize.width());
        if (horizontalTileMode == QQuickBorderImage::Round)
            hTiles = qCeil(hTiles);
    }
    if (innerSourceRect->height() <= 0)
        vTiles = 0;
    else if (verticalTileMode != QQuickBorderImage::Stretch) {
        vTiles = innerTargetSize.height() / qreal(innerSourceRect->height() * sourceSize.height());
        if (verticalTileMode == QQuickBorderImage::Round)
            vTiles = qCeil(vTiles);
    }

    *subSourceRect = QRectF(0, 0, hTiles, vTiles);
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffectmesh.cpp, line 289, as _ZN21QQuickBorderImageMesh18validateAttributesERK5QListI10QByteArrayEPi
inline bool QQuickBorderImageMesh::validateAttributes(const QList<QByteArray> &attributes, int *posIndex)
{
    Q_UNUSED(attributes);
    Q_UNUSED(posIndex);
    return true;
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffectmesh.cpp, line 296, as _ZN21QQuickBorderImageMesh14updateGeometryEP11QSGGeometryiiRK6QRectFS4_
inline QSGGeometry *QQuickBorderImageMesh::updateGeometry(QSGGeometry *geometry, int attrCount, int posIndex,
                                                   const QRectF &srcRect, const QRectF &rect)
{
    Q_UNUSED(attrCount);
    Q_UNUSED(posIndex);

    QRectF innerSourceRect;
    QRectF targetRect;
    QRectF innerTargetRect;
    QRectF subSourceRect;

    QQuickBorderImagePrivate::calculateRects(m_border, m_size, rect.size(), m_horizontalTileMode, m_verticalTileMode,
                                             1, &targetRect, &innerTargetRect, &innerSourceRect, &subSourceRect);

    QRectF sourceRect = srcRect;
    QRectF modifiedInnerSourceRect(sourceRect.x() + innerSourceRect.x() * sourceRect.width(),
                                   sourceRect.y() + innerSourceRect.y() * sourceRect.height(),
                                   innerSourceRect.width() * sourceRect.width(),
                                   innerSourceRect.height() * sourceRect.height());

    geometry = QSGBasicInternalImageNode::updateGeometry(targetRect, innerTargetRect, sourceRect,
                                                         modifiedInnerSourceRect, subSourceRect, geometry);

    return geometry;
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffectmesh.cpp, line 349, as _ZNK21QQuickBorderImageMesh6borderEv
inline QQuickScaleGrid *QQuickBorderImageMesh::border() const
{
    return m_border;
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffectmesh.cpp, line 360, as _ZNK21QQuickBorderImageMesh4sizeEv
inline QSize QQuickBorderImageMesh::size() const
{
    return m_size;
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffectmesh.cpp, line 389, as _ZNK21QQuickBorderImageMesh18horizontalTileModeEv
inline QQuickBorderImageMesh::TileMode QQuickBorderImageMesh::horizontalTileMode() const
{
    return m_horizontalTileMode;
}

//  from ../qtdeclarative/src/quick/items/qquickshadereffectmesh.cpp, line 403, as _ZNK21QQuickBorderImageMesh16verticalTileModeEv
inline QQuickBorderImageMesh::TileMode QQuickBorderImageMesh::verticalTileMode() const
{
    return m_verticalTileMode;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickBorderImageMesh::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickBorderImageMesh10metaObjectEv(
    const QQuickBorderImageMesh *self) {
  return self->metaObject();
}

//  bool QQuickBorderImageMesh::validateAttributes(const QList<QByteArray>
//      &attributes, int *posIndex)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickBorderImageMesh18validateAttributesERK5QListI10QByteArrayEPi(
    QQuickBorderImageMesh *self,
    const QList<QByteArray> *attributes,
    int *posIndex) {
  return self->validateAttributes(*attributes, posIndex);
}

//  QSGGeometry *QQuickBorderImageMesh::updateGeometry(QSGGeometry *geometry,
//      int attrCount, int posIndex, const QRectF &srcRect, const QRectF
//      &rect)
extern "C" Q_DECL_EXPORT
QSGGeometry *ritual_ZN21QQuickBorderImageMesh14updateGeometryEP11QSGGeometryiiRK6QRectFS4_(
    QQuickBorderImageMesh *self,
    QSGGeometry *geometry,
    int attrCount,
    int posIndex,
    const QRectF *srcRect,
    const QRectF *rect) {
  return self->updateGeometry(
      geometry,
      attrCount,
      posIndex,
      *srcRect,
      *rect);
}

//  QQuickScaleGrid *QQuickBorderImageMesh::border() const
extern "C" Q_DECL_EXPORT
QQuickScaleGrid *ritual_ZNK21QQuickBorderImageMesh6borderEv(
    const QQuickBorderImageMesh *self) {
  return self->border();
}

//  QSize QQuickBorderImageMesh::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK21QQuickBorderImageMesh4sizeEv(
    const QQuickBorderImageMesh *self) {
  return new QSize(self->size());
}

//  TileMode QQuickBorderImageMesh::horizontalTileMode() const
extern "C" Q_DECL_EXPORT
QQuickBorderImageMesh::TileMode ritual_ZNK21QQuickBorderImageMesh18horizontalTileModeEv(
    const QQuickBorderImageMesh *self) {
  return self->horizontalTileMode();
}

//  TileMode QQuickBorderImageMesh::verticalTileMode() const
extern "C" Q_DECL_EXPORT
QQuickBorderImageMesh::TileMode ritual_ZNK21QQuickBorderImageMesh16verticalTileModeEv(
    const QQuickBorderImageMesh *self) {
  return self->verticalTileMode();
}

//  QSGGeometry *QQuickBorderImageMesh::updateGeometry(QSGGeometry *geometry,
//      int attrCount, int posIndex, const QRectF &srcRect, const QRectF
//      &rect)
extern "C" Q_DECL_EXPORT
QSGGeometry *ritual_own_ZN21QQuickBorderImageMesh14updateGeometryEP11QSGGeometryiiRK6QRectFS4_(
    QQuickBorderImageMesh *self,
    QSGGeometry *geometry,
    int attrCount,
    int posIndex,
    const QRectF *srcRect,
    const QRectF *rect) {
  return self->QQuickBorderImageMesh::updateGeometry(
      geometry,
      attrCount,
      posIndex,
      *srcRect,
      *rect);
}

#endif  // QT_CONFIG(quick_shadereffect)
#endif  // QT_CONFIG(quick_shadereffect)
