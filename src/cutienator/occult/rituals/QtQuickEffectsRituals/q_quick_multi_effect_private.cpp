//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickEffects/6.12.0/QtQuickEffects/private/qquickmultieffect_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuickEffects/qtquickeffectsexports.h>
#include <QtQuickEffects/6.12.0/QtQuickEffects/private/qtquickeffectsglobal_p.h>
#if QT_CONFIG(quick_shadereffect)
#include <QtQuickEffects/6.12.0/QtQuickEffects/private/qtquickeffectsglobal_p.h>
#include <QtQuickEffects/QtQuickEffects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickEffects/6.12.0/QtQuickEffects/private/qquickmultieffect_p.h>
#include <QtQuickEffects/6.12.0/QtQuickEffects/private/qquickmultieffect_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtCore/qstring.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickEffects/private/qgfxsourceproxy_p.h>
#include <QtQuick/private/qquickshadereffectsource_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qquickimage_p.h>
#include <QtCore/qtypes.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQuickEffects/private/qquickmultieffect_p_p.h>
#include <QtQuick/private/qquickshadereffect_p.h>
#include <QtQuick/private/qquickshadereffectsource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/effects/qgfxsourceproxy.cpp, line 51, as _ZN17QGfxSourceProxyME13setSourceRectERK6QRectF
inline void QGfxSourceProxyME::setSourceRect(const QRectF &sourceRect)
{
    if (m_sourceRect == sourceRect)
        return;
    m_sourceRect = sourceRect;
    polish();
    Q_EMIT sourceRectChanged();
}

//  from ../qtdeclarative/src/effects/qgfxsourceproxy.cpp, line 23, as _ZN17QGfxSourceProxyME8setInputEP10QQuickItem
inline void QGfxSourceProxyME::setInput(QQuickItem *input)
{
    if (m_input == input)
        return;

    if (m_input)
        disconnect(m_input, nullptr, this, nullptr);
    m_input = input;
    polish();
    if (m_input) {
        if (QQuickImage *image = qobject_cast<QQuickImage *>(m_input)) {
            connect(image, &QQuickImage::sourceSizeChanged, this, &QGfxSourceProxyME::repolish);
            connect(image, &QQuickImage::fillModeChanged, this, &QGfxSourceProxyME::repolish);
        }
        connect(m_input, &QQuickItem::childrenChanged, this, &QGfxSourceProxyME::repolish);
    }
    Q_EMIT inputChanged();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1620, as _ZN24QQuickMultiEffectPrivate14getBlurWeightsEfR9QVector4DR9QVector2D
inline void QQuickMultiEffectPrivate::getBlurWeights(float blurLod, QVector4D &blurWeight1, QVector2D &blurWeight2)
{
    float bw1 = blurWeight(std::fabs(blurLod - 0.1f));
    float bw2 = blurWeight(std::fabs(blurLod - 0.3f));
    float bw3 = blurWeight(std::fabs(blurLod - 0.5f));
    float bw4 = blurWeight(std::fabs(blurLod - 0.7f));
    float bw5 = blurWeight(std::fabs(blurLod - 0.9f));
    float bw6 = blurWeight(std::fabs(blurLod - 1.1f));
    float bsum = bw1 + bw2 + bw3 + bw4 + bw5 + bw6;
    blurWeight1 = QVector4D(bw1 / bsum, bw2 / bsum, bw3 / bsum, bw4 / bsum);
    blurWeight2 = QVector2D(bw5 / bsum, bw6 / bsum);
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 937, as _ZN24QQuickMultiEffectPrivateD1Ev
inline QQuickMultiEffectPrivate::~QQuickMultiEffectPrivate()
{
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 960, as _ZNK24QQuickMultiEffectPrivate6sourceEv
inline QQuickItem *QQuickMultiEffectPrivate::source() const
{
    return m_sourceItem;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 985, as _ZNK24QQuickMultiEffectPrivate18autoPaddingEnabledEv
inline bool QQuickMultiEffectPrivate::autoPaddingEnabled() const
{
    return m_autoPaddingEnabled;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1002, as _ZNK24QQuickMultiEffectPrivate11paddingRectEv
inline QRectF QQuickMultiEffectPrivate::paddingRect() const
{
    return m_paddingRect;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1019, as _ZNK24QQuickMultiEffectPrivate10brightnessEv
inline qreal QQuickMultiEffectPrivate::brightness() const
{
    return m_brightness;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1024, as _ZN24QQuickMultiEffectPrivate13setBrightnessEd
inline void QQuickMultiEffectPrivate::setBrightness(qreal brightness)
{
    Q_Q(QQuickMultiEffect);
    if (brightness == m_brightness)
        return;

    m_brightness = brightness;
    if (m_shaderEffect)
        m_shaderEffect->setProperty("brightness", m_brightness);

    q->update();
    Q_EMIT q->brightnessChanged();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1038, as _ZNK24QQuickMultiEffectPrivate8contrastEv
inline qreal QQuickMultiEffectPrivate::contrast() const
{
    return m_contrast;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1043, as _ZN24QQuickMultiEffectPrivate11setContrastEd
inline void QQuickMultiEffectPrivate::setContrast(qreal contrast)
{
    Q_Q(QQuickMultiEffect);
    if (contrast == m_contrast)
        return;

    m_contrast = contrast;
    if (m_shaderEffect)
        m_shaderEffect->setProperty("contrast", m_contrast);

    q->update();
    Q_EMIT q->contrastChanged();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1057, as _ZNK24QQuickMultiEffectPrivate10saturationEv
inline qreal QQuickMultiEffectPrivate::saturation() const
{
    return m_saturation;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1062, as _ZN24QQuickMultiEffectPrivate13setSaturationEd
inline void QQuickMultiEffectPrivate::setSaturation(qreal saturation)
{
    Q_Q(QQuickMultiEffect);
    if (saturation == m_saturation)
        return;

    m_saturation = saturation;
    if (m_shaderEffect)
        m_shaderEffect->setProperty("saturation", m_saturation);

    q->update();
    Q_EMIT q->saturationChanged();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1076, as _ZNK24QQuickMultiEffectPrivate12colorizationEv
inline qreal QQuickMultiEffectPrivate::colorization() const
{
    return m_colorization;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1081, as _ZN24QQuickMultiEffectPrivate15setColorizationEd
inline void QQuickMultiEffectPrivate::setColorization(qreal colorization)
{
    Q_Q(QQuickMultiEffect);
    if (colorization == m_colorization)
        return;

    m_colorization = colorization;
    updateColorizationColor();

    q->update();
    Q_EMIT q->colorizationChanged();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1094, as _ZNK24QQuickMultiEffectPrivate17colorizationColorEv
inline QColor QQuickMultiEffectPrivate::colorizationColor() const
{
    return m_colorizationColor;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1099, as _ZN24QQuickMultiEffectPrivate20setColorizationColorERK6QColor
inline void QQuickMultiEffectPrivate::setColorizationColor(const QColor &color)
{
    Q_Q(QQuickMultiEffect);
    if (color == m_colorizationColor)
        return;

    m_colorizationColor = color;
    updateColorizationColor();

    q->update();
    Q_EMIT q->colorizationColorChanged();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1112, as _ZNK24QQuickMultiEffectPrivate11blurEnabledEv
inline bool QQuickMultiEffectPrivate::blurEnabled() const
{
    return m_blurEnabled;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1132, as _ZNK24QQuickMultiEffectPrivate4blurEv
inline qreal QQuickMultiEffectPrivate::blur() const
{
    return m_blur;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1137, as _ZN24QQuickMultiEffectPrivate7setBlurEd
inline void QQuickMultiEffectPrivate::setBlur(qreal blur)
{
    Q_Q(QQuickMultiEffect);
    if (blur == m_blur)
        return;

    m_blur = blur;
    updateBlurWeights();

    q->update();
    Q_EMIT q->blurChanged();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1150, as _ZNK24QQuickMultiEffectPrivate7blurMaxEv
inline int QQuickMultiEffectPrivate::blurMax() const
{
    return m_blurMax;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1173, as _ZNK24QQuickMultiEffectPrivate14blurMultiplierEv
inline qreal QQuickMultiEffectPrivate::blurMultiplier() const
{
    return m_blurMultiplier;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1194, as _ZNK24QQuickMultiEffectPrivate13shadowEnabledEv
inline bool QQuickMultiEffectPrivate::shadowEnabled() const
{
    return m_shadowEnabled;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1214, as _ZNK24QQuickMultiEffectPrivate13shadowOpacityEv
inline qreal QQuickMultiEffectPrivate::shadowOpacity() const
{
    return m_shadowOpacity;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1219, as _ZN24QQuickMultiEffectPrivate16setShadowOpacityEd
inline void QQuickMultiEffectPrivate::setShadowOpacity(qreal shadowOpacity)
{
    Q_Q(QQuickMultiEffect);
    if (shadowOpacity == m_shadowOpacity)
        return;

    m_shadowOpacity = shadowOpacity;
    updateShadowColor();

    q->update();
    Q_EMIT q->shadowOpacityChanged();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1232, as _ZNK24QQuickMultiEffectPrivate10shadowBlurEv
inline qreal QQuickMultiEffectPrivate::shadowBlur() const
{
    return m_shadowBlur;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1237, as _ZN24QQuickMultiEffectPrivate13setShadowBlurEd
inline void QQuickMultiEffectPrivate::setShadowBlur(qreal shadowBlur)
{
    Q_Q(QQuickMultiEffect);
    if (shadowBlur == m_shadowBlur)
        return;

    m_shadowBlur = shadowBlur;
    updateShadowBlurWeights();

    q->update();
    Q_EMIT q->shadowBlurChanged();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1250, as _ZNK24QQuickMultiEffectPrivate22shadowHorizontalOffsetEv
inline qreal QQuickMultiEffectPrivate::shadowHorizontalOffset() const
{
    return m_shadowHorizontalOffset;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1255, as _ZN24QQuickMultiEffectPrivate25setShadowHorizontalOffsetEd
inline void QQuickMultiEffectPrivate::setShadowHorizontalOffset(qreal offset)
{
    Q_Q(QQuickMultiEffect);
    if (offset == m_shadowHorizontalOffset)
        return;

    m_shadowHorizontalOffset = offset;
    updateShadowOffset();

    q->update();
    Q_EMIT q->shadowHorizontalOffsetChanged();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1268, as _ZNK24QQuickMultiEffectPrivate20shadowVerticalOffsetEv
inline qreal QQuickMultiEffectPrivate::shadowVerticalOffset() const
{
    return m_shadowVerticalOffset;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1273, as _ZN24QQuickMultiEffectPrivate23setShadowVerticalOffsetEd
inline void QQuickMultiEffectPrivate::setShadowVerticalOffset(qreal offset)
{
    Q_Q(QQuickMultiEffect);
    if (offset == m_shadowVerticalOffset)
        return;

    m_shadowVerticalOffset = offset;
    updateShadowOffset();

    q->update();
    Q_EMIT q->shadowVerticalOffsetChanged();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1286, as _ZNK24QQuickMultiEffectPrivate11shadowColorEv
inline QColor QQuickMultiEffectPrivate::shadowColor() const
{
    return m_shadowColor;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1291, as _ZN24QQuickMultiEffectPrivate14setShadowColorERK6QColor
inline void QQuickMultiEffectPrivate::setShadowColor(const QColor &color)
{
    Q_Q(QQuickMultiEffect);
    if (color == m_shadowColor)
        return;

    m_shadowColor = color;
    updateShadowColor();

    q->update();
    Q_EMIT q->shadowColorChanged();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1304, as _ZNK24QQuickMultiEffectPrivate11shadowScaleEv
inline qreal QQuickMultiEffectPrivate::shadowScale() const
{
    return m_shadowScale;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1309, as _ZN24QQuickMultiEffectPrivate14setShadowScaleEd
inline void QQuickMultiEffectPrivate::setShadowScale(qreal shadowScale)
{
    Q_Q(QQuickMultiEffect);
    if (shadowScale == m_shadowScale)
        return;

    m_shadowScale = shadowScale;
    updateCenterOffset();
    if (m_shaderEffect)
        m_shaderEffect->setProperty("shadowScale", 1.0 / m_shadowScale);

    q->update();
    Q_EMIT q->shadowScaleChanged();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1324, as _ZNK24QQuickMultiEffectPrivate11maskEnabledEv
inline bool QQuickMultiEffectPrivate::maskEnabled() const
{
    return m_maskEnabled;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1342, as _ZNK24QQuickMultiEffectPrivate10maskSourceEv
inline QQuickItem *QQuickMultiEffectPrivate::maskSource() const
{
    return m_maskSourceItem;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1347, as _ZN24QQuickMultiEffectPrivate13setMaskSourceEP10QQuickItem
inline void QQuickMultiEffectPrivate::setMaskSource(QQuickItem *item)
{
    Q_Q(QQuickMultiEffect);
    if (item == m_maskSourceItem)
        return;

    if (m_maskSourceItem) {
        QQuickItemPrivate::get(m_maskSourceItem)
                ->removeItemChangeListener(this, ChangeType::Destroyed);
    }
    if (item)
        QQuickItemPrivate::get(item)->addItemChangeListener(this, ChangeType::Destroyed);

    m_maskSourceItem = item;
    if (m_shaderEffect) {
        auto maskSourceVariant = QVariant::fromValue<QQuickItem*>(m_maskSourceItem);
        m_shaderEffect->setProperty("maskSrc", maskSourceVariant);
    }

    q->update();
    Q_EMIT q->maskSourceChanged();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1370, as _ZNK24QQuickMultiEffectPrivate16maskThresholdMinEv
inline qreal QQuickMultiEffectPrivate::maskThresholdMin() const
{
    return m_maskThresholdMin;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1375, as _ZN24QQuickMultiEffectPrivate19setMaskThresholdMinEd
inline void QQuickMultiEffectPrivate::setMaskThresholdMin(qreal threshold)
{
    Q_Q(QQuickMultiEffect);
    if (threshold == m_maskThresholdMin)
        return;

    m_maskThresholdMin = threshold;
    updateMaskThresholdSpread();

    q->update();
    Q_EMIT q->maskThresholdMinChanged();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1388, as _ZNK24QQuickMultiEffectPrivate15maskSpreadAtMinEv
inline qreal QQuickMultiEffectPrivate::maskSpreadAtMin() const
{
    return m_maskSpreadAtMin;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1393, as _ZN24QQuickMultiEffectPrivate18setMaskSpreadAtMinEd
inline void QQuickMultiEffectPrivate::setMaskSpreadAtMin(qreal spread)
{
    Q_Q(QQuickMultiEffect);
    if (spread == m_maskSpreadAtMin)
        return;

    m_maskSpreadAtMin = spread;
    updateMaskThresholdSpread();

    q->update();
    Q_EMIT q->maskSpreadAtMinChanged();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1406, as _ZNK24QQuickMultiEffectPrivate16maskThresholdMaxEv
inline qreal QQuickMultiEffectPrivate::maskThresholdMax() const
{
    return m_maskThresholdMax;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1411, as _ZN24QQuickMultiEffectPrivate19setMaskThresholdMaxEd
inline void QQuickMultiEffectPrivate::setMaskThresholdMax(qreal threshold)
{
    Q_Q(QQuickMultiEffect);
    if (threshold == m_maskThresholdMax)
        return;

    m_maskThresholdMax = threshold;
    updateMaskThresholdSpread();

    q->update();
    Q_EMIT q->maskThresholdMaxChanged();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1424, as _ZNK24QQuickMultiEffectPrivate15maskSpreadAtMaxEv
inline qreal QQuickMultiEffectPrivate::maskSpreadAtMax() const
{
    return m_maskSpreadAtMax;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1429, as _ZN24QQuickMultiEffectPrivate18setMaskSpreadAtMaxEd
inline void QQuickMultiEffectPrivate::setMaskSpreadAtMax(qreal spread)
{
    Q_Q(QQuickMultiEffect);
    if (spread == m_maskSpreadAtMax)
        return;

    m_maskSpreadAtMax = spread;
    updateMaskThresholdSpread();

    q->update();
    Q_EMIT q->maskSpreadAtMaxChanged();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1442, as _ZNK24QQuickMultiEffectPrivate12maskInvertedEv
inline bool QQuickMultiEffectPrivate::maskInverted() const
{
    return m_maskInverted;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1447, as _ZN24QQuickMultiEffectPrivate15setMaskInvertedEb
inline void QQuickMultiEffectPrivate::setMaskInverted(bool inverted)
{
    Q_Q(QQuickMultiEffect);
    if (inverted == m_maskInverted)
        return;

    m_maskInverted = inverted;
    if (m_shaderEffect)
        m_shaderEffect->setProperty("maskInverted", float(m_maskInverted));

    q->update();
    Q_EMIT q->maskInvertedChanged();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1461, as _ZNK24QQuickMultiEffectPrivate8itemRectEv
inline QRectF QQuickMultiEffectPrivate::itemRect() const
{
    if (!m_shaderEffect  || !m_shaderSource)
        return QRectF();

    QRectF sourceRect = m_shaderSource->sourceRect();
    if (sourceRect.width() > 0 && sourceRect.height() > 0)
        return sourceRect;
    else
        return m_shaderEffect->boundingRect();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1473, as _ZNK24QQuickMultiEffectPrivate14fragmentShaderEv
inline QString QQuickMultiEffectPrivate::fragmentShader() const
{
    return m_fragShader;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1478, as _ZNK24QQuickMultiEffectPrivate12vertexShaderEv
inline QString QQuickMultiEffectPrivate::vertexShader() const
{
    return m_vertShader;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1483, as _ZNK24QQuickMultiEffectPrivate14hasProxySourceEv
inline bool QQuickMultiEffectPrivate::hasProxySource() const
{
    return m_shaderSource && m_shaderSource->isActive();
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1542, as _ZN24QQuickMultiEffectPrivate25updateMaskThresholdSpreadEv
inline void QQuickMultiEffectPrivate::updateMaskThresholdSpread()
{
    if (!m_shaderEffect)
        return;

    // Calculate threshold and spread values for mask
    // smoothstep, keeping always edge0 < edge1.
    const qreal c0 = 0.0001;
    const qreal c1 = 1.0 - c0;
    const qreal mt1 = m_maskThresholdMin + c0;
    const qreal ms1 = m_maskSpreadAtMin + 1.0;
    const qreal mt2 = c1 - m_maskThresholdMax;
    const qreal ms2 = m_maskSpreadAtMax + 1.0;
    const QVector4D maskThresholdSpread = QVector4D(
                mt1 * ms1 - (ms1 - c1),
                mt1 * ms1,
                mt2 * ms2 - (ms2 - c1),
                mt2 * ms2);
    m_shaderEffect->setProperty("mask", maskThresholdSpread);
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1563, as _ZN24QQuickMultiEffectPrivate18updateCenterOffsetEv
inline void QQuickMultiEffectPrivate::updateCenterOffset()
{
    if (!m_shaderEffect)
        return;

    const qreal scale = 1.0 / m_shadowScale;
    QVector2D centerOffset((1.0 - scale) * (0.5 + 0.5 * (m_paddingRect.x() - m_paddingRect.width()) / m_shaderEffect->width()),
                           (1.0 - scale) * (0.5 + 0.5 * (m_paddingRect.y() - m_paddingRect.height()) / m_shaderEffect->height()));
    m_shaderEffect->setProperty("centerOffset", centerOffset);
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1574, as _ZN24QQuickMultiEffectPrivate18updateShadowOffsetEv
inline void QQuickMultiEffectPrivate::updateShadowOffset()
{
    if (!m_shaderEffect)
        return;

    QVector2D shadowOffset = QVector2D(m_shadowHorizontalOffset / m_shaderEffect->width(), m_shadowVerticalOffset / m_shaderEffect->height());
    m_shaderEffect->setProperty("shadowOffset", shadowOffset);
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1583, as _ZN24QQuickMultiEffectPrivate23updateColorizationColorEv
inline void QQuickMultiEffectPrivate::updateColorizationColor()
{
    if (!m_shaderEffect)
        return;

    float alpha = std::clamp(float(m_colorizationColor.alphaF() * m_colorization), 0.0f, 1.0f);
    QVector4D colorizationColor(m_colorizationColor.redF(),
                                m_colorizationColor.greenF(),
                                m_colorizationColor.blueF(),
                                alpha);
    m_shaderEffect->setProperty("colorizationColor", colorizationColor);
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1596, as _ZN24QQuickMultiEffectPrivate17updateShadowColorEv
inline void QQuickMultiEffectPrivate::updateShadowColor()
{
    if (!m_shaderEffect)
        return;

    // Shader shadowColor has premultiplied alpha
    float alpha = std::clamp(float(m_shadowOpacity), 0.0f, 1.0f);
    QVector4D shadowColor(m_shadowColor.redF() * alpha,
                          m_shadowColor.greenF() * alpha,
                          m_shadowColor.blueF() * alpha,
                          m_shadowColor.alphaF() * alpha);
    m_shaderEffect->setProperty("shadowColor", shadowColor);
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1610, as _ZN24QQuickMultiEffectPrivate12calculateLodEf
inline float QQuickMultiEffectPrivate::calculateLod(float blurAmount)
{
    return qSqrt(blurAmount * float(m_blurMax) / 64.0f) * 1.2f - 0.2f;
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1615, as _ZN24QQuickMultiEffectPrivate10blurWeightEf
inline float QQuickMultiEffectPrivate::blurWeight(float v)
{
    return std::max(0.0f, std::min(1.0f, 1.0f - v * 2.0f));
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1633, as _ZN24QQuickMultiEffectPrivate17updateBlurWeightsEv
inline void QQuickMultiEffectPrivate::updateBlurWeights()
{
    if (!m_shaderEffect)
        return;
    float blurLod = calculateLod(m_blur);
    getBlurWeights(blurLod, m_blurWeight1, m_blurWeight2);
    m_shaderEffect->setProperty("blurWeight1", m_blurWeight1);
    m_shaderEffect->setProperty("blurWeight2", m_blurWeight2);
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1643, as _ZN24QQuickMultiEffectPrivate23updateShadowBlurWeightsEv
inline void QQuickMultiEffectPrivate::updateShadowBlurWeights()
{
    if (!m_shaderEffect)
        return;
    float blurLod = calculateLod(m_shadowBlur);
    getBlurWeights(blurLod, m_shadowBlurWeight1, m_shadowBlurWeight2);
    m_shaderEffect->setProperty("shadowBlurWeight1", m_shadowBlurWeight1);
    m_shaderEffect->setProperty("shadowBlurWeight2", m_shadowBlurWeight2);
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1746, as _ZN24QQuickMultiEffectPrivate21updateBlurItemsAmountEi
inline void QQuickMultiEffectPrivate::updateBlurItemsAmount(int blurLevel)
{
    Q_Q(QQuickMultiEffect);
    if (!m_shaderEffect)
        return;

    const auto engine = qmlEngine(q);
    if (!engine)
        return;

    // Lowest blur level uses 3 items, highest 5 items.
    int itemsAmount = blurLevel == 0 ? 0 : blurLevel + 2;

    if (m_blurEffects.size() < itemsAmount) {
        // Add more blur items.
        // Note that by design blur items are only added and never reduced
        // during the lifetime of the effect component.
        QUrl blurVs = QUrl(QStringLiteral("qrc:/data/shaders/bluritems.vert.qsb"));
        QUrl blurFs = QUrl(QStringLiteral("qrc:/data/shaders/bluritems.frag.qsb"));
        QQmlComponent blurComponent(
                engine,
                QUrl(QStringLiteral("qrc:/qt-project.org/imports/QtQuick/Effects/BlurItem.qml")));
        for (int i = m_blurEffects.size(); i < itemsAmount; i++) {
            auto blurEffect = qobject_cast<QQuickShaderEffect*>(blurComponent.create());
            blurEffect->setParent(q);
            blurEffect->setParentItem(q);
            auto sourceVariant = QVariant::fromValue<QQuickItem*>(blurEffect);
            QString sourceProperty = QStringLiteral("blurSrc%1").arg(i + 1);
            m_shaderEffect->setProperty(sourceProperty.toUtf8(), sourceVariant);
            // Initial value to avoid "'source' does not have a matching property" warning.
            // Will be updated with the correct one few lines forward.
            blurEffect->setProperty("source", sourceVariant);
            QQuickItemPrivate *priv = QQuickItemPrivate::get(blurEffect);
            priv->layer()->setEnabled(true);
            priv->layer()->setSmooth(true);
            blurEffect->setVertexShader(blurVs);
            blurEffect->setFragmentShader(blurFs);
            m_blurEffects << blurEffect;
        }
    }

    // Set the blur items source components
    if (!m_dummyShaderSource)
        m_dummyShaderSource = new QQuickShaderEffectSource(q);
    for (int i = 0; i < m_blurEffects.size(); i++) {
        auto *blurEffect = m_blurEffects[i];
        auto sourceItem = (i >= itemsAmount) ?
                    static_cast<QQuickItem *>(m_dummyShaderSource) : (i == 0) ?
                        static_cast<QQuickItem *>(m_shaderSource->output()) :
                        static_cast<QQuickItem *>(m_blurEffects[i - 1]);
        auto sourceVariant = QVariant::fromValue<QQuickItem*>(sourceItem);
        blurEffect->setProperty("source", sourceVariant);
    }
}

//  from ../qtdeclarative/src/effects/qquickmultieffect.cpp, line 1882, as _ZN24QQuickMultiEffectPrivate22updateProxyActiveCheckEv
inline void QQuickMultiEffectPrivate::updateProxyActiveCheck()
{
    if (!m_shaderSource)
        return;

    m_shaderSource->polish();
}
//  -----------------------------------------------------------------------

//  A QQuickMultiEffectPrivate that Python can take functions over in. Every QQuickMultiEffectPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickMultiEffectPrivateCall0)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickMultiEffectPrivateCall1)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickMultiEffectPrivateCall2)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickMultiEffectPrivateCall3)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickMultiEffectPrivateCall4)(const void *, int, int *);
typedef qreal (*CuteQQuickMultiEffectPrivateCall5)(const void *, int *);
typedef qreal (*CuteQQuickMultiEffectPrivateCall6)(const void *, int *);
typedef void (*CuteQQuickMultiEffectPrivateCall7)(const void *, int *);
typedef void (*CuteQQuickMultiEffectPrivateCall8)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickMultiEffectPrivateCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickMultiEffectPrivateCall10)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickMultiEffectPrivateCall11)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickMultiEffectPrivateCall12)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickMultiEffectPrivateCall13)(const void *, bool, int *);
typedef void * (*CuteQQuickMultiEffectPrivateCall14)(const void *, int *);
typedef void (*CuteQQuickMultiEffectPrivateCall15)(const void *, int *);
typedef void (*CuteQQuickMultiEffectPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickMultiEffectPrivateCall17)(const void *, int, int *);
class CuteQQuickMultiEffectPrivate : public QQuickMultiEffectPrivate {
public:
  using QQuickMultiEffectPrivate::QQuickMultiEffectPrivate;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[8] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[11] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[17] = call;
      return true;
    }
    return false;
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickMultiEffectPrivateCall0 call = reinterpret_cast<CuteQQuickMultiEffectPrivateCall0>(taken[0]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickMultiEffectPrivateCall1 call = reinterpret_cast<CuteQQuickMultiEffectPrivateCall1>(taken[1]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::removePointerHandler(h);
  }

  //  QtPrivate::QQuickAttachedPropertyPropagator
  //      *QQuickItemPrivate::attachedPropertyPropagator_parent(const
  //      QMetaObject *attachedType)
  QtPrivate::QQuickAttachedPropertyPropagator *attachedPropertyPropagator_parent(
      const QMetaObject *attachedType) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickMultiEffectPrivateCall2 call = reinterpret_cast<CuteQQuickMultiEffectPrivateCall2>(taken[2]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickMultiEffectPrivateCall3 call = reinterpret_cast<CuteQQuickMultiEffectPrivateCall3>(taken[3]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      reason)
  bool setLastFocusChangeReason(Qt::FocusReason reason) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickMultiEffectPrivateCall4 call = reinterpret_cast<CuteQQuickMultiEffectPrivateCall4>(taken[4]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickMultiEffectPrivateCall5 call = reinterpret_cast<CuteQQuickMultiEffectPrivateCall5>(taken[5]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickMultiEffectPrivateCall6 call = reinterpret_cast<CuteQQuickMultiEffectPrivateCall6>(taken[6]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickMultiEffectPrivateCall7 call = reinterpret_cast<CuteQQuickMultiEffectPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickMultiEffectPrivateCall8 call = reinterpret_cast<CuteQQuickMultiEffectPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickItemPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickMultiEffectPrivateCall9 call = reinterpret_cast<CuteQQuickMultiEffectPrivateCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickItemPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickMultiEffectPrivateCall10 call = reinterpret_cast<CuteQQuickMultiEffectPrivateCall10>(taken[10]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickMultiEffectPrivateCall11 call = reinterpret_cast<CuteQQuickMultiEffectPrivateCall11>(taken[11]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickMultiEffectPrivateCall12 call = reinterpret_cast<CuteQQuickMultiEffectPrivateCall12>(taken[12]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickMultiEffectPrivateCall13 call = reinterpret_cast<CuteQQuickMultiEffectPrivateCall13>(taken[13]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickMultiEffectPrivateCall14 call = reinterpret_cast<CuteQQuickMultiEffectPrivateCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickMultiEffectPrivateCall15 call = reinterpret_cast<CuteQQuickMultiEffectPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickMultiEffectPrivateCall16 call = reinterpret_cast<CuteQQuickMultiEffectPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickMultiEffectPrivateCall17 call = reinterpret_cast<CuteQQuickMultiEffectPrivateCall17>(taken[17]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickMultiEffect *QQuickMultiEffectPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickMultiEffect *ritual_ZN24QQuickMultiEffectPrivate6q_funcEv(
    QQuickMultiEffectPrivate *self) {
  return self->q_func();
}

//  const QQuickMultiEffect *QQuickMultiEffectPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickMultiEffect *ritual_ZNK24QQuickMultiEffectPrivate6q_funcEv(
    const QQuickMultiEffectPrivate *self) {
  return self->q_func();
}

//  QQuickMultiEffectPrivate::~QQuickMultiEffectPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivateD1Ev(
    QQuickMultiEffectPrivate *self) {
  delete self;
}

//  QQuickItem *QQuickMultiEffectPrivate::source() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK24QQuickMultiEffectPrivate6sourceEv(
    const QQuickMultiEffectPrivate *self) {
  return self->source();
}

//  bool QQuickMultiEffectPrivate::autoPaddingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickMultiEffectPrivate18autoPaddingEnabledEv(
    const QQuickMultiEffectPrivate *self) {
  return self->autoPaddingEnabled();
}

//  QRectF QQuickMultiEffectPrivate::paddingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK24QQuickMultiEffectPrivate11paddingRectEv(
    const QQuickMultiEffectPrivate *self) {
  return new QRectF(self->paddingRect());
}

//  qreal QQuickMultiEffectPrivate::brightness() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QQuickMultiEffectPrivate10brightnessEv(
    const QQuickMultiEffectPrivate *self) {
  return self->brightness();
}

//  void QQuickMultiEffectPrivate::setBrightness(qreal brightness)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate13setBrightnessEd(
    QQuickMultiEffectPrivate *self,
    qreal brightness) {
  self->setBrightness(brightness);
}

//  qreal QQuickMultiEffectPrivate::contrast() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QQuickMultiEffectPrivate8contrastEv(
    const QQuickMultiEffectPrivate *self) {
  return self->contrast();
}

//  void QQuickMultiEffectPrivate::setContrast(qreal contrast)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate11setContrastEd(
    QQuickMultiEffectPrivate *self,
    qreal contrast) {
  self->setContrast(contrast);
}

//  qreal QQuickMultiEffectPrivate::saturation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QQuickMultiEffectPrivate10saturationEv(
    const QQuickMultiEffectPrivate *self) {
  return self->saturation();
}

//  void QQuickMultiEffectPrivate::setSaturation(qreal saturation)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate13setSaturationEd(
    QQuickMultiEffectPrivate *self,
    qreal saturation) {
  self->setSaturation(saturation);
}

//  qreal QQuickMultiEffectPrivate::colorization() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QQuickMultiEffectPrivate12colorizationEv(
    const QQuickMultiEffectPrivate *self) {
  return self->colorization();
}

//  void QQuickMultiEffectPrivate::setColorization(qreal colorization)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate15setColorizationEd(
    QQuickMultiEffectPrivate *self,
    qreal colorization) {
  self->setColorization(colorization);
}

//  QColor QQuickMultiEffectPrivate::colorizationColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK24QQuickMultiEffectPrivate17colorizationColorEv(
    const QQuickMultiEffectPrivate *self) {
  return new QColor(self->colorizationColor());
}

//  void QQuickMultiEffectPrivate::setColorizationColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate20setColorizationColorERK6QColor(
    QQuickMultiEffectPrivate *self,
    const QColor *color) {
  self->setColorizationColor(*color);
}

//  bool QQuickMultiEffectPrivate::blurEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickMultiEffectPrivate11blurEnabledEv(
    const QQuickMultiEffectPrivate *self) {
  return self->blurEnabled();
}

//  qreal QQuickMultiEffectPrivate::blur() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QQuickMultiEffectPrivate4blurEv(
    const QQuickMultiEffectPrivate *self) {
  return self->blur();
}

//  void QQuickMultiEffectPrivate::setBlur(qreal blur)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate7setBlurEd(
    QQuickMultiEffectPrivate *self,
    qreal blur) {
  self->setBlur(blur);
}

//  int QQuickMultiEffectPrivate::blurMax() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QQuickMultiEffectPrivate7blurMaxEv(
    const QQuickMultiEffectPrivate *self) {
  return self->blurMax();
}

//  qreal QQuickMultiEffectPrivate::blurMultiplier() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QQuickMultiEffectPrivate14blurMultiplierEv(
    const QQuickMultiEffectPrivate *self) {
  return self->blurMultiplier();
}

//  bool QQuickMultiEffectPrivate::shadowEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickMultiEffectPrivate13shadowEnabledEv(
    const QQuickMultiEffectPrivate *self) {
  return self->shadowEnabled();
}

//  qreal QQuickMultiEffectPrivate::shadowOpacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QQuickMultiEffectPrivate13shadowOpacityEv(
    const QQuickMultiEffectPrivate *self) {
  return self->shadowOpacity();
}

//  void QQuickMultiEffectPrivate::setShadowOpacity(qreal shadowOpacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate16setShadowOpacityEd(
    QQuickMultiEffectPrivate *self,
    qreal shadowOpacity) {
  self->setShadowOpacity(shadowOpacity);
}

//  qreal QQuickMultiEffectPrivate::shadowBlur() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QQuickMultiEffectPrivate10shadowBlurEv(
    const QQuickMultiEffectPrivate *self) {
  return self->shadowBlur();
}

//  void QQuickMultiEffectPrivate::setShadowBlur(qreal shadowBlur)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate13setShadowBlurEd(
    QQuickMultiEffectPrivate *self,
    qreal shadowBlur) {
  self->setShadowBlur(shadowBlur);
}

//  qreal QQuickMultiEffectPrivate::shadowHorizontalOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QQuickMultiEffectPrivate22shadowHorizontalOffsetEv(
    const QQuickMultiEffectPrivate *self) {
  return self->shadowHorizontalOffset();
}

//  void QQuickMultiEffectPrivate::setShadowHorizontalOffset(qreal offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate25setShadowHorizontalOffsetEd(
    QQuickMultiEffectPrivate *self,
    qreal offset) {
  self->setShadowHorizontalOffset(offset);
}

//  qreal QQuickMultiEffectPrivate::shadowVerticalOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QQuickMultiEffectPrivate20shadowVerticalOffsetEv(
    const QQuickMultiEffectPrivate *self) {
  return self->shadowVerticalOffset();
}

//  void QQuickMultiEffectPrivate::setShadowVerticalOffset(qreal offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate23setShadowVerticalOffsetEd(
    QQuickMultiEffectPrivate *self,
    qreal offset) {
  self->setShadowVerticalOffset(offset);
}

//  QColor QQuickMultiEffectPrivate::shadowColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK24QQuickMultiEffectPrivate11shadowColorEv(
    const QQuickMultiEffectPrivate *self) {
  return new QColor(self->shadowColor());
}

//  void QQuickMultiEffectPrivate::setShadowColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate14setShadowColorERK6QColor(
    QQuickMultiEffectPrivate *self,
    const QColor *color) {
  self->setShadowColor(*color);
}

//  qreal QQuickMultiEffectPrivate::shadowScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QQuickMultiEffectPrivate11shadowScaleEv(
    const QQuickMultiEffectPrivate *self) {
  return self->shadowScale();
}

//  void QQuickMultiEffectPrivate::setShadowScale(qreal shadowScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate14setShadowScaleEd(
    QQuickMultiEffectPrivate *self,
    qreal shadowScale) {
  self->setShadowScale(shadowScale);
}

//  bool QQuickMultiEffectPrivate::maskEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickMultiEffectPrivate11maskEnabledEv(
    const QQuickMultiEffectPrivate *self) {
  return self->maskEnabled();
}

//  QQuickItem *QQuickMultiEffectPrivate::maskSource() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK24QQuickMultiEffectPrivate10maskSourceEv(
    const QQuickMultiEffectPrivate *self) {
  return self->maskSource();
}

//  void QQuickMultiEffectPrivate::setMaskSource(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate13setMaskSourceEP10QQuickItem(
    QQuickMultiEffectPrivate *self,
    QQuickItem *item) {
  self->setMaskSource(item);
}

//  qreal QQuickMultiEffectPrivate::maskThresholdMin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QQuickMultiEffectPrivate16maskThresholdMinEv(
    const QQuickMultiEffectPrivate *self) {
  return self->maskThresholdMin();
}

//  void QQuickMultiEffectPrivate::setMaskThresholdMin(qreal threshold)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate19setMaskThresholdMinEd(
    QQuickMultiEffectPrivate *self,
    qreal threshold) {
  self->setMaskThresholdMin(threshold);
}

//  qreal QQuickMultiEffectPrivate::maskSpreadAtMin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QQuickMultiEffectPrivate15maskSpreadAtMinEv(
    const QQuickMultiEffectPrivate *self) {
  return self->maskSpreadAtMin();
}

//  void QQuickMultiEffectPrivate::setMaskSpreadAtMin(qreal spread)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate18setMaskSpreadAtMinEd(
    QQuickMultiEffectPrivate *self,
    qreal spread) {
  self->setMaskSpreadAtMin(spread);
}

//  qreal QQuickMultiEffectPrivate::maskThresholdMax() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QQuickMultiEffectPrivate16maskThresholdMaxEv(
    const QQuickMultiEffectPrivate *self) {
  return self->maskThresholdMax();
}

//  void QQuickMultiEffectPrivate::setMaskThresholdMax(qreal threshold)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate19setMaskThresholdMaxEd(
    QQuickMultiEffectPrivate *self,
    qreal threshold) {
  self->setMaskThresholdMax(threshold);
}

//  qreal QQuickMultiEffectPrivate::maskSpreadAtMax() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QQuickMultiEffectPrivate15maskSpreadAtMaxEv(
    const QQuickMultiEffectPrivate *self) {
  return self->maskSpreadAtMax();
}

//  void QQuickMultiEffectPrivate::setMaskSpreadAtMax(qreal spread)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate18setMaskSpreadAtMaxEd(
    QQuickMultiEffectPrivate *self,
    qreal spread) {
  self->setMaskSpreadAtMax(spread);
}

//  bool QQuickMultiEffectPrivate::maskInverted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickMultiEffectPrivate12maskInvertedEv(
    const QQuickMultiEffectPrivate *self) {
  return self->maskInverted();
}

//  void QQuickMultiEffectPrivate::setMaskInverted(bool inverted)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate15setMaskInvertedEb(
    QQuickMultiEffectPrivate *self,
    bool inverted) {
  self->setMaskInverted(inverted);
}

//  QRectF QQuickMultiEffectPrivate::itemRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK24QQuickMultiEffectPrivate8itemRectEv(
    const QQuickMultiEffectPrivate *self) {
  return new QRectF(self->itemRect());
}

//  QString QQuickMultiEffectPrivate::fragmentShader() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QQuickMultiEffectPrivate14fragmentShaderEv(
    const QQuickMultiEffectPrivate *self) {
  return new QString(self->fragmentShader());
}

//  QString QQuickMultiEffectPrivate::vertexShader() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QQuickMultiEffectPrivate12vertexShaderEv(
    const QQuickMultiEffectPrivate *self) {
  return new QString(self->vertexShader());
}

//  bool QQuickMultiEffectPrivate::hasProxySource() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickMultiEffectPrivate14hasProxySourceEv(
    const QQuickMultiEffectPrivate *self) {
  return self->hasProxySource();
}

//  void QQuickMultiEffectPrivate::updateMaskThresholdSpread()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate25updateMaskThresholdSpreadEv(
    QQuickMultiEffectPrivate *self) {
  self->updateMaskThresholdSpread();
}

//  void QQuickMultiEffectPrivate::updateCenterOffset()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate18updateCenterOffsetEv(
    QQuickMultiEffectPrivate *self) {
  self->updateCenterOffset();
}

//  void QQuickMultiEffectPrivate::updateShadowOffset()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate18updateShadowOffsetEv(
    QQuickMultiEffectPrivate *self) {
  self->updateShadowOffset();
}

//  void QQuickMultiEffectPrivate::updateColorizationColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate23updateColorizationColorEv(
    QQuickMultiEffectPrivate *self) {
  self->updateColorizationColor();
}

//  void QQuickMultiEffectPrivate::updateShadowColor()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate17updateShadowColorEv(
    QQuickMultiEffectPrivate *self) {
  self->updateShadowColor();
}

//  float QQuickMultiEffectPrivate::calculateLod(float blurAmount)
extern "C" Q_DECL_EXPORT
float ritual_ZN24QQuickMultiEffectPrivate12calculateLodEf(
    QQuickMultiEffectPrivate *self,
    float blurAmount) {
  return self->calculateLod(blurAmount);
}

//  float QQuickMultiEffectPrivate::blurWeight(float v)
extern "C" Q_DECL_EXPORT
float ritual_ZN24QQuickMultiEffectPrivate10blurWeightEf(
    QQuickMultiEffectPrivate *self,
    float v) {
  return self->blurWeight(v);
}

//  void QQuickMultiEffectPrivate::updateBlurWeights()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate17updateBlurWeightsEv(
    QQuickMultiEffectPrivate *self) {
  self->updateBlurWeights();
}

//  void QQuickMultiEffectPrivate::updateShadowBlurWeights()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate23updateShadowBlurWeightsEv(
    QQuickMultiEffectPrivate *self) {
  self->updateShadowBlurWeights();
}

//  void QQuickMultiEffectPrivate::updateBlurItemsAmount(int blurLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate21updateBlurItemsAmountEi(
    QQuickMultiEffectPrivate *self,
    int blurLevel) {
  self->updateBlurItemsAmount(blurLevel);
}

//  void QQuickMultiEffectPrivate::updateProxyActiveCheck()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickMultiEffectPrivate22updateProxyActiveCheckEv(
    QQuickMultiEffectPrivate *self) {
  self->updateProxyActiveCheck();
}

//  a Python function taken by a CuteQQuickMultiEffectPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickMultiEffectPrivate(
    QQuickMultiEffectPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickMultiEffectPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_shadereffect)
