//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwareinternalrectanglenode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwareinternalrectanglenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgsoftwareinternalrectanglenode_p.h>
#include <QtCore/qmath.h>
#include <QtGui/QPainter>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 70, as local:qsgsoftwareinternalrectanglenode.cpp:interpolateStop
static QGradientStop interpolateStop(const QGradientStop &firstStop, const QGradientStop &secondStop, double newPos)
{
    double distance = secondStop.first - firstStop.first;
    double distanceDelta = newPos - firstStop.first;
    double modifierValue = distanceDelta / distance;
    const auto firstStopRgbColor = firstStop.second.toRgb();
    const auto secondStopRgbColor = secondStop.second.toRgb();
    int redDelta = (secondStopRgbColor.red() - firstStopRgbColor.red()) * modifierValue;
    int greenDelta = (secondStopRgbColor.green() - firstStopRgbColor.green()) * modifierValue;
    int blueDelta = (secondStopRgbColor.blue() - firstStopRgbColor.blue()) * modifierValue;
    int alphaDelta = (secondStopRgbColor.alpha() - firstStopRgbColor.alpha()) * modifierValue;

    QGradientStop newStop;
    newStop.first = newPos;
    newStop.second = QColor(firstStopRgbColor.red() + redDelta,
                            firstStopRgbColor.green() + greenDelta,
                            firstStopRgbColor.blue() + blueDelta,
                            firstStopRgbColor.alpha() + alphaDelta);

    return newStop;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 33, as _ZN32QSGSoftwareInternalRectangleNode7setRectERK6QRectF
inline void QSGSoftwareInternalRectangleNode::setRect(const QRectF &rect)
{
    QRect alignedRect = rect.toAlignedRect();
    if (m_rect != alignedRect) {
        m_rect = alignedRect;
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 42, as _ZN32QSGSoftwareInternalRectangleNode8setColorERK6QColor
inline void QSGSoftwareInternalRectangleNode::setColor(const QColor &color)
{
    if (m_color != color) {
        m_color = color;
        m_cornerPixmapIsDirty = true;
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 51, as _ZN32QSGSoftwareInternalRectangleNode11setPenColorERK6QColor
inline void QSGSoftwareInternalRectangleNode::setPenColor(const QColor &color)
{
    if (m_penColor != color) {
        m_penColor = color;
        m_cornerPixmapIsDirty = true;
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 60, as _ZN32QSGSoftwareInternalRectangleNode11setPenWidthEd
inline void QSGSoftwareInternalRectangleNode::setPenWidth(qreal width)
{
    if (m_penWidth != width) {
        m_penWidth = width;
        m_cornerPixmapIsDirty = true;
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 165, as _ZN32QSGSoftwareInternalRectangleNode19setGradientVerticalEb
inline void QSGSoftwareInternalRectangleNode::setGradientVertical(bool vertical)
{
    if (m_vertical != vertical) {
        m_vertical = vertical;
        m_cornerPixmapIsDirty = true;
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 174, as _ZN32QSGSoftwareInternalRectangleNode9setRadiusEd
inline void QSGSoftwareInternalRectangleNode::setRadius(qreal radius)
{
    if (m_radius == radius)
        return;
    m_radius = radius;
    m_cornerPixmapIsDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 183, as _ZN32QSGSoftwareInternalRectangleNode16setTopLeftRadiusEd
inline void QSGSoftwareInternalRectangleNode::setTopLeftRadius(qreal radius)
{
    if (m_isTopLeftRadiusSet && m_topLeftRadius == radius)
        return;
    m_isTopLeftRadiusSet = true;
    m_topLeftRadius = radius;
    m_cornerPixmapIsDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 193, as _ZN32QSGSoftwareInternalRectangleNode17setTopRightRadiusEd
inline void QSGSoftwareInternalRectangleNode::setTopRightRadius(qreal radius)
{
    if (m_isTopRightRadiusSet && m_topRightRadius == radius)
        return;
    m_isTopRightRadiusSet = true;
    m_topRightRadius = radius;
    m_cornerPixmapIsDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 203, as _ZN32QSGSoftwareInternalRectangleNode19setBottomLeftRadiusEd
inline void QSGSoftwareInternalRectangleNode::setBottomLeftRadius(qreal radius)
{
    if (m_isBottomLeftRadiusSet && m_bottomLeftRadius == radius)
        return;
    m_isBottomLeftRadiusSet = true;
    m_bottomLeftRadius = radius;
    m_cornerPixmapIsDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 213, as _ZN32QSGSoftwareInternalRectangleNode20setBottomRightRadiusEd
inline void QSGSoftwareInternalRectangleNode::setBottomRightRadius(qreal radius)
{
    if (m_isBottomRightRadiusSet && m_bottomRightRadius == radius)
        return;
    m_isBottomRightRadiusSet = true;
    m_bottomRightRadius = radius;
    m_cornerPixmapIsDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 223, as _ZN32QSGSoftwareInternalRectangleNode18resetTopLeftRadiusEv
inline void QSGSoftwareInternalRectangleNode::resetTopLeftRadius()
{
    if (!m_isTopLeftRadiusSet)
        return;
    m_isTopLeftRadiusSet = false;
    m_cornerPixmapIsDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 232, as _ZN32QSGSoftwareInternalRectangleNode19resetTopRightRadiusEv
inline void QSGSoftwareInternalRectangleNode::resetTopRightRadius()
{
    if (!m_isTopRightRadiusSet)
        return;
    m_isTopRightRadiusSet = false;
    m_cornerPixmapIsDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 241, as _ZN32QSGSoftwareInternalRectangleNode21resetBottomLeftRadiusEv
inline void QSGSoftwareInternalRectangleNode::resetBottomLeftRadius()
{
    if (!m_isBottomLeftRadiusSet)
        return;
    m_isBottomLeftRadiusSet = false;
    m_cornerPixmapIsDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 250, as _ZN32QSGSoftwareInternalRectangleNode22resetBottomRightRadiusEv
inline void QSGSoftwareInternalRectangleNode::resetBottomRightRadius()
{
    if (!m_isBottomRightRadiusSet)
        return;
    m_isBottomRightRadiusSet = false;
    m_cornerPixmapIsDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 259, as _ZN32QSGSoftwareInternalRectangleNode10setAlignedEb
inline void QSGSoftwareInternalRectangleNode::setAligned(bool /*aligned*/)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 263, as _ZN32QSGSoftwareInternalRectangleNode6updateEv
inline void QSGSoftwareInternalRectangleNode::update()
{
    if (!m_penWidth || m_penColor == Qt::transparent) {
        m_pen = Qt::NoPen;
    } else {
        m_pen = QPen(m_penColor);
        m_pen.setWidthF(m_penWidth);
    }

    if (!m_stops.isEmpty()) {
        QLinearGradient gradient(QPoint(0,0), QPoint(m_vertical ? 0 : m_rect.width(), m_vertical ? m_rect.height() : 0));
        gradient.setStops(m_stops);
        m_brush = QBrush(gradient);
    } else {
        m_brush = QBrush(m_color);
    }

    if (m_cornerPixmapIsDirty) {
        generateCornerPixmap();
        m_cornerPixmapIsDirty = false;
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 286, as _ZN32QSGSoftwareInternalRectangleNode5paintEP8QPainter
inline void QSGSoftwareInternalRectangleNode::paint(QPainter *painter)
{
    //We can only check for a device pixel ratio change when we know what
    //paint device is being used.
    if (!qFuzzyCompare(painter->device()->devicePixelRatio(), m_devicePixelRatio)) {
        m_devicePixelRatio = painter->device()->devicePixelRatio();
        generateCornerPixmap();
    }

    if (painter->transform().isRotating()) {
        //Rotated rectangles lose the benefits of direct rendering, and have poor rendering
        //quality when using only blits and fills.

        if (m_radius == 0
            && m_penWidth == 0
            && !m_isTopLeftRadiusSet
            && !m_isTopRightRadiusSet
            && !m_isBottomLeftRadiusSet
            && !m_isBottomRightRadiusSet) {
            //Non-Rounded Rects without borders (fall back to drawRect)
            //Most common case
            painter->setPen(Qt::NoPen);
            painter->setBrush(m_brush);
            painter->drawRect(m_rect);
        } else if (!m_isTopLeftRadiusSet
                   && !m_isTopRightRadiusSet
                   && !m_isBottomLeftRadiusSet
                   && !m_isBottomRightRadiusSet) {
            //Rounded Rects and Rects with Borders
            //Avoids broken behaviors of QPainter::drawRect/roundedRect
            QPixmap pixmap = QPixmap(qRound(m_rect.width() * m_devicePixelRatio), qRound(m_rect.height() * m_devicePixelRatio));
            pixmap.fill(Qt::transparent);
            pixmap.setDevicePixelRatio(m_devicePixelRatio);
            QPainter pixmapPainter(&pixmap);
            paintRectangle(&pixmapPainter, QRect(0, 0, m_rect.width(), m_rect.height()));

            QPainter::RenderHints previousRenderHints = painter->renderHints();
            painter->setRenderHint(QPainter::SmoothPixmapTransform, true);
            painter->drawPixmap(m_rect, pixmap);
            painter->setRenderHints(previousRenderHints);
        } else {
            // Corners with different radii. Split implementation to avoid
            // performance regression of the majority of cases
            QPixmap pixmap = QPixmap(qRound(m_rect.width() * m_devicePixelRatio), qRound(m_rect.height() * m_devicePixelRatio));
            pixmap.fill(Qt::transparent);
            pixmap.setDevicePixelRatio(m_devicePixelRatio);
            QPainter pixmapPainter(&pixmap);
            // Slow function relying on paths
            paintRectangleIndividualCorners(&pixmapPainter, QRect(0, 0, m_rect.width(), m_rect.height()));

            QPainter::RenderHints previousRenderHints = painter->renderHints();
            painter->setRenderHint(QPainter::SmoothPixmapTransform, true);
            painter->drawPixmap(m_rect, pixmap);
            painter->setRenderHints(previousRenderHints);

        }


    } else {
        //Paint directly
        if (!m_isTopLeftRadiusSet
            && !m_isTopRightRadiusSet
            && !m_isBottomLeftRadiusSet
            && !m_isBottomRightRadiusSet) {
            paintRectangle(painter, m_rect);
        } else {
            paintRectangleIndividualCorners(painter, m_rect);
        }
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 357, as _ZNK32QSGSoftwareInternalRectangleNode8isOpaqueEv
inline bool QSGSoftwareInternalRectangleNode::isOpaque() const
{
    if (m_radius > 0.0f
        || m_topLeftRadius > 0.0f
        || m_topRightRadius > 0.0f
        || m_bottomRightRadius > 0.0f
        || m_bottomLeftRadius > 0.0f)
        return false;
    if (m_color.alpha() < 255)
        return false;
    if (m_penWidth > 0.0f && m_penColor.alpha() < 255)
        return false;
    if (m_stops.size() > 0) {
        for (const QGradientStop &stop : std::as_const(m_stops)) {
            if (stop.second.alpha() < 255)
                return false;
        }
    }

    return true;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 379, as _ZNK32QSGSoftwareInternalRectangleNode4rectEv
inline QRectF QSGSoftwareInternalRectangleNode::rect() const
{
    //TODO: double check that this is correct.
    return m_rect;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 385, as _ZN32QSGSoftwareInternalRectangleNode14paintRectangleEP8QPainterRK5QRect
inline void QSGSoftwareInternalRectangleNode::paintRectangle(QPainter *painter, const QRect &rect)
{
    //Radius should never exceeds half of the width or half of the height
    int radius = qFloor(qMin(qMin(rect.width(), rect.height()) * 0.5, m_radius));
    QPainter::RenderHints previousRenderHints = painter->renderHints();
    painter->setRenderHint(QPainter::Antialiasing, false);

    if (m_penWidth > 0) {
        //Fill border Rects

        //Borders can not be more than half the height/width of a rect
        double borderWidth = qMin(m_penWidth, rect.width() * 0.5);
        double borderHeight = qMin(m_penWidth, rect.height() * 0.5);



        if (borderWidth > radius) {
            //4 Rects
            QRectF borderTopOutside(QPointF(rect.x() + radius, rect.y()),
                                    QPointF(rect.x() + rect.width() - radius, rect.y() + radius));
            QRectF borderTopInside(QPointF(rect.x() + borderWidth, rect.y() + radius),
                                   QPointF(rect.x() + rect.width() - borderWidth, rect.y() + borderHeight));
            QRectF borderBottomOutside(QPointF(rect.x() + radius, rect.y() + rect.height() - radius),
                                       QPointF(rect.x() + rect.width() - radius, rect.y() + rect.height()));
            QRectF borderBottomInside(QPointF(rect.x() + borderWidth, rect.y() + rect.height() - borderHeight),
                                      QPointF(rect.x() + rect.width() - borderWidth, rect.y() + rect.height() - radius));

            if (borderTopOutside.isValid())
                painter->fillRect(borderTopOutside, m_penColor);
            if (borderTopInside.isValid())
                painter->fillRect(borderTopInside, m_penColor);
            if (borderBottomOutside.isValid())
                painter->fillRect(borderBottomOutside, m_penColor);
            if (borderBottomInside.isValid())
                painter->fillRect(borderBottomInside, m_penColor);

        } else {
            //2 Rects
            QRectF borderTop(QPointF(rect.x() + radius, rect.y()),
                             QPointF(rect.x() + rect.width() - radius, rect.y() + borderHeight));
            QRectF borderBottom(QPointF(rect.x() + radius, rect.y() + rect.height() - borderHeight),
                                QPointF(rect.x() + rect.width() - radius, rect.y() + rect.height()));
            if (borderTop.isValid())
                painter->fillRect(borderTop, m_penColor);
            if (borderBottom.isValid())
                painter->fillRect(borderBottom, m_penColor);
        }
        QRectF borderLeft(QPointF(rect.x(), rect.y() + radius),
                          QPointF(rect.x() + borderWidth, rect.y() + rect.height() - radius));
        QRectF borderRight(QPointF(rect.x() + rect.width() - borderWidth, rect.y() + radius),
                           QPointF(rect.x() + rect.width(), rect.y() + rect.height() - radius));
        if (borderLeft.isValid())
            painter->fillRect(borderLeft, m_penColor);
        if (borderRight.isValid())
            painter->fillRect(borderRight, m_penColor);
    }


    if (radius > 0) {

        if (radius * 2 >= rect.width() && radius * 2 >= rect.height()) {
            //Blit whole pixmap for circles
            painter->drawPixmap(rect, m_cornerPixmap, m_cornerPixmap.rect());
        } else {

            //blit 4 corners to border
            int scaledRadius = qRound(radius * m_devicePixelRatio);
            QRectF topLeftCorner(QPointF(rect.x(), rect.y()),
                                 QPointF(rect.x() + radius, rect.y() + radius));
            painter->drawPixmap(topLeftCorner, m_cornerPixmap, QRectF(0, 0, scaledRadius, scaledRadius));
            QRectF topRightCorner(QPointF(rect.x() + rect.width() - radius, rect.y()),
                                  QPointF(rect.x() + rect.width(), rect.y() + radius));
            painter->drawPixmap(topRightCorner, m_cornerPixmap, QRectF(scaledRadius, 0, scaledRadius, scaledRadius));
            QRectF bottomLeftCorner(QPointF(rect.x(), rect.y() + rect.height() - radius),
                                    QPointF(rect.x() + radius, rect.y() + rect.height()));
            painter->drawPixmap(bottomLeftCorner, m_cornerPixmap, QRectF(0, scaledRadius, scaledRadius, scaledRadius));
            QRectF bottomRightCorner(QPointF(rect.x() + rect.width() - radius, rect.y() + rect.height() - radius),
                                     QPointF(rect.x() + rect.width(), rect.y() + rect.height()));
            painter->drawPixmap(bottomRightCorner, m_cornerPixmap, QRectF(scaledRadius, scaledRadius, scaledRadius, scaledRadius));

        }

    }

    QRectF brushRect = QRectF(rect).marginsRemoved(QMarginsF(m_penWidth, m_penWidth, m_penWidth, m_penWidth));
    if (brushRect.width() < 0)
        brushRect.setWidth(0);
    if (brushRect.height() < 0)
        brushRect.setHeight(0);
    double innerRectRadius = qMax(0.0, radius - m_penWidth);

    //If not completely transparent or has a gradient
    if (m_color.alpha() > 0 || !m_stops.empty()) {
        if (innerRectRadius > 0) {
            //Rounded Rect
            if (m_stops.empty()) {
                //Rounded Rects without gradient need 3 blits
                QRectF centerRect(QPointF(brushRect.x() + innerRectRadius, brushRect.y()),
                                  QPointF(brushRect.x() + brushRect.width() - innerRectRadius, brushRect.y() + brushRect.height()));
                painter->fillRect(centerRect, m_color);
                QRectF leftRect(QPointF(brushRect.x(), brushRect.y() + innerRectRadius),
                                QPointF(brushRect.x() + innerRectRadius, brushRect.y() + brushRect.height() - innerRectRadius));
                painter->fillRect(leftRect, m_color);
                QRectF rightRect(QPointF(brushRect.x() + brushRect.width() - innerRectRadius, brushRect.y() + innerRectRadius),
                                 QPointF(brushRect.x() + brushRect.width(), brushRect.y() + brushRect.height() - innerRectRadius));
                painter->fillRect(rightRect, m_color);
            } else {
                //Rounded Rect with gradient (slow)
                painter->setPen(Qt::NoPen);
                painter->setBrush(m_brush);
                painter->drawRoundedRect(brushRect, innerRectRadius, innerRectRadius);
            }
        } else {
            //non-rounded rects only need 1 blit
            painter->fillRect(brushRect, m_brush);
        }
    }

    painter->setRenderHints(previousRenderHints);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 506, as _ZN32QSGSoftwareInternalRectangleNode31paintRectangleIndividualCornersEP8QPainterRK5QRect
inline void QSGSoftwareInternalRectangleNode::paintRectangleIndividualCorners(QPainter *painter, const QRect &rect)
{
    QPainterPath path;

    const float w = m_penWidth;

    // Radius should never exceeds half of the width or half of the height
    const float radiusTL = qMin(qMin(rect.width(), rect.height()) * 0.5f,
                                m_isTopLeftRadiusSet ? m_topLeftRadius : m_radius);
    const float radiusTR = qMin(qMin(rect.width(), rect.height()) * 0.5f,
                                m_isTopRightRadiusSet ? m_topRightRadius : m_radius);
    const float radiusBL = qMin(qMin(rect.width(), rect.height()) * 0.5f,
                                m_isBottomLeftRadiusSet ? m_bottomLeftRadius : m_radius);
    const float radiusBR = qMin(qMin(rect.width(), rect.height()) * 0.5f,
                                m_isBottomRightRadiusSet ? m_bottomRightRadius : m_radius);

    const float innerRadiusTL = qMin(qMin(rect.width(), rect.height()) * 0.5f, radiusTL - w);
    const float innerRadiusTR = qMin(qMin(rect.width(), rect.height()) * 0.5f, radiusTR - w);
    const float innerRadiusBL = qMin(qMin(rect.width(), rect.height()) * 0.5f, radiusBL - w);
    const float innerRadiusBR = qMin(qMin(rect.width(), rect.height()) * 0.5f, radiusBR - w);

    QRect rect2 = rect.adjusted(0, 0, 1, 1);

    path.moveTo(rect2.topRight() - QPointF(radiusTR, -w));
    if (innerRadiusTR > 0.)
        path.arcTo(QRectF(rect2.topRight() - QPointF(radiusTR + innerRadiusTR, -w), 2. * QSizeF(innerRadiusTR, innerRadiusTR)), 90, -90);
    else
        path.lineTo(rect2.topRight() - QPointF(w, -w));

    if (innerRadiusBR > 0.)
        path.arcTo(QRectF(rect2.bottomRight() - QPointF(radiusBR + innerRadiusBR, radiusBR + innerRadiusBR), 2. * QSizeF(innerRadiusBR, innerRadiusBR)), 0, -90);
    else
        path.lineTo(rect2.bottomRight() - QPointF(w, w));

    if (innerRadiusBL > 0.)
        path.arcTo(QRectF(rect2.bottomLeft() - QPointF(-w, radiusBL + innerRadiusBL), 2. * QSizeF(innerRadiusBL, innerRadiusBL)), -90, -90);
    else
        path.lineTo(rect2.bottomLeft() - QPointF(-w, w));
    if (innerRadiusTL > 0.)
        path.arcTo(QRectF(rect2.topLeft() + QPointF(w, w), 2. * QSizeF(innerRadiusTL, innerRadiusTL)), -180, -90);
    else
        path.lineTo(rect2.topLeft() + QPointF(w, w));
    path.closeSubpath();

    painter->setPen(Qt::NoPen);
    painter->setBrush(m_brush);
    painter->drawPath(path);

    if (w > 0) {
        path.moveTo(rect2.topRight() - QPointF(radiusTR, 0.));
        if (radiusTR > 0.)
            path.arcTo(QRectF(rect2.topRight() - 2. * QPointF(radiusTR, 0.), 2. * QSizeF(radiusTR, radiusTR)), 90, -90);
        else
            path.lineTo(rect2.topRight());
        if (radiusBR > 0.)
            path.arcTo(QRectF(rect2.bottomRight() - 2. * QPointF(radiusBR, radiusBR), 2. * QSizeF(radiusBR, radiusBR)), 0, -90);
        else
            path.lineTo(rect2.bottomRight());
        if (radiusBL > 0.)
            path.arcTo(QRectF(rect2.bottomLeft() - 2. * QPointF(0., radiusBL), 2. * QSizeF(radiusBL, radiusBL)), -90, -90);
        else
            path.lineTo(rect2.bottomLeft());
        if (radiusTL > 0.)
            path.arcTo(QRectF(rect2.topLeft() - 2. * QPointF(0., 0.), 2. * QSizeF(radiusTL, radiusTL)), -180, -90);
        else
            path.lineTo(rect2.topLeft());
        path.closeSubpath();

        painter->setBrush(m_penColor);
        painter->drawPath(path);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 579, as _ZN32QSGSoftwareInternalRectangleNode20generateCornerPixmapEv
inline void QSGSoftwareInternalRectangleNode::generateCornerPixmap()
{
    //Generate new corner Pixmap
    int radius = qFloor(qMin(qMin(m_rect.width(), m_rect.height()) * 0.5, m_radius));
    const auto width = qRound(radius * 2 * m_devicePixelRatio);

    if (m_cornerPixmap.width() != width)
        m_cornerPixmap = QPixmap(width, width);

    m_cornerPixmap.setDevicePixelRatio(m_devicePixelRatio);
    m_cornerPixmap.fill(Qt::transparent);

    if (radius > 0) {
        QPainter cornerPainter(&m_cornerPixmap);
        cornerPainter.setRenderHint(QPainter::Antialiasing);
        cornerPainter.setCompositionMode(QPainter::CompositionMode_Source);

        //Paint outer cicle
        if (m_penWidth > 0) {
            cornerPainter.setPen(Qt::NoPen);
            cornerPainter.setBrush(m_penColor);
            cornerPainter.drawRoundedRect(QRectF(0, 0, radius * 2, radius *2), radius, radius);
        }

        //Paint inner circle
        if (radius > m_penWidth) {
            cornerPainter.setPen(Qt::NoPen);
            if (m_stops.isEmpty())
                cornerPainter.setBrush(m_brush);
            else
                cornerPainter.setBrush(Qt::transparent);

            QMarginsF adjustmentMargins(m_penWidth, m_penWidth, m_penWidth, m_penWidth);
            QRectF cornerCircleRect = QRectF(0, 0, radius * 2, radius * 2).marginsRemoved(adjustmentMargins);
            cornerPainter.drawRoundedRect(cornerCircleRect, radius, radius);
        }
        cornerPainter.end();
    }
}
//  -----------------------------------------------------------------------

//  void QSGSoftwareInternalRectangleNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode7setRectERK6QRectF(
    QSGSoftwareInternalRectangleNode *self,
    const QRectF *rect) {
  self->setRect(*rect);
}

//  void QSGSoftwareInternalRectangleNode::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode8setColorERK6QColor(
    QSGSoftwareInternalRectangleNode *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void QSGSoftwareInternalRectangleNode::setPenColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode11setPenColorERK6QColor(
    QSGSoftwareInternalRectangleNode *self,
    const QColor *color) {
  self->setPenColor(*color);
}

//  void QSGSoftwareInternalRectangleNode::setPenWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode11setPenWidthEd(
    QSGSoftwareInternalRectangleNode *self,
    qreal width) {
  self->setPenWidth(width);
}

//  void QSGSoftwareInternalRectangleNode::setGradientStops(const
//      QGradientStops &stops)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode16setGradientStopsERK5QListISt4pairId6QColorEE(
    QSGSoftwareInternalRectangleNode *self,
    const QGradientStops *stops) {
  self->setGradientStops(*stops);
}

//  void QSGSoftwareInternalRectangleNode::setGradientVertical(bool vertical)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode19setGradientVerticalEb(
    QSGSoftwareInternalRectangleNode *self,
    bool vertical) {
  self->setGradientVertical(vertical);
}

//  void QSGSoftwareInternalRectangleNode::setRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode9setRadiusEd(
    QSGSoftwareInternalRectangleNode *self,
    qreal radius) {
  self->setRadius(radius);
}

//  void QSGSoftwareInternalRectangleNode::setTopLeftRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode16setTopLeftRadiusEd(
    QSGSoftwareInternalRectangleNode *self,
    qreal radius) {
  self->setTopLeftRadius(radius);
}

//  void QSGSoftwareInternalRectangleNode::setTopRightRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode17setTopRightRadiusEd(
    QSGSoftwareInternalRectangleNode *self,
    qreal radius) {
  self->setTopRightRadius(radius);
}

//  void QSGSoftwareInternalRectangleNode::setBottomLeftRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode19setBottomLeftRadiusEd(
    QSGSoftwareInternalRectangleNode *self,
    qreal radius) {
  self->setBottomLeftRadius(radius);
}

//  void QSGSoftwareInternalRectangleNode::setBottomRightRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode20setBottomRightRadiusEd(
    QSGSoftwareInternalRectangleNode *self,
    qreal radius) {
  self->setBottomRightRadius(radius);
}

//  void QSGSoftwareInternalRectangleNode::resetTopLeftRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode18resetTopLeftRadiusEv(
    QSGSoftwareInternalRectangleNode *self) {
  self->resetTopLeftRadius();
}

//  void QSGSoftwareInternalRectangleNode::resetTopRightRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode19resetTopRightRadiusEv(
    QSGSoftwareInternalRectangleNode *self) {
  self->resetTopRightRadius();
}

//  void QSGSoftwareInternalRectangleNode::resetBottomLeftRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode21resetBottomLeftRadiusEv(
    QSGSoftwareInternalRectangleNode *self) {
  self->resetBottomLeftRadius();
}

//  void QSGSoftwareInternalRectangleNode::resetBottomRightRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode22resetBottomRightRadiusEv(
    QSGSoftwareInternalRectangleNode *self) {
  self->resetBottomRightRadius();
}

//  void QSGSoftwareInternalRectangleNode::setAntialiasing(bool antialiasing)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode15setAntialiasingEb(
    QSGSoftwareInternalRectangleNode *self,
    bool antialiasing) {
  self->setAntialiasing(antialiasing);
}

//  void QSGSoftwareInternalRectangleNode::setAligned(bool aligned)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode10setAlignedEb(
    QSGSoftwareInternalRectangleNode *self,
    bool aligned) {
  self->setAligned(aligned);
}

//  void QSGSoftwareInternalRectangleNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode6updateEv(
    QSGSoftwareInternalRectangleNode *self) {
  self->update();
}

//  void QSGSoftwareInternalRectangleNode::paint(QPainter *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode5paintEP8QPainter(
    QSGSoftwareInternalRectangleNode *self,
    QPainter *a0) {
  self->paint(a0);
}

//  bool QSGSoftwareInternalRectangleNode::isOpaque() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QSGSoftwareInternalRectangleNode8isOpaqueEv(
    const QSGSoftwareInternalRectangleNode *self) {
  return self->isOpaque();
}

//  QRectF QSGSoftwareInternalRectangleNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK32QSGSoftwareInternalRectangleNode4rectEv(
    const QSGSoftwareInternalRectangleNode *self) {
  return new QRectF(self->rect());
}

//  void QSGSoftwareInternalRectangleNode::paintRectangle(QPainter *painter,
//      const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode14paintRectangleEP8QPainterRK5QRect(
    QSGSoftwareInternalRectangleNode *self,
    QPainter *painter,
    const QRect *rect) {
  self->paintRectangle(painter, *rect);
}

//  void QSGSoftwareInternalRectangleNode::paintRectangleIndividualCorners(QP
//      ainter *painter, const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode31paintRectangleIndividualCornersEP8QPainterRK5QRect(
    QSGSoftwareInternalRectangleNode *self,
    QPainter *painter,
    const QRect *rect) {
  self->paintRectangleIndividualCorners(painter, *rect);
}

//  void QSGSoftwareInternalRectangleNode::generateCornerPixmap()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSGSoftwareInternalRectangleNode20generateCornerPixmapEv(
    QSGSoftwareInternalRectangleNode *self) {
  self->generateCornerPixmap();
}

//  void QSGSoftwareInternalRectangleNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QSGSoftwareInternalRectangleNode7setRectERK6QRectF(
    QSGSoftwareInternalRectangleNode *self,
    const QRectF *rect) {
  self->QSGSoftwareInternalRectangleNode::setRect(*rect);
}

//  void QSGSoftwareInternalRectangleNode::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QSGSoftwareInternalRectangleNode8setColorERK6QColor(
    QSGSoftwareInternalRectangleNode *self,
    const QColor *color) {
  self->QSGSoftwareInternalRectangleNode::setColor(*color);
}

//  void QSGSoftwareInternalRectangleNode::setPenColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QSGSoftwareInternalRectangleNode11setPenColorERK6QColor(
    QSGSoftwareInternalRectangleNode *self,
    const QColor *color) {
  self->QSGSoftwareInternalRectangleNode::setPenColor(*color);
}

//  void QSGSoftwareInternalRectangleNode::setPenWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QSGSoftwareInternalRectangleNode11setPenWidthEd(
    QSGSoftwareInternalRectangleNode *self,
    qreal width) {
  self->QSGSoftwareInternalRectangleNode::setPenWidth(width);
}

//  void QSGSoftwareInternalRectangleNode::setGradientVertical(bool vertical)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QSGSoftwareInternalRectangleNode19setGradientVerticalEb(
    QSGSoftwareInternalRectangleNode *self,
    bool vertical) {
  self->QSGSoftwareInternalRectangleNode::setGradientVertical(vertical);
}

//  void QSGSoftwareInternalRectangleNode::setRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QSGSoftwareInternalRectangleNode9setRadiusEd(
    QSGSoftwareInternalRectangleNode *self,
    qreal radius) {
  self->QSGSoftwareInternalRectangleNode::setRadius(radius);
}

//  void QSGSoftwareInternalRectangleNode::setTopLeftRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QSGSoftwareInternalRectangleNode16setTopLeftRadiusEd(
    QSGSoftwareInternalRectangleNode *self,
    qreal radius) {
  self->QSGSoftwareInternalRectangleNode::setTopLeftRadius(radius);
}

//  void QSGSoftwareInternalRectangleNode::setTopRightRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QSGSoftwareInternalRectangleNode17setTopRightRadiusEd(
    QSGSoftwareInternalRectangleNode *self,
    qreal radius) {
  self->QSGSoftwareInternalRectangleNode::setTopRightRadius(radius);
}

//  void QSGSoftwareInternalRectangleNode::setBottomLeftRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QSGSoftwareInternalRectangleNode19setBottomLeftRadiusEd(
    QSGSoftwareInternalRectangleNode *self,
    qreal radius) {
  self->QSGSoftwareInternalRectangleNode::setBottomLeftRadius(radius);
}

//  void QSGSoftwareInternalRectangleNode::setBottomRightRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QSGSoftwareInternalRectangleNode20setBottomRightRadiusEd(
    QSGSoftwareInternalRectangleNode *self,
    qreal radius) {
  self->QSGSoftwareInternalRectangleNode::setBottomRightRadius(radius);
}

//  void QSGSoftwareInternalRectangleNode::resetTopLeftRadius()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QSGSoftwareInternalRectangleNode18resetTopLeftRadiusEv(
    QSGSoftwareInternalRectangleNode *self) {
  self->QSGSoftwareInternalRectangleNode::resetTopLeftRadius();
}

//  void QSGSoftwareInternalRectangleNode::resetTopRightRadius()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QSGSoftwareInternalRectangleNode19resetTopRightRadiusEv(
    QSGSoftwareInternalRectangleNode *self) {
  self->QSGSoftwareInternalRectangleNode::resetTopRightRadius();
}

//  void QSGSoftwareInternalRectangleNode::resetBottomLeftRadius()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QSGSoftwareInternalRectangleNode21resetBottomLeftRadiusEv(
    QSGSoftwareInternalRectangleNode *self) {
  self->QSGSoftwareInternalRectangleNode::resetBottomLeftRadius();
}

//  void QSGSoftwareInternalRectangleNode::resetBottomRightRadius()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QSGSoftwareInternalRectangleNode22resetBottomRightRadiusEv(
    QSGSoftwareInternalRectangleNode *self) {
  self->QSGSoftwareInternalRectangleNode::resetBottomRightRadius();
}

//  void QSGSoftwareInternalRectangleNode::setAntialiasing(bool antialiasing)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QSGSoftwareInternalRectangleNode15setAntialiasingEb(
    QSGSoftwareInternalRectangleNode *self,
    bool antialiasing) {
  self->QSGSoftwareInternalRectangleNode::setAntialiasing(antialiasing);
}

//  void QSGSoftwareInternalRectangleNode::setAligned(bool aligned)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QSGSoftwareInternalRectangleNode10setAlignedEb(
    QSGSoftwareInternalRectangleNode *self,
    bool aligned) {
  self->QSGSoftwareInternalRectangleNode::setAligned(aligned);
}

//  void QSGSoftwareInternalRectangleNode::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QSGSoftwareInternalRectangleNode6updateEv(
    QSGSoftwareInternalRectangleNode *self) {
  self->QSGSoftwareInternalRectangleNode::update();
}
