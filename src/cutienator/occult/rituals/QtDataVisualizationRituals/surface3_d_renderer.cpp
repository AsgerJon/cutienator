//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/surface3drenderer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/surface3drenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDataVisualization/qabstract3dseries.h>
#include <QtDataVisualization/qsurface3dseries.h>
#include <QtCore/qpoint.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "abstract3drenderer_p.h"
#include "texturehelper_p.h"
#include "q3dcamera_p.h"
#include "q3dtheme_p.h"
#include "qvalue3daxisformatter_p.h"
#include "shaderhelper_p.h"
#include "qcustom3ditem_p.h"
#include "qcustom3dlabel_p.h"
#include "qcustom3dvolume_p.h"
#include "scatter3drenderer_p.h"
#include <QtCore/qmath.h>
#include <QtGui/QOffscreenSurface>
#include <QtCore/QThread>
#include "shaderhelper_p.h"
#include <QtOpenGL/QOpenGLShader>
#include "texturehelper_p.h"
#include "utils_p.h"
#include <QtGui/QImage>
#include <QtGui/QPainter>
#include <QtCore/QTime>
#include "axisrendercache_p.h"
#include <QtGui/QFontMetrics>
#include "customrenderitem_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 518, as _ZN18Abstract3DRenderer11updatePolarEb
inline void Abstract3DRenderer::updatePolar(bool enable)
{
    m_polarGraph = enable;
    for (auto cache: m_renderCacheList)
        cache->setDataDirty(true);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 336, as _ZN18Abstract3DRenderer11updateThemeEP8Q3DTheme
inline void Abstract3DRenderer::updateTheme(Q3DTheme *theme)
{
    // Synchronize the controller theme with renderer
    bool updateDrawer = theme->d_ptr->sync(*m_cachedTheme->d_ptr);

    if (updateDrawer)
        m_drawer->setTheme(m_cachedTheme);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 542, as _ZN18Abstract3DRenderer12handleResizeEv
inline void Abstract3DRenderer::handleResize()
{
    if (m_primarySubViewport.width() == 0 || m_primarySubViewport.height() == 0)
        return;

    // Recalculate zoom
    calculateZoomLevel();

    // Re-init selection buffer
    initSelectionBuffer();

    // Re-init depth buffer
    updateDepthBuffer();

    initCursorPositionBuffer();
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 1129, as _ZN18Abstract3DRenderer13addCustomItemEP13QCustom3DItem
inline CustomRenderItem *Abstract3DRenderer::addCustomItem(QCustom3DItem *item)
{
    CustomRenderItem *newItem = new CustomRenderItem();
    newItem->setRenderer(this);
    newItem->setItemPointer(item); // Store pointer for render item updates
    if (!newItem->setMesh(item->meshFile())) {
        delete newItem;
        return nullptr;
    }
    newItem->setOrigPosition(item->position());
    newItem->setOrigScaling(item->scaling());
    newItem->setScalingAbsolute(item->isScalingAbsolute());
    newItem->setPositionAbsolute(item->isPositionAbsolute());
    QImage textureImage = item->d_ptr->textureImage();
    bool facingCamera = false;
    GLuint texture = 0;
    if (item->d_ptr->m_isLabelItem) {
        QCustom3DLabel *labelItem = static_cast<QCustom3DLabel *>(item);
        newItem->setLabelItem(true);
        float pointSize = labelItem->font().pointSizeF();
        // Check do we have custom visuals or need to use theme
        if (!labelItem->dptr()->m_customVisuals) {
            // Recreate texture using theme
            labelItem->dptr()->createTextureImage(m_cachedTheme->labelBackgroundColor(),
                                                  m_cachedTheme->labelTextColor(),
                                                  m_cachedTheme->isLabelBackgroundEnabled(),
                                                  m_cachedTheme->isLabelBorderEnabled());
            pointSize = m_cachedTheme->font().pointSizeF();
            textureImage = item->d_ptr->textureImage();
        }
        // Calculate scaling based on text (texture size), font size and asked scaling
        float scaledFontSize = (0.05f + pointSize / 500.0f) / float(textureImage.height());
        QVector3D scaling = newItem->origScaling();
        scaling.setX(scaling.x() * textureImage.width() * scaledFontSize);
        scaling.setY(scaling.y() * textureImage.height() * scaledFontSize);
        newItem->setOrigScaling(scaling);
        // Check if facing camera
        facingCamera = labelItem->isFacingCamera();
    } else if (item->d_ptr->m_isVolumeItem && !m_isOpenGLES) {
        QCustom3DVolume *volumeItem = static_cast<QCustom3DVolume *>(item);
        newItem->setTextureWidth(volumeItem->textureWidth());
        newItem->setTextureHeight(volumeItem->textureHeight());
        newItem->setTextureDepth(volumeItem->textureDepth());
        if (volumeItem->textureFormat() == QImage::Format_Indexed8)
            newItem->setColorTable(volumeItem->colorTable());
        newItem->setTextureFormat(volumeItem->textureFormat());
        newItem->setVolume(true);
        newItem->setBlendNeeded(true);
        texture = m_textureHelper->create3DTexture(volumeItem->textureData(),
                                                   volumeItem->textureWidth(),
                                                   volumeItem->textureHeight(),
                                                   volumeItem->textureDepth(),
                                                   volumeItem->textureFormat());
        newItem->setSliceIndexX(volumeItem->sliceIndexX());
        newItem->setSliceIndexY(volumeItem->sliceIndexY());
        newItem->setSliceIndexZ(volumeItem->sliceIndexZ());
        newItem->setAlphaMultiplier(volumeItem->alphaMultiplier());
        newItem->setPreserveOpacity(volumeItem->preserveOpacity());
        newItem->setUseHighDefShader(volumeItem->useHighDefShader());

        newItem->setDrawSlices(volumeItem->drawSlices());
        newItem->setDrawSliceFrames(volumeItem->drawSliceFrames());
        newItem->setSliceFrameColor(volumeItem->sliceFrameColor());
        newItem->setSliceFrameWidths(volumeItem->sliceFrameWidths());
        newItem->setSliceFrameGaps(volumeItem->sliceFrameGaps());
        newItem->setSliceFrameThicknesses(volumeItem->sliceFrameThicknesses());
    }
    recalculateCustomItemScalingAndPos(newItem);
    newItem->setRotation(item->rotation());

    // In OpenGL ES we simply draw volumes as regular custom item placeholders.
    if (!item->d_ptr->m_isVolumeItem || m_isOpenGLES)
    {
        newItem->setBlendNeeded(textureImage.hasAlphaChannel());
        texture = m_textureHelper->create2DTexture(textureImage, true, true, true);
    }
    newItem->setTexture(texture);
    item->d_ptr->clearTextureImage();
    newItem->setVisible(item->isVisible());
    newItem->setShadowCasting(item->isShadowCasting());
    newItem->setFacingCamera(facingCamera);
    m_customRenderCache.insert(item, newItem);
    return newItem;
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 571, as _ZN18Abstract3DRenderer14updateAxisTypeEN15QAbstract3DAxis15AxisOrientationENS0_8AxisTypeE
inline void Abstract3DRenderer::updateAxisType(QAbstract3DAxis::AxisOrientation orientation,
                                        QAbstract3DAxis::AxisType type)
{
    axisCacheForOrientation(orientation).setType(type);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 677, as _ZN18Abstract3DRenderer15fixMeshFileNameER7QStringN17QAbstract3DSeries4MeshE
inline void Abstract3DRenderer::fixMeshFileName(QString &fileName, QAbstract3DSeries::Mesh mesh)
{
    // Default implementation does nothing.
    Q_UNUSED(fileName);
    Q_UNUSED(mesh);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 589, as _ZN18Abstract3DRenderer15updateAxisRangeEN15QAbstract3DAxis15AxisOrientationEff
inline void Abstract3DRenderer::updateAxisRange(QAbstract3DAxis::AxisOrientation orientation,
                                         float min, float max)
{
    AxisRenderCache &cache = axisCacheForOrientation(orientation);
    cache.setMin(min);
    cache.setMax(max);

    for (auto cache: m_renderCacheList)
        cache->setDataDirty(true);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 577, as _ZN18Abstract3DRenderer15updateAxisTitleEN15QAbstract3DAxis15AxisOrientationERK7QString
inline void Abstract3DRenderer::updateAxisTitle(QAbstract3DAxis::AxisOrientation orientation,
                                         const QString &title)
{
    axisCacheForOrientation(orientation).setTitle(title);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 306, as _ZN18Abstract3DRenderer16initLabelShadersERK7QStringS2_
inline void Abstract3DRenderer::initLabelShaders(const QString &vertexShader, const QString &fragmentShader)
{
    delete m_labelShader;
    m_labelShader = new ShaderHelper(this, vertexShader, fragmentShader);
    m_labelShader->initialize();
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 713, as _ZN18Abstract3DRenderer16updateCustomDataERK5QListIP13QCustom3DItemE
inline void Abstract3DRenderer::updateCustomData(const QList<QCustom3DItem *> &customItems)
{
    if (customItems.isEmpty() && m_customRenderCache.isEmpty())
        return;

    for (auto item: m_customRenderCache)
        item->setValid(false);

    int itemCount = customItems.size();
    // Check custom item list for items that are not yet in render item cache
    for (int i = 0; i < itemCount; i++) {
        QCustom3DItem *item = customItems.at(i);
        CustomRenderItem *renderItem = m_customRenderCache.value(item);
        if (!renderItem)
            renderItem = addCustomItem(item);
        if (renderItem) {
            renderItem->setValid(true);
            renderItem->setIndex(i); // always update index, as it must match the custom item index
        }
    }

    // Check render item cache and remove items that are not in customItems list anymore
    for (auto renderItem: m_customRenderCache) {
        if (!renderItem->isValid()) {
            m_customRenderCache.remove(renderItem->itemPointer());
            GLuint texture = renderItem->texture();
            m_textureHelper->deleteTexture(&texture);
            delete renderItem;
        }
    }

    m_customItemDrawOrder.clear();
    m_customItemDrawOrder = QList<QCustom3DItem *>(customItems);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 1282, as _ZN18Abstract3DRenderer16updateCustomItemEP16CustomRenderItem
inline void Abstract3DRenderer::updateCustomItem(CustomRenderItem *renderItem)
{
    QCustom3DItem *item = renderItem->itemPointer();
    if (item->d_ptr->m_dirtyBits.meshDirty) {
        renderItem->setMesh(item->meshFile());
        item->d_ptr->m_dirtyBits.meshDirty = false;
    }
    if (item->d_ptr->m_dirtyBits.positionDirty) {
        renderItem->setOrigPosition(item->position());
        renderItem->setPositionAbsolute(item->isPositionAbsolute());
        if (!item->d_ptr->m_dirtyBits.scalingDirty)
            recalculateCustomItemScalingAndPos(renderItem);
        item->d_ptr->m_dirtyBits.positionDirty = false;
    }
    if (item->d_ptr->m_dirtyBits.scalingDirty) {
        QVector3D scaling = item->scaling();
        renderItem->setOrigScaling(scaling);
        renderItem->setScalingAbsolute(item->isScalingAbsolute());
        // In case we have label item, we need to recreate texture for scaling adjustment
        if (item->d_ptr->m_isLabelItem) {
            QCustom3DLabel *labelItem = static_cast<QCustom3DLabel *>(item);
            float pointSize = labelItem->font().pointSizeF();
            // Check do we have custom visuals or need to use theme
            if (labelItem->dptr()->m_customVisuals) {
                // Recreate texture
                labelItem->dptr()->createTextureImage();
            } else {
                // Recreate texture using theme
                labelItem->dptr()->createTextureImage(m_cachedTheme->labelBackgroundColor(),
                                                      m_cachedTheme->labelTextColor(),
                                                      m_cachedTheme->isLabelBackgroundEnabled(),
                                                      m_cachedTheme->isLabelBorderEnabled());
                pointSize = m_cachedTheme->font().pointSizeF();
            }
            QImage textureImage = item->d_ptr->textureImage();
            // Calculate scaling based on text (texture size), font size and asked scaling
            float scaledFontSize = (0.05f + pointSize / 500.0f) / float(textureImage.height());
            scaling.setX(scaling.x() * textureImage.width() * scaledFontSize);
            scaling.setY(scaling.y() * textureImage.height() * scaledFontSize);
            item->d_ptr->clearTextureImage();
            renderItem->setOrigScaling(scaling);
        }
        recalculateCustomItemScalingAndPos(renderItem);
        item->d_ptr->m_dirtyBits.scalingDirty = false;
    }
    if (item->d_ptr->m_dirtyBits.rotationDirty) {
        renderItem->setRotation(item->rotation());
        item->d_ptr->m_dirtyBits.rotationDirty = false;
    }
    if (item->d_ptr->m_dirtyBits.textureDirty) {
        QImage textureImage = item->d_ptr->textureImage();
        if (item->d_ptr->m_isLabelItem) {
            QCustom3DLabel *labelItem = static_cast<QCustom3DLabel *>(item);
            // Check do we have custom visuals or need to use theme
            if (!labelItem->dptr()->m_customVisuals) {
                // Recreate texture using theme
                labelItem->dptr()->createTextureImage(m_cachedTheme->labelBackgroundColor(),
                                                      m_cachedTheme->labelTextColor(),
                                                      m_cachedTheme->isLabelBackgroundEnabled(),
                                                      m_cachedTheme->isLabelBorderEnabled());
                textureImage = item->d_ptr->textureImage();
            }
        } else if (!item->d_ptr->m_isVolumeItem || m_isOpenGLES) {
            renderItem->setBlendNeeded(textureImage.hasAlphaChannel());
            GLuint oldTexture = renderItem->texture();
            m_textureHelper->deleteTexture(&oldTexture);
            GLuint texture = m_textureHelper->create2DTexture(textureImage, true, true, true);
            renderItem->setTexture(texture);
        }
        item->d_ptr->clearTextureImage();
        item->d_ptr->m_dirtyBits.textureDirty = false;
    }
    if (item->d_ptr->m_dirtyBits.visibleDirty) {
        renderItem->setVisible(item->isVisible());
        item->d_ptr->m_dirtyBits.visibleDirty = false;
    }
    if (item->d_ptr->m_dirtyBits.shadowCastingDirty) {
        renderItem->setShadowCasting(item->isShadowCasting());
        item->d_ptr->m_dirtyBits.shadowCastingDirty = false;
    }
    if (item->d_ptr->m_isLabelItem) {
        QCustom3DLabel *labelItem = static_cast<QCustom3DLabel *>(item);
        if (labelItem->dptr()->m_facingCameraDirty) {
            renderItem->setFacingCamera(labelItem->isFacingCamera());
            labelItem->dptr()->m_facingCameraDirty = false;
        }
    } else if (item->d_ptr->m_isVolumeItem && !m_isOpenGLES) {
        QCustom3DVolume *volumeItem = static_cast<QCustom3DVolume *>(item);
        if (volumeItem->dptr()->m_dirtyBitsVolume.colorTableDirty) {
            renderItem->setColorTable(volumeItem->colorTable());
            volumeItem->dptr()->m_dirtyBitsVolume.colorTableDirty = false;
        }
        if (volumeItem->dptr()->m_dirtyBitsVolume.textureDimensionsDirty
                || volumeItem->dptr()->m_dirtyBitsVolume.textureDataDirty
                || volumeItem->dptr()->m_dirtyBitsVolume.textureFormatDirty) {
            GLuint oldTexture = renderItem->texture();
            m_textureHelper->deleteTexture(&oldTexture);
            GLuint texture = m_textureHelper->create3DTexture(volumeItem->textureData(),
                                                              volumeItem->textureWidth(),
                                                              volumeItem->textureHeight(),
                                                              volumeItem->textureDepth(),
                                                              volumeItem->textureFormat());
            renderItem->setTexture(texture);
            renderItem->setTextureWidth(volumeItem->textureWidth());
            renderItem->setTextureHeight(volumeItem->textureHeight());
            renderItem->setTextureDepth(volumeItem->textureDepth());
            renderItem->setTextureFormat(volumeItem->textureFormat());
            volumeItem->dptr()->m_dirtyBitsVolume.textureDimensionsDirty = false;
            volumeItem->dptr()->m_dirtyBitsVolume.textureDataDirty = false;
            volumeItem->dptr()->m_dirtyBitsVolume.textureFormatDirty = false;
        }
        if (volumeItem->dptr()->m_dirtyBitsVolume.slicesDirty) {
            renderItem->setDrawSlices(volumeItem->drawSlices());
            renderItem->setDrawSliceFrames(volumeItem->drawSliceFrames());
            renderItem->setSliceFrameColor(volumeItem->sliceFrameColor());
            renderItem->setSliceFrameWidths(volumeItem->sliceFrameWidths());
            renderItem->setSliceFrameGaps(volumeItem->sliceFrameGaps());
            renderItem->setSliceFrameThicknesses(volumeItem->sliceFrameThicknesses());
            renderItem->setSliceIndexX(volumeItem->sliceIndexX());
            renderItem->setSliceIndexY(volumeItem->sliceIndexY());
            renderItem->setSliceIndexZ(volumeItem->sliceIndexZ());
            volumeItem->dptr()->m_dirtyBitsVolume.slicesDirty = false;
        }
        if (volumeItem->dptr()->m_dirtyBitsVolume.alphaDirty) {
            renderItem->setAlphaMultiplier(volumeItem->alphaMultiplier());
            renderItem->setPreserveOpacity(volumeItem->preserveOpacity());
            volumeItem->dptr()->m_dirtyBitsVolume.alphaDirty = false;
        }
        if (volumeItem->dptr()->m_dirtyBitsVolume.shaderDirty) {
            renderItem->setUseHighDefShader(volumeItem->useHighDefShader());
            volumeItem->dptr()->m_dirtyBitsVolume.shaderDirty = false;
        }
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 504, as _ZN18Abstract3DRenderer17updateAspectRatioEf
inline void Abstract3DRenderer::updateAspectRatio(float ratio)
{
    m_graphAspectRatio = ratio;
    for (auto cache: m_renderCacheList)
        cache->setDataDirty(true);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 748, as _ZN18Abstract3DRenderer17updateCustomItemsEv
inline void Abstract3DRenderer::updateCustomItems()
{
    // Check all items
    for (auto item: m_customRenderCache)
        updateCustomItem(item);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 783, as _ZN18Abstract3DRenderer18lowerShadowQualityEv
inline void Abstract3DRenderer::lowerShadowQuality()
{
    QAbstract3DGraph::ShadowQuality newQuality = QAbstract3DGraph::ShadowQualityNone;

    switch (m_cachedShadowQuality) {
    case QAbstract3DGraph::ShadowQualityHigh:
        qWarning("Creating high quality shadows failed. Changing to medium quality.");
        newQuality = QAbstract3DGraph::ShadowQualityMedium;
        break;
    case QAbstract3DGraph::ShadowQualityMedium:
        qWarning("Creating medium quality shadows failed. Changing to low quality.");
        newQuality = QAbstract3DGraph::ShadowQualityLow;
        break;
    case QAbstract3DGraph::ShadowQualityLow:
        qWarning("Creating low quality shadows failed. Switching shadows off.");
        newQuality = QAbstract3DGraph::ShadowQualityNone;
        break;
    case QAbstract3DGraph::ShadowQualitySoftHigh:
        qWarning("Creating soft high quality shadows failed. Changing to soft medium quality.");
        newQuality = QAbstract3DGraph::ShadowQualitySoftMedium;
        break;
    case QAbstract3DGraph::ShadowQualitySoftMedium:
        qWarning("Creating soft medium quality shadows failed. Changing to soft low quality.");
        newQuality = QAbstract3DGraph::ShadowQualitySoftLow;
        break;
    case QAbstract3DGraph::ShadowQualitySoftLow:
        qWarning("Creating soft low quality shadows failed. Switching shadows off.");
        newQuality = QAbstract3DGraph::ShadowQualityNone;
        break;
    default:
        // You'll never get here
        break;
    }

    emit requestShadowQuality(newQuality);
    updateShadowQuality(newQuality);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 668, as _ZN18Abstract3DRenderer18modifiedSeriesListERK5QListIP17QAbstract3DSeriesE
inline void Abstract3DRenderer::modifiedSeriesList(const QList<QAbstract3DSeries *> &seriesList)
{
    for (auto series: seriesList) {
        SeriesRenderCache *cache = m_renderCacheList.value(series, 0);
        if (cache)
            cache->setDataDirty(true);
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 620, as _ZN18Abstract3DRenderer18updateAxisReversedEN15QAbstract3DAxis15AxisOrientationEb
inline void Abstract3DRenderer::updateAxisReversed(QAbstract3DAxis::AxisOrientation orientation,
                                            bool enable)
{
    axisCacheForOrientation(orientation).setReversed(enable);
    for (auto cache: m_renderCacheList)
        cache->setDataDirty(true);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 253, as _ZN18Abstract3DRenderer19initGradientShadersERK7QStringS2_
inline void Abstract3DRenderer::initGradientShaders(const QString &vertexShader,
                                             const QString &fragmentShader)
{
    // Do nothing by default
    Q_UNUSED(vertexShader);
    Q_UNUSED(fragmentShader);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 628, as _ZN18Abstract3DRenderer19updateAxisFormatterEN15QAbstract3DAxis15AxisOrientationEP21QValue3DAxisFormatter
inline void Abstract3DRenderer::updateAxisFormatter(QAbstract3DAxis::AxisOrientation orientation,
                                             QValue3DAxisFormatter *formatter)
{
    AxisRenderCache &cache = axisCacheForOrientation(orientation);
    if (cache.ctrlFormatter() != formatter) {
        delete cache.formatter();
        cache.setFormatter(formatter->createNewInstance());
        cache.setCtrlFormatter(formatter);
    }
    formatter->d_ptr->populateCopy(*(cache.formatter()));
    cache.markPositionsDirty();

    for (auto cache: m_renderCacheList)
        cache->setDataDirty(true);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 660, as _ZN18Abstract3DRenderer20updateAxisTitleFixedEN15QAbstract3DAxis15AxisOrientationEb
inline void Abstract3DRenderer::updateAxisTitleFixed(QAbstract3DAxis::AxisOrientation orientation,
                                              bool fixed)
{
    AxisRenderCache &cache = axisCacheForOrientation(orientation);
    if (cache.isTitleFixed() != fixed)
        cache.setTitleFixed(fixed);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 248, as _ZN18Abstract3DRenderer20updateSelectionStateENS_14SelectionStateE
inline void Abstract3DRenderer::updateSelectionState(SelectionState state)
{
    m_selectionState = state;
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 273, as _ZN18Abstract3DRenderer21initCustomItemShadersERK7QStringS2_
inline void Abstract3DRenderer::initCustomItemShaders(const QString &vertexShader,
                                               const QString &fragmentShader)
{
    delete m_customItemShader;
    m_customItemShader = new ShaderHelper(this, vertexShader, fragmentShader);
    m_customItemShader->initialize();
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 614, as _ZN18Abstract3DRenderer21updateAxisLabelFormatEN15QAbstract3DAxis15AxisOrientationERK7QString
inline void Abstract3DRenderer::updateAxisLabelFormat(QAbstract3DAxis::AxisOrientation orientation,
                                               const QString &format)
{
    axisCacheForOrientation(orientation).setLabelFormat(format);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 600, as _ZN18Abstract3DRenderer22updateAxisSegmentCountEN15QAbstract3DAxis15AxisOrientationEi
inline void Abstract3DRenderer::updateAxisSegmentCount(QAbstract3DAxis::AxisOrientation orientation,
                                                int count)
{
    AxisRenderCache &cache = axisCacheForOrientation(orientation);
    cache.setSegmentCount(count);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 535, as _ZN18Abstract3DRenderer22updateOptimizationHintE6QFlagsIN16QAbstract3DGraph16OptimizationHintEE
inline void Abstract3DRenderer::updateOptimizationHint(QAbstract3DGraph::OptimizationHints hint)
{
    m_cachedOptimizationHint = hint;
    for (auto cache: m_renderCacheList)
        cache->setDataDirty(true);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 525, as _ZN18Abstract3DRenderer23updateRadialLabelOffsetEf
inline void Abstract3DRenderer::updateRadialLabelOffset(float offset)
{
    m_radialLabelOffset = offset;
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 322, as _ZN18Abstract3DRenderer24initCursorPositionBufferEv
inline void Abstract3DRenderer::initCursorPositionBuffer()
{
    m_textureHelper->deleteTexture(&m_cursorPositionTexture);
    m_textureHelper->glDeleteFramebuffers(1, &m_cursorPositionFrameBuffer);
    m_cursorPositionFrameBuffer = 0;

    if (m_primarySubViewport.size().isEmpty())
        return;

    m_cursorPositionTexture =
            m_textureHelper->createCursorPositionTexture(m_primarySubViewport.size(),
                                                         m_cursorPositionFrameBuffer);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 281, as _ZN18Abstract3DRenderer24initVolumeTextureShadersERK7QStringS2_S2_S2_S2_S2_
inline void Abstract3DRenderer::initVolumeTextureShaders(const QString &vertexShader,
                                                  const QString &fragmentShader,
                                                  const QString &fragmentLowDefShader,
                                                  const QString &sliceShader,
                                                  const QString &sliceFrameVertexShader,
                                                  const QString &sliceFrameShader)
{

    delete m_volumeTextureShader;
    m_volumeTextureShader = new ShaderHelper(this, vertexShader, fragmentShader);
    m_volumeTextureShader->initialize();

    delete m_volumeTextureLowDefShader;
    m_volumeTextureLowDefShader = new ShaderHelper(this, vertexShader, fragmentLowDefShader);
    m_volumeTextureLowDefShader->initialize();

    delete m_volumeTextureSliceShader;
    m_volumeTextureSliceShader = new ShaderHelper(this, vertexShader, sliceShader);
    m_volumeTextureSliceShader->initialize();

    delete m_volumeSliceFrameShader;
    m_volumeSliceFrameShader = new ShaderHelper(this, sliceFrameVertexShader, sliceFrameShader);
    m_volumeSliceFrameShader->initialize();
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 482, as _ZN18Abstract3DRenderer25handleShadowQualityChangeEv
inline void Abstract3DRenderer::handleShadowQualityChange()
{
    reInitShaders();

    if (m_cachedScene->activeLight()->isAutoPosition()
            || m_cachedShadowQuality > QAbstract3DGraph::ShadowQualityNone) {
        m_cachedScene->d_ptr->setLightPositionRelativeToCamera(defaultLightPos);
        emit needRender();
    }
    if (m_isOpenGLES && m_cachedShadowQuality != QAbstract3DGraph::ShadowQualityNone) {
        emit requestShadowQuality(QAbstract3DGraph::ShadowQualityNone);
        qWarning("Shadows are not yet supported for OpenGL ES2");
        m_cachedShadowQuality = QAbstract3DGraph::ShadowQualityNone;
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 313, as _ZN18Abstract3DRenderer25initCursorPositionShadersERK7QStringS2_
inline void Abstract3DRenderer::initCursorPositionShaders(const QString &vertexShader,
                                                   const QString &fragmentShader)
{
    // Init the shader
    delete m_cursorPositionShader;
    m_cursorPositionShader = new ShaderHelper(this, vertexShader, fragmentShader);
    m_cursorPositionShader->initialize();
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 607, as _ZN18Abstract3DRenderer25updateAxisSubSegmentCountEN15QAbstract3DAxis15AxisOrientationEi
inline void Abstract3DRenderer::updateAxisSubSegmentCount(QAbstract3DAxis::AxisOrientation orientation,
                                                   int count)
{
    AxisRenderCache &cache = axisCacheForOrientation(orientation);
    cache.setSubSegmentCount(count);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 1417, as _ZN18Abstract3DRenderer25updateCustomItemPositionsEv
inline void Abstract3DRenderer::updateCustomItemPositions()
{
    for (auto renderItem: m_customRenderCache)
        recalculateCustomItemScalingAndPos(renderItem);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 644, as _ZN18Abstract3DRenderer27updateAxisLabelAutoRotationEN15QAbstract3DAxis15AxisOrientationEf
inline void Abstract3DRenderer::updateAxisLabelAutoRotation(QAbstract3DAxis::AxisOrientation orientation,
                                                     float angle)
{
    AxisRenderCache &cache = axisCacheForOrientation(orientation);
    if (cache.labelAutoRotation() != angle)
        cache.setLabelAutoRotation(angle);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 511, as _ZN18Abstract3DRenderer27updateHorizontalAspectRatioEf
inline void Abstract3DRenderer::updateHorizontalAspectRatio(float ratio)
{
    m_graphHorizontalAspectRatio = ratio;
    for (auto cache: m_renderCacheList)
        cache->setDataDirty(true);
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 261, as _ZN18Abstract3DRenderer29initStaticSelectedItemShadersERK7QStringS2_S2_S2_
inline void Abstract3DRenderer::initStaticSelectedItemShaders(const QString &vertexShader,
                                                       const QString &fragmentShader,
                                                       const QString &gradientVertexShader,
                                                       const QString &gradientFragmentShader)
{
    // Do nothing by default
    Q_UNUSED(vertexShader);
    Q_UNUSED(fragmentShader);
    Q_UNUSED(gradientVertexShader);
    Q_UNUSED(gradientFragmentShader);
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 81, as _ZN12ShaderHelper10initializeEv
inline void ShaderHelper::initialize()
{
    if (m_program)
        delete m_program;
    m_program = new QOpenGLShaderProgram(m_caller);
    if (!m_program->addShaderFromSourceFile(QOpenGLShader::Vertex, m_vertexShaderFile))
        qFatal("Compiling Vertex shader failed");
    if (!m_program->addShaderFromSourceFile(QOpenGLShader::Fragment, m_fragmentShaderFile))
        qFatal("Compiling Fragment shader failed");

    if (!m_program->link()) {
        qWarning() << "Unable to link shader program:" <<
                      m_vertexShaderFile << m_fragmentShaderFile;
        return;
    }

    m_positionAttr = m_program->attributeLocation("vertexPosition_mdl");
    m_normalAttr = m_program->attributeLocation("vertexNormal_mdl");
    m_uvAttr = m_program->attributeLocation("vertexUV");

    m_mvpMatrixUniform = m_program->uniformLocation("MVP");
    m_viewMatrixUniform = m_program->uniformLocation("V");
    m_modelMatrixUniform = m_program->uniformLocation("M");
    m_invTransModelMatrixUniform = m_program->uniformLocation("itM");
    m_depthMatrixUniform = m_program->uniformLocation("depthMVP");
    m_lightPositionUniform = m_program->uniformLocation("lightPosition_wrld");
    m_lightStrengthUniform = m_program->uniformLocation("lightStrength");
    m_ambientStrengthUniform = m_program->uniformLocation("ambientStrength");
    m_shadowQualityUniform = m_program->uniformLocation("shadowQuality");
    m_colorUniform = m_program->uniformLocation("color_mdl");
    m_textureUniform = m_program->uniformLocation("textureSampler");
    m_shadowUniform = m_program->uniformLocation("shadowMap");
    m_gradientMinUniform = m_program->uniformLocation("gradMin");
    m_gradientHeightUniform = m_program->uniformLocation("gradHeight");
    m_lightColorUniform = m_program->uniformLocation("lightColor");
    m_volumeSliceIndicesUniform = m_program->uniformLocation("volumeSliceIndices");
    m_colorIndexUniform = m_program->uniformLocation("colorIndex");
    m_cameraPositionRelativeToModelUniform = m_program->uniformLocation("cameraPositionRelativeToModel");
    m_color8BitUniform = m_program->uniformLocation("color8Bit");
    m_textureDimensionsUniform = m_program->uniformLocation("textureDimensions");
    m_sampleCountUniform = m_program->uniformLocation("sampleCount");
    m_alphaMultiplierUniform = m_program->uniformLocation("alphaMultiplier");
    m_preserveOpacityUniform = m_program->uniformLocation("preserveOpacity");
    m_minBoundsUniform = m_program->uniformLocation("minBounds");
    m_maxBoundsUniform = m_program->uniformLocation("maxBounds");
    m_sliceFrameWidthUniform = m_program->uniformLocation("sliceFrameWidth");
    m_initialized = true;
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 18, as _ZN12ShaderHelperC1EP7QObjectRK7QStringS4_S4_S4_
inline ShaderHelper::ShaderHelper(QObject *parent,
                           const QString &vertexShader,
                           const QString &fragmentShader,
                           const QString &texture,
                           const QString &depthTexture)
    : m_caller(parent),
      m_program(0),
      m_vertexShaderFile(vertexShader),
      m_fragmentShaderFile(fragmentShader),
      m_textureFile(texture),
      m_depthTextureFile(depthTexture),
      m_positionAttr(0),
      m_uvAttr(0),
      m_normalAttr(0),
      m_colorUniform(0),
      m_viewMatrixUniform(0),
      m_modelMatrixUniform(0),
      m_invTransModelMatrixUniform(0),
      m_depthMatrixUniform(0),
      m_mvpMatrixUniform(0),
      m_lightPositionUniform(0),
      m_lightStrengthUniform(0),
      m_ambientStrengthUniform(0),
      m_shadowQualityUniform(0),
      m_textureUniform(0),
      m_shadowUniform(0),
      m_gradientMinUniform(0),
      m_gradientHeightUniform(0),
      m_lightColorUniform(0),
      m_volumeSliceIndicesUniform(0),
      m_colorIndexUniform(0),
      m_cameraPositionRelativeToModelUniform(0),
      m_color8BitUniform(0),
      m_textureDimensionsUniform(0),
      m_sampleCountUniform(0),
      m_alphaMultiplierUniform(0),
      m_preserveOpacityUniform(0),
      m_minBoundsUniform(0),
      m_maxBoundsUniform(0),
      m_sliceFrameWidthUniform(0),
      m_initialized(false)
{
}

//  from ../qtdatavis3d/src/datavisualization/utils/shaderhelper.cpp, line 62, as _ZN12ShaderHelperD1Ev
inline ShaderHelper::~ShaderHelper()
{
    delete m_program;
}

//  from ../qtdatavis3d/src/datavisualization/utils/texturehelper.cpp, line 325, as _ZN13TextureHelper13deleteTextureEPj
inline void TextureHelper::deleteTexture(GLuint *texture)
{
    if (texture && *texture) {
        if (QOpenGLContext::currentContext())
            glDeleteTextures(1, texture);
        *texture = 0;
    }
}

//  from ../qtdatavis3d/src/datavisualization/utils/texturehelper.cpp, line 44, as _ZN13TextureHelper15create2DTextureERK6QImagebbbb
inline GLuint TextureHelper::create2DTexture(const QImage &image, bool useTrilinearFiltering,
                                      bool convert, bool smoothScale, bool clampY)
{
    if (image.isNull())
        return 0;

    QImage texImage = image;

    if (Utils::isOpenGLES()) {
        GLuint imageWidth = Utils::getNearestPowerOfTwo(image.width());
        GLuint imageHeight = Utils::getNearestPowerOfTwo(image.height());
        if (smoothScale) {
            texImage = image.scaled(imageWidth, imageHeight, Qt::IgnoreAspectRatio,
                                    Qt::SmoothTransformation);
        } else {
            texImage = image.scaled(imageWidth, imageHeight, Qt::IgnoreAspectRatio);
        }
    }

    GLuint textureId;
    glGenTextures(1, &textureId);
    glBindTexture(GL_TEXTURE_2D, textureId);
    if (convert)
        texImage = convertToGLFormat(texImage);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, texImage.width(), texImage.height(),
                 0, GL_RGBA, GL_UNSIGNED_BYTE, texImage.bits());
    if (smoothScale)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    else
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    if (useTrilinearFiltering) {
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
        glGenerateMipmap(GL_TEXTURE_2D);
    } else {
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    }
    if (clampY)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
    glBindTexture(GL_TEXTURE_2D, 0);

    return textureId;
}

//  from ../qtdatavis3d/src/datavisualization/utils/texturehelper.cpp, line 87, as _ZN13TextureHelper15create3DTextureEPK5QListIhEiiiN6QImage6FormatE
inline GLuint TextureHelper::create3DTexture(const QList<uchar> *data, int width, int height, int depth,
                                      QImage::Format dataFormat)
{
    if (Utils::isOpenGLES() || !width || !height || !depth)
        return 0;

    GLuint textureId = 0;
#if QT_CONFIG(opengles2)
    Q_UNUSED(dataFormat);
    Q_UNUSED(data);
#else
    glEnable(GL_TEXTURE_3D);

    glGenTextures(1, &textureId);
    glBindTexture(GL_TEXTURE_3D, textureId);
    glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_WRAP_R, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);

    GLenum status = glGetError();
    // glGetError docs advise to call glGetError in loop to clear all error flags
    while (status)
        status = glGetError();

    GLint internalFormat = 4;
    GLint format = GL_BGRA;
    if (dataFormat == QImage::Format_Indexed8) {
        internalFormat = 1;
        format = GL_RED;
        // Align width to 32bits
        width = width + width % 4;
    }
    m_openGlFunctions_2_1->glTexImage3D(GL_TEXTURE_3D, 0, internalFormat, width, height, depth, 0,
                                        format, GL_UNSIGNED_BYTE, data->constData());
    status = glGetError();
    if (status)
        qWarning() << __FUNCTION__ << "3D texture creation failed:" << status;

    glBindTexture(GL_TEXTURE_3D, 0);
    glDisable(GL_TEXTURE_3D);
#endif
    return textureId;
}

//  from ../qtdatavis3d/src/datavisualization/utils/texturehelper.cpp, line 217, as _ZN13TextureHelper27createCursorPositionTextureERK5QSizeRj
inline GLuint TextureHelper::createCursorPositionTexture(const QSize &size, GLuint &frameBuffer)
{
    GLuint textureid;
    glGenTextures(1, &textureid);
    glBindTexture(GL_TEXTURE_2D, textureid);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, size.width(), size.height(), 0, GL_RGBA,
                 GL_UNSIGNED_BYTE, NULL);
    glBindTexture(GL_TEXTURE_2D, 0);

    glGenFramebuffers(1, &frameBuffer);
    glBindFramebuffer(GL_FRAMEBUFFER, frameBuffer);
    glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D,
                           textureid, 0);

    GLenum status = glCheckFramebufferStatus(GL_FRAMEBUFFER);
    if (status != GL_FRAMEBUFFER_COMPLETE) {
        qCritical() << "Cursor position mapper frame buffer creation failed:" << status;
        glDeleteTextures(1, &textureid);
        textureid = 0;
    }
    glBindFramebuffer(GL_FRAMEBUFFER, 0);

    return textureid;
}

//  from ../qtdatavis3d/src/datavisualization/engine/axisrendercache.cpp, line 49, as _ZN15AxisRenderCache7setTypeEN15QAbstract3DAxis8AxisTypeE
inline void AxisRenderCache::setType(QAbstract3DAxis::AxisType type)
{
    m_type = type;

    // If type is set, it means completely new axis instance, so clear all old data
    m_labels.clear();
    m_title.clear();
    m_min = 0.0f;
    m_max = 10.0f;
    m_segmentCount = 5;
    m_subSegmentCount = 1;
    m_labelFormat.clear();

    m_titleItem.clear();
    for (auto label: m_labelItems)
        delete label;
    m_labelItems.clear();
}

//  from ../qtdatavis3d/src/datavisualization/engine/axisrendercache.cpp, line 68, as _ZN15AxisRenderCache8setTitleERK7QString
inline void AxisRenderCache::setTitle(const QString &title)
{
    if (m_title != title) {
        m_title = title;
        // Generate axis label texture
        if (m_drawer)
            m_drawer->generateLabelItem(m_titleItem, title);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/customrenderitem.cpp, line 51, as _ZN16CustomRenderItem13setColorTableERK5QListIjE
inline void CustomRenderItem::setColorTable(const QList<QRgb> &colors)
{
    m_colorTable.resize(256);
    for (int i = 0; i < 256; i++) {
        if (i < colors.size()) {
            const QRgb &rgb = colors.at(i);
            m_colorTable[i] = QVector4D(float(qRed(rgb)) / 255.0f,
                                        float(qGreen(rgb)) / 255.0f,
                                        float(qBlue(rgb)) / 255.0f,
                                        float(qAlpha(rgb)) / 255.0f);
        } else {
            m_colorTable[i] = QVector4D(0.0f, 0.0f, 0.0f, 0.0f);
        }
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/customrenderitem.cpp, line 85, as _ZN16CustomRenderItem18setSliceFrameColorERK6QColor
inline void CustomRenderItem::setSliceFrameColor(const QColor &color)
{
    const QRgb &rgb = color.rgba();
    m_sliceFrameColor = QVector4D(float(qRed(rgb)) / 255.0f,
                                  float(qGreen(rgb)) / 255.0f,
                                  float(qBlue(rgb)) / 255.0f,
                                  float(1.0f)); // Alpha not supported for frames
}

//  from ../qtdatavis3d/src/datavisualization/data/customrenderitem.cpp, line 45, as _ZN16CustomRenderItem7setMeshERK7QString
inline bool CustomRenderItem::setMesh(const QString &meshFile)
{
    ObjectHelper::resetObjectHelper(m_renderer, m_object, meshFile);
    return m_object ? true : false;
}

//  from ../qtdatavis3d/src/datavisualization/data/customrenderitem.cpp, line 8, as _ZN16CustomRenderItemC1Ev
inline CustomRenderItem::CustomRenderItem()
    : AbstractRenderItem(),
      m_texture(0),
      m_positionAbsolute(false),
      m_scalingAbsolute(true),
      m_object(0),
      m_needBlend(true),
      m_visible(true),
      m_valid(true),
      m_index(0),
      m_shadowCasting(false),
      m_isFacingCamera(false),
      m_item(0),
      m_renderer(0),
      m_labelItem(false),
      m_textureWidth(0),
      m_textureHeight(0),
      m_textureDepth(0),
      m_isVolume(false),
      m_textureFormat(QImage::Format_ARGB32),
      m_sliceIndexX(-1),
      m_sliceIndexY(-1),
      m_sliceIndexZ(-1),
      m_alphaMultiplier(1.0f),
      m_preserveOpacity(true),
      m_useHighDefShader(true),
      m_drawSlices(false),
      m_drawSliceFrames(false)

{
}
//  -----------------------------------------------------------------------

//  Only a class built on Surface3DRenderer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnSurface3DRenderer : Surface3DRenderer {
  using Surface3DRenderer::contextCleanup;
  using Surface3DRenderer::initializeOpenGL;
};

//  A Surface3DRenderer that Python can take functions over in. Every Surface3DRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteSurface3DRendererCall0)(const void *, int *);
typedef void * (*CuteSurface3DRendererCall1)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteSurface3DRendererCall2)(const void *, SeriesRenderCache *, int *);
typedef void (*CuteSurface3DRendererCall3)(const void *, int, int *);
typedef void (*CuteSurface3DRendererCall4)(const void *, Q3DScene *, int *);
typedef const QVector3D * (*CuteSurface3DRendererCall5)(const void *, const QVector3D *, bool, int *);
typedef void (*CuteSurface3DRendererCall6)(const void *, int, bool, int *);
typedef void (*CuteSurface3DRendererCall7)(const void *, float, int *);
typedef void (*CuteSurface3DRendererCall8)(const void *, GLuint, int *);
typedef void (*CuteSurface3DRendererCall9)(const void *, int *);
typedef void (*CuteSurface3DRendererCall10)(const void *, int *);
typedef void (*CuteSurface3DRendererCall11)(const void *, int, int *);
typedef void (*CuteSurface3DRendererCall12)(const void *, int *);
typedef void (*CuteSurface3DRendererCall13)(const void *, const QString *, const QString *, int *);
typedef void (*CuteSurface3DRendererCall14)(const void *, const QString *, const QString *, int *);
typedef void (*CuteSurface3DRendererCall15)(const void *, int *);
typedef void (*CuteSurface3DRendererCall16)(const void *, int *);
typedef void (*CuteSurface3DRendererCall17)(const void *, int *);
typedef void (*CuteSurface3DRendererCall18)(const void *, int *);
typedef void (*CuteSurface3DRendererCall19)(const void *, Q3DTheme *, int *);
typedef void (*CuteSurface3DRendererCall20)(const void *, int, int *);
typedef void (*CuteSurface3DRendererCall21)(const void *, const QString *, const QString *, int *);
typedef void (*CuteSurface3DRendererCall22)(const void *, const QString *, const QString *, const QString *, const QString *, int *);
typedef void (*CuteSurface3DRendererCall23)(const void *, const QString *, const QString *, int *);
typedef void (*CuteSurface3DRendererCall24)(const void *, const QString *, const QString *, const QString *, const QString *, const QString *, const QString *, int *);
typedef void (*CuteSurface3DRendererCall25)(const void *, const QString *, const QString *, int *);
typedef void (*CuteSurface3DRendererCall26)(const void *, const QString *, const QString *, int *);
typedef void (*CuteSurface3DRendererCall27)(const void *, int *);
typedef void (*CuteSurface3DRendererCall28)(const void *, int, int, int *);
typedef void (*CuteSurface3DRendererCall29)(const void *, int, const QString *, int *);
typedef void (*CuteSurface3DRendererCall30)(const void *, int, float, float, int *);
typedef void (*CuteSurface3DRendererCall31)(const void *, int, int, int *);
typedef void (*CuteSurface3DRendererCall32)(const void *, int, int, int *);
typedef void (*CuteSurface3DRendererCall33)(const void *, int, const QString *, int *);
typedef void (*CuteSurface3DRendererCall34)(const void *, int, bool, int *);
typedef void (*CuteSurface3DRendererCall35)(const void *, int, QValue3DAxisFormatter *, int *);
typedef void (*CuteSurface3DRendererCall36)(const void *, int, float, int *);
typedef void (*CuteSurface3DRendererCall37)(const void *, int, bool, int *);
typedef void * (*CuteSurface3DRendererCall38)(const void *, QCustom3DItem *, int *);
typedef void (*CuteSurface3DRendererCall39)(const void *, CustomRenderItem *, int *);
typedef void (*CuteSurface3DRendererCall40)(const void *, float, int *);
typedef void (*CuteSurface3DRendererCall41)(const void *, float, int *);
typedef void (*CuteSurface3DRendererCall42)(const void *, bool, int *);
typedef void (*CuteSurface3DRendererCall43)(const void *, float, int *);
typedef void (*CuteSurface3DRendererCall44)(const void *, int *);
typedef void (*CuteSurface3DRendererCall45)(const void *, int *);
typedef void (*CuteSurface3DRendererCall46)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteSurface3DRendererCall47)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteSurface3DRendererCall48)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSurface3DRendererCall49)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSurface3DRendererCall50)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSurface3DRendererCall51)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSurface3DRendererCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteSurface3DRendererCall53)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteSurface3DRenderer : public Surface3DRenderer {
public:
  using Surface3DRenderer::Surface3DRenderer;
  void *taken[54] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer10updateDataEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer14createNewCacheEP17QAbstract3DSeries")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer10cleanCacheEP17SeriesRenderCache")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer19updateSelectionModeE6QFlagsIN16QAbstract3DGraph13SelectionFlagEE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer11updateSceneEP8Q3DScene")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer28convertPositionToTranslationERK9QVector3Db")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer25updateAxisTitleVisibilityEN15QAbstract3DAxis15AxisOrientationEb")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer12updateMarginEf")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer6renderEj")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer14contextCleanupEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer16initializeOpenGLEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer19updateShadowQualityEN16QAbstract3DGraph13ShadowQualityE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer14updateTexturesEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer11initShadersERK7QStringS2_")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer21initBackgroundShadersERK7QStringS2_")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer19initSelectionBufferEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer17updateDepthBufferEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer17updateCustomItemsEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer25updateCustomItemPositionsEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer11updateThemeEP8Q3DTheme")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer22updateOptimizationHintE6QFlagsIN16QAbstract3DGraph16OptimizationHintEE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer19initGradientShadersERK7QStringS2_")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer29initStaticSelectedItemShadersERK7QStringS2_S2_S2_")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer21initCustomItemShadersERK7QStringS2_")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer24initVolumeTextureShadersERK7QStringS2_S2_S2_S2_S2_")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer16initLabelShadersERK7QStringS2_")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer25initCursorPositionShadersERK7QStringS2_")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer24initCursorPositionBufferEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer14updateAxisTypeEN15QAbstract3DAxis15AxisOrientationENS0_8AxisTypeE")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer15updateAxisTitleEN15QAbstract3DAxis15AxisOrientationERK7QString")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer15updateAxisRangeEN15QAbstract3DAxis15AxisOrientationEff")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer22updateAxisSegmentCountEN15QAbstract3DAxis15AxisOrientationEi")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer25updateAxisSubSegmentCountEN15QAbstract3DAxis15AxisOrientationEi")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer21updateAxisLabelFormatEN15QAbstract3DAxis15AxisOrientationERK7QString")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer18updateAxisReversedEN15QAbstract3DAxis15AxisOrientationEb")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer19updateAxisFormatterEN15QAbstract3DAxis15AxisOrientationEP21QValue3DAxisFormatter")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer27updateAxisLabelAutoRotationEN15QAbstract3DAxis15AxisOrientationEf")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer20updateAxisTitleFixedEN15QAbstract3DAxis15AxisOrientationEb")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer13addCustomItemEP13QCustom3DItem")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer16updateCustomItemEP16CustomRenderItem")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer17updateAspectRatioEf")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer27updateHorizontalAspectRatioEf")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer11updatePolarEb")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer23updateRadialLabelOffsetEf")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer25handleShadowQualityChangeEv")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer12handleResizeEv")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer18lowerShadowQualityEv")) {
      taken[46] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[50] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[51] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[52] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[53] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void Surface3DRenderer::updateData()
  void updateData() override {
    if (taken[0]) {
      int handled = 0;
      CuteSurface3DRendererCall0 call = reinterpret_cast<CuteSurface3DRendererCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Surface3DRenderer::updateData();
  }

  //  SeriesRenderCache
  //      *Surface3DRenderer::createNewCache(QAbstract3DSeries *series)
  SeriesRenderCache *createNewCache(QAbstract3DSeries *series) override {
    if (taken[1]) {
      int handled = 0;
      CuteSurface3DRendererCall1 call = reinterpret_cast<CuteSurface3DRendererCall1>(taken[1]);
      void * given = call(this, series, &handled);
      if (handled) return static_cast<SeriesRenderCache *>(given);
    }
    return Surface3DRenderer::createNewCache(series);
  }

  //  void Surface3DRenderer::cleanCache(SeriesRenderCache *cache)
  void cleanCache(SeriesRenderCache *cache) override {
    if (taken[2]) {
      int handled = 0;
      CuteSurface3DRendererCall2 call = reinterpret_cast<CuteSurface3DRendererCall2>(taken[2]);
      call(this, cache, &handled);
      if (handled) return;
    }
    Surface3DRenderer::cleanCache(cache);
  }

  //  void Surface3DRenderer::updateSelectionMode(QAbstract3DGraph::Selecti
  //      onFlags mode)
  void updateSelectionMode(QAbstract3DGraph::SelectionFlags mode) override {
    if (taken[3]) {
      int handled = 0;
      CuteSurface3DRendererCall3 call = reinterpret_cast<CuteSurface3DRendererCall3>(taken[3]);
      call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return;
    }
    Surface3DRenderer::updateSelectionMode(mode);
  }

  //  void Surface3DRenderer::updateScene(Q3DScene *scene)
  void updateScene(Q3DScene *scene) override {
    if (taken[4]) {
      int handled = 0;
      CuteSurface3DRendererCall4 call = reinterpret_cast<CuteSurface3DRendererCall4>(taken[4]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Surface3DRenderer::updateScene(scene);
  }

  //  QVector3D Surface3DRenderer::convertPositionToTranslation(const
  //      QVector3D &position, bool isAbsolute)
  QVector3D convertPositionToTranslation(
      const QVector3D &position,
      bool isAbsolute) override {
    if (taken[5]) {
      int handled = 0;
      CuteSurface3DRendererCall5 call = reinterpret_cast<CuteSurface3DRendererCall5>(taken[5]);
      const QVector3D * given = call(this, &position, isAbsolute, &handled);
      if (handled && given) return *given;
    }
    return Surface3DRenderer::convertPositionToTranslation(position, isAbsolute);
  }

  //  void Surface3DRenderer::updateAxisTitleVisibility(QAbstract3DAxis::Ax
  //      isOrientation orientation, bool visible)
  void updateAxisTitleVisibility(
      QAbstract3DAxis::AxisOrientation orientation,
      bool visible) override {
    if (taken[6]) {
      int handled = 0;
      CuteSurface3DRendererCall6 call = reinterpret_cast<CuteSurface3DRendererCall6>(taken[6]);
      call(this, static_cast<int>(orientation), visible, &handled);
      if (handled) return;
    }
    Surface3DRenderer::updateAxisTitleVisibility(orientation, visible);
  }

  //  void Surface3DRenderer::updateMargin(float margin)
  void updateMargin(float margin) override {
    if (taken[7]) {
      int handled = 0;
      CuteSurface3DRendererCall7 call = reinterpret_cast<CuteSurface3DRendererCall7>(taken[7]);
      call(this, margin, &handled);
      if (handled) return;
    }
    Surface3DRenderer::updateMargin(margin);
  }

  //  void Surface3DRenderer::render(GLuint defaultFboHandle)
  void render(GLuint defaultFboHandle) override {
    if (taken[8]) {
      int handled = 0;
      CuteSurface3DRendererCall8 call = reinterpret_cast<CuteSurface3DRendererCall8>(taken[8]);
      call(this, defaultFboHandle, &handled);
      if (handled) return;
    }
    Surface3DRenderer::render(defaultFboHandle);
  }

  //  void Surface3DRenderer::contextCleanup()
  void contextCleanup() override {
    if (taken[9]) {
      int handled = 0;
      CuteSurface3DRendererCall9 call = reinterpret_cast<CuteSurface3DRendererCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    Surface3DRenderer::contextCleanup();
  }

  //  void Surface3DRenderer::initializeOpenGL()
  void initializeOpenGL() override {
    if (taken[10]) {
      int handled = 0;
      CuteSurface3DRendererCall10 call = reinterpret_cast<CuteSurface3DRendererCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    Surface3DRenderer::initializeOpenGL();
  }

  //  void Surface3DRenderer::updateShadowQuality(QAbstract3DGraph::ShadowQ
  //      uality quality)
  void updateShadowQuality(
      QAbstract3DGraph::ShadowQuality quality) override {
    if (taken[11]) {
      int handled = 0;
      CuteSurface3DRendererCall11 call = reinterpret_cast<CuteSurface3DRendererCall11>(taken[11]);
      call(this, static_cast<int>(quality), &handled);
      if (handled) return;
    }
    Surface3DRenderer::updateShadowQuality(quality);
  }

  //  void Surface3DRenderer::updateTextures()
  void updateTextures() override {
    if (taken[12]) {
      int handled = 0;
      CuteSurface3DRendererCall12 call = reinterpret_cast<CuteSurface3DRendererCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    Surface3DRenderer::updateTextures();
  }

  //  void Surface3DRenderer::initShaders(const QString &vertexShader,
  //      const QString &fragmentShader)
  void initShaders(
      const QString &vertexShader,
      const QString &fragmentShader) override {
    if (taken[13]) {
      int handled = 0;
      CuteSurface3DRendererCall13 call = reinterpret_cast<CuteSurface3DRendererCall13>(taken[13]);
      call(this, &vertexShader, &fragmentShader, &handled);
      if (handled) return;
    }
    Surface3DRenderer::initShaders(vertexShader, fragmentShader);
  }

  //  void Surface3DRenderer::initBackgroundShaders(const QString
  //      &vertexShader, const QString &fragmentShader)
  void initBackgroundShaders(
      const QString &vertexShader,
      const QString &fragmentShader) override {
    if (taken[14]) {
      int handled = 0;
      CuteSurface3DRendererCall14 call = reinterpret_cast<CuteSurface3DRendererCall14>(taken[14]);
      call(this, &vertexShader, &fragmentShader, &handled);
      if (handled) return;
    }
    Surface3DRenderer::initBackgroundShaders(vertexShader, fragmentShader);
  }

  //  void Surface3DRenderer::initSelectionBuffer()
  void initSelectionBuffer() override {
    if (taken[15]) {
      int handled = 0;
      CuteSurface3DRendererCall15 call = reinterpret_cast<CuteSurface3DRendererCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    Surface3DRenderer::initSelectionBuffer();
  }

  //  void Surface3DRenderer::updateDepthBuffer()
  void updateDepthBuffer() override {
    if (taken[16]) {
      int handled = 0;
      CuteSurface3DRendererCall16 call = reinterpret_cast<CuteSurface3DRendererCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    Surface3DRenderer::updateDepthBuffer();
  }

  //  void Abstract3DRenderer::updateCustomItems()
  void updateCustomItems() override {
    if (taken[17]) {
      int handled = 0;
      CuteSurface3DRendererCall17 call = reinterpret_cast<CuteSurface3DRendererCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateCustomItems();
  }

  //  void Abstract3DRenderer::updateCustomItemPositions()
  void updateCustomItemPositions() override {
    if (taken[18]) {
      int handled = 0;
      CuteSurface3DRendererCall18 call = reinterpret_cast<CuteSurface3DRendererCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateCustomItemPositions();
  }

  //  void Abstract3DRenderer::updateTheme(Q3DTheme *theme)
  void updateTheme(Q3DTheme *theme) override {
    if (taken[19]) {
      int handled = 0;
      CuteSurface3DRendererCall19 call = reinterpret_cast<CuteSurface3DRendererCall19>(taken[19]);
      call(this, theme, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateTheme(theme);
  }

  //  void Abstract3DRenderer::updateOptimizationHint(QAbstract3DGraph::Opt
  //      imizationHints hint)
  void updateOptimizationHint(
      QAbstract3DGraph::OptimizationHints hint) override {
    if (taken[20]) {
      int handled = 0;
      CuteSurface3DRendererCall20 call = reinterpret_cast<CuteSurface3DRendererCall20>(taken[20]);
      call(this, static_cast<int>(hint.toInt()), &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateOptimizationHint(hint);
  }

  //  void Abstract3DRenderer::initGradientShaders(const QString
  //      &vertexShader, const QString &fragmentShader)
  void initGradientShaders(
      const QString &vertexShader,
      const QString &fragmentShader) override {
    if (taken[21]) {
      int handled = 0;
      CuteSurface3DRendererCall21 call = reinterpret_cast<CuteSurface3DRendererCall21>(taken[21]);
      call(this, &vertexShader, &fragmentShader, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::initGradientShaders(vertexShader, fragmentShader);
  }

  //  void Abstract3DRenderer::initStaticSelectedItemShaders(const QString
  //      &vertexShader, const QString &fragmentShader, const QString
  //      &gradientVertexShader, const QString &gradientFragmentShader)
  void initStaticSelectedItemShaders(
      const QString &vertexShader,
      const QString &fragmentShader,
      const QString &gradientVertexShader,
      const QString &gradientFragmentShader) override {
    if (taken[22]) {
      int handled = 0;
      CuteSurface3DRendererCall22 call = reinterpret_cast<CuteSurface3DRendererCall22>(taken[22]);
      call(this, &vertexShader, &fragmentShader, &gradientVertexShader, &gradientFragmentShader, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::initStaticSelectedItemShaders(vertexShader, fragmentShader, gradientVertexShader, gradientFragmentShader);
  }

  //  void Abstract3DRenderer::initCustomItemShaders(const QString
  //      &vertexShader, const QString &fragmentShader)
  void initCustomItemShaders(
      const QString &vertexShader,
      const QString &fragmentShader) override {
    if (taken[23]) {
      int handled = 0;
      CuteSurface3DRendererCall23 call = reinterpret_cast<CuteSurface3DRendererCall23>(taken[23]);
      call(this, &vertexShader, &fragmentShader, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::initCustomItemShaders(vertexShader, fragmentShader);
  }

  //  void Abstract3DRenderer::initVolumeTextureShaders(const QString
  //      &vertexShader, const QString &fragmentShader, const QString
  //      &fragmentLowDefShader, const QString &sliceShader, const QString
  //      &sliceFrameVertexShader, const QString &sliceFrameShader)
  void initVolumeTextureShaders(
      const QString &vertexShader,
      const QString &fragmentShader,
      const QString &fragmentLowDefShader,
      const QString &sliceShader,
      const QString &sliceFrameVertexShader,
      const QString &sliceFrameShader) override {
    if (taken[24]) {
      int handled = 0;
      CuteSurface3DRendererCall24 call = reinterpret_cast<CuteSurface3DRendererCall24>(taken[24]);
      call(this, &vertexShader, &fragmentShader, &fragmentLowDefShader, &sliceShader, &sliceFrameVertexShader, &sliceFrameShader, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::initVolumeTextureShaders(vertexShader, fragmentShader, fragmentLowDefShader, sliceShader, sliceFrameVertexShader, sliceFrameShader);
  }

  //  void Abstract3DRenderer::initLabelShaders(const QString
  //      &vertexShader, const QString &fragmentShader)
  void initLabelShaders(
      const QString &vertexShader,
      const QString &fragmentShader) override {
    if (taken[25]) {
      int handled = 0;
      CuteSurface3DRendererCall25 call = reinterpret_cast<CuteSurface3DRendererCall25>(taken[25]);
      call(this, &vertexShader, &fragmentShader, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::initLabelShaders(vertexShader, fragmentShader);
  }

  //  void Abstract3DRenderer::initCursorPositionShaders(const QString
  //      &vertexShader, const QString &fragmentShader)
  void initCursorPositionShaders(
      const QString &vertexShader,
      const QString &fragmentShader) override {
    if (taken[26]) {
      int handled = 0;
      CuteSurface3DRendererCall26 call = reinterpret_cast<CuteSurface3DRendererCall26>(taken[26]);
      call(this, &vertexShader, &fragmentShader, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::initCursorPositionShaders(vertexShader, fragmentShader);
  }

  //  void Abstract3DRenderer::initCursorPositionBuffer()
  void initCursorPositionBuffer() override {
    if (taken[27]) {
      int handled = 0;
      CuteSurface3DRendererCall27 call = reinterpret_cast<CuteSurface3DRendererCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::initCursorPositionBuffer();
  }

  //  void
  //      Abstract3DRenderer::updateAxisType(QAbstract3DAxis::AxisOrientati
  //      on orientation, QAbstract3DAxis::AxisType type)
  void updateAxisType(
      QAbstract3DAxis::AxisOrientation orientation,
      QAbstract3DAxis::AxisType type) override {
    if (taken[28]) {
      int handled = 0;
      CuteSurface3DRendererCall28 call = reinterpret_cast<CuteSurface3DRendererCall28>(taken[28]);
      call(this, static_cast<int>(orientation), static_cast<int>(type), &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateAxisType(orientation, type);
  }

  //  void
  //      Abstract3DRenderer::updateAxisTitle(QAbstract3DAxis::AxisOrientat
  //      ion orientation, const QString &title)
  void updateAxisTitle(
      QAbstract3DAxis::AxisOrientation orientation,
      const QString &title) override {
    if (taken[29]) {
      int handled = 0;
      CuteSurface3DRendererCall29 call = reinterpret_cast<CuteSurface3DRendererCall29>(taken[29]);
      call(this, static_cast<int>(orientation), &title, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateAxisTitle(orientation, title);
  }

  //  void
  //      Abstract3DRenderer::updateAxisRange(QAbstract3DAxis::AxisOrientat
  //      ion orientation, float min, float max)
  void updateAxisRange(
      QAbstract3DAxis::AxisOrientation orientation,
      float min,
      float max) override {
    if (taken[30]) {
      int handled = 0;
      CuteSurface3DRendererCall30 call = reinterpret_cast<CuteSurface3DRendererCall30>(taken[30]);
      call(this, static_cast<int>(orientation), min, max, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateAxisRange(orientation, min, max);
  }

  //  void Abstract3DRenderer::updateAxisSegmentCount(QAbstract3DAxis::Axis
  //      Orientation orientation, int count)
  void updateAxisSegmentCount(
      QAbstract3DAxis::AxisOrientation orientation,
      int count) override {
    if (taken[31]) {
      int handled = 0;
      CuteSurface3DRendererCall31 call = reinterpret_cast<CuteSurface3DRendererCall31>(taken[31]);
      call(this, static_cast<int>(orientation), count, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateAxisSegmentCount(orientation, count);
  }

  //  void Abstract3DRenderer::updateAxisSubSegmentCount(QAbstract3DAxis::A
  //      xisOrientation orientation, int count)
  void updateAxisSubSegmentCount(
      QAbstract3DAxis::AxisOrientation orientation,
      int count) override {
    if (taken[32]) {
      int handled = 0;
      CuteSurface3DRendererCall32 call = reinterpret_cast<CuteSurface3DRendererCall32>(taken[32]);
      call(this, static_cast<int>(orientation), count, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateAxisSubSegmentCount(orientation, count);
  }

  //  void Abstract3DRenderer::updateAxisLabelFormat(QAbstract3DAxis::AxisO
  //      rientation orientation, const QString &format)
  void updateAxisLabelFormat(
      QAbstract3DAxis::AxisOrientation orientation,
      const QString &format) override {
    if (taken[33]) {
      int handled = 0;
      CuteSurface3DRendererCall33 call = reinterpret_cast<CuteSurface3DRendererCall33>(taken[33]);
      call(this, static_cast<int>(orientation), &format, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateAxisLabelFormat(orientation, format);
  }

  //  void Abstract3DRenderer::updateAxisReversed(QAbstract3DAxis::AxisOrie
  //      ntation orientation, bool enable)
  void updateAxisReversed(
      QAbstract3DAxis::AxisOrientation orientation,
      bool enable) override {
    if (taken[34]) {
      int handled = 0;
      CuteSurface3DRendererCall34 call = reinterpret_cast<CuteSurface3DRendererCall34>(taken[34]);
      call(this, static_cast<int>(orientation), enable, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateAxisReversed(orientation, enable);
  }

  //  void Abstract3DRenderer::updateAxisFormatter(QAbstract3DAxis::AxisOri
  //      entation orientation, QValue3DAxisFormatter *formatter)
  void updateAxisFormatter(
      QAbstract3DAxis::AxisOrientation orientation,
      QValue3DAxisFormatter *formatter) override {
    if (taken[35]) {
      int handled = 0;
      CuteSurface3DRendererCall35 call = reinterpret_cast<CuteSurface3DRendererCall35>(taken[35]);
      call(this, static_cast<int>(orientation), formatter, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateAxisFormatter(orientation, formatter);
  }

  //  void Abstract3DRenderer::updateAxisLabelAutoRotation(QAbstract3DAxis:
  //      :AxisOrientation orientation, float angle)
  void updateAxisLabelAutoRotation(
      QAbstract3DAxis::AxisOrientation orientation,
      float angle) override {
    if (taken[36]) {
      int handled = 0;
      CuteSurface3DRendererCall36 call = reinterpret_cast<CuteSurface3DRendererCall36>(taken[36]);
      call(this, static_cast<int>(orientation), angle, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateAxisLabelAutoRotation(orientation, angle);
  }

  //  void Abstract3DRenderer::updateAxisTitleFixed(QAbstract3DAxis::AxisOr
  //      ientation orientation, bool fixed)
  void updateAxisTitleFixed(
      QAbstract3DAxis::AxisOrientation orientation,
      bool fixed) override {
    if (taken[37]) {
      int handled = 0;
      CuteSurface3DRendererCall37 call = reinterpret_cast<CuteSurface3DRendererCall37>(taken[37]);
      call(this, static_cast<int>(orientation), fixed, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateAxisTitleFixed(orientation, fixed);
  }

  //  CustomRenderItem *Abstract3DRenderer::addCustomItem(QCustom3DItem
  //      *item)
  CustomRenderItem *addCustomItem(QCustom3DItem *item) override {
    if (taken[38]) {
      int handled = 0;
      CuteSurface3DRendererCall38 call = reinterpret_cast<CuteSurface3DRendererCall38>(taken[38]);
      void * given = call(this, item, &handled);
      if (handled) return static_cast<CustomRenderItem *>(given);
    }
    return Abstract3DRenderer::addCustomItem(item);
  }

  //  void Abstract3DRenderer::updateCustomItem(CustomRenderItem
  //      *renderItem)
  void updateCustomItem(CustomRenderItem *renderItem) override {
    if (taken[39]) {
      int handled = 0;
      CuteSurface3DRendererCall39 call = reinterpret_cast<CuteSurface3DRendererCall39>(taken[39]);
      call(this, renderItem, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateCustomItem(renderItem);
  }

  //  void Abstract3DRenderer::updateAspectRatio(float ratio)
  void updateAspectRatio(float ratio) override {
    if (taken[40]) {
      int handled = 0;
      CuteSurface3DRendererCall40 call = reinterpret_cast<CuteSurface3DRendererCall40>(taken[40]);
      call(this, ratio, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateAspectRatio(ratio);
  }

  //  void Abstract3DRenderer::updateHorizontalAspectRatio(float ratio)
  void updateHorizontalAspectRatio(float ratio) override {
    if (taken[41]) {
      int handled = 0;
      CuteSurface3DRendererCall41 call = reinterpret_cast<CuteSurface3DRendererCall41>(taken[41]);
      call(this, ratio, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateHorizontalAspectRatio(ratio);
  }

  //  void Abstract3DRenderer::updatePolar(bool enable)
  void updatePolar(bool enable) override {
    if (taken[42]) {
      int handled = 0;
      CuteSurface3DRendererCall42 call = reinterpret_cast<CuteSurface3DRendererCall42>(taken[42]);
      call(this, enable, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updatePolar(enable);
  }

  //  void Abstract3DRenderer::updateRadialLabelOffset(float offset)
  void updateRadialLabelOffset(float offset) override {
    if (taken[43]) {
      int handled = 0;
      CuteSurface3DRendererCall43 call = reinterpret_cast<CuteSurface3DRendererCall43>(taken[43]);
      call(this, offset, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateRadialLabelOffset(offset);
  }

  //  void Abstract3DRenderer::handleShadowQualityChange()
  void handleShadowQualityChange() override {
    if (taken[44]) {
      int handled = 0;
      CuteSurface3DRendererCall44 call = reinterpret_cast<CuteSurface3DRendererCall44>(taken[44]);
      call(this, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::handleShadowQualityChange();
  }

  //  void Abstract3DRenderer::handleResize()
  void handleResize() override {
    if (taken[45]) {
      int handled = 0;
      CuteSurface3DRendererCall45 call = reinterpret_cast<CuteSurface3DRendererCall45>(taken[45]);
      call(this, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::handleResize();
  }

  //  void Abstract3DRenderer::lowerShadowQuality()
  void lowerShadowQuality() override {
    if (taken[46]) {
      int handled = 0;
      CuteSurface3DRendererCall46 call = reinterpret_cast<CuteSurface3DRendererCall46>(taken[46]);
      call(this, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::lowerShadowQuality();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteSurface3DRendererCall47 call = reinterpret_cast<CuteSurface3DRendererCall47>(taken[47]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteSurface3DRendererCall48 call = reinterpret_cast<CuteSurface3DRendererCall48>(taken[48]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteSurface3DRendererCall49 call = reinterpret_cast<CuteSurface3DRendererCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteSurface3DRendererCall50 call = reinterpret_cast<CuteSurface3DRendererCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[51]) {
      int handled = 0;
      CuteSurface3DRendererCall51 call = reinterpret_cast<CuteSurface3DRendererCall51>(taken[51]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[52]) {
      int handled = 0;
      CuteSurface3DRendererCall52 call = reinterpret_cast<CuteSurface3DRendererCall52>(taken[52]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[53]) {
      int handled = 0;
      CuteSurface3DRendererCall53 call = reinterpret_cast<CuteSurface3DRendererCall53>(taken[53]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Surface3DRenderer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17Surface3DRenderer10metaObjectEv(
    const Surface3DRenderer *self) {
  return self->metaObject();
}

//  QString Surface3DRenderer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17Surface3DRenderer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Surface3DRenderer::tr(s, c, n));
}

//  Surface3DRenderer::~Surface3DRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRendererD1Ev(Surface3DRenderer *self) {
  delete self;
}

//  void Surface3DRenderer::updateData()
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer10updateDataEv(Surface3DRenderer *self) {
  self->updateData();
}

//  void Surface3DRenderer::updateSeries(const QList<QAbstract3DSeries *>
//      &seriesList)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer12updateSeriesERK5QListIP17QAbstract3DSeriesE(
    Surface3DRenderer *self,
    const QList<QAbstract3DSeries *> *seriesList) {
  self->updateSeries(*seriesList);
}

//  void Surface3DRenderer::updateSurfaceTextures(QList<QSurface3DSeries *>
//      seriesList)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer21updateSurfaceTexturesE5QListIP16QSurface3DSeriesE(
    Surface3DRenderer *self,
    const QList<QSurface3DSeries *> *seriesList) {
  self->updateSurfaceTextures(*seriesList);
}

//  SeriesRenderCache *Surface3DRenderer::createNewCache(QAbstract3DSeries
//      *series)
extern "C" Q_DECL_EXPORT
SeriesRenderCache *ritual_ZN17Surface3DRenderer14createNewCacheEP17QAbstract3DSeries(
    Surface3DRenderer *self,
    QAbstract3DSeries *series) {
  return self->createNewCache(series);
}

//  void Surface3DRenderer::cleanCache(SeriesRenderCache *cache)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer10cleanCacheEP17SeriesRenderCache(
    Surface3DRenderer *self,
    SeriesRenderCache *cache) {
  self->cleanCache(cache);
}

//  void
//      Surface3DRenderer::updateSelectionMode(QAbstract3DGraph::SelectionFla
//      gs mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer19updateSelectionModeE6QFlagsIN16QAbstract3DGraph13SelectionFlagEE(
    Surface3DRenderer *self,
    int mode) {
  self->updateSelectionMode(
      QFlags<QAbstract3DGraph::SelectionFlag>::fromInt(mode));
}

//  void Surface3DRenderer::updateScene(Q3DScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer11updateSceneEP8Q3DScene(
    Surface3DRenderer *self,
    Q3DScene *scene) {
  self->updateScene(scene);
}

//  void Surface3DRenderer::updateSlicingActive(bool isSlicing)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer19updateSlicingActiveEb(
    Surface3DRenderer *self,
    bool isSlicing) {
  self->updateSlicingActive(isSlicing);
}

//  void Surface3DRenderer::updateSelectedPoint(const QPoint &position,
//      QSurface3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer19updateSelectedPointERK6QPointP16QSurface3DSeries(
    Surface3DRenderer *self,
    const QPoint *position,
    QSurface3DSeries *series) {
  self->updateSelectedPoint(*position, series);
}

//  void Surface3DRenderer::updateFlipHorizontalGrid(bool flip)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer24updateFlipHorizontalGridEb(
    Surface3DRenderer *self,
    bool flip) {
  self->updateFlipHorizontalGrid(flip);
}

//  QPoint Surface3DRenderer::clickedPosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK17Surface3DRenderer15clickedPositionEv(
    const Surface3DRenderer *self) {
  return new QPoint(self->clickedPosition());
}

//  void Surface3DRenderer::resetClickedStatus()
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer18resetClickedStatusEv(
    Surface3DRenderer *self) {
  self->resetClickedStatus();
}

//  QVector3D Surface3DRenderer::convertPositionToTranslation(const QVector3D
//      &position, bool isAbsolute)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN17Surface3DRenderer28convertPositionToTranslationERK9QVector3Db(
    Surface3DRenderer *self,
    const QVector3D *position,
    bool isAbsolute) {
  return new QVector3D(
      self->convertPositionToTranslation(
          *position,
          isAbsolute));
}

//  void Surface3DRenderer::updateAxisLabels(QAbstract3DAxis::AxisOrientation
//      orientation, const QStringList &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer16updateAxisLabelsEN15QAbstract3DAxis15AxisOrientationERK5QListI7QStringE(
    Surface3DRenderer *self,
    QAbstract3DAxis::AxisOrientation orientation,
    const QList<QString> *labels) {
  self->updateAxisLabels(orientation, *labels);
}

//  void Surface3DRenderer::updateAxisTitleVisibility(QAbstract3DAxis::AxisOr
//      ientation orientation, bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer25updateAxisTitleVisibilityEN15QAbstract3DAxis15AxisOrientationEb(
    Surface3DRenderer *self,
    QAbstract3DAxis::AxisOrientation orientation,
    bool visible) {
  self->updateAxisTitleVisibility(orientation, visible);
}

//  void Surface3DRenderer::updateMargin(float margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer12updateMarginEf(
    Surface3DRenderer *self,
    float margin) {
  self->updateMargin(margin);
}

//  void Surface3DRenderer::render(GLuint defaultFboHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer6renderEj(
    Surface3DRenderer *self,
    GLuint defaultFboHandle) {
  self->render(defaultFboHandle);
}

//  void Surface3DRenderer::contextCleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer14contextCleanupEv(
    Surface3DRenderer *self) {
  self->contextCleanup();
}

//  void Surface3DRenderer::initializeOpenGL()
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer16initializeOpenGLEv(
    Surface3DRenderer *self) {
  self->initializeOpenGL();
}

//  void Surface3DRenderer::checkFlatSupport(SurfaceSeriesRenderCache *cache)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer16checkFlatSupportEP24SurfaceSeriesRenderCache(
    Surface3DRenderer *self,
    SurfaceSeriesRenderCache *cache) {
  self->checkFlatSupport(cache);
}

//  void Surface3DRenderer::updateObjects(SurfaceSeriesRenderCache *cache,
//      bool dimensionChanged)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer13updateObjectsEP24SurfaceSeriesRenderCacheb(
    Surface3DRenderer *self,
    SurfaceSeriesRenderCache *cache,
    bool dimensionChanged) {
  self->updateObjects(cache, dimensionChanged);
}

//  void Surface3DRenderer::updateSliceDataModel(const QPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer20updateSliceDataModelERK6QPoint(
    Surface3DRenderer *self,
    const QPoint *point) {
  self->updateSliceDataModel(*point);
}

//  QPoint Surface3DRenderer::mapCoordsToSampleSpace(SurfaceSeriesRenderCache
//      *cache, const QPointF &coords)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN17Surface3DRenderer22mapCoordsToSampleSpaceEP24SurfaceSeriesRenderCacheRK7QPointF(
    Surface3DRenderer *self,
    SurfaceSeriesRenderCache *cache,
    const QPointF *coords) {
  return new QPoint(self->mapCoordsToSampleSpace(cache, *coords));
}

//  void Surface3DRenderer::updateSliceObject(SurfaceSeriesRenderCache
//      *cache, const QPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer17updateSliceObjectEP24SurfaceSeriesRenderCacheRK6QPoint(
    Surface3DRenderer *self,
    SurfaceSeriesRenderCache *cache,
    const QPoint *point) {
  self->updateSliceObject(cache, *point);
}

//  void
//      Surface3DRenderer::updateShadowQuality(QAbstract3DGraph::ShadowQualit
//      y quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer19updateShadowQualityEN16QAbstract3DGraph13ShadowQualityE(
    Surface3DRenderer *self,
    QAbstract3DGraph::ShadowQuality quality) {
  self->updateShadowQuality(quality);
}

//  void Surface3DRenderer::updateTextures()
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer14updateTexturesEv(
    Surface3DRenderer *self) {
  self->updateTextures();
}

//  void Surface3DRenderer::initShaders(const QString &vertexShader, const
//      QString &fragmentShader)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer11initShadersERK7QStringS2_(
    Surface3DRenderer *self,
    const QString *vertexShader,
    const QString *fragmentShader) {
  self->initShaders(*vertexShader, *fragmentShader);
}

//  void Surface3DRenderer::loadBackgroundMesh()
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer18loadBackgroundMeshEv(
    Surface3DRenderer *self) {
  self->loadBackgroundMesh();
}

//  void Surface3DRenderer::drawSlicedScene()
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer15drawSlicedSceneEv(
    Surface3DRenderer *self) {
  self->drawSlicedScene();
}

//  void Surface3DRenderer::drawScene(GLuint defaultFboHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer9drawSceneEj(
    Surface3DRenderer *self,
    GLuint defaultFboHandle) {
  self->drawScene(defaultFboHandle);
}

//  void Surface3DRenderer::drawLabels(bool drawSelection, const Q3DCamera
//      *activeCamera, const QMatrix4x4 &viewMatrix, const QMatrix4x4
//      &projectionMatrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer10drawLabelsEbPK9Q3DCameraRK10QMatrix4x4S5_(
    Surface3DRenderer *self,
    bool drawSelection,
    const Q3DCamera *activeCamera,
    const QMatrix4x4 *viewMatrix,
    const QMatrix4x4 *projectionMatrix) {
  self->drawLabels(
      drawSelection,
      activeCamera,
      *viewMatrix,
      *projectionMatrix);
}

//  void Surface3DRenderer::calculateSceneScalingFactors()
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer28calculateSceneScalingFactorsEv(
    Surface3DRenderer *self) {
  self->calculateSceneScalingFactors();
}

//  void Surface3DRenderer::initBackgroundShaders(const QString
//      &vertexShader, const QString &fragmentShader)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer21initBackgroundShadersERK7QStringS2_(
    Surface3DRenderer *self,
    const QString *vertexShader,
    const QString *fragmentShader) {
  self->initBackgroundShaders(*vertexShader, *fragmentShader);
}

//  void Surface3DRenderer::initSelectionShaders()
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer20initSelectionShadersEv(
    Surface3DRenderer *self) {
  self->initSelectionShaders();
}

//  void Surface3DRenderer::initSurfaceShaders()
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer18initSurfaceShadersEv(
    Surface3DRenderer *self) {
  self->initSurfaceShaders();
}

//  void Surface3DRenderer::initSelectionBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer19initSelectionBufferEv(
    Surface3DRenderer *self) {
  self->initSelectionBuffer();
}

//  void Surface3DRenderer::initDepthShader()
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer15initDepthShaderEv(
    Surface3DRenderer *self) {
  self->initDepthShader();
}

//  void Surface3DRenderer::updateSelectionTextures()
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer23updateSelectionTexturesEv(
    Surface3DRenderer *self) {
  self->updateSelectionTextures();
}

//  void Surface3DRenderer::createSelectionTexture(SurfaceSeriesRenderCache
//      *cache, uint &lastSelectionId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer22createSelectionTextureEP24SurfaceSeriesRenderCacheRj(
    Surface3DRenderer *self,
    SurfaceSeriesRenderCache *cache,
    uint *lastSelectionId) {
  self->createSelectionTexture(cache, *lastSelectionId);
}

//  void Surface3DRenderer::idToRGBA(uint id, uchar *r, uchar *g, uchar *b,
//      uchar *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer8idToRGBAEjPhS0_S0_S0_(
    Surface3DRenderer *self,
    uint id,
    uchar *r,
    uchar *g,
    uchar *b,
    uchar *a) {
  self->idToRGBA(id, r, g, b, a);
}

//  void Surface3DRenderer::fillIdCorner(uchar *p, uchar r, uchar g, uchar b,
//      uchar a)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer12fillIdCornerEPhhhhh(
    Surface3DRenderer *self,
    uchar *p,
    uchar r,
    uchar g,
    uchar b,
    uchar a) {
  self->fillIdCorner(p, r, g, b, a);
}

//  void Surface3DRenderer::surfacePointSelected(const QPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer20surfacePointSelectedERK6QPoint(
    Surface3DRenderer *self,
    const QPoint *point) {
  self->surfacePointSelected(*point);
}

//  void Surface3DRenderer::updateSelectionPoint(SurfaceSeriesRenderCache
//      *cache, const QPoint &point, bool label)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer20updateSelectionPointEP24SurfaceSeriesRenderCacheRK6QPointb(
    Surface3DRenderer *self,
    SurfaceSeriesRenderCache *cache,
    const QPoint *point,
    bool label) {
  self->updateSelectionPoint(cache, *point, label);
}

//  QPoint Surface3DRenderer::selectionIdToSurfacePoint(uint id)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN17Surface3DRenderer25selectionIdToSurfacePointEj(
    Surface3DRenderer *self,
    uint id) {
  return new QPoint(self->selectionIdToSurfacePoint(id));
}

//  void Surface3DRenderer::updateDepthBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN17Surface3DRenderer17updateDepthBufferEv(
    Surface3DRenderer *self) {
  self->updateDepthBuffer();
}

//  a Python function taken by a CuteSurface3DRenderer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Surface3DRenderer(
    Surface3DRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteSurface3DRenderer *>(self)->take(key, call);
}

//  void Surface3DRenderer::updateData()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17Surface3DRenderer10updateDataEv(
    Surface3DRenderer *self) {
  self->Surface3DRenderer::updateData();
}

//  SeriesRenderCache *Surface3DRenderer::createNewCache(QAbstract3DSeries
//      *series)
extern "C" Q_DECL_EXPORT
SeriesRenderCache *ritual_own_ZN17Surface3DRenderer14createNewCacheEP17QAbstract3DSeries(
    Surface3DRenderer *self,
    QAbstract3DSeries *series) {
  return self->Surface3DRenderer::createNewCache(series);
}

//  void Surface3DRenderer::cleanCache(SeriesRenderCache *cache)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17Surface3DRenderer10cleanCacheEP17SeriesRenderCache(
    Surface3DRenderer *self,
    SeriesRenderCache *cache) {
  self->Surface3DRenderer::cleanCache(cache);
}

//  void
//      Surface3DRenderer::updateSelectionMode(QAbstract3DGraph::SelectionFla
//      gs mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17Surface3DRenderer19updateSelectionModeE6QFlagsIN16QAbstract3DGraph13SelectionFlagEE(
    Surface3DRenderer *self,
    int mode) {
  self->Surface3DRenderer::updateSelectionMode(
      QFlags<QAbstract3DGraph::SelectionFlag>::fromInt(mode));
}

//  void Surface3DRenderer::updateScene(Q3DScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17Surface3DRenderer11updateSceneEP8Q3DScene(
    Surface3DRenderer *self,
    Q3DScene *scene) {
  self->Surface3DRenderer::updateScene(scene);
}

//  QVector3D Surface3DRenderer::convertPositionToTranslation(const QVector3D
//      &position, bool isAbsolute)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_own_ZN17Surface3DRenderer28convertPositionToTranslationERK9QVector3Db(
    Surface3DRenderer *self,
    const QVector3D *position,
    bool isAbsolute) {
  return new QVector3D(
      self->Surface3DRenderer::convertPositionToTranslation(
          *position,
          isAbsolute));
}

//  void Surface3DRenderer::updateAxisTitleVisibility(QAbstract3DAxis::AxisOr
//      ientation orientation, bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17Surface3DRenderer25updateAxisTitleVisibilityEN15QAbstract3DAxis15AxisOrientationEb(
    Surface3DRenderer *self,
    QAbstract3DAxis::AxisOrientation orientation,
    bool visible) {
  self->Surface3DRenderer::updateAxisTitleVisibility(orientation, visible);
}

//  void Surface3DRenderer::updateMargin(float margin)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17Surface3DRenderer12updateMarginEf(
    Surface3DRenderer *self,
    float margin) {
  self->Surface3DRenderer::updateMargin(margin);
}

//  void Surface3DRenderer::render(GLuint defaultFboHandle)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17Surface3DRenderer6renderEj(
    Surface3DRenderer *self,
    GLuint defaultFboHandle) {
  self->Surface3DRenderer::render(defaultFboHandle);
}

//  void Surface3DRenderer::contextCleanup()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17Surface3DRenderer14contextCleanupEv(
    Surface3DRenderer *self) {
  static_cast<OwnSurface3DRenderer *>(self)->OwnSurface3DRenderer::contextCleanup();
}

//  void Surface3DRenderer::initializeOpenGL()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17Surface3DRenderer16initializeOpenGLEv(
    Surface3DRenderer *self) {
  static_cast<OwnSurface3DRenderer *>(self)->OwnSurface3DRenderer::initializeOpenGL();
}

//  void
//      Surface3DRenderer::updateShadowQuality(QAbstract3DGraph::ShadowQualit
//      y quality)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17Surface3DRenderer19updateShadowQualityEN16QAbstract3DGraph13ShadowQualityE(
    Surface3DRenderer *self,
    QAbstract3DGraph::ShadowQuality quality) {
  self->Surface3DRenderer::updateShadowQuality(quality);
}

//  void Surface3DRenderer::updateTextures()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17Surface3DRenderer14updateTexturesEv(
    Surface3DRenderer *self) {
  self->Surface3DRenderer::updateTextures();
}

//  void Surface3DRenderer::initShaders(const QString &vertexShader, const
//      QString &fragmentShader)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17Surface3DRenderer11initShadersERK7QStringS2_(
    Surface3DRenderer *self,
    const QString *vertexShader,
    const QString *fragmentShader) {
  self->Surface3DRenderer::initShaders(*vertexShader, *fragmentShader);
}

//  void Surface3DRenderer::initBackgroundShaders(const QString
//      &vertexShader, const QString &fragmentShader)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17Surface3DRenderer21initBackgroundShadersERK7QStringS2_(
    Surface3DRenderer *self,
    const QString *vertexShader,
    const QString *fragmentShader) {
  self->Surface3DRenderer::initBackgroundShaders(
      *vertexShader,
      *fragmentShader);
}

//  void Surface3DRenderer::initSelectionBuffer()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17Surface3DRenderer19initSelectionBufferEv(
    Surface3DRenderer *self) {
  self->Surface3DRenderer::initSelectionBuffer();
}

//  void Surface3DRenderer::updateDepthBuffer()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17Surface3DRenderer17updateDepthBufferEv(
    Surface3DRenderer *self) {
  self->Surface3DRenderer::updateDepthBuffer();
}
