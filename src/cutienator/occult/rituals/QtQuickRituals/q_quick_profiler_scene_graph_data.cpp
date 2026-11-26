//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickprofiler_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: added by hand, instances of templates of the class:
//  5. Kept as it is when the generator runs again.
#include <QtQml/qtqmlglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickprofiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuickProfilerSceneGraphData::~QQuickProfilerSceneGraphData()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickProfilerSceneGraphDataD1Ev(
    QQuickProfilerSceneGraphData *self) {
  delete self;
}

//  qint64
//      *QQuickProfilerSceneGraphData::timings<QQuickProfiler::SceneGraphRendererFrame>()
extern "C" Q_DECL_EXPORT
long long *ritual_ZN28QQuickProfilerSceneGraphData7timingsILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE0EEEPxv(
    QQuickProfilerSceneGraphData *self) {
  return self->timings<QQuickProfiler::SceneGraphRendererFrame>();
}

//  qint64
//      *QQuickProfilerSceneGraphData::timings<QQuickProfiler::SceneGraphAdaptationLayerFrame>()
extern "C" Q_DECL_EXPORT
long long *ritual_ZN28QQuickProfilerSceneGraphData7timingsILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE1EEEPxv(
    QQuickProfilerSceneGraphData *self) {
  return self->timings<QQuickProfiler::SceneGraphAdaptationLayerFrame>();
}

//  qint64
//      *QQuickProfilerSceneGraphData::timings<QQuickProfiler::SceneGraphRenderLoopFrame>()
extern "C" Q_DECL_EXPORT
long long *ritual_ZN28QQuickProfilerSceneGraphData7timingsILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE3EEEPxv(
    QQuickProfilerSceneGraphData *self) {
  return self->timings<QQuickProfiler::SceneGraphRenderLoopFrame>();
}

//  qint64
//      *QQuickProfilerSceneGraphData::timings<QQuickProfiler::SceneGraphPolishAndSync>()
extern "C" Q_DECL_EXPORT
long long *ritual_ZN28QQuickProfilerSceneGraphData7timingsILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE6EEEPxv(
    QQuickProfilerSceneGraphData *self) {
  return self->timings<QQuickProfiler::SceneGraphPolishAndSync>();
}

//  qint64
//      *QQuickProfilerSceneGraphData::timings<QQuickProfiler::SceneGraphPolishFrame>()
extern "C" Q_DECL_EXPORT
long long *ritual_ZN28QQuickProfilerSceneGraphData7timingsILN23QQmlProfilerDefinitions19SceneGraphFrameTypeE9EEEPxv(
    QQuickProfilerSceneGraphData *self) {
  return self->timings<QQuickProfiler::SceneGraphPolishFrame>();
}

#endif  // !(!QT_CONFIG(qml_debug))
