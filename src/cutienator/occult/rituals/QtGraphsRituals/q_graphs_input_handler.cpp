//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qgraphsinputhandler_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-27: code taken from Qt's source no longer
//  stands under defined(Q_OS_LINUX), which Qt does not write there; its
//  rituals no longer stand under defined(Q_OS_LINUX), as the code taken from
//  Qt they call no longer does. Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsinputhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qeventpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#include <QtGraphs/private/qgraphsinputhandler_p.h>
#include <QtQuick/private/qquickdraghandler_p.h>
#include <QtQuick/private/qquickpinchhandler_p.h>
#include <QtQuick/private/qquicktaphandler_p.h>
#include <QtQuick/private/qquickwheelhandler_p.h>
#include <QtGraphs/private/qquickgraphsitem_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs3d/utils/qgraphs3dlogging.cpp, line 14, as _Z10lcEvents3Dv
inline const QLoggingCategory &lcEvents3D()
{
    static const QLoggingCategory category("qt.graphs3d.events");
    return category;
}

//  from ../qtgraphs/src/graphs3d/utils/qgraphs3dlogging.cpp, line 13, as _Z14lcProperties3Dv
inline const QLoggingCategory &lcProperties3D()
{
    static const QLoggingCategory category("qt.graphs3d.properties");
    return category;
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 441, as _ZN19QGraphsInputHandler14hoverMoveEventEP11QHoverEvent
inline void QGraphsInputHandler::hoverMoveEvent(QHoverEvent *event)
{
    Q_EMIT mouseMove(event->oldPos());
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 67, as _ZN19QGraphsInputHandler14setZoomEnabledEb
inline void QGraphsInputHandler::setZoomEnabled(bool enable)
{
    if (m_flags.zoomEnabled == enable) {
        qCDebug(lcProperties3D) << __FUNCTION__
            << "value is already set to:" << enable;
        return;
    }
    m_flags.zoomEnabled = enable;
    if (m_graphsItem)
        emit m_graphsItem->zoomEnabledChanged(enable);
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 79, as _ZN19QGraphsInputHandler13isZoomEnabledEv
inline bool QGraphsInputHandler::isZoomEnabled()
{
    return m_flags.zoomEnabled;
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 84, as _ZN19QGraphsInputHandler22setZoomAtTargetEnabledEb
inline void QGraphsInputHandler::setZoomAtTargetEnabled(bool enable)
{
    if (m_flags.zoomAtTarget == enable) {
        qCDebug(lcProperties3D) << __FUNCTION__
            << "value is already set to:" << enable;
        return;
    }
    m_flags.zoomAtTarget = enable;
    if (m_graphsItem)
        emit m_graphsItem->zoomAtTargetEnabledChanged(enable);
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 96, as _ZN19QGraphsInputHandler21isZoomAtTargetEnabledEv
inline bool QGraphsInputHandler::isZoomAtTargetEnabled()
{
    return m_flags.zoomAtTarget;
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 101, as _ZN19QGraphsInputHandler18setRotationEnabledEb
inline void QGraphsInputHandler::setRotationEnabled(bool enable)
{
    if (m_flags.rotationEnabled == enable) {
        qCDebug(lcProperties3D) << __FUNCTION__
            << "value is already set to:" << enable;
    }
    m_flags.rotationEnabled = enable;
    if (m_graphsItem)
        emit m_graphsItem->rotationEnabledChanged(enable);
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 112, as _ZN19QGraphsInputHandler17isRotationEnabledEv
inline bool QGraphsInputHandler::isRotationEnabled()
{
    return m_flags.rotationEnabled;
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 117, as _ZN19QGraphsInputHandler13setPanEnabledEb
inline void QGraphsInputHandler::setPanEnabled(bool enable)
{
    if (m_flags.panEnabled == enable) {
        qCDebug(lcProperties3D) << __FUNCTION__
            << "value is already set to:" << enable;
    }
    m_flags.panEnabled = enable;
    if (m_graphsItem)
        emit m_graphsItem->panEnabledChanged(enable);
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 128, as _ZN19QGraphsInputHandler12isPanEnabledEv
inline bool QGraphsInputHandler::isPanEnabled()
{
    return m_flags.panEnabled;
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 133, as _ZN19QGraphsInputHandler11setDragModeEN10QtGraphs3D8DragModeE
inline void QGraphsInputHandler::setDragMode(QtGraphs3D::DragMode mode)
{
    if (m_dragMode == mode) {
        qCDebug(lcProperties3D) << __FUNCTION__
            << "value is already set to:" << mode;
    }
    m_dragMode = mode;
    if (m_graphsItem)
        emit m_graphsItem->dragModeChanged(mode);
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 144, as _ZN19QGraphsInputHandler8dragModeEv
inline QtGraphs3D::DragMode QGraphsInputHandler::dragMode()
{
    return m_dragMode;
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 149, as _ZN19QGraphsInputHandler19setSelectionEnabledEb
inline void QGraphsInputHandler::setSelectionEnabled(bool enable)
{
    if (m_flags.selectionEnabled == enable) {
        qCDebug(lcProperties3D) << __FUNCTION__
            << "value is already set to:" << enable;
        return;
    }
    m_flags.selectionEnabled = enable;
    if (m_graphsItem)
        emit m_graphsItem->selectionEnabledChanged(enable);
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 161, as _ZN19QGraphsInputHandler18isSelectionEnabledEv
inline bool QGraphsInputHandler::isSelectionEnabled()
{
    return m_flags.selectionEnabled;
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 166, as _ZN19QGraphsInputHandler22setDefaultInputHandlerEv
inline void QGraphsInputHandler::setDefaultInputHandler()
{
    setVisible(true);
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 171, as _ZN19QGraphsInputHandler24unsetDefaultInputHandlerEv
inline void QGraphsInputHandler::unsetDefaultInputHandler()
{
    setVisible(false);
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 176, as _ZN19QGraphsInputHandler22unsetDefaultTapHandlerEv
inline void QGraphsInputHandler::unsetDefaultTapHandler()
{
    QObject::disconnect(m_tapHandler,
                        &QQuickTapHandler::tapped,
                        this,
                        &QGraphsInputHandler::onTapped);
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 184, as _ZN19QGraphsInputHandler23unsetDefaultDragHandlerEv
inline void QGraphsInputHandler::unsetDefaultDragHandler()
{
    QObject::disconnect(m_dragHandler,
                        &QQuickDragHandler::translationChanged,
                        this,
                        &QGraphsInputHandler::onTranslationChanged);
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 192, as _ZN19QGraphsInputHandler24unsetDefaultWheelHandlerEv
inline void QGraphsInputHandler::unsetDefaultWheelHandler()
{
    QObject::disconnect(m_wheelHandler,
                        &QQuickWheelHandler::wheel,
                        this,
                        &QGraphsInputHandler::onWheel);
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 200, as _ZN19QGraphsInputHandler24unsetDefaultPinchHandlerEv
inline void QGraphsInputHandler::unsetDefaultPinchHandler()
{
    QObject::disconnect(m_pinchHandler,
                        &QQuickPinchHandler::scaleChanged,
                        this,
                        &QGraphsInputHandler::onPinchScaleChanged);
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 208, as _ZN19QGraphsInputHandler13setDragButtonE6QFlagsIN2Qt11MouseButtonEE
inline void QGraphsInputHandler::setDragButton(Qt::MouseButtons button)
{
    m_dragHandler->setAcceptedButtons(button);
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 213, as _ZN19QGraphsInputHandler12setPanButtonE6QFlagsIN2Qt11MouseButtonEE
inline void QGraphsInputHandler::setPanButton(Qt::MouseButtons button)
{
    m_panHandler->setAcceptedButtons(button);
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 242, as _ZN19QGraphsInputHandler8onTappedEv
inline void QGraphsInputHandler::onTapped()
{
    if (!m_flags.selectionEnabled)
        return;

    if (m_graphsItem->isSlicingActive()) {
        m_graphsItem->setSliceActivatedChanged(true);
        m_graphsItem->update();
        return;
    }
    m_graphsItem->doPicking(m_tapHandler->point().position());
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 255, as _ZN19QGraphsInputHandler20onTranslationChangedE9QVector2D
inline void QGraphsInputHandler::onTranslationChanged(QVector2D delta)
{

  bool dragButtons = m_dragHandler->centroid().pressedButtons().testAnyFlags(
                  m_dragHandler->acceptedButtons());

  bool panButtons = m_panHandler->centroid().pressedButtons().testAnyFlags(
                  m_panHandler->acceptedButtons());

    QQuickGraphsItem *item = m_graphsItem;
    float xRotation = item->cameraXRotation();
    float yRotation = item->cameraYRotation();

    if (panButtons || (dragButtons && m_dragMode == QtGraphs3D::DragMode::Pan)) {
        if (!m_flags.panEnabled)
            return;

        QVector3D camPos = item->cameraTargetPosition();
        QVector3D diff = item->cameraTarget()->mapDirectionToScene({delta.x(), -delta.y(), 0});
        float zoom = 1 / (item->cameraZoomLevel() / 100.0f);
        item->setCameraTargetPosition(camPos - diff * zoom);

    } else if (dragButtons && m_dragMode == QtGraphs3D::DragMode::Rotate) {
        if (!m_flags.rotationEnabled)
            return;

        float rotationSpeed = 1.0f;
    #if !defined(Q_OS_IOS)
        rotationSpeed = 10.0f;
    #endif
        // Calculate mouse movement since last frame
        // Apply to rotations
        xRotation += (delta.x() / rotationSpeed);
        yRotation += (delta.y() / rotationSpeed);
        item->setCameraXRotation(xRotation);
        item->setCameraYRotation(yRotation);
    }
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 294, as _ZN19QGraphsInputHandler13onGrabChangedEN15QPointingDevice14GrabTransitionE11QEventPoint
inline void QGraphsInputHandler::onGrabChanged(QPointingDevice::GrabTransition transition,
                                        QEventPoint point)
{
    static QPointF pickPoint;

    if (transition == QPointingDevice::GrabPassive) {
        pickPoint = point.position().toPoint();
    } else if (transition == QPointingDevice::GrabExclusive) {
        if (m_dragHandler->centroid().pressedButtons().testFlag(Qt::LeftButton))
            m_graphsItem->doPicking(pickPoint);
    } else if (transition == QPointingDevice::UngrabExclusive
               || transition == QPointingDevice::UngrabPassive) {
        setPosition(QPointF(.0f, .0f));
        setScale(1.f);
        setRotation(.0f);
        emit m_graphsItem->selectedElementChanged(QtGraphs3D::ElementType::None);
        pickPoint = QPointF();
    }
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 314, as _ZN19QGraphsInputHandler7onWheelEP16QQuickWheelEvent
inline void QGraphsInputHandler::onWheel(QQuickWheelEvent *event)
{
    if (!m_flags.zoomEnabled) {
        qCWarning(lcEvents3D, "%s zooming needs to be enabled",
                qUtf8Printable(QLatin1String(__FUNCTION__)));
        return;
    }

    int halfSizeZoomLevel = 50;
    int oneToOneZoomLevel = 100;

    int driftTowardCenterLevel = 175;
    float wheelZoomDrift = 0.1f;

    int nearZoomRangeDivider = 12;
    int midZoomRangeDivider = 60;
    int farZoomRangeDivider = 120;

    if (m_graphsItem->isSlicingActive())
        return;

    // Adjust zoom level based on what zoom range we're in.
    QQuickGraphsItem *item = m_graphsItem;
    int zoomLevel = int(item->cameraZoomLevel());
    const int minZoomLevel = int(item->minCameraZoomLevel());
    const int maxZoomLevel = int(item->maxCameraZoomLevel());
    if (zoomLevel > oneToOneZoomLevel)
        zoomLevel += event->angleDelta().y() / nearZoomRangeDivider;
    else if (zoomLevel > halfSizeZoomLevel)
        zoomLevel += event->angleDelta().y() / midZoomRangeDivider;
    else
        zoomLevel += event->angleDelta().y() / farZoomRangeDivider;
    zoomLevel = qBound(minZoomLevel, zoomLevel, maxZoomLevel);

    if (m_flags.zoomAtTarget) {
        QVector3D targetPosition = item->graphPositionAt(QPoint(event->x(), event->y()));
        float previousZoom = item->cameraZoomLevel();
        item->setCameraZoomLevel(zoomLevel);

        float diffAdj = 0.0f;

        // If zooming in/out outside the graph, or zooming out after certain point,
        // move towards the center.
        if ((qAbs(targetPosition.x()) > 2.0f || qAbs(targetPosition.y()) > 2.0f
             || qAbs(targetPosition.z()) > 2.0f)
            || (previousZoom > zoomLevel && zoomLevel <= driftTowardCenterLevel)) {
            targetPosition = QVector3D();
            // Add some extra correction so that we actually reach the center
            // eventually
            diffAdj = wheelZoomDrift;
            if (previousZoom > zoomLevel)
                diffAdj *= 2.0f; // Correct towards center little more when zooming out
        }

        float zoomFraction = 1.0f - (previousZoom / zoomLevel);

        // Adjust camera towards the zoom point, attempting to keep the cursor at
        // same graph point
        QVector3D oldTarget = item->cameraTargetPosition();
        QVector3D origDiff = targetPosition - oldTarget;
        QVector3D diff = origDiff * zoomFraction + (origDiff.normalized() * diffAdj);
        if (diff.length() > origDiff.length())
            diff = origDiff;
        item->setCameraTargetPosition(oldTarget + diff);
    } else {
        item->setCameraZoomLevel(zoomLevel);
    }

    item->update();
}

//  from ../qtgraphs/src/graphs3d/input/qgraphsinputhandler.cpp, line 385, as _ZN19QGraphsInputHandler19onPinchScaleChangedEd
inline void QGraphsInputHandler::onPinchScaleChanged(qreal delta)
{
    if (!m_flags.zoomEnabled) {
        qCWarning(lcEvents3D, "%s zooming needs to be enabled",
                qUtf8Printable(QLatin1String(__FUNCTION__)));
        return;
    }

    m_pinchDiff += (delta - 1.0f);
    int driftTowardCenterLevel = 175;
    float wheelZoomDrift = 0.1f;

    QQuickGraphsItem *item = m_graphsItem;
    int zoomLevel = int(item->cameraZoomLevel());
    const int minZoomLevel = int(item->minCameraZoomLevel());
    const int maxZoomLevel = int(item->maxCameraZoomLevel());
    float zoomRate = qSqrt(qSqrt(zoomLevel));
    if (m_pinchDiff > .0f)
        zoomLevel += zoomRate;
    else
        zoomLevel -= zoomRate;
    zoomLevel = qBound(minZoomLevel, zoomLevel, maxZoomLevel);
    if (m_flags.zoomAtTarget) {
        QVector3D targetPosition = item->graphPositionAt(
            m_pinchHandler->centroid().position().toPoint());
        item->setCameraZoomLevel(zoomLevel);

        float diffAdj = 0.0f;

        // If zooming in/out outside the graph, or zooming out after certain point,
        // move towards the center.
        if ((qAbs(targetPosition.x()) > 2.0f || qAbs(targetPosition.y()) > 2.0f
             || qAbs(targetPosition.z()) > 2.0f)
            || (m_pinchDiff > .0f && zoomLevel <= driftTowardCenterLevel)) {
            targetPosition = QVector3D();
            // Add some extra correction so that we actually reach the center
            // eventually
            diffAdj = wheelZoomDrift;
            if (m_pinchDiff > .0f)
                diffAdj *= 2.0f; // Correct towards center little more when zooming out
        }

        // Adjust camera towards the zoom point, attempting to keep the cursor at
        // same graph point
        QVector3D oldTarget = item->cameraTargetPosition();
        QVector3D origDiff = targetPosition - oldTarget;
        QVector3D diff = origDiff * m_pinchDiff + (origDiff.normalized() * diffAdj);
        if (diff.length() > origDiff.length())
            diff = origDiff;
        item->setCameraTargetPosition(oldTarget + diff);
    } else {
        item->setCameraZoomLevel(zoomLevel);
    }
    m_pinchDiff = .0f;
}
//  -----------------------------------------------------------------------

//  A QGraphsInputHandler that Python can take functions over in. Every QGraphsInputHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphsInputHandlerCall0)(const void *, QHoverEvent *, int *);
typedef const QRectF * (*CuteQGraphsInputHandlerCall1)(const void *, int *);
typedef const QRectF * (*CuteQGraphsInputHandlerCall2)(const void *, int *);
typedef bool (*CuteQGraphsInputHandlerCall3)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQGraphsInputHandlerCall4)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQGraphsInputHandlerCall5)(const void *, int *);
typedef void * (*CuteQGraphsInputHandlerCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphsInputHandlerCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphsInputHandlerCall8)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQGraphsInputHandlerCall9)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQGraphsInputHandlerCall10)(const void *, int *);
typedef void (*CuteQGraphsInputHandlerCall11)(const void *, int *);
typedef void (*CuteQGraphsInputHandlerCall12)(const void *, QKeyEvent *, int *);
typedef void (*CuteQGraphsInputHandlerCall13)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQGraphsInputHandlerCall14)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQGraphsInputHandlerCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQGraphsInputHandlerCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQGraphsInputHandlerCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQGraphsInputHandlerCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQGraphsInputHandlerCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQGraphsInputHandlerCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQGraphsInputHandlerCall21)(const void *, int *);
typedef void (*CuteQGraphsInputHandlerCall22)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQGraphsInputHandlerCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQGraphsInputHandlerCall24)(const void *, QTouchEvent *, int *);
typedef void (*CuteQGraphsInputHandlerCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteQGraphsInputHandlerCall26)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQGraphsInputHandlerCall27)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQGraphsInputHandlerCall28)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQGraphsInputHandlerCall29)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQGraphsInputHandlerCall30)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQGraphsInputHandlerCall31)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQGraphsInputHandlerCall32)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQGraphsInputHandlerCall33)(const void *, int *);
typedef void (*CuteQGraphsInputHandlerCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphsInputHandlerCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphsInputHandlerCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphsInputHandlerCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphsInputHandlerCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphsInputHandlerCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphsInputHandlerCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGraphsInputHandler : public QGraphsInputHandler {
public:
  using QGraphsInputHandler::QGraphsInputHandler;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[3] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[13] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[22] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[26] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[34] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QGraphsInputHandler::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall0 call = reinterpret_cast<CuteQGraphsInputHandlerCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphsInputHandler::hoverMoveEvent(event);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall1 call = reinterpret_cast<CuteQGraphsInputHandlerCall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall2 call = reinterpret_cast<CuteQGraphsInputHandlerCall2>(taken[2]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall3 call = reinterpret_cast<CuteQGraphsInputHandlerCall3>(taken[3]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall4 call = reinterpret_cast<CuteQGraphsInputHandlerCall4>(taken[4]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall5 call = reinterpret_cast<CuteQGraphsInputHandlerCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall6 call = reinterpret_cast<CuteQGraphsInputHandlerCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall7 call = reinterpret_cast<CuteQGraphsInputHandlerCall7>(taken[7]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::itemChange(ItemChange a0, const ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall8 call = reinterpret_cast<CuteQGraphsInputHandlerCall8>(taken[8]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall9 call = reinterpret_cast<CuteQGraphsInputHandlerCall9>(taken[9]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[10]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall10 call = reinterpret_cast<CuteQGraphsInputHandlerCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[11]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall11 call = reinterpret_cast<CuteQGraphsInputHandlerCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall12 call = reinterpret_cast<CuteQGraphsInputHandlerCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall13 call = reinterpret_cast<CuteQGraphsInputHandlerCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall14 call = reinterpret_cast<CuteQGraphsInputHandlerCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall15 call = reinterpret_cast<CuteQGraphsInputHandlerCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall16 call = reinterpret_cast<CuteQGraphsInputHandlerCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall17 call = reinterpret_cast<CuteQGraphsInputHandlerCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall18 call = reinterpret_cast<CuteQGraphsInputHandlerCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall19 call = reinterpret_cast<CuteQGraphsInputHandlerCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall20 call = reinterpret_cast<CuteQGraphsInputHandlerCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall21 call = reinterpret_cast<CuteQGraphsInputHandlerCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall22 call = reinterpret_cast<CuteQGraphsInputHandlerCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall23 call = reinterpret_cast<CuteQGraphsInputHandlerCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall24 call = reinterpret_cast<CuteQGraphsInputHandlerCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall25 call = reinterpret_cast<CuteQGraphsInputHandlerCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall26 call = reinterpret_cast<CuteQGraphsInputHandlerCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall27 call = reinterpret_cast<CuteQGraphsInputHandlerCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall28 call = reinterpret_cast<CuteQGraphsInputHandlerCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall29 call = reinterpret_cast<CuteQGraphsInputHandlerCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall30 call = reinterpret_cast<CuteQGraphsInputHandlerCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[31]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall31 call = reinterpret_cast<CuteQGraphsInputHandlerCall31>(taken[31]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  QSGNode *QQuickItem::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
  //      *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[32]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall32 call = reinterpret_cast<CuteQGraphsInputHandlerCall32>(taken[32]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall33 call = reinterpret_cast<CuteQGraphsInputHandlerCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall34 call = reinterpret_cast<CuteQGraphsInputHandlerCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall35 call = reinterpret_cast<CuteQGraphsInputHandlerCall35>(taken[35]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall36 call = reinterpret_cast<CuteQGraphsInputHandlerCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall37 call = reinterpret_cast<CuteQGraphsInputHandlerCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall38 call = reinterpret_cast<CuteQGraphsInputHandlerCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[39]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall39 call = reinterpret_cast<CuteQGraphsInputHandlerCall39>(taken[39]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[40]) {
      int handled = 0;
      CuteQGraphsInputHandlerCall40 call = reinterpret_cast<CuteQGraphsInputHandlerCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGraphsInputHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QGraphsInputHandler10metaObjectEv(
    const QGraphsInputHandler *self) {
  return self->metaObject();
}

//  void *QGraphsInputHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QGraphsInputHandler11qt_metacastEPKc(
    QGraphsInputHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGraphsInputHandler::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QGraphsInputHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QGraphsInputHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QGraphsInputHandler::~QGraphsInputHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandlerD1Ev(QGraphsInputHandler *self) {
  delete self;
}

//  QPoint QGraphsInputHandler::pendingPoint()
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN19QGraphsInputHandler12pendingPointEv(
    QGraphsInputHandler *self) {
  return new QPoint(self->pendingPoint());
}

//  void QGraphsInputHandler::setZoomEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler14setZoomEnabledEb(
    QGraphsInputHandler *self,
    bool enable) {
  self->setZoomEnabled(enable);
}

//  bool QGraphsInputHandler::isZoomEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QGraphsInputHandler13isZoomEnabledEv(
    QGraphsInputHandler *self) {
  return self->isZoomEnabled();
}

//  void QGraphsInputHandler::setZoomAtTargetEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler22setZoomAtTargetEnabledEb(
    QGraphsInputHandler *self,
    bool enable) {
  self->setZoomAtTargetEnabled(enable);
}

//  bool QGraphsInputHandler::isZoomAtTargetEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QGraphsInputHandler21isZoomAtTargetEnabledEv(
    QGraphsInputHandler *self) {
  return self->isZoomAtTargetEnabled();
}

//  void QGraphsInputHandler::setRotationEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler18setRotationEnabledEb(
    QGraphsInputHandler *self,
    bool enable) {
  self->setRotationEnabled(enable);
}

//  bool QGraphsInputHandler::isRotationEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QGraphsInputHandler17isRotationEnabledEv(
    QGraphsInputHandler *self) {
  return self->isRotationEnabled();
}

//  void QGraphsInputHandler::setPanEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler13setPanEnabledEb(
    QGraphsInputHandler *self,
    bool enable) {
  self->setPanEnabled(enable);
}

//  bool QGraphsInputHandler::isPanEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QGraphsInputHandler12isPanEnabledEv(
    QGraphsInputHandler *self) {
  return self->isPanEnabled();
}

//  void QGraphsInputHandler::setDragMode(QtGraphs3D::DragMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler11setDragModeEN10QtGraphs3D8DragModeE(
    QGraphsInputHandler *self,
    QtGraphs3D::DragMode mode) {
  self->setDragMode(mode);
}

//  QtGraphs3D::DragMode QGraphsInputHandler::dragMode()
extern "C" Q_DECL_EXPORT
QtGraphs3D::DragMode ritual_ZN19QGraphsInputHandler8dragModeEv(
    QGraphsInputHandler *self) {
  return self->dragMode();
}

//  void QGraphsInputHandler::setSelectionEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler19setSelectionEnabledEb(
    QGraphsInputHandler *self,
    bool enable) {
  self->setSelectionEnabled(enable);
}

//  bool QGraphsInputHandler::isSelectionEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QGraphsInputHandler18isSelectionEnabledEv(
    QGraphsInputHandler *self) {
  return self->isSelectionEnabled();
}

//  void QGraphsInputHandler::setDefaultInputHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler22setDefaultInputHandlerEv(
    QGraphsInputHandler *self) {
  self->setDefaultInputHandler();
}

//  void QGraphsInputHandler::unsetDefaultInputHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler24unsetDefaultInputHandlerEv(
    QGraphsInputHandler *self) {
  self->unsetDefaultInputHandler();
}

//  void QGraphsInputHandler::unsetDefaultTapHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler22unsetDefaultTapHandlerEv(
    QGraphsInputHandler *self) {
  self->unsetDefaultTapHandler();
}

//  void QGraphsInputHandler::unsetDefaultDragHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler23unsetDefaultDragHandlerEv(
    QGraphsInputHandler *self) {
  self->unsetDefaultDragHandler();
}

//  void QGraphsInputHandler::unsetDefaultWheelHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler24unsetDefaultWheelHandlerEv(
    QGraphsInputHandler *self) {
  self->unsetDefaultWheelHandler();
}

//  void QGraphsInputHandler::unsetDefaultPinchHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler24unsetDefaultPinchHandlerEv(
    QGraphsInputHandler *self) {
  self->unsetDefaultPinchHandler();
}

//  void QGraphsInputHandler::setDragButton(Qt::MouseButtons button)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler13setDragButtonE6QFlagsIN2Qt11MouseButtonEE(
    QGraphsInputHandler *self,
    int button) {
  self->setDragButton(QFlags<Qt::MouseButton>::fromInt(button));
}

//  void QGraphsInputHandler::setPanButton(Qt::MouseButtons button)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler12setPanButtonE6QFlagsIN2Qt11MouseButtonEE(
    QGraphsInputHandler *self,
    int button) {
  self->setPanButton(QFlags<Qt::MouseButton>::fromInt(button));
}

//  void QGraphsInputHandler::onTapped()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler8onTappedEv(QGraphsInputHandler *self) {
  self->onTapped();
}

//  void QGraphsInputHandler::onTranslationChanged(QVector2D delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler20onTranslationChangedE9QVector2D(
    QGraphsInputHandler *self,
    const QVector2D *delta) {
  self->onTranslationChanged(*delta);
}

//  void QGraphsInputHandler::onGrabChanged(QPointingDevice::GrabTransition
//      transition, QEventPoint point)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler13onGrabChangedEN15QPointingDevice14GrabTransitionE11QEventPoint(
    QGraphsInputHandler *self,
    QPointingDevice::GrabTransition transition,
    const QEventPoint *point) {
  self->onGrabChanged(transition, *point);
}

//  void QGraphsInputHandler::onWheel(QQuickWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler7onWheelEP16QQuickWheelEvent(
    QGraphsInputHandler *self,
    QQuickWheelEvent *event) {
  self->onWheel(event);
}

//  void QGraphsInputHandler::onPinchScaleChanged(qreal delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler19onPinchScaleChangedEd(
    QGraphsInputHandler *self,
    qreal delta) {
  self->onPinchScaleChanged(delta);
}

//  void QGraphsInputHandler::mouseMove(QPoint mousePos)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler9mouseMoveE6QPoint(
    QGraphsInputHandler *self,
    const QPoint *mousePos) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QGraphsInputHandler")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "mouseMove(QPoint)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "mouseMove(QPoint)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(mousePos)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QGraphsInputHandler::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsInputHandler14hoverMoveEventEP11QHoverEvent(
    QGraphsInputHandler *self,
    QHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  a Python function taken by a CuteQGraphsInputHandler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphsInputHandler(
    QGraphsInputHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphsInputHandler *>(self)->take(key, call);
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
