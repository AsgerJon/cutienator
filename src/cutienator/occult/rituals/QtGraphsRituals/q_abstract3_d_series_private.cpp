//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qabstract3dseries_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if !(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qabstract3dseries.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qabstract3dseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qquaternion.h>
#include <QtGui/qcolor.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/private/qabstract3dseries_p.h>
#include <QtGraphs/private/qabstractdataproxy_p.h>
#include <QtGraphs/private/qquickgraphsitem_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 902, as _ZN24QAbstract3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy
inline void QAbstract3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
{
    Q_Q(QAbstract3DSeries);
    Q_ASSERT(proxy && proxy != m_dataProxy && !proxy->d_func()->series());

    delete m_dataProxy;
    m_dataProxy = proxy;

    proxy->d_func()->setSeries(q); // also sets parent

    if (m_graph) {
        connectGraphAndProxy(m_graph);
        m_graph->markDataDirty();
    }
}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 918, as _ZN24QAbstract3DSeriesPrivate8setGraphEP16QQuickGraphsItem
inline void QAbstract3DSeriesPrivate::setGraph(QQuickGraphsItem *graph)
{
    Q_Q(QAbstract3DSeries);
    m_graph = graph;
    q->setParent(graph);
    connectGraphAndProxy(graph);
    markItemLabelDirty();
}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 897, as _ZNK24QAbstract3DSeriesPrivate9dataProxyEv
inline QAbstractDataProxy *QAbstract3DSeriesPrivate::dataProxy() const
{
    return m_dataProxy;
}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 927, as _ZN24QAbstract3DSeriesPrivate18setItemLabelFormatERK7QString
inline void QAbstract3DSeriesPrivate::setItemLabelFormat(const QString &format)
{
    m_itemLabelFormat = format;
    markItemLabelDirty();
}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 933, as _ZN24QAbstract3DSeriesPrivate10setVisibleEb
inline void QAbstract3DSeriesPrivate::setVisible(bool visible)
{
    m_visible = visible;
    markItemLabelDirty();
}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 939, as _ZN24QAbstract3DSeriesPrivate7setMeshEN17QAbstract3DSeries4MeshE
inline void QAbstract3DSeriesPrivate::setMesh(QAbstract3DSeries::Mesh mesh)
{
    m_mesh = mesh;
    m_changeTracker.meshChanged = true;
    if (m_graph) {
        m_graph->markSeriesVisualsDirty();

        if (m_graph->optimizationHint() == QtGraphs3D::OptimizationHint::Default)
            m_graph->markDataDirty();
    }
}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 951, as _ZN24QAbstract3DSeriesPrivate13setMeshSmoothEb
inline void QAbstract3DSeriesPrivate::setMeshSmooth(bool enable)
{
    m_meshSmooth = enable;
    m_changeTracker.meshSmoothChanged = true;
    if (m_graph) {
        m_graph->markSeriesVisualsDirty();

        if (m_graph->optimizationHint() == QtGraphs3D::OptimizationHint::Default)
            m_graph->markDataDirty();
    }
}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 963, as _ZN24QAbstract3DSeriesPrivate15setMeshRotationERK11QQuaternion
inline void QAbstract3DSeriesPrivate::setMeshRotation(const QQuaternion &rotation)
{
    m_meshRotation = rotation;
    m_changeTracker.meshRotationChanged = true;
    if (m_graph) {
        m_graph->markSeriesVisualsDirty();

        if (m_graph->optimizationHint() == QtGraphs3D::OptimizationHint::Default)
            m_graph->markDataDirty();
    }
}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 975, as _ZN24QAbstract3DSeriesPrivate18setUserDefinedMeshERK7QString
inline void QAbstract3DSeriesPrivate::setUserDefinedMesh(const QString &meshFile)
{
    m_userDefinedMesh = meshFile;
    m_changeTracker.userDefinedMeshChanged = true;
    if (m_graph) {
        m_graph->markSeriesVisualsDirty();

        if (m_graph->optimizationHint() == QtGraphs3D::OptimizationHint::Default)
            m_graph->markDataDirty();
    }
}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 987, as _ZN24QAbstract3DSeriesPrivate13setColorStyleEN12QGraphsTheme10ColorStyleE
inline void QAbstract3DSeriesPrivate::setColorStyle(QGraphsTheme::ColorStyle style)
{
    m_colorStyle = style;
    m_changeTracker.colorStyleChanged = true;
    if (m_graph)
        m_graph->markSeriesVisualsDirty();
}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 995, as _ZN24QAbstract3DSeriesPrivate12setBaseColorE6QColor
inline void QAbstract3DSeriesPrivate::setBaseColor(QColor color)
{
    m_baseColor = color;
    m_changeTracker.baseColorChanged = true;
    if (m_graph)
        m_graph->markSeriesVisualsDirty();
}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 1012, as _ZN24QAbstract3DSeriesPrivate23setSingleHighlightColorE6QColor
inline void QAbstract3DSeriesPrivate::setSingleHighlightColor(QColor color)
{
    m_singleHighlightColor = color;
    m_changeTracker.singleHighlightColorChanged = true;
    if (m_graph)
        m_graph->markSeriesVisualsDirty();
}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 1029, as _ZN24QAbstract3DSeriesPrivate22setMultiHighlightColorE6QColor
inline void QAbstract3DSeriesPrivate::setMultiHighlightColor(QColor color)
{
    m_multiHighlightColor = color;
    m_changeTracker.multiHighlightColorChanged = true;
    if (m_graph)
        m_graph->markSeriesVisualsDirty();
}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 1054, as _ZN24QAbstract3DSeriesPrivate7setNameERK7QString
inline void QAbstract3DSeriesPrivate::setName(const QString &name)
{
    m_name = name;
    markItemLabelDirty();
    m_changeTracker.nameChanged = true;
}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 1099, as _ZN24QAbstract3DSeriesPrivate9itemLabelEv
inline QString QAbstract3DSeriesPrivate::itemLabel()
{
    Q_Q(QAbstract3DSeries);
    if (m_itemLabelDirty) {
        QString oldLabel = m_itemLabel;
        if (m_graph && m_visible)
            createItemLabel();
        else
            m_itemLabel = QString();
        m_itemLabelDirty = false;

        if (oldLabel != m_itemLabel)
            emit q->itemLabelChanged(m_itemLabel);
    }

    return m_itemLabel;
}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 1117, as _ZN24QAbstract3DSeriesPrivate18markItemLabelDirtyEv
inline void QAbstract3DSeriesPrivate::markItemLabelDirty()
{
    m_itemLabelDirty = true;
    m_changeTracker.itemLabelChanged = true;
}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 1123, as _ZN24QAbstract3DSeriesPrivate19setItemLabelVisibleEb
inline void QAbstract3DSeriesPrivate::setItemLabelVisible(bool visible)
{
    m_itemLabelVisible = visible;
    markItemLabelDirty();
    m_changeTracker.itemLabelVisibilityChanged = true;
}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 1130, as _ZN24QAbstract3DSeriesPrivate15isUsingGradientEv
inline bool QAbstract3DSeriesPrivate::isUsingGradient()
{
    return m_colorStyle != QGraphsTheme::ColorStyle::Uniform ? true : false;
}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 1046, as _ZN24QAbstract3DSeriesPrivate15setLightingModeEN17QAbstract3DSeries12LightingModeE
inline void QAbstract3DSeriesPrivate::setLightingMode(QAbstract3DSeries::LightingMode lightingMode)
{
    m_lightingMode = lightingMode;
    if (m_graph)
        m_graph->markSeriesVisualsDirty();
    m_changeTracker.lightingModeChanged = true;
}
//  -----------------------------------------------------------------------

//  A QAbstract3DSeriesPrivate that Python can take functions over in. Every QAbstract3DSeriesPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstract3DSeriesPrivateCall0)(const void *, QAbstractDataProxy *, int *);
typedef void (*CuteQAbstract3DSeriesPrivateCall1)(const void *, QQuickGraphsItem *, int *);
typedef void (*CuteQAbstract3DSeriesPrivateCall2)(const void *, QQuickGraphsItem *, int *);
typedef void (*CuteQAbstract3DSeriesPrivateCall3)(const void *, int *);
class CuteQAbstract3DSeriesPrivate : public QAbstract3DSeriesPrivate {
public:
  using QAbstract3DSeriesPrivate::QAbstract3DSeriesPrivate;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QAbstract3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstract3DSeriesPrivate8setGraphEP16QQuickGraphsItem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstract3DSeriesPrivate20connectGraphAndProxyEP16QQuickGraphsItem")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstract3DSeriesPrivate15createItemLabelEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QAbstract3DSeriesPrivate::setDataProxy(QAbstractDataProxy
  //      *proxy)
  void setDataProxy(QAbstractDataProxy *proxy) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstract3DSeriesPrivateCall0 call = reinterpret_cast<CuteQAbstract3DSeriesPrivateCall0>(taken[0]);
      call(this, proxy, &handled);
      if (handled) return;
    }
    QAbstract3DSeriesPrivate::setDataProxy(proxy);
  }

  //  void QAbstract3DSeriesPrivate::setGraph(QQuickGraphsItem *graph)
  void setGraph(QQuickGraphsItem *graph) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstract3DSeriesPrivateCall1 call = reinterpret_cast<CuteQAbstract3DSeriesPrivateCall1>(taken[1]);
      call(this, graph, &handled);
      if (handled) return;
    }
    QAbstract3DSeriesPrivate::setGraph(graph);
  }

  //  void QAbstract3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem
  //      *newGraph)
  void connectGraphAndProxy(QQuickGraphsItem *newGraph) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstract3DSeriesPrivateCall2 call = reinterpret_cast<CuteQAbstract3DSeriesPrivateCall2>(taken[2]);
      call(this, newGraph, &handled);
      if (handled) return;
    }
  }

  //  void QAbstract3DSeriesPrivate::createItemLabel()
  void createItemLabel() override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstract3DSeriesPrivateCall3 call = reinterpret_cast<CuteQAbstract3DSeriesPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QAbstract3DSeries *QAbstract3DSeriesPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstract3DSeries *ritual_ZN24QAbstract3DSeriesPrivate6q_funcEv(
    QAbstract3DSeriesPrivate *self) {
  return self->q_func();
}

//  const QAbstract3DSeries *QAbstract3DSeriesPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstract3DSeries *ritual_ZNK24QAbstract3DSeriesPrivate6q_funcEv(
    const QAbstract3DSeriesPrivate *self) {
  return self->q_func();
}

//  QAbstractDataProxy *QAbstract3DSeriesPrivate::dataProxy() const
extern "C" Q_DECL_EXPORT
QAbstractDataProxy *ritual_ZNK24QAbstract3DSeriesPrivate9dataProxyEv(
    const QAbstract3DSeriesPrivate *self) {
  return self->dataProxy();
}

//  void QAbstract3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy(
    QAbstract3DSeriesPrivate *self,
    QAbstractDataProxy *proxy) {
  self->setDataProxy(proxy);
}

//  void QAbstract3DSeriesPrivate::setGraph(QQuickGraphsItem *graph)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate8setGraphEP16QQuickGraphsItem(
    QAbstract3DSeriesPrivate *self,
    QQuickGraphsItem *graph) {
  self->setGraph(graph);
}

//  void QAbstract3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem
//      *newGraph)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate20connectGraphAndProxyEP16QQuickGraphsItem(
    QAbstract3DSeriesPrivate *self,
    QQuickGraphsItem *newGraph) {
  self->connectGraphAndProxy(newGraph);
}

//  void QAbstract3DSeriesPrivate::createItemLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate15createItemLabelEv(
    QAbstract3DSeriesPrivate *self) {
  self->createItemLabel();
}

//  void QAbstract3DSeriesPrivate::setItemLabelFormat(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate18setItemLabelFormatERK7QString(
    QAbstract3DSeriesPrivate *self,
    const QString *format) {
  self->setItemLabelFormat(*format);
}

//  void QAbstract3DSeriesPrivate::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate10setVisibleEb(
    QAbstract3DSeriesPrivate *self,
    bool visible) {
  self->setVisible(visible);
}

//  void QAbstract3DSeriesPrivate::setMesh(QAbstract3DSeries::Mesh mesh)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate7setMeshEN17QAbstract3DSeries4MeshE(
    QAbstract3DSeriesPrivate *self,
    QAbstract3DSeries::Mesh mesh) {
  self->setMesh(mesh);
}

//  void QAbstract3DSeriesPrivate::setMeshSmooth(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate13setMeshSmoothEb(
    QAbstract3DSeriesPrivate *self,
    bool enable) {
  self->setMeshSmooth(enable);
}

//  void QAbstract3DSeriesPrivate::setMeshRotation(const QQuaternion
//      &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate15setMeshRotationERK11QQuaternion(
    QAbstract3DSeriesPrivate *self,
    const QQuaternion *rotation) {
  self->setMeshRotation(*rotation);
}

//  void QAbstract3DSeriesPrivate::setUserDefinedMesh(const QString
//      &meshFile)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate18setUserDefinedMeshERK7QString(
    QAbstract3DSeriesPrivate *self,
    const QString *meshFile) {
  self->setUserDefinedMesh(*meshFile);
}

//  void QAbstract3DSeriesPrivate::setColorStyle(QGraphsTheme::ColorStyle
//      style)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate13setColorStyleEN12QGraphsTheme10ColorStyleE(
    QAbstract3DSeriesPrivate *self,
    QGraphsTheme::ColorStyle style) {
  self->setColorStyle(style);
}

//  void QAbstract3DSeriesPrivate::setBaseColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate12setBaseColorE6QColor(
    QAbstract3DSeriesPrivate *self,
    const QColor *color) {
  self->setBaseColor(*color);
}

//  void QAbstract3DSeriesPrivate::setSingleHighlightColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate23setSingleHighlightColorE6QColor(
    QAbstract3DSeriesPrivate *self,
    const QColor *color) {
  self->setSingleHighlightColor(*color);
}

//  void QAbstract3DSeriesPrivate::setMultiHighlightColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate22setMultiHighlightColorE6QColor(
    QAbstract3DSeriesPrivate *self,
    const QColor *color) {
  self->setMultiHighlightColor(*color);
}

//  void QAbstract3DSeriesPrivate::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate7setNameERK7QString(
    QAbstract3DSeriesPrivate *self,
    const QString *name) {
  self->setName(*name);
}

//  QString QAbstract3DSeriesPrivate::itemLabel()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QAbstract3DSeriesPrivate9itemLabelEv(
    QAbstract3DSeriesPrivate *self) {
  return new QString(self->itemLabel());
}

//  void QAbstract3DSeriesPrivate::markItemLabelDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate18markItemLabelDirtyEv(
    QAbstract3DSeriesPrivate *self) {
  self->markItemLabelDirty();
}

//  bool QAbstract3DSeriesPrivate::itemLabelDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAbstract3DSeriesPrivate14itemLabelDirtyEv(
    const QAbstract3DSeriesPrivate *self) {
  return self->itemLabelDirty();
}

//  void QAbstract3DSeriesPrivate::setItemLabelVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate19setItemLabelVisibleEb(
    QAbstract3DSeriesPrivate *self,
    bool visible) {
  self->setItemLabelVisible(visible);
}

//  bool QAbstract3DSeriesPrivate::isUsingGradient()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QAbstract3DSeriesPrivate15isUsingGradientEv(
    QAbstract3DSeriesPrivate *self) {
  return self->isUsingGradient();
}

//  void
//      QAbstract3DSeriesPrivate::setLightingMode(QAbstract3DSeries::Lighting
//      Mode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstract3DSeriesPrivate15setLightingModeEN17QAbstract3DSeries12LightingModeE(
    QAbstract3DSeriesPrivate *self,
    QAbstract3DSeries::LightingMode mode) {
  self->setLightingMode(mode);
}

//  a Python function taken by a CuteQAbstract3DSeriesPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstract3DSeriesPrivate(
    QAbstract3DSeriesPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstract3DSeriesPrivate *>(self)->take(key, call);
}

//  void QAbstract3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAbstract3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy(
    QAbstract3DSeriesPrivate *self,
    QAbstractDataProxy *proxy) {
  self->QAbstract3DSeriesPrivate::setDataProxy(proxy);
}

//  void QAbstract3DSeriesPrivate::setGraph(QQuickGraphsItem *graph)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAbstract3DSeriesPrivate8setGraphEP16QQuickGraphsItem(
    QAbstract3DSeriesPrivate *self,
    QQuickGraphsItem *graph) {
  self->QAbstract3DSeriesPrivate::setGraph(graph);
}

#endif  // !(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))
