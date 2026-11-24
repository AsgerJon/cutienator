//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphsWidgets/6.12.0/QtGraphsWidgets/private/q3dgraphswidgetitem_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtGraphsWidgets/q3dgraphswidgetitem.h>
#include <QtGraphsWidgets/QtGraphsWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphsWidgets/6.12.0/QtGraphsWidgets/private/q3dgraphswidgetitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphsWidgets/q3dgraphswidgetitem.h>
#include <QtGraphsWidgets/private/q3dgraphswidgetitem_p.h>
#include <QtGraphs/private/q3dscene_p.h>
#include <QtGraphs/private/qquickgraphsitem_p.h>
#ifdef Q_OS_DARWIN
#include <QtQuick3D/qquick3d.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs3d/widget/q3dgraphswidgetitem.cpp, line 1481, as _ZN26Q3DGraphsWidgetItemPrivate11createGraphEv
#if defined(Q_OS_LINUX)
inline void Q3DGraphsWidgetItemPrivate::createGraph()
{
    Q_Q(Q3DGraphsWidgetItem);
    if (m_widget == nullptr)
        return;
    m_widget->setResizeMode(QQuickWidget::SizeRootObjectToView);

#ifdef Q_OS_DARWIN
    // Take care of widget users (or CI) wanting to use OpenGL backend on macOS
    if (QQuickWindow::graphicsApi() == QSGRendererInterface::OpenGL)
        QSurfaceFormat::setDefaultFormat(QQuick3D::idealSurfaceFormat(4));
#endif

    const QString qmlData = QLatin1StringView(R"QML(
        import QtQuick;
        import QtGraphs;

        %1
        {
            anchors.fill: parent;
        }
    )QML")
                                .arg(m_graphType);
    QQmlComponent *component = new QQmlComponent(m_widget->engine(), q);
    component->setData(qmlData.toUtf8(), QUrl());
    m_graphsItem.reset(qobject_cast<QQuickGraphsItem *>(component->create()));
    if (!m_graphsItem) {
        qWarning("Failed to create %ls: %ls",
                 qUtf16Printable(m_graphType),
                 qUtf16Printable(component->errorString().trimmed()));
        return;
    }
    m_widget->setContent(component->url(), component, m_graphsItem.get());

    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::selectedElementChanged,
                     q,
                     &Q3DGraphsWidgetItem::selectedElementChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::msaaSamplesChanged,
                     q,
                     &Q3DGraphsWidgetItem::msaaSamplesChanged);

    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::tapped,
                     q,
                     &Q3DGraphsWidgetItem::tapped);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::doubleTapped,
                     q,
                     &Q3DGraphsWidgetItem::doubleTapped);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::longPressed,
                     q,
                     &Q3DGraphsWidgetItem::longPressed);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::dragged,
                     q,
                     &Q3DGraphsWidgetItem::dragged);
    QObjectPrivate::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::wheel,
                     this,
                     &Q3DGraphsWidgetItemPrivate::onWheel);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::pinch,
                     q,
                     &Q3DGraphsWidgetItem::pinch);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::mouseMove,
                     q,
                     &Q3DGraphsWidgetItem::mouseMove);

    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::zoomEnabledChanged,
                     q,
                     &Q3DGraphsWidgetItem::zoomEnabledChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::zoomAtTargetEnabledChanged,
                     q,
                     &Q3DGraphsWidgetItem::zoomAtTargetEnabledChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::rotationEnabledChanged,
                     q,
                     &Q3DGraphsWidgetItem::rotationEnabledChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::selectionEnabledChanged,
                     q,
                     &Q3DGraphsWidgetItem::selectionEnabledChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::queriedGraphPositionChanged,
                     q,
                     &Q3DGraphsWidgetItem::queriedGraphPositionChanged);

    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::ambientLightStrengthChanged,
                     q,
                     &Q3DGraphsWidgetItem::ambientLightStrengthChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::lightStrengthChanged,
                     q,
                     &Q3DGraphsWidgetItem::lightStrengthChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::shadowStrengthChanged,
                     q,
                     &Q3DGraphsWidgetItem::shadowStrengthChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::lightColorChanged,
                     q,
                     &Q3DGraphsWidgetItem::lightColorChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::gridLineTypeChanged,
                     q,
                     &Q3DGraphsWidgetItem::gridLineTypeChanged);

    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::activeThemeChanged,
                     q,
                     &Q3DGraphsWidgetItem::activeThemeChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::transparencyTechniqueChanged,
                     q,
                     &Q3DGraphsWidgetItem::transparencyTechniqueChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::selectionModeChanged,
                     q,
                     &Q3DGraphsWidgetItem::selectionModeChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::shadowQualityChanged,
                     q,
                     &Q3DGraphsWidgetItem::shadowQualityChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::cameraPresetChanged,
                     q,
                     &Q3DGraphsWidgetItem::cameraPresetChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::cameraXRotationChanged,
                     q,
                     &Q3DGraphsWidgetItem::cameraXRotationChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::cameraYRotationChanged,
                     q,
                     &Q3DGraphsWidgetItem::cameraYRotationChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::minCameraXRotationChanged,
                     q,
                     &Q3DGraphsWidgetItem::minCameraXRotationChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::maxCameraXRotationChanged,
                     q,
                     &Q3DGraphsWidgetItem::maxCameraXRotationChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::minCameraYRotationChanged,
                     q,
                     &Q3DGraphsWidgetItem::minCameraYRotationChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::maxCameraYRotationChanged,
                     q,
                     &Q3DGraphsWidgetItem::maxCameraYRotationChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::cameraZoomLevelChanged,
                     q,
                     &Q3DGraphsWidgetItem::cameraZoomLevelChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::minCameraZoomLevelChanged,
                     q,
                     &Q3DGraphsWidgetItem::minCameraZoomLevelChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::maxCameraZoomLevelChanged,
                     q,
                     &Q3DGraphsWidgetItem::maxCameraZoomLevelChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::wrapCameraXRotationChanged,
                     q,
                     &Q3DGraphsWidgetItem::wrapCameraXRotationChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::wrapCameraYRotationChanged,
                     q,
                     &Q3DGraphsWidgetItem::wrapCameraYRotationChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::measureFpsChanged,
                     q,
                     &Q3DGraphsWidgetItem::measureFpsChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::orthoProjectionChanged,
                     q,
                     &Q3DGraphsWidgetItem::orthoProjectionChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::aspectRatioChanged,
                     q,
                     &Q3DGraphsWidgetItem::aspectRatioChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::optimizationHintChanged,
                     q,
                     &Q3DGraphsWidgetItem::optimizationHintChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::polarChanged,
                     q,
                     &Q3DGraphsWidgetItem::polarChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::labelMarginChanged,
                     q,
                     &Q3DGraphsWidgetItem::labelMarginChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::radialLabelOffsetChanged,
                     q,
                     &Q3DGraphsWidgetItem::radialLabelOffsetChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::horizontalAspectRatioChanged,
                     q,
                     &Q3DGraphsWidgetItem::horizontalAspectRatioChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::localeChanged,
                     q,
                     &Q3DGraphsWidgetItem::localeChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::marginChanged,
                     q,
                     &Q3DGraphsWidgetItem::marginChanged);
    QObject::connect(m_graphsItem.get(),
                     &QQuickGraphsItem::cutoffMarginChanged,
                     q,
                     &Q3DGraphsWidgetItem::cutoffMarginChanged);

    m_widget->installEventFilter(q);
}
#endif  // defined(Q_OS_LINUX)

//  from ../qtgraphs/src/graphs3d/widget/q3dgraphswidgetitem.cpp, line 1464, as _ZN26Q3DGraphsWidgetItemPrivate7onWheelEP16QQuickWheelEvent
inline void Q3DGraphsWidgetItemPrivate::onWheel(QQuickWheelEvent *event)
{
    Q_Q(Q3DGraphsWidgetItem);

    QWheelEvent *ev = new QWheelEvent(QPointF(event->x(), event->y()),
                                      QPointF(event->x(), event->y()),
                                      event->pixelDelta(),
                                      event->angleDelta(),
                                      static_cast<Qt::MouseButton>(event->buttons()),
                                      static_cast<Qt::KeyboardModifier>(event->modifiers()),
                                      event->phase(),
                                      event->inverted(),
                                      Qt::MouseEventSynthesizedBySystem,
                                      event->pointingDevice());
    emit q->wheel(ev);
}
//  -----------------------------------------------------------------------

//  Q3DGraphsWidgetItemPrivate::Q3DGraphsWidgetItemPrivate()
extern "C" Q_DECL_EXPORT
Q3DGraphsWidgetItemPrivate *ritual_ZN26Q3DGraphsWidgetItemPrivateC1Ev() {
  return new Q3DGraphsWidgetItemPrivate();
}

#if defined(Q_OS_LINUX)
//  void Q3DGraphsWidgetItemPrivate::createGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN26Q3DGraphsWidgetItemPrivate11createGraphEv(
    Q3DGraphsWidgetItemPrivate *self) {
  self->createGraph();
}
#endif  // defined(Q_OS_LINUX)

//  void Q3DGraphsWidgetItemPrivate::onWheel(QQuickWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN26Q3DGraphsWidgetItemPrivate7onWheelEP16QQuickWheelEvent(
    Q3DGraphsWidgetItemPrivate *self,
    QQuickWheelEvent *event) {
  self->onWheel(event);
}

//  Q3DGraphsWidgetItem *Q3DGraphsWidgetItemPrivate::q_func()
extern "C" Q_DECL_EXPORT
Q3DGraphsWidgetItem *ritual_ZN26Q3DGraphsWidgetItemPrivate6q_funcEv(
    Q3DGraphsWidgetItemPrivate *self) {
  return self->q_func();
}

//  const Q3DGraphsWidgetItem *Q3DGraphsWidgetItemPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Q3DGraphsWidgetItem *ritual_ZNK26Q3DGraphsWidgetItemPrivate6q_funcEv(
    const Q3DGraphsWidgetItemPrivate *self) {
  return self->q_func();
}
