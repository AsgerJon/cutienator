//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/bars3drenderer_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/bars3drenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDataVisualization/qabstract3dseries.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtGui/qmatrix4x4.h>
#include <QtDataVisualization/qbardataitem.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/abstract3drenderer_p.h>
#include <QtDataVisualization/private/texturehelper_p.h>
#include <QtDataVisualization/private/q3dcamera_p.h>
#include <QtDataVisualization/private/q3dtheme_p.h>
#include <QtDataVisualization/private/qvalue3daxisformatter_p.h>
#include <QtDataVisualization/private/shaderhelper_p.h>
#include <QtDataVisualization/private/qcustom3ditem_p.h>
#include <QtDataVisualization/private/qcustom3dlabel_p.h>
#include <QtDataVisualization/private/qcustom3dvolume_p.h>
#include <QtDataVisualization/private/scatter3drenderer_p.h>
#include <QtCore/qmath.h>
#include <QtGui/QOffscreenSurface>
#include <QtCore/QThread>
#include <QtDataVisualization/private/barrenderitem_p.h>
#include <QtDataVisualization/private/shaderhelper_p.h>
#include <QtOpenGL/QOpenGLShader>
#include <QtDataVisualization/private/texturehelper_p.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtGui/QImage>
#include <QtGui/QPainter>
#include <QtCore/QTime>
#include <QtDataVisualization/private/axisrendercache_p.h>
#include <QtGui/QFontMetrics>
#include <QtDataVisualization/private/customrenderitem_p.h>
#include <QtDataVisualization/private/qcustom3ditem_p.h>
#include <QtDataVisualization/private/qcustom3dlabel_p.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtDataVisualization/private/qvalue3daxisformatter_p.h>
#include <QtDataVisualization/private/qvalue3daxis_p.h>
#include <QtDataVisualization/private/drawer_p.h>
#include <QtDataVisualization/private/shaderhelper_p.h>
#include <QtDataVisualization/private/surfaceobject_p.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtDataVisualization/private/texturehelper_p.h>
#include <QtDataVisualization/private/abstract3drenderer_p.h>
#include <QtDataVisualization/private/scatterpointbufferhelper_p.h>
#include <QtGui/QMatrix4x4>
#include <QtGui/qquaternion.h>
#include <QtCore/qmath.h>
#include <QtDataVisualization/private/abstractrenderitem_p.h>
#include <QtDataVisualization/private/meshloader_p.h>
#include <QtDataVisualization/private/vertexindexer_p.h>
#include <QtDataVisualization/private/objecthelper_p.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtGui/QPainter>
#include <QtGui/QOpenGLContext>
#include <QtGui/QOffscreenSurface>
#include <QtGui/qquaternion.h>
#include <QtCore/QCoreApplication>
#include <QtCore/QRegularExpression>
#include <QtCore/QLocale>
#include <QtDataVisualization/private/labelitem_p.h>
#include <QtDataVisualization/private/bars3drenderer_p.h>
#include <QtDataVisualization/private/q3dcamera_p.h>
#include <QtDataVisualization/private/shaderhelper_p.h>
#include <QtDataVisualization/private/texturehelper_p.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtDataVisualization/private/barseriesrendercache_p.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qmath.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/utils/objecthelper.cpp, line 16, as local:objecthelper.cpp:ObjectHelperRef
struct ObjectHelperRef {
    int refCount;
    ObjectHelper *obj;
};

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 17, as local:utils.cpp:NUM_IN_POWER
#define NUM_IN_POWER(y, x) for (;y<x;y<<=1)

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 18, as local:utils.cpp:MIN_POWER
#define MIN_POWER 2

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 760, as _ZN18Abstract3DRenderer10cleanCacheEP17SeriesRenderCache
inline void Abstract3DRenderer::cleanCache(SeriesRenderCache *cache)
{
    m_renderCacheList.remove(cache->series());
    cache->cleanup(m_textureHelper);
    delete cache;
}

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

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 583, as _ZN18Abstract3DRenderer16updateAxisLabelsEN15QAbstract3DAxis15AxisOrientationERK5QListI7QStringE
inline void Abstract3DRenderer::updateAxisLabels(QAbstract3DAxis::AxisOrientation orientation,
                                          const QStringList &labels)
{
    axisCacheForOrientation(orientation).setLabels(labels);
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

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 498, as _ZN18Abstract3DRenderer19updateSelectionModeE6QFlagsIN16QAbstract3DGraph13SelectionFlagEE
inline void Abstract3DRenderer::updateSelectionMode(QAbstract3DGraph::SelectionFlags mode)
{
    m_cachedSelectionMode = mode;
    m_selectionDirty = true;
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

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 652, as _ZN18Abstract3DRenderer25updateAxisTitleVisibilityEN15QAbstract3DAxis15AxisOrientationEb
inline void Abstract3DRenderer::updateAxisTitleVisibility(QAbstract3DAxis::AxisOrientation orientation,
                                                   bool visible)
{
    AxisRenderCache &cache = axisCacheForOrientation(orientation);
    if (cache.isTitleVisible() != visible)
        cache.setTitleVisible(visible);
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

//  from ../qtdatavis3d/src/datavisualization/data/barrenderitem.cpp, line 15, as _ZN13BarRenderItemC1ERKS_
inline BarRenderItem::BarRenderItem(const BarRenderItem &other)
    : AbstractRenderItem(other)
{
    m_value = other.m_value;
    m_position = other.m_position;
    m_height = other.m_height;
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

//  from ../qtdatavis3d/src/datavisualization/engine/axisrendercache.cpp, line 78, as _ZN15AxisRenderCache9setLabelsERK5QListI7QStringE
inline void AxisRenderCache::setLabels(const QStringList &labels)
{
    if (m_labels != labels) {
        int newSize(labels.size());
        int oldSize(m_labels.size());

        for (int i = newSize; i < oldSize; i++)
            delete m_labelItems.takeLast();

        m_labelItems.reserve(newSize);

        int widest = maxLabelWidth(labels);

        for (int i = 0; i < newSize; i++) {
            if (i >= oldSize)
                m_labelItems.append(new LabelItem);
            if (m_drawer) {
                if (labels.at(i).isEmpty()) {
                    m_labelItems[i]->clear();
                } else if (i >= oldSize || labels.at(i) != m_labels.at(i)
                           || m_labelItems[i]->size().width() != widest) {
                    m_drawer->generateLabelItem(*m_labelItems[i], labels.at(i), widest);
                }
            }
        }
        m_labels = labels;
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

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 406, as _ZN18Abstract3DRenderer13reInitShadersEv
inline void Abstract3DRenderer::reInitShaders()
{
    if (!m_isOpenGLES) {
        if (m_cachedShadowQuality > QAbstract3DGraph::ShadowQualityNone) {
            if (m_cachedOptimizationHint.testFlag(QAbstract3DGraph::OptimizationStatic)
                    && qobject_cast<Scatter3DRenderer *>(this)) {
                initGradientShaders(QStringLiteral(":/shaders/vertexShadow"),
                                    QStringLiteral(":/shaders/fragmentShadow"));
                initStaticSelectedItemShaders(QStringLiteral(":/shaders/vertexShadow"),
                                              QStringLiteral(":/shaders/fragmentShadowNoTex"),
                                              QStringLiteral(":/shaders/vertexShadow"),
                                              QStringLiteral(":/shaders/fragmentShadowNoTexColorOnY"));
                initShaders(QStringLiteral(":/shaders/vertexShadowNoMatrices"),
                            QStringLiteral(":/shaders/fragmentShadowNoTex"));
            } else {
                initGradientShaders(QStringLiteral(":/shaders/vertexShadow"),
                                    QStringLiteral(":/shaders/fragmentShadowNoTexColorOnY"));
                initShaders(QStringLiteral(":/shaders/vertexShadow"),
                            QStringLiteral(":/shaders/fragmentShadowNoTex"));
            }
            initBackgroundShaders(QStringLiteral(":/shaders/vertexShadow"),
                                  QStringLiteral(":/shaders/fragmentShadowNoTex"));
            initCustomItemShaders(QStringLiteral(":/shaders/vertexShadow"),
                                  QStringLiteral(":/shaders/fragmentShadow"));
        } else {
            if (m_cachedOptimizationHint.testFlag(QAbstract3DGraph::OptimizationStatic)
                    && qobject_cast<Scatter3DRenderer *>(this)) {
                initGradientShaders(QStringLiteral(":/shaders/vertexTexture"),
                                    QStringLiteral(":/shaders/fragmentTexture"));
                initStaticSelectedItemShaders(QStringLiteral(":/shaders/vertex"),
                                              QStringLiteral(":/shaders/fragment"),
                                              QStringLiteral(":/shaders/vertex"),
                                              QStringLiteral(":/shaders/fragmentColorOnY"));
                initShaders(QStringLiteral(":/shaders/vertexNoMatrices"),
                            QStringLiteral(":/shaders/fragment"));
            } else {
                initGradientShaders(QStringLiteral(":/shaders/vertex"),
                                    QStringLiteral(":/shaders/fragmentColorOnY"));
                initShaders(QStringLiteral(":/shaders/vertex"),
                            QStringLiteral(":/shaders/fragment"));
            }
            initBackgroundShaders(QStringLiteral(":/shaders/vertex"),
                                  QStringLiteral(":/shaders/fragment"));
            initCustomItemShaders(QStringLiteral(":/shaders/vertexTexture"),
                                  QStringLiteral(":/shaders/fragmentTexture"));
        }
        initVolumeTextureShaders(QStringLiteral(":/shaders/vertexTexture3D"),
                                 QStringLiteral(":/shaders/fragmentTexture3D"),
                                 QStringLiteral(":/shaders/fragmentTexture3DLowDef"),
                                 QStringLiteral(":/shaders/fragmentTexture3DSlice"),
                                 QStringLiteral(":/shaders/vertexPosition"),
                                 QStringLiteral(":/shaders/fragment3DSliceFrames"));
    } else  {
        if (m_cachedOptimizationHint.testFlag(QAbstract3DGraph::OptimizationStatic)
                && qobject_cast<Scatter3DRenderer *>(this)) {
            initGradientShaders(QStringLiteral(":/shaders/vertexTexture"),
                                QStringLiteral(":/shaders/fragmentTextureES2"));
            initStaticSelectedItemShaders(QStringLiteral(":/shaders/vertex"),
                                          QStringLiteral(":/shaders/fragmentES2"),
                                          QStringLiteral(":/shaders/vertex"),
                                          QStringLiteral(":/shaders/fragmentColorOnYES2"));
            initShaders(QStringLiteral(":/shaders/vertexNoMatrices"),
                        QStringLiteral(":/shaders/fragmentES2"));
        } else {
            initGradientShaders(QStringLiteral(":/shaders/vertex"),
                                QStringLiteral(":/shaders/fragmentColorOnYES2"));
            initShaders(QStringLiteral(":/shaders/vertex"),
                        QStringLiteral(":/shaders/fragmentES2"));
        }
        initBackgroundShaders(QStringLiteral(":/shaders/vertex"),
                              QStringLiteral(":/shaders/fragmentES2"));
        initCustomItemShaders(QStringLiteral(":/shaders/vertexTexture"),
                              QStringLiteral(":/shaders/fragmentTextureES2"));
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 559, as _ZN18Abstract3DRenderer18calculateZoomLevelEv
inline void Abstract3DRenderer::calculateZoomLevel()
{
    // Calculate zoom level based on aspect ratio
    GLfloat div;
    GLfloat zoomAdjustment;
    div = qMin(m_primarySubViewport.width(), m_primarySubViewport.height());
    zoomAdjustment = defaultRatio
            * ((m_primarySubViewport.width() / div)
               / (m_primarySubViewport.height() / div));
    m_autoScaleAdjustment = qMin(zoomAdjustment, 1.0f); // clamp to 1.0f
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 767, as _ZN18Abstract3DRenderer23axisCacheForOrientationEN15QAbstract3DAxis15AxisOrientationE
inline AxisRenderCache &Abstract3DRenderer::axisCacheForOrientation(
        QAbstract3DAxis::AxisOrientation orientation)
{
    switch (orientation) {
    case QAbstract3DAxis::AxisOrientationX:
        return m_axisCacheX;
    case QAbstract3DAxis::AxisOrientationY:
        return m_axisCacheY;
    case QAbstract3DAxis::AxisOrientationZ:
        return m_axisCacheZ;
    default:
        qFatal("Abstract3DRenderer::axisCacheForOrientation");
        return m_axisCacheX;
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/abstract3drenderer.cpp, line 1214, as _ZN18Abstract3DRenderer34recalculateCustomItemScalingAndPosEP16CustomRenderItem
inline void Abstract3DRenderer::recalculateCustomItemScalingAndPos(CustomRenderItem *item)
{
    if (!m_polarGraph && !item->isLabel() && !item->isScalingAbsolute()
            && !item->isPositionAbsolute()) {
        QVector3D scale = item->origScaling() / 2.0f;
        QVector3D pos = item->origPosition();
        QVector3D minBounds(pos.x() - scale.x(),
                            pos.y() - scale.y(),
                            pos.z() + scale.z());
        QVector3D maxBounds(pos.x() + scale.x(),
                            pos.y() + scale.y(),
                            pos.z() - scale.z());
        QVector3D minCorner = convertPositionToTranslation(minBounds, false);
        QVector3D maxCorner = convertPositionToTranslation(maxBounds, false);
        scale = QVector3D(qAbs(maxCorner.x() - minCorner.x()),
                          qAbs(maxCorner.y() - minCorner.y()),
                          qAbs(maxCorner.z() - minCorner.z())) / 2.0f;
        if (item->isVolume()) {
            // Only volume items need to scale and reposition according to bounds
            QVector3D minBoundsNormal = minCorner;
            QVector3D maxBoundsNormal = maxCorner;
            // getVisibleItemBounds returns bounds normalized for fragment shader [-1,1]
            // Y and Z are also flipped.
            getVisibleItemBounds(minBoundsNormal, maxBoundsNormal);
            item->setMinBounds(minBoundsNormal);
            item->setMaxBounds(maxBoundsNormal);
            // For scaling calculations, we want [0,1] normalized values
            minBoundsNormal = item->minBoundsNormal();
            maxBoundsNormal = item->maxBoundsNormal();

            // Rescale and reposition the item so that it doesn't go over the edges
            QVector3D adjScaling =
                    QVector3D(scale.x() * (maxBoundsNormal.x() - minBoundsNormal.x()),
                              scale.y() * (maxBoundsNormal.y() - minBoundsNormal.y()),
                              scale.z() * (maxBoundsNormal.z() - minBoundsNormal.z()));

            item->setScaling(adjScaling);

            QVector3D adjPos = item->origPosition();
            QVector3D dataExtents = QVector3D(maxBounds.x() - minBounds.x(),
                                              maxBounds.y() - minBounds.y(),
                                              maxBounds.z() - minBounds.z()) / 2.0f;
            adjPos.setX(adjPos.x() + (dataExtents.x() * minBoundsNormal.x())
                        - (dataExtents.x() * (1.0f - maxBoundsNormal.x())));
            adjPos.setY(adjPos.y() + (dataExtents.y() * minBoundsNormal.y())
                        - (dataExtents.y() * (1.0f - maxBoundsNormal.y())));
            adjPos.setZ(adjPos.z() + (dataExtents.z() * minBoundsNormal.z())
                        - (dataExtents.z() * (1.0f - maxBoundsNormal.z())));
            item->setPosition(adjPos);
        } else {
            // Only scale for non-volume items, and do not readjust position
            item->setScaling(scale);
            item->setPosition(item->origPosition());
        }
    } else {
        item->setScaling(item->origScaling());
        item->setPosition(item->origPosition());
        if (item->isVolume()) {
            // Y and Z need to be flipped as shader flips those axes
            item->setMinBounds(QVector3D(-1.0f, 1.0f, 1.0f));
            item->setMaxBounds(QVector3D(1.0f, -1.0f, -1.0f));
        }
    }
    QVector3D translation = convertPositionToTranslation(item->position(),
                                                         item->isPositionAbsolute());
    item->setTranslation(translation);
}

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3ditem.cpp, line 497, as _ZN20QCustom3DItemPrivate12textureImageEv
inline QImage QCustom3DItemPrivate::textureImage()
{
    return m_textureImage;
}

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3ditem.cpp, line 502, as _ZN20QCustom3DItemPrivate17clearTextureImageEv
inline void QCustom3DItemPrivate::clearTextureImage()
{
    m_textureImage = QImage();
    m_textureFile.clear();
}

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3dlabel.cpp, line 342, as _ZN21QCustom3DLabelPrivate18createTextureImageERK6QColorS2_bb
inline void QCustom3DLabelPrivate::createTextureImage(const QColor &bgrColor, const QColor &txtColor,
                                               bool background, bool borders)
{
    m_textureImage = Utils::printTextToImage(m_font, m_text, bgrColor, txtColor, background,
                                             borders, 0);
}

//  from ../qtdatavis3d/src/datavisualization/data/qcustom3dlabel.cpp, line 337, as _ZN21QCustom3DLabelPrivate18createTextureImageEv
inline void QCustom3DLabelPrivate::createTextureImage()
{
    createTextureImage(m_bgrColor, m_txtColor, m_background, m_borders);
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxisformatter.cpp, line 364, as _ZN28QValue3DAxisFormatterPrivate12populateCopyER21QValue3DAxisFormatter
inline void QValue3DAxisFormatterPrivate::populateCopy(QValue3DAxisFormatter &copy)
{
    recalculate();
    q_ptr->populateCopy(copy);
}

//  from ../qtdatavis3d/src/datavisualization/engine/drawer.cpp, line 61, as _ZN6Drawer8setThemeEP8Q3DTheme
inline void Drawer::setTheme(Q3DTheme *theme)
{
    m_theme = theme;
    m_scaledFontSize = 0.05f + m_theme->font().pointSizeF() / 500.0f;
    emit drawerChanged();
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractrenderitem.cpp, line 12, as _ZN18AbstractRenderItemC2ERKS_
inline AbstractRenderItem::AbstractRenderItem(const AbstractRenderItem &other)
{
    m_translation = other.m_translation;
    m_rotation = other.m_rotation;
}

//  from ../qtdatavis3d/src/datavisualization/data/barrenderitem.cpp, line 23, as _ZN13BarRenderItemD1Ev
inline BarRenderItem::~BarRenderItem()
{
}

//  from ../qtdatavis3d/src/datavisualization/utils/objecthelper.cpp, line 28, as _ZN12ObjectHelper17resetObjectHelperEPK18Abstract3DRendererRPS_RK7QString
inline void ObjectHelper::resetObjectHelper(const Abstract3DRenderer *cacheId, ObjectHelper *&obj,
                                     const QString &meshFile)
{
    Q_ASSERT(cacheId);

    if (obj) {
        const QString &oldFile = obj->objectFile();
        if (meshFile == oldFile)
            return; // same file, do nothing
        releaseObjectHelper(cacheId, obj);
    }
    obj = getObjectHelper(cacheId, meshFile);
}

//  from ../qtdatavis3d/src/datavisualization/utils/texturehelper.cpp, line 334, as _ZN13TextureHelper17convertToGLFormatERK6QImage
inline QImage TextureHelper::convertToGLFormat(const QImage &srcImage)
{
    QImage res(srcImage.size(), QImage::Format_ARGB32);
    convertToGLFormatHelper(res, srcImage.convertToFormat(QImage::Format_ARGB32), GL_RGBA);
    return res;
}

//  from ../qtdatavis3d/src/datavisualization/data/customrenderitem.cpp, line 76, as _ZN16CustomRenderItem12setMaxBoundsERK9QVector3D
inline void CustomRenderItem::setMaxBounds(const QVector3D &bounds)
{
    m_maxBounds = bounds;
    m_maxBoundsNormal = m_maxBounds;
    m_maxBoundsNormal.setY(-m_maxBoundsNormal.y());
    m_maxBoundsNormal.setZ(-m_maxBoundsNormal.z());
    m_maxBoundsNormal = 0.5f * (m_maxBoundsNormal + oneVector);
}

//  from ../qtdatavis3d/src/datavisualization/data/customrenderitem.cpp, line 67, as _ZN16CustomRenderItem12setMinBoundsERK9QVector3D
inline void CustomRenderItem::setMinBounds(const QVector3D &bounds)
{
    m_minBounds = bounds;
    m_minBoundsNormal = m_minBounds;
    m_minBoundsNormal.setY(-m_minBoundsNormal.y());
    m_minBoundsNormal.setZ(-m_minBoundsNormal.z());
    m_minBoundsNormal = 0.5f * (m_minBoundsNormal + oneVector);
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractrenderitem.cpp, line 8, as _ZN18AbstractRenderItemC2Ev
inline AbstractRenderItem::AbstractRenderItem()
{
}

//  from ../qtdatavis3d/src/datavisualization/axis/qvalue3daxisformatter.cpp, line 311, as _ZN28QValue3DAxisFormatterPrivate11recalculateEv
inline void QValue3DAxisFormatterPrivate::recalculate()
{
    // Only recalculate if we need to and have m_axis pointer. If we do not have
    // m_axis, either we are not attached to an axis or this is a renderer cache.
    if (m_axis && m_needsRecalculate) {
        m_min = m_axis->min();
        m_max = m_axis->max();
        m_rangeNormalizer = (m_max - m_min);

        q_ptr->recalculate();
        m_needsRecalculate = false;
    }
}

//  from ../qtdatavis3d/src/datavisualization/utils/utils.cpp, line 25, as _ZN5Utils20getNearestPowerOfTwoEj
inline GLuint Utils::getNearestPowerOfTwo(GLuint value)
{
    GLuint powOfTwoValue = MIN_POWER;
    NUM_IN_POWER(powOfTwoValue, value);
    return powOfTwoValue;
}

//  from ../qtdatavis3d/src/datavisualization/engine/drawer.cpp, line 407, as _ZN6Drawer17generateLabelItemER9LabelItemRK7QStringi
inline void Drawer::generateLabelItem(LabelItem &item, const QString &text, int widestLabel)
{
    initializeOpenGL();

    item.clear();

    if (!text.isEmpty()) {
        // Create labels
        // Print label into a QImage using QPainter
        QImage label = Utils::printTextToImage(m_theme->font(),
                                               text,
                                               m_theme->labelBackgroundColor(),
                                               m_theme->labelTextColor(),
                                               m_theme->isLabelBackgroundEnabled(),
                                               m_theme->isLabelBorderEnabled(),
                                               widestLabel);

        // Set label size
        item.setSize(label.size());
        // Insert text texture into label (also deletes the old texture)
        item.setTextureId(m_textureHelper->create2DTexture(label, true, true));
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 40, as _ZN9LabelItem5clearEv
inline void LabelItem::clear()
{
    if (m_textureId && QOpenGLContext::currentContext())
        QOpenGLContext::currentContext()->functions()->glDeleteTextures(1, &m_textureId);
    m_textureId = 0;
    m_size = QSize(0, 0);
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 8, as _ZN9LabelItemC1Ev
inline LabelItem::LabelItem()
    : m_size(QSize(0, 0)),
      m_textureId(0)
{
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 14, as _ZN9LabelItemD1Ev
inline LabelItem::~LabelItem()
{
    clear();
}

//  from ../qtdatavis3d/src/datavisualization/engine/axisrendercache.cpp, line 173, as _ZNK15AxisRenderCache13maxLabelWidthERK5QListI7QStringE
inline int AxisRenderCache::maxLabelWidth(const QStringList &labels) const
{
    int labelWidth = 0;
    QFont labelFont = m_font;
    labelFont.setPointSize(textureFontSize);
    QFontMetrics labelFM(labelFont);
    for (int i = 0; i < labels.size(); i++) {
        int newWidth = labelFM.horizontalAdvance(labels.at(i));
        if (labelWidth < newWidth)
            labelWidth = newWidth;
    }
    return labelWidth;
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 24, as _ZNK9LabelItem4sizeEv
inline QSize LabelItem::size() const
{
    return m_size;
}

//  from ../qtdatavis3d/src/datavisualization/data/customrenderitem.cpp, line 40, as _ZN16CustomRenderItemD1Ev
inline CustomRenderItem::~CustomRenderItem()
{
    ObjectHelper::releaseObjectHelper(m_renderer, m_object);
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractrenderitem.cpp, line 18, as _ZN18AbstractRenderItemD2Ev
inline AbstractRenderItem::~AbstractRenderItem()
{
}

//  from ../qtdatavis3d/src/datavisualization/utils/texturehelper.cpp, line 341, as _ZN13TextureHelper23convertToGLFormatHelperER6QImageRKS0_j
inline void TextureHelper::convertToGLFormatHelper(QImage &dstImage, const QImage &srcImage,
                                            GLenum texture_format)
{
    Q_ASSERT(dstImage.depth() == 32);
    Q_ASSERT(srcImage.depth() == 32);

    if (dstImage.size() != srcImage.size()) {
        int target_width = dstImage.width();
        int target_height = dstImage.height();
        float sx = target_width / float(srcImage.width());
        float sy = target_height / float(srcImage.height());

        quint32 *dest = (quint32 *) dstImage.scanLine(0); // NB! avoid detach here
        uchar *srcPixels = (uchar *) srcImage.scanLine(srcImage.height() - 1);
        int sbpl = srcImage.bytesPerLine();
        int dbpl = dstImage.bytesPerLine();

        int ix = int(0x00010000 / sx);
        int iy = int(0x00010000 / sy);

        quint32 basex = int(0.5 * ix);
        quint32 srcy = int(0.5 * iy);

        // scale, swizzle and mirror in one loop
        while (target_height--) {
            const uint *src = (const quint32 *) (srcPixels - (srcy >> 16) * sbpl);
            int srcx = basex;
            for (int x=0; x<target_width; ++x) {
                dest[x] = qt_gl_convertToGLFormatHelper(src[srcx >> 16], texture_format);
                srcx += ix;
            }
            dest = (quint32 *)(((uchar *) dest) + dbpl);
            srcy += iy;
        }
    } else {
        const int width = srcImage.width();
        const int height = srcImage.height();
        const uint *p = (const uint*) srcImage.scanLine(srcImage.height() - 1);
        uint *q = (uint*) dstImage.scanLine(0);

#if !QT_CONFIG(opengles2)
        if (texture_format == GL_BGRA) {
#else
        if (texture_format == GL_BGRA8_EXT) {
#endif
            if (QSysInfo::ByteOrder == QSysInfo::BigEndian) {
                // mirror + swizzle
                for (int i=0; i < height; ++i) {
                    const uint *end = p + width;
                    while (p < end) {
                        *q = ((*p << 24) & 0xff000000)
                                | ((*p >> 24) & 0x000000ff)
                                | ((*p << 8) & 0x00ff0000)
                                | ((*p >> 8) & 0x0000ff00);
                        p++;
                        q++;
                    }
                    p -= 2 * width;
                }
            } else {
                const uint bytesPerLine = srcImage.bytesPerLine();
                for (int i=0; i < height; ++i) {
                    memcpy(q, p, bytesPerLine);
                    q += width;
                    p -= width;
                }
            }
        } else {
            if (QSysInfo::ByteOrder == QSysInfo::BigEndian) {
                for (int i=0; i < height; ++i) {
                    const uint *end = p + width;
                    while (p < end) {
                        *q = (*p << 8) | ((*p >> 24) & 0xff);
                        p++;
                        q++;
                    }
                    p -= 2 * width;
                }
            } else {
                for (int i=0; i < height; ++i) {
                    const uint *end = p + width;
                    while (p < end) {
                        *q = ((*p << 16) & 0xff0000) | ((*p >> 16) & 0xff) | (*p & 0xff00ff00);
                        p++;
                        q++;
                    }
                    p -= 2 * width;
                }
            }
        }
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/bars3drenderer.cpp, line 245, as _ZN14Bars3DRenderer15updateRenderRowEPK5QListI12QBarDataItemERS0_I13BarRenderItemE
inline void Bars3DRenderer::updateRenderRow(const QBarDataRow *dataRow, BarRenderItemRow &renderRow)
{
    int j = 0;
    int renderRowSize = renderRow.size();
    int startIndex = m_axisCacheX.min();

    if (dataRow) {
        int updateSize = qMin((dataRow->size() - startIndex), renderRowSize);
        int dataColIndex = startIndex;
        for (; j < updateSize ; j++) {
            updateRenderItem(dataRow->at(dataColIndex), renderRow[j]);
            dataColIndex++;
        }
    }
    for (; j < renderRowSize; j++) {
        renderRow[j].setValue(0.0f);
        renderRow[j].setHeight(0.0f);
        renderRow[j].setRotation(identityQuaternion);
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/bars3drenderer.cpp, line 266, as _ZN14Bars3DRenderer16updateRenderItemERK12QBarDataItemR13BarRenderItem
inline void Bars3DRenderer::updateRenderItem(const QBarDataItem &dataItem, BarRenderItem &renderItem)
{
    float value = dataItem.value();
    float heightValue = m_axisCacheY.formatter()->positionAt(value);
    if (m_noZeroInRange) {
        if (m_hasNegativeValues) {
            heightValue = -1.0f + heightValue;
            if (heightValue > 0.0f)
                heightValue = 0.0f;
        } else {
            if (heightValue < 0.0f)
                heightValue = 0.0f;
        }
    } else {
        heightValue -= m_zeroPosition;
    }
    if (m_axisCacheY.reversed())
        heightValue = -heightValue;

    renderItem.setValue(value);
    renderItem.setHeight(heightValue);

    float angle = dataItem.rotation();
    if (angle) {
        renderItem.setRotation(
                    QQuaternion::fromAxisAndAngle(
                        upVector, angle));
    } else {
        renderItem.setRotation(identityQuaternion);
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on Bars3DRenderer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnBars3DRenderer : Bars3DRenderer {
  using Bars3DRenderer::contextCleanup;
  using Bars3DRenderer::initializeOpenGL;
};

//  A Bars3DRenderer that Python can take functions over in. Every Bars3DRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteBars3DRendererCall0)(const void *, int *);
typedef void * (*CuteBars3DRendererCall1)(const void *, QAbstract3DSeries *, int *);
typedef void (*CuteBars3DRendererCall2)(const void *, Q3DScene *, int *);
typedef void (*CuteBars3DRendererCall3)(const void *, GLuint, int *);
typedef const QVector3D * (*CuteBars3DRendererCall4)(const void *, const QVector3D *, bool, int *);
typedef void (*CuteBars3DRendererCall5)(const void *, float, int *);
typedef void (*CuteBars3DRendererCall6)(const void *, float, int *);
typedef void (*CuteBars3DRendererCall7)(const void *, int *);
typedef void (*CuteBars3DRendererCall8)(const void *, int *);
typedef void (*CuteBars3DRendererCall9)(const void *, int, float, float, int *);
typedef void (*CuteBars3DRendererCall10)(const void *, int, bool, int *);
typedef void (*CuteBars3DRendererCall11)(const void *, const QString *, const QString *, int *);
typedef void (*CuteBars3DRendererCall12)(const void *, const QString *, const QString *, int *);
typedef void (*CuteBars3DRendererCall13)(const void *, int, int *);
typedef void (*CuteBars3DRendererCall14)(const void *, int *);
typedef void (*CuteBars3DRendererCall15)(const void *, const QString *, const QString *, int *);
typedef void (*CuteBars3DRendererCall16)(const void *, int *);
typedef void (*CuteBars3DRendererCall17)(const void *, int *);
typedef void (*CuteBars3DRendererCall18)(const void *, int *);
typedef void (*CuteBars3DRendererCall19)(const void *, int *);
typedef void (*CuteBars3DRendererCall20)(const void *, SeriesRenderCache *, int *);
typedef void (*CuteBars3DRendererCall21)(const void *, Q3DTheme *, int *);
typedef void (*CuteBars3DRendererCall22)(const void *, int, int *);
typedef void (*CuteBars3DRendererCall23)(const void *, int, int *);
typedef void (*CuteBars3DRendererCall24)(const void *, const QString *, const QString *, const QString *, const QString *, int *);
typedef void (*CuteBars3DRendererCall25)(const void *, const QString *, const QString *, int *);
typedef void (*CuteBars3DRendererCall26)(const void *, const QString *, const QString *, const QString *, const QString *, const QString *, const QString *, int *);
typedef void (*CuteBars3DRendererCall27)(const void *, const QString *, const QString *, int *);
typedef void (*CuteBars3DRendererCall28)(const void *, const QString *, const QString *, int *);
typedef void (*CuteBars3DRendererCall29)(const void *, int *);
typedef void (*CuteBars3DRendererCall30)(const void *, int, int, int *);
typedef void (*CuteBars3DRendererCall31)(const void *, int, const QString *, int *);
typedef void (*CuteBars3DRendererCall32)(const void *, int, int, int *);
typedef void (*CuteBars3DRendererCall33)(const void *, int, int, int *);
typedef void (*CuteBars3DRendererCall34)(const void *, int, const QString *, int *);
typedef void (*CuteBars3DRendererCall35)(const void *, int, QValue3DAxisFormatter *, int *);
typedef void (*CuteBars3DRendererCall36)(const void *, int, float, int *);
typedef void (*CuteBars3DRendererCall37)(const void *, int, bool, int *);
typedef void (*CuteBars3DRendererCall38)(const void *, int, bool, int *);
typedef void * (*CuteBars3DRendererCall39)(const void *, QCustom3DItem *, int *);
typedef void (*CuteBars3DRendererCall40)(const void *, CustomRenderItem *, int *);
typedef void (*CuteBars3DRendererCall41)(const void *, float, int *);
typedef void (*CuteBars3DRendererCall42)(const void *, bool, int *);
typedef void (*CuteBars3DRendererCall43)(const void *, float, int *);
typedef void (*CuteBars3DRendererCall44)(const void *, int *);
typedef void (*CuteBars3DRendererCall45)(const void *, int *);
typedef void (*CuteBars3DRendererCall46)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteBars3DRendererCall47)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteBars3DRendererCall48)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBars3DRendererCall49)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBars3DRendererCall50)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBars3DRendererCall51)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBars3DRendererCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteBars3DRendererCall53)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteBars3DRenderer : public Bars3DRenderer {
public:
  using Bars3DRenderer::Bars3DRenderer;
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
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer11updateSceneEP8Q3DScene")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer6renderEj")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer28convertPositionToTranslationERK9QVector3Db")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer17updateAspectRatioEf")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer12updateMarginEf")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer14contextCleanupEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer16initializeOpenGLEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer15updateAxisRangeEN15QAbstract3DAxis15AxisOrientationEff")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer18updateAxisReversedEN15QAbstract3DAxis15AxisOrientationEb")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer11initShadersERK7QStringS2_")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer19initGradientShadersERK7QStringS2_")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer19updateShadowQualityEN16QAbstract3DGraph13ShadowQualityE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer14updateTexturesEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer21initBackgroundShadersERK7QStringS2_")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer19initSelectionBufferEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer17updateDepthBufferEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer17updateCustomItemsEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer25updateCustomItemPositionsEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer10cleanCacheEP17SeriesRenderCache")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer11updateThemeEP8Q3DTheme")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer19updateSelectionModeE6QFlagsIN16QAbstract3DGraph13SelectionFlagEE")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer22updateOptimizationHintE6QFlagsIN16QAbstract3DGraph16OptimizationHintEE")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer29initStaticSelectedItemShadersERK7QStringS2_S2_S2_")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer21initCustomItemShadersERK7QStringS2_")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer24initVolumeTextureShadersERK7QStringS2_S2_S2_S2_S2_")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer16initLabelShadersERK7QStringS2_")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer25initCursorPositionShadersERK7QStringS2_")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer24initCursorPositionBufferEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer14updateAxisTypeEN15QAbstract3DAxis15AxisOrientationENS0_8AxisTypeE")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer15updateAxisTitleEN15QAbstract3DAxis15AxisOrientationERK7QString")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer22updateAxisSegmentCountEN15QAbstract3DAxis15AxisOrientationEi")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer25updateAxisSubSegmentCountEN15QAbstract3DAxis15AxisOrientationEi")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer21updateAxisLabelFormatEN15QAbstract3DAxis15AxisOrientationERK7QString")) {
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
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer25updateAxisTitleVisibilityEN15QAbstract3DAxis15AxisOrientationEb")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer20updateAxisTitleFixedEN15QAbstract3DAxis15AxisOrientationEb")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer13addCustomItemEP13QCustom3DItem")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18Abstract3DRenderer16updateCustomItemEP16CustomRenderItem")) {
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

  //  void Bars3DRenderer::updateData()
  void updateData() override {
    if (taken[0]) {
      int handled = 0;
      CuteBars3DRendererCall0 call = reinterpret_cast<CuteBars3DRendererCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Bars3DRenderer::updateData();
  }

  //  SeriesRenderCache *Bars3DRenderer::createNewCache(QAbstract3DSeries
  //      *series)
  SeriesRenderCache *createNewCache(QAbstract3DSeries *series) override {
    if (taken[1]) {
      int handled = 0;
      CuteBars3DRendererCall1 call = reinterpret_cast<CuteBars3DRendererCall1>(taken[1]);
      void * given = call(this, series, &handled);
      if (handled) return static_cast<SeriesRenderCache *>(given);
    }
    return Bars3DRenderer::createNewCache(series);
  }

  //  void Bars3DRenderer::updateScene(Q3DScene *scene)
  void updateScene(Q3DScene *scene) override {
    if (taken[2]) {
      int handled = 0;
      CuteBars3DRendererCall2 call = reinterpret_cast<CuteBars3DRendererCall2>(taken[2]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Bars3DRenderer::updateScene(scene);
  }

  //  void Bars3DRenderer::render(GLuint defaultFboHandle)
  void render(GLuint defaultFboHandle) override {
    if (taken[3]) {
      int handled = 0;
      CuteBars3DRendererCall3 call = reinterpret_cast<CuteBars3DRendererCall3>(taken[3]);
      call(this, defaultFboHandle, &handled);
      if (handled) return;
    }
    Bars3DRenderer::render(defaultFboHandle);
  }

  //  QVector3D Bars3DRenderer::convertPositionToTranslation(const
  //      QVector3D &position, bool isAbsolute)
  QVector3D convertPositionToTranslation(
      const QVector3D &position,
      bool isAbsolute) override {
    if (taken[4]) {
      int handled = 0;
      CuteBars3DRendererCall4 call = reinterpret_cast<CuteBars3DRendererCall4>(taken[4]);
      const QVector3D * given = call(this, &position, isAbsolute, &handled);
      if (handled && given) return *given;
    }
    return Bars3DRenderer::convertPositionToTranslation(position, isAbsolute);
  }

  //  void Bars3DRenderer::updateAspectRatio(float ratio)
  void updateAspectRatio(float ratio) override {
    if (taken[5]) {
      int handled = 0;
      CuteBars3DRendererCall5 call = reinterpret_cast<CuteBars3DRendererCall5>(taken[5]);
      call(this, ratio, &handled);
      if (handled) return;
    }
    Bars3DRenderer::updateAspectRatio(ratio);
  }

  //  void Bars3DRenderer::updateMargin(float margin)
  void updateMargin(float margin) override {
    if (taken[6]) {
      int handled = 0;
      CuteBars3DRendererCall6 call = reinterpret_cast<CuteBars3DRendererCall6>(taken[6]);
      call(this, margin, &handled);
      if (handled) return;
    }
    Bars3DRenderer::updateMargin(margin);
  }

  //  void Bars3DRenderer::contextCleanup()
  void contextCleanup() override {
    if (taken[7]) {
      int handled = 0;
      CuteBars3DRendererCall7 call = reinterpret_cast<CuteBars3DRendererCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    Bars3DRenderer::contextCleanup();
  }

  //  void Bars3DRenderer::initializeOpenGL()
  void initializeOpenGL() override {
    if (taken[8]) {
      int handled = 0;
      CuteBars3DRendererCall8 call = reinterpret_cast<CuteBars3DRendererCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    Bars3DRenderer::initializeOpenGL();
  }

  //  void Bars3DRenderer::updateAxisRange(QAbstract3DAxis::AxisOrientation
  //      orientation, float min, float max)
  void updateAxisRange(
      QAbstract3DAxis::AxisOrientation orientation,
      float min,
      float max) override {
    if (taken[9]) {
      int handled = 0;
      CuteBars3DRendererCall9 call = reinterpret_cast<CuteBars3DRendererCall9>(taken[9]);
      call(this, static_cast<int>(orientation), min, max, &handled);
      if (handled) return;
    }
    Bars3DRenderer::updateAxisRange(orientation, min, max);
  }

  //  void
  //      Bars3DRenderer::updateAxisReversed(QAbstract3DAxis::AxisOrientati
  //      on orientation, bool enable)
  void updateAxisReversed(
      QAbstract3DAxis::AxisOrientation orientation,
      bool enable) override {
    if (taken[10]) {
      int handled = 0;
      CuteBars3DRendererCall10 call = reinterpret_cast<CuteBars3DRendererCall10>(taken[10]);
      call(this, static_cast<int>(orientation), enable, &handled);
      if (handled) return;
    }
    Bars3DRenderer::updateAxisReversed(orientation, enable);
  }

  //  void Bars3DRenderer::initShaders(const QString &vertexShader, const
  //      QString &fragmentShader)
  void initShaders(
      const QString &vertexShader,
      const QString &fragmentShader) override {
    if (taken[11]) {
      int handled = 0;
      CuteBars3DRendererCall11 call = reinterpret_cast<CuteBars3DRendererCall11>(taken[11]);
      call(this, &vertexShader, &fragmentShader, &handled);
      if (handled) return;
    }
    Bars3DRenderer::initShaders(vertexShader, fragmentShader);
  }

  //  void Bars3DRenderer::initGradientShaders(const QString &vertexShader,
  //      const QString &fragmentShader)
  void initGradientShaders(
      const QString &vertexShader,
      const QString &fragmentShader) override {
    if (taken[12]) {
      int handled = 0;
      CuteBars3DRendererCall12 call = reinterpret_cast<CuteBars3DRendererCall12>(taken[12]);
      call(this, &vertexShader, &fragmentShader, &handled);
      if (handled) return;
    }
    Bars3DRenderer::initGradientShaders(vertexShader, fragmentShader);
  }

  //  void
  //      Bars3DRenderer::updateShadowQuality(QAbstract3DGraph::ShadowQuali
  //      ty quality)
  void updateShadowQuality(
      QAbstract3DGraph::ShadowQuality quality) override {
    if (taken[13]) {
      int handled = 0;
      CuteBars3DRendererCall13 call = reinterpret_cast<CuteBars3DRendererCall13>(taken[13]);
      call(this, static_cast<int>(quality), &handled);
      if (handled) return;
    }
    Bars3DRenderer::updateShadowQuality(quality);
  }

  //  void Bars3DRenderer::updateTextures()
  void updateTextures() override {
    if (taken[14]) {
      int handled = 0;
      CuteBars3DRendererCall14 call = reinterpret_cast<CuteBars3DRendererCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    Bars3DRenderer::updateTextures();
  }

  //  void Bars3DRenderer::initBackgroundShaders(const QString
  //      &vertexShader, const QString &fragmentShader)
  void initBackgroundShaders(
      const QString &vertexShader,
      const QString &fragmentShader) override {
    if (taken[15]) {
      int handled = 0;
      CuteBars3DRendererCall15 call = reinterpret_cast<CuteBars3DRendererCall15>(taken[15]);
      call(this, &vertexShader, &fragmentShader, &handled);
      if (handled) return;
    }
    Bars3DRenderer::initBackgroundShaders(vertexShader, fragmentShader);
  }

  //  void Bars3DRenderer::initSelectionBuffer()
  void initSelectionBuffer() override {
    if (taken[16]) {
      int handled = 0;
      CuteBars3DRendererCall16 call = reinterpret_cast<CuteBars3DRendererCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    Bars3DRenderer::initSelectionBuffer();
  }

  //  void Bars3DRenderer::updateDepthBuffer()
  void updateDepthBuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteBars3DRendererCall17 call = reinterpret_cast<CuteBars3DRendererCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    Bars3DRenderer::updateDepthBuffer();
  }

  //  void Abstract3DRenderer::updateCustomItems()
  void updateCustomItems() override {
    if (taken[18]) {
      int handled = 0;
      CuteBars3DRendererCall18 call = reinterpret_cast<CuteBars3DRendererCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateCustomItems();
  }

  //  void Abstract3DRenderer::updateCustomItemPositions()
  void updateCustomItemPositions() override {
    if (taken[19]) {
      int handled = 0;
      CuteBars3DRendererCall19 call = reinterpret_cast<CuteBars3DRendererCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateCustomItemPositions();
  }

  //  void Abstract3DRenderer::cleanCache(SeriesRenderCache *cache)
  void cleanCache(SeriesRenderCache *cache) override {
    if (taken[20]) {
      int handled = 0;
      CuteBars3DRendererCall20 call = reinterpret_cast<CuteBars3DRendererCall20>(taken[20]);
      call(this, cache, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::cleanCache(cache);
  }

  //  void Abstract3DRenderer::updateTheme(Q3DTheme *theme)
  void updateTheme(Q3DTheme *theme) override {
    if (taken[21]) {
      int handled = 0;
      CuteBars3DRendererCall21 call = reinterpret_cast<CuteBars3DRendererCall21>(taken[21]);
      call(this, theme, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateTheme(theme);
  }

  //  void Abstract3DRenderer::updateSelectionMode(QAbstract3DGraph::Select
  //      ionFlags newMode)
  void updateSelectionMode(
      QAbstract3DGraph::SelectionFlags newMode) override {
    if (taken[22]) {
      int handled = 0;
      CuteBars3DRendererCall22 call = reinterpret_cast<CuteBars3DRendererCall22>(taken[22]);
      call(this, static_cast<int>(newMode.toInt()), &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateSelectionMode(newMode);
  }

  //  void Abstract3DRenderer::updateOptimizationHint(QAbstract3DGraph::Opt
  //      imizationHints hint)
  void updateOptimizationHint(
      QAbstract3DGraph::OptimizationHints hint) override {
    if (taken[23]) {
      int handled = 0;
      CuteBars3DRendererCall23 call = reinterpret_cast<CuteBars3DRendererCall23>(taken[23]);
      call(this, static_cast<int>(hint.toInt()), &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateOptimizationHint(hint);
  }

  //  void Abstract3DRenderer::initStaticSelectedItemShaders(const QString
  //      &vertexShader, const QString &fragmentShader, const QString
  //      &gradientVertexShader, const QString &gradientFragmentShader)
  void initStaticSelectedItemShaders(
      const QString &vertexShader,
      const QString &fragmentShader,
      const QString &gradientVertexShader,
      const QString &gradientFragmentShader) override {
    if (taken[24]) {
      int handled = 0;
      CuteBars3DRendererCall24 call = reinterpret_cast<CuteBars3DRendererCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteBars3DRendererCall25 call = reinterpret_cast<CuteBars3DRendererCall25>(taken[25]);
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
    if (taken[26]) {
      int handled = 0;
      CuteBars3DRendererCall26 call = reinterpret_cast<CuteBars3DRendererCall26>(taken[26]);
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
    if (taken[27]) {
      int handled = 0;
      CuteBars3DRendererCall27 call = reinterpret_cast<CuteBars3DRendererCall27>(taken[27]);
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
    if (taken[28]) {
      int handled = 0;
      CuteBars3DRendererCall28 call = reinterpret_cast<CuteBars3DRendererCall28>(taken[28]);
      call(this, &vertexShader, &fragmentShader, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::initCursorPositionShaders(vertexShader, fragmentShader);
  }

  //  void Abstract3DRenderer::initCursorPositionBuffer()
  void initCursorPositionBuffer() override {
    if (taken[29]) {
      int handled = 0;
      CuteBars3DRendererCall29 call = reinterpret_cast<CuteBars3DRendererCall29>(taken[29]);
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
    if (taken[30]) {
      int handled = 0;
      CuteBars3DRendererCall30 call = reinterpret_cast<CuteBars3DRendererCall30>(taken[30]);
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
    if (taken[31]) {
      int handled = 0;
      CuteBars3DRendererCall31 call = reinterpret_cast<CuteBars3DRendererCall31>(taken[31]);
      call(this, static_cast<int>(orientation), &title, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateAxisTitle(orientation, title);
  }

  //  void Abstract3DRenderer::updateAxisSegmentCount(QAbstract3DAxis::Axis
  //      Orientation orientation, int count)
  void updateAxisSegmentCount(
      QAbstract3DAxis::AxisOrientation orientation,
      int count) override {
    if (taken[32]) {
      int handled = 0;
      CuteBars3DRendererCall32 call = reinterpret_cast<CuteBars3DRendererCall32>(taken[32]);
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
    if (taken[33]) {
      int handled = 0;
      CuteBars3DRendererCall33 call = reinterpret_cast<CuteBars3DRendererCall33>(taken[33]);
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
    if (taken[34]) {
      int handled = 0;
      CuteBars3DRendererCall34 call = reinterpret_cast<CuteBars3DRendererCall34>(taken[34]);
      call(this, static_cast<int>(orientation), &format, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateAxisLabelFormat(orientation, format);
  }

  //  void Abstract3DRenderer::updateAxisFormatter(QAbstract3DAxis::AxisOri
  //      entation orientation, QValue3DAxisFormatter *formatter)
  void updateAxisFormatter(
      QAbstract3DAxis::AxisOrientation orientation,
      QValue3DAxisFormatter *formatter) override {
    if (taken[35]) {
      int handled = 0;
      CuteBars3DRendererCall35 call = reinterpret_cast<CuteBars3DRendererCall35>(taken[35]);
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
      CuteBars3DRendererCall36 call = reinterpret_cast<CuteBars3DRendererCall36>(taken[36]);
      call(this, static_cast<int>(orientation), angle, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateAxisLabelAutoRotation(orientation, angle);
  }

  //  void Abstract3DRenderer::updateAxisTitleVisibility(QAbstract3DAxis::A
  //      xisOrientation orientation, bool visible)
  void updateAxisTitleVisibility(
      QAbstract3DAxis::AxisOrientation orientation,
      bool visible) override {
    if (taken[37]) {
      int handled = 0;
      CuteBars3DRendererCall37 call = reinterpret_cast<CuteBars3DRendererCall37>(taken[37]);
      call(this, static_cast<int>(orientation), visible, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateAxisTitleVisibility(orientation, visible);
  }

  //  void Abstract3DRenderer::updateAxisTitleFixed(QAbstract3DAxis::AxisOr
  //      ientation orientation, bool fixed)
  void updateAxisTitleFixed(
      QAbstract3DAxis::AxisOrientation orientation,
      bool fixed) override {
    if (taken[38]) {
      int handled = 0;
      CuteBars3DRendererCall38 call = reinterpret_cast<CuteBars3DRendererCall38>(taken[38]);
      call(this, static_cast<int>(orientation), fixed, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateAxisTitleFixed(orientation, fixed);
  }

  //  CustomRenderItem *Abstract3DRenderer::addCustomItem(QCustom3DItem
  //      *item)
  CustomRenderItem *addCustomItem(QCustom3DItem *item) override {
    if (taken[39]) {
      int handled = 0;
      CuteBars3DRendererCall39 call = reinterpret_cast<CuteBars3DRendererCall39>(taken[39]);
      void * given = call(this, item, &handled);
      if (handled) return static_cast<CustomRenderItem *>(given);
    }
    return Abstract3DRenderer::addCustomItem(item);
  }

  //  void Abstract3DRenderer::updateCustomItem(CustomRenderItem
  //      *renderItem)
  void updateCustomItem(CustomRenderItem *renderItem) override {
    if (taken[40]) {
      int handled = 0;
      CuteBars3DRendererCall40 call = reinterpret_cast<CuteBars3DRendererCall40>(taken[40]);
      call(this, renderItem, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateCustomItem(renderItem);
  }

  //  void Abstract3DRenderer::updateHorizontalAspectRatio(float ratio)
  void updateHorizontalAspectRatio(float ratio) override {
    if (taken[41]) {
      int handled = 0;
      CuteBars3DRendererCall41 call = reinterpret_cast<CuteBars3DRendererCall41>(taken[41]);
      call(this, ratio, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateHorizontalAspectRatio(ratio);
  }

  //  void Abstract3DRenderer::updatePolar(bool enable)
  void updatePolar(bool enable) override {
    if (taken[42]) {
      int handled = 0;
      CuteBars3DRendererCall42 call = reinterpret_cast<CuteBars3DRendererCall42>(taken[42]);
      call(this, enable, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updatePolar(enable);
  }

  //  void Abstract3DRenderer::updateRadialLabelOffset(float offset)
  void updateRadialLabelOffset(float offset) override {
    if (taken[43]) {
      int handled = 0;
      CuteBars3DRendererCall43 call = reinterpret_cast<CuteBars3DRendererCall43>(taken[43]);
      call(this, offset, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::updateRadialLabelOffset(offset);
  }

  //  void Abstract3DRenderer::handleShadowQualityChange()
  void handleShadowQualityChange() override {
    if (taken[44]) {
      int handled = 0;
      CuteBars3DRendererCall44 call = reinterpret_cast<CuteBars3DRendererCall44>(taken[44]);
      call(this, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::handleShadowQualityChange();
  }

  //  void Abstract3DRenderer::handleResize()
  void handleResize() override {
    if (taken[45]) {
      int handled = 0;
      CuteBars3DRendererCall45 call = reinterpret_cast<CuteBars3DRendererCall45>(taken[45]);
      call(this, &handled);
      if (handled) return;
    }
    Abstract3DRenderer::handleResize();
  }

  //  void Abstract3DRenderer::lowerShadowQuality()
  void lowerShadowQuality() override {
    if (taken[46]) {
      int handled = 0;
      CuteBars3DRendererCall46 call = reinterpret_cast<CuteBars3DRendererCall46>(taken[46]);
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
      CuteBars3DRendererCall47 call = reinterpret_cast<CuteBars3DRendererCall47>(taken[47]);
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
      CuteBars3DRendererCall48 call = reinterpret_cast<CuteBars3DRendererCall48>(taken[48]);
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
      CuteBars3DRendererCall49 call = reinterpret_cast<CuteBars3DRendererCall49>(taken[49]);
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
      CuteBars3DRendererCall50 call = reinterpret_cast<CuteBars3DRendererCall50>(taken[50]);
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
      CuteBars3DRendererCall51 call = reinterpret_cast<CuteBars3DRendererCall51>(taken[51]);
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
      CuteBars3DRendererCall52 call = reinterpret_cast<CuteBars3DRendererCall52>(taken[52]);
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
      CuteBars3DRendererCall53 call = reinterpret_cast<CuteBars3DRendererCall53>(taken[53]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Bars3DRenderer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14Bars3DRenderer10metaObjectEv(
    const Bars3DRenderer *self) {
  return self->metaObject();
}

//  void *Bars3DRenderer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14Bars3DRenderer11qt_metacastEPKc(
    Bars3DRenderer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Bars3DRenderer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14Bars3DRenderer11qt_metacallEN11QMetaObject4CallEiPPv(
    Bars3DRenderer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Bars3DRenderer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14Bars3DRenderer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Bars3DRenderer::tr(s, c, n));
}

//  Bars3DRenderer::~Bars3DRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRendererD1Ev(Bars3DRenderer *self) {
  delete self;
}

//  void Bars3DRenderer::updateData()
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer10updateDataEv(Bars3DRenderer *self) {
  self->updateData();
}

//  void Bars3DRenderer::updateSeries(const QList<QAbstract3DSeries *>
//      &seriesList)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer12updateSeriesERK5QListIP17QAbstract3DSeriesE(
    Bars3DRenderer *self,
    const QList<QAbstract3DSeries *> *seriesList) {
  self->updateSeries(*seriesList);
}

//  SeriesRenderCache *Bars3DRenderer::createNewCache(QAbstract3DSeries
//      *series)
extern "C" Q_DECL_EXPORT
SeriesRenderCache *ritual_ZN14Bars3DRenderer14createNewCacheEP17QAbstract3DSeries(
    Bars3DRenderer *self,
    QAbstract3DSeries *series) {
  return self->createNewCache(series);
}

//  void Bars3DRenderer::updateRows(const QList<Bars3DController::ChangeRow>
//      &rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer10updateRowsERK5QListIN16Bars3DController9ChangeRowEE(
    Bars3DRenderer *self,
    const QList<Bars3DController::ChangeRow> *rows) {
  self->updateRows(*rows);
}

//  void Bars3DRenderer::updateItems(const
//      QList<Bars3DController::ChangeItem> &items)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer11updateItemsERK5QListIN16Bars3DController10ChangeItemEE(
    Bars3DRenderer *self,
    const QList<Bars3DController::ChangeItem> *items) {
  self->updateItems(*items);
}

//  void Bars3DRenderer::updateScene(Q3DScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer11updateSceneEP8Q3DScene(
    Bars3DRenderer *self,
    Q3DScene *scene) {
  self->updateScene(scene);
}

//  void Bars3DRenderer::render(GLuint defaultFboHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer6renderEj(
    Bars3DRenderer *self,
    GLuint defaultFboHandle) {
  self->render(defaultFboHandle);
}

//  QVector3D Bars3DRenderer::convertPositionToTranslation(const QVector3D
//      &position, bool isAbsolute)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN14Bars3DRenderer28convertPositionToTranslationERK9QVector3Db(
    Bars3DRenderer *self,
    const QVector3D *position,
    bool isAbsolute) {
  return new QVector3D(
      self->convertPositionToTranslation(
          *position,
          isAbsolute));
}

//  void Bars3DRenderer::updateAspectRatio(float ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer17updateAspectRatioEf(
    Bars3DRenderer *self,
    float ratio) {
  self->updateAspectRatio(ratio);
}

//  void Bars3DRenderer::updateFloorLevel(float level)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer16updateFloorLevelEf(
    Bars3DRenderer *self,
    float level) {
  self->updateFloorLevel(level);
}

//  void Bars3DRenderer::updateMargin(float margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer12updateMarginEf(
    Bars3DRenderer *self,
    float margin) {
  self->updateMargin(margin);
}

//  void Bars3DRenderer::contextCleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer14contextCleanupEv(Bars3DRenderer *self) {
  self->contextCleanup();
}

//  void Bars3DRenderer::initializeOpenGL()
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer16initializeOpenGLEv(Bars3DRenderer *self) {
  self->initializeOpenGL();
}

//  void Bars3DRenderer::fixCameraTarget(QVector3D &target)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer15fixCameraTargetER9QVector3D(
    Bars3DRenderer *self,
    QVector3D *target) {
  self->fixCameraTarget(*target);
}

//  void Bars3DRenderer::getVisibleItemBounds(QVector3D &minBounds, QVector3D
//      &maxBounds)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer20getVisibleItemBoundsER9QVector3DS1_(
    Bars3DRenderer *self,
    QVector3D *minBounds,
    QVector3D *maxBounds) {
  self->getVisibleItemBounds(*minBounds, *maxBounds);
}

//  void Bars3DRenderer::updateMultiSeriesScaling(bool uniform)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer24updateMultiSeriesScalingEb(
    Bars3DRenderer *self,
    bool uniform) {
  self->updateMultiSeriesScaling(uniform);
}

//  void Bars3DRenderer::updateBarSpecs(GLfloat thicknessRatio, const QSizeF
//      &spacing, bool relative)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer14updateBarSpecsEfRK6QSizeFb(
    Bars3DRenderer *self,
    GLfloat thicknessRatio,
    const QSizeF *spacing,
    bool relative) {
  self->updateBarSpecs(thicknessRatio, *spacing, relative);
}

//  void Bars3DRenderer::updateBarSeriesMargin(const QSizeF &margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer21updateBarSeriesMarginERK6QSizeF(
    Bars3DRenderer *self,
    const QSizeF *margin) {
  self->updateBarSeriesMargin(*margin);
}

//  void Bars3DRenderer::updateSlicingActive(bool isSlicing)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer19updateSlicingActiveEb(
    Bars3DRenderer *self,
    bool isSlicing) {
  self->updateSlicingActive(isSlicing);
}

//  void Bars3DRenderer::updateSelectedBar(const QPoint &position,
//      QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer17updateSelectedBarERK6QPointP12QBar3DSeries(
    Bars3DRenderer *self,
    const QPoint *position,
    QBar3DSeries *series) {
  self->updateSelectedBar(*position, series);
}

//  QPoint Bars3DRenderer::clickedPosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK14Bars3DRenderer15clickedPositionEv(
    const Bars3DRenderer *self) {
  return new QPoint(self->clickedPosition());
}

//  void Bars3DRenderer::resetClickedStatus()
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer18resetClickedStatusEv(Bars3DRenderer *self) {
  self->resetClickedStatus();
}

//  void Bars3DRenderer::updateAxisRange(QAbstract3DAxis::AxisOrientation
//      orientation, float min, float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer15updateAxisRangeEN15QAbstract3DAxis15AxisOrientationEff(
    Bars3DRenderer *self,
    QAbstract3DAxis::AxisOrientation orientation,
    float min,
    float max) {
  self->updateAxisRange(orientation, min, max);
}

//  void Bars3DRenderer::updateAxisReversed(QAbstract3DAxis::AxisOrientation
//      orientation, bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer18updateAxisReversedEN15QAbstract3DAxis15AxisOrientationEb(
    Bars3DRenderer *self,
    QAbstract3DAxis::AxisOrientation orientation,
    bool enable) {
  self->updateAxisReversed(orientation, enable);
}

//  void Bars3DRenderer::initShaders(const QString &vertexShader, const
//      QString &fragmentShader)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer11initShadersERK7QStringS2_(
    Bars3DRenderer *self,
    const QString *vertexShader,
    const QString *fragmentShader) {
  self->initShaders(*vertexShader, *fragmentShader);
}

//  void Bars3DRenderer::initGradientShaders(const QString &vertexShader,
//      const QString &fragmentShader)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer19initGradientShadersERK7QStringS2_(
    Bars3DRenderer *self,
    const QString *vertexShader,
    const QString *fragmentShader) {
  self->initGradientShaders(*vertexShader, *fragmentShader);
}

//  void Bars3DRenderer::updateShadowQuality(QAbstract3DGraph::ShadowQuality
//      quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer19updateShadowQualityEN16QAbstract3DGraph13ShadowQualityE(
    Bars3DRenderer *self,
    QAbstract3DGraph::ShadowQuality quality) {
  self->updateShadowQuality(quality);
}

//  void Bars3DRenderer::updateTextures()
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer14updateTexturesEv(Bars3DRenderer *self) {
  self->updateTextures();
}

//  void Bars3DRenderer::fixMeshFileName(QString &fileName,
//      QAbstract3DSeries::Mesh mesh)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer15fixMeshFileNameER7QStringN17QAbstract3DSeries4MeshE(
    Bars3DRenderer *self,
    QString *fileName,
    QAbstract3DSeries::Mesh mesh) {
  self->fixMeshFileName(*fileName, mesh);
}

//  void Bars3DRenderer::drawSlicedScene()
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer15drawSlicedSceneEv(Bars3DRenderer *self) {
  self->drawSlicedScene();
}

//  void Bars3DRenderer::drawScene(GLuint defaultFboHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer9drawSceneEj(
    Bars3DRenderer *self,
    GLuint defaultFboHandle) {
  self->drawScene(defaultFboHandle);
}

//  void Bars3DRenderer::drawLabels(bool drawSelection, const Q3DCamera
//      *activeCamera, const QMatrix4x4 &viewMatrix, const QMatrix4x4
//      &projectionMatrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer10drawLabelsEbPK9Q3DCameraRK10QMatrix4x4S5_(
    Bars3DRenderer *self,
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

//  bool Bars3DRenderer::drawBars(BarRenderItem **selectedBar, const
//      QMatrix4x4 &depthProjectionViewMatrix, const QMatrix4x4
//      &projectionViewMatrix, const QMatrix4x4 &viewMatrix, GLint startRow,
//      GLint stopRow, GLint stepRow, GLint startBar, GLint stopBar, GLint
//      stepBar, GLfloat reflection)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14Bars3DRenderer8drawBarsEPP13BarRenderItemRK10QMatrix4x4S5_S5_iiiiiif(
    Bars3DRenderer *self,
    BarRenderItem **selectedBar,
    const QMatrix4x4 *depthProjectionViewMatrix,
    const QMatrix4x4 *projectionViewMatrix,
    const QMatrix4x4 *viewMatrix,
    GLint startRow,
    GLint stopRow,
    GLint stepRow,
    GLint startBar,
    GLint stopBar,
    GLint stepBar,
    GLfloat reflection) {
  return self->drawBars(
      selectedBar,
      *depthProjectionViewMatrix,
      *projectionViewMatrix,
      *viewMatrix,
      startRow,
      stopRow,
      stepRow,
      startBar,
      stopBar,
      stepBar,
      reflection);
}

//  void Bars3DRenderer::drawBackground(GLfloat backgroundRotation, const
//      QMatrix4x4 &depthProjectionViewMatrix, const QMatrix4x4
//      &projectionViewMatrix, const QMatrix4x4 &viewMatrix, bool
//      reflectingDraw, bool drawingSelectionBuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer14drawBackgroundEfRK10QMatrix4x4S2_S2_bb(
    Bars3DRenderer *self,
    GLfloat backgroundRotation,
    const QMatrix4x4 *depthProjectionViewMatrix,
    const QMatrix4x4 *projectionViewMatrix,
    const QMatrix4x4 *viewMatrix,
    bool reflectingDraw,
    bool drawingSelectionBuffer) {
  self->drawBackground(
      backgroundRotation,
      *depthProjectionViewMatrix,
      *projectionViewMatrix,
      *viewMatrix,
      reflectingDraw,
      drawingSelectionBuffer);
}

//  void Bars3DRenderer::drawGridLines(const QMatrix4x4
//      &depthProjectionViewMatrix, const QMatrix4x4 &projectionViewMatrix,
//      const QMatrix4x4 &viewMatrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer13drawGridLinesERK10QMatrix4x4S2_S2_(
    Bars3DRenderer *self,
    const QMatrix4x4 *depthProjectionViewMatrix,
    const QMatrix4x4 *projectionViewMatrix,
    const QMatrix4x4 *viewMatrix) {
  self->drawGridLines(
      *depthProjectionViewMatrix,
      *projectionViewMatrix,
      *viewMatrix);
}

//  void Bars3DRenderer::loadBackgroundMesh()
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer18loadBackgroundMeshEv(Bars3DRenderer *self) {
  self->loadBackgroundMesh();
}

//  void Bars3DRenderer::initSelectionShader()
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer19initSelectionShaderEv(Bars3DRenderer *self) {
  self->initSelectionShader();
}

//  void Bars3DRenderer::initBackgroundShaders(const QString &vertexShader,
//      const QString &fragmentShader)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer21initBackgroundShadersERK7QStringS2_(
    Bars3DRenderer *self,
    const QString *vertexShader,
    const QString *fragmentShader) {
  self->initBackgroundShaders(*vertexShader, *fragmentShader);
}

//  void Bars3DRenderer::initSelectionBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer19initSelectionBufferEv(Bars3DRenderer *self) {
  self->initSelectionBuffer();
}

//  void Bars3DRenderer::initDepthShader()
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer15initDepthShaderEv(Bars3DRenderer *self) {
  self->initDepthShader();
}

//  void Bars3DRenderer::updateDepthBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer17updateDepthBufferEv(Bars3DRenderer *self) {
  self->updateDepthBuffer();
}

//  void Bars3DRenderer::calculateSceneScalingFactors()
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer28calculateSceneScalingFactorsEv(
    Bars3DRenderer *self) {
  self->calculateSceneScalingFactors();
}

//  void Bars3DRenderer::calculateHeightAdjustment()
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer25calculateHeightAdjustmentEv(
    Bars3DRenderer *self) {
  self->calculateHeightAdjustment();
}

//  void Bars3DRenderer::calculateSeriesStartPosition()
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer28calculateSeriesStartPositionEv(
    Bars3DRenderer *self) {
  self->calculateSeriesStartPosition();
}

//  Abstract3DController::SelectionType Bars3DRenderer::isSelected(int row,
//      int bar, const BarSeriesRenderCache *cache)
extern "C" Q_DECL_EXPORT
Abstract3DController::SelectionType ritual_ZN14Bars3DRenderer10isSelectedEiiPK20BarSeriesRenderCache(
    Bars3DRenderer *self,
    int row,
    int bar,
    const BarSeriesRenderCache *cache) {
  return self->isSelected(row, bar, cache);
}

//  QPoint Bars3DRenderer::selectionColorToArrayPosition(const QVector4D
//      &selectionColor)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN14Bars3DRenderer29selectionColorToArrayPositionERK9QVector4D(
    Bars3DRenderer *self,
    const QVector4D *selectionColor) {
  return new QPoint(self->selectionColorToArrayPosition(*selectionColor));
}

//  QBar3DSeries *Bars3DRenderer::selectionColorToSeries(const QVector4D
//      &selectionColor)
extern "C" Q_DECL_EXPORT
QBar3DSeries *ritual_ZN14Bars3DRenderer22selectionColorToSeriesERK9QVector4D(
    Bars3DRenderer *self,
    const QVector4D *selectionColor) {
  return self->selectionColorToSeries(*selectionColor);
}

//  void Bars3DRenderer::updateRenderRow(const QBarDataRow *dataRow,
//      BarRenderItemRow &renderRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer15updateRenderRowEPK5QListI12QBarDataItemERS0_I13BarRenderItemE(
    Bars3DRenderer *self,
    const QBarDataRow *dataRow,
    BarRenderItemRow *renderRow) {
  self->updateRenderRow(dataRow, *renderRow);
}

//  void Bars3DRenderer::updateRenderItem(const QBarDataItem &dataItem,
//      BarRenderItem &renderItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN14Bars3DRenderer16updateRenderItemERK12QBarDataItemR13BarRenderItem(
    Bars3DRenderer *self,
    const QBarDataItem *dataItem,
    BarRenderItem *renderItem) {
  self->updateRenderItem(*dataItem, *renderItem);
}

//  a Python function taken by a CuteBars3DRenderer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Bars3DRenderer(
    Bars3DRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteBars3DRenderer *>(self)->take(key, call);
}

//  void Bars3DRenderer::updateData()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Bars3DRenderer10updateDataEv(Bars3DRenderer *self) {
  self->Bars3DRenderer::updateData();
}

//  SeriesRenderCache *Bars3DRenderer::createNewCache(QAbstract3DSeries
//      *series)
extern "C" Q_DECL_EXPORT
SeriesRenderCache *ritual_own_ZN14Bars3DRenderer14createNewCacheEP17QAbstract3DSeries(
    Bars3DRenderer *self,
    QAbstract3DSeries *series) {
  return self->Bars3DRenderer::createNewCache(series);
}

//  void Bars3DRenderer::updateScene(Q3DScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Bars3DRenderer11updateSceneEP8Q3DScene(
    Bars3DRenderer *self,
    Q3DScene *scene) {
  self->Bars3DRenderer::updateScene(scene);
}

//  void Bars3DRenderer::render(GLuint defaultFboHandle)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Bars3DRenderer6renderEj(
    Bars3DRenderer *self,
    GLuint defaultFboHandle) {
  self->Bars3DRenderer::render(defaultFboHandle);
}

//  QVector3D Bars3DRenderer::convertPositionToTranslation(const QVector3D
//      &position, bool isAbsolute)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_own_ZN14Bars3DRenderer28convertPositionToTranslationERK9QVector3Db(
    Bars3DRenderer *self,
    const QVector3D *position,
    bool isAbsolute) {
  return new QVector3D(
      self->Bars3DRenderer::convertPositionToTranslation(
          *position,
          isAbsolute));
}

//  void Bars3DRenderer::updateAspectRatio(float ratio)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Bars3DRenderer17updateAspectRatioEf(
    Bars3DRenderer *self,
    float ratio) {
  self->Bars3DRenderer::updateAspectRatio(ratio);
}

//  void Bars3DRenderer::updateMargin(float margin)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Bars3DRenderer12updateMarginEf(
    Bars3DRenderer *self,
    float margin) {
  self->Bars3DRenderer::updateMargin(margin);
}

//  void Bars3DRenderer::contextCleanup()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Bars3DRenderer14contextCleanupEv(Bars3DRenderer *self) {
  static_cast<OwnBars3DRenderer *>(self)->OwnBars3DRenderer::contextCleanup();
}

//  void Bars3DRenderer::initializeOpenGL()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Bars3DRenderer16initializeOpenGLEv(
    Bars3DRenderer *self) {
  static_cast<OwnBars3DRenderer *>(self)->OwnBars3DRenderer::initializeOpenGL();
}

//  void Bars3DRenderer::updateAxisRange(QAbstract3DAxis::AxisOrientation
//      orientation, float min, float max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Bars3DRenderer15updateAxisRangeEN15QAbstract3DAxis15AxisOrientationEff(
    Bars3DRenderer *self,
    QAbstract3DAxis::AxisOrientation orientation,
    float min,
    float max) {
  self->Bars3DRenderer::updateAxisRange(orientation, min, max);
}

//  void Bars3DRenderer::updateAxisReversed(QAbstract3DAxis::AxisOrientation
//      orientation, bool enable)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Bars3DRenderer18updateAxisReversedEN15QAbstract3DAxis15AxisOrientationEb(
    Bars3DRenderer *self,
    QAbstract3DAxis::AxisOrientation orientation,
    bool enable) {
  self->Bars3DRenderer::updateAxisReversed(orientation, enable);
}

//  void Bars3DRenderer::initShaders(const QString &vertexShader, const
//      QString &fragmentShader)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Bars3DRenderer11initShadersERK7QStringS2_(
    Bars3DRenderer *self,
    const QString *vertexShader,
    const QString *fragmentShader) {
  self->Bars3DRenderer::initShaders(*vertexShader, *fragmentShader);
}

//  void Bars3DRenderer::initGradientShaders(const QString &vertexShader,
//      const QString &fragmentShader)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Bars3DRenderer19initGradientShadersERK7QStringS2_(
    Bars3DRenderer *self,
    const QString *vertexShader,
    const QString *fragmentShader) {
  self->Bars3DRenderer::initGradientShaders(*vertexShader, *fragmentShader);
}

//  void Bars3DRenderer::updateShadowQuality(QAbstract3DGraph::ShadowQuality
//      quality)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Bars3DRenderer19updateShadowQualityEN16QAbstract3DGraph13ShadowQualityE(
    Bars3DRenderer *self,
    QAbstract3DGraph::ShadowQuality quality) {
  self->Bars3DRenderer::updateShadowQuality(quality);
}

//  void Bars3DRenderer::updateTextures()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Bars3DRenderer14updateTexturesEv(Bars3DRenderer *self) {
  self->Bars3DRenderer::updateTextures();
}

//  void Bars3DRenderer::initBackgroundShaders(const QString &vertexShader,
//      const QString &fragmentShader)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Bars3DRenderer21initBackgroundShadersERK7QStringS2_(
    Bars3DRenderer *self,
    const QString *vertexShader,
    const QString *fragmentShader) {
  self->Bars3DRenderer::initBackgroundShaders(
      *vertexShader,
      *fragmentShader);
}

//  void Bars3DRenderer::initSelectionBuffer()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Bars3DRenderer19initSelectionBufferEv(
    Bars3DRenderer *self) {
  self->Bars3DRenderer::initSelectionBuffer();
}

//  void Bars3DRenderer::updateDepthBuffer()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14Bars3DRenderer17updateDepthBufferEv(
    Bars3DRenderer *self) {
  self->Bars3DRenderer::updateDepthBuffer();
}
