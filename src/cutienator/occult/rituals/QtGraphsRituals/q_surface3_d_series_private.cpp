//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qsurface3dseries_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qsurface3dseries.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qsurface3dseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtGui/qcolor.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/private/qabstract3dseries_p.h>
#include <QtGraphs/private/qabstractdataproxy_p.h>
#include <QtGraphs/private/qquickgraphsitem_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#include <QtGraphs/qcategory3daxis.h>
#include <QtGraphs/private/qquickgraphssurface_p.h>
#include <QtGraphs/private/qsurface3dseries_p.h>
#include <QtGraphs/qvalue3daxis.h>
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

//  from ../qtgraphs/src/graphs3d/data/qsurface3dseries.cpp, line 752, as _ZN23QSurface3DSeriesPrivateD1Ev
inline QSurface3DSeriesPrivate::~QSurface3DSeriesPrivate()
{
    clearArray();
}

//  from ../qtgraphs/src/graphs3d/data/qsurface3dseries.cpp, line 757, as _ZN23QSurface3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy
inline void QSurface3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
{
    Q_ASSERT(proxy->type() == QAbstractDataProxy::DataType::Surface);
    Q_Q(QSurface3DSeries);

    QAbstract3DSeriesPrivate::setDataProxy(proxy);

    emit q->dataProxyChanged(static_cast<QSurfaceDataProxy *>(proxy));
}

//  from ../qtgraphs/src/graphs3d/data/qsurface3dseries.cpp, line 767, as _ZN23QSurface3DSeriesPrivate20connectGraphAndProxyEP16QQuickGraphsItem
inline void QSurface3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem *newGraph)
{
    Q_Q(QSurface3DSeries);
    QSurfaceDataProxy *surfaceDataProxy = static_cast<QSurfaceDataProxy *>(m_dataProxy);

    if (m_graph && surfaceDataProxy) {
        // Disconnect old graph/old proxy
        QObject::disconnect(surfaceDataProxy, 0, m_graph, 0);
        QObject::disconnect(q, 0, m_graph, 0);
    }

    if (newGraph && surfaceDataProxy) {
        QQuickGraphsSurface *graph = static_cast<QQuickGraphsSurface *>(newGraph);

        QObject::connect(surfaceDataProxy,
                         &QSurfaceDataProxy::arrayReset,
                         graph,
                         &QQuickGraphsSurface::handleArrayReset);
        QObject::connect(surfaceDataProxy,
                         &QSurfaceDataProxy::rowsAdded,
                         graph,
                         &QQuickGraphsSurface::handleRowsAdded);
        QObject::connect(surfaceDataProxy,
                         &QSurfaceDataProxy::rowsChanged,
                         graph,
                         &QQuickGraphsSurface::handleRowsChanged);
        QObject::connect(surfaceDataProxy,
                         &QSurfaceDataProxy::rowsRemoved,
                         graph,
                         &QQuickGraphsSurface::handleRowsRemoved);
        QObject::connect(surfaceDataProxy,
                         &QSurfaceDataProxy::rowsInserted,
                         graph,
                         &QQuickGraphsSurface::handleRowsInserted);
        QObject::connect(surfaceDataProxy,
                         &QSurfaceDataProxy::itemChanged,
                         graph,
                         &QQuickGraphsSurface::handleItemChanged);
        QObject::connect(q,
                         &QSurface3DSeries::dataProxyChanged,
                         graph,
                         &QQuickGraphsSurface::handleArrayReset);
    }
}

//  from ../qtgraphs/src/graphs3d/data/qsurface3dseries.cpp, line 812, as _ZN23QSurface3DSeriesPrivate15createItemLabelEv
inline void QSurface3DSeriesPrivate::createItemLabel()
{
    Q_Q(QSurface3DSeries);
    static const QString xTitleTag(QStringLiteral("@xTitle"));
    static const QString yTitleTag(QStringLiteral("@yTitle"));
    static const QString zTitleTag(QStringLiteral("@zTitle"));
    static const QString xLabelTag(QStringLiteral("@xLabel"));
    static const QString yLabelTag(QStringLiteral("@yLabel"));
    static const QString zLabelTag(QStringLiteral("@zLabel"));
    static const QString seriesNameTag(QStringLiteral("@seriesName"));

    if (m_selectedPoint == QSurface3DSeries::invalidSelectionPosition()) {
        m_itemLabel = QString(hiddenLabelTag);
        return;
    }

    QValue3DAxis *axisX = static_cast<QValue3DAxis *>(m_graph->axisX());
    QValue3DAxis *axisY = static_cast<QValue3DAxis *>(m_graph->axisY());
    QValue3DAxis *axisZ = static_cast<QValue3DAxis *>(m_graph->axisZ());
    QVector3D selectedPosition
        = q->dataProxy()->itemAt(QPoint(m_selectedPoint.y(), m_selectedPoint.x())).position();

    m_itemLabel = m_itemLabelFormat;

    m_itemLabel.replace(xTitleTag, axisX->title());
    m_itemLabel.replace(yTitleTag, axisY->title());
    m_itemLabel.replace(zTitleTag, axisZ->title());

    if (m_itemLabel.contains(xLabelTag)) {
        QString valueLabelText = axisX->formatter()->stringForValue(qreal(selectedPosition.x()),
                                                                    axisX->labelFormat());
        m_itemLabel.replace(xLabelTag, valueLabelText);
    }
    if (m_itemLabel.contains(yLabelTag)) {
        QString valueLabelText = axisY->formatter()->stringForValue(qreal(selectedPosition.y()),
                                                                    axisY->labelFormat());
        m_itemLabel.replace(yLabelTag, valueLabelText);
    }
    if (m_itemLabel.contains(zLabelTag)) {
        QString valueLabelText = axisZ->formatter()->stringForValue(qreal(selectedPosition.z()),
                                                                    axisZ->labelFormat());
        m_itemLabel.replace(zLabelTag, valueLabelText);
    }
    m_itemLabel.replace(seriesNameTag, m_name);
}

//  from ../qtgraphs/src/graphs3d/data/qsurface3dseries.cpp, line 897, as _ZN23QSurface3DSeriesPrivate10setTextureERK6QImage
inline void QSurface3DSeriesPrivate::setTexture(const QImage &texture)
{
    Q_Q(QSurface3DSeries);
    m_texture = texture;
    if (m_graph)
        m_graph->markSeriesVisualsDirty();
    if (static_cast<QQuickGraphsSurface *>(m_graph))
        static_cast<QQuickGraphsSurface *>(m_graph)->updateSurfaceTexture(q);
}

//  from ../qtgraphs/src/graphs3d/data/qsurface3dseries.cpp, line 907, as _ZN23QSurface3DSeriesPrivate17setWireframeColorE6QColor
inline void QSurface3DSeriesPrivate::setWireframeColor(QColor color)
{
    m_wireframeColor = color;
    if (m_graph)
        m_graph->markSeriesVisualsDirty();
}

//  from ../qtgraphs/src/graphs3d/data/qsurface3dseries.cpp, line 914, as _ZN23QSurface3DSeriesPrivate16setRowsSanitizedEb
inline void QSurface3DSeriesPrivate::setRowsSanitized(bool enabled)
{
    m_rowsSanitized = enabled;
    if (m_graph)
        m_graph->markDataDirty();
}

//  from ../qtgraphs/src/graphs3d/data/qsurface3dseries.cpp, line 926, as _ZN23QSurface3DSeriesPrivate8clearRowEx
inline void QSurface3DSeriesPrivate::clearRow(qsizetype rowIndex)
{
    m_dataArray[rowIndex].clear();
}

//  from ../qtgraphs/src/graphs3d/data/qsurface3dseries.cpp, line 931, as _ZN23QSurface3DSeriesPrivate10clearArrayEv
inline void QSurface3DSeriesPrivate::clearArray()
{
    m_dataArray.clear();
}

//  from ../qtgraphs/src/graphs3d/data/qsurface3dseries.cpp, line 936, as _ZN23QSurface3DSeriesPrivate8setAxisXEP12QValue3DAxis
inline void QSurface3DSeriesPrivate::setAxisX(QValue3DAxis *axis)
{
    m_axisX = axis;
}

//  from ../qtgraphs/src/graphs3d/data/qsurface3dseries.cpp, line 946, as _ZN23QSurface3DSeriesPrivate8setAxisYEP12QValue3DAxis
inline void QSurface3DSeriesPrivate::setAxisY(QValue3DAxis *axis)
{
    m_axisY = axis;
}

//  from ../qtgraphs/src/graphs3d/data/qsurface3dseries.cpp, line 956, as _ZN23QSurface3DSeriesPrivate8setAxisZEP12QValue3DAxis
inline void QSurface3DSeriesPrivate::setAxisZ(QValue3DAxis *axis)
{
    m_axisZ = axis;
}

//  from ../qtgraphs/src/graphs3d/data/qsurface3dseries.cpp, line 941, as _ZN23QSurface3DSeriesPrivate10resetAxisXEv
inline void QSurface3DSeriesPrivate::resetAxisX()
{
    m_axisX = nullptr;
}

//  from ../qtgraphs/src/graphs3d/data/qsurface3dseries.cpp, line 951, as _ZN23QSurface3DSeriesPrivate10resetAxisYEv
inline void QSurface3DSeriesPrivate::resetAxisY()
{
    m_axisY = nullptr;
}

//  from ../qtgraphs/src/graphs3d/data/qsurface3dseries.cpp, line 961, as _ZN23QSurface3DSeriesPrivate10resetAxisZEv
inline void QSurface3DSeriesPrivate::resetAxisZ()
{
    m_axisZ = nullptr;
}
//  -----------------------------------------------------------------------

//  A QSurface3DSeriesPrivate that Python can take functions over in. Every QSurface3DSeriesPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSurface3DSeriesPrivateCall0)(const void *, QAbstractDataProxy *, int *);
typedef void (*CuteQSurface3DSeriesPrivateCall1)(const void *, QQuickGraphsItem *, int *);
typedef void (*CuteQSurface3DSeriesPrivateCall2)(const void *, int *);
typedef void (*CuteQSurface3DSeriesPrivateCall3)(const void *, QQuickGraphsItem *, int *);
class CuteQSurface3DSeriesPrivate : public QSurface3DSeriesPrivate {
public:
  using QSurface3DSeriesPrivate::QSurface3DSeriesPrivate;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QAbstract3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstract3DSeriesPrivate20connectGraphAndProxyEP16QQuickGraphsItem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstract3DSeriesPrivate15createItemLabelEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstract3DSeriesPrivate8setGraphEP16QQuickGraphsItem")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QSurface3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
  void setDataProxy(QAbstractDataProxy *proxy) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSurface3DSeriesPrivateCall0 call = reinterpret_cast<CuteQSurface3DSeriesPrivateCall0>(taken[0]);
      call(this, proxy, &handled);
      if (handled) return;
    }
    QSurface3DSeriesPrivate::setDataProxy(proxy);
  }

  //  void QSurface3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem
  //      *newGraph)
  void connectGraphAndProxy(QQuickGraphsItem *newGraph) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSurface3DSeriesPrivateCall1 call = reinterpret_cast<CuteQSurface3DSeriesPrivateCall1>(taken[1]);
      call(this, newGraph, &handled);
      if (handled) return;
    }
    QSurface3DSeriesPrivate::connectGraphAndProxy(newGraph);
  }

  //  void QSurface3DSeriesPrivate::createItemLabel()
  void createItemLabel() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSurface3DSeriesPrivateCall2 call = reinterpret_cast<CuteQSurface3DSeriesPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QSurface3DSeriesPrivate::createItemLabel();
  }

  //  void QAbstract3DSeriesPrivate::setGraph(QQuickGraphsItem *graph)
  void setGraph(QQuickGraphsItem *graph) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSurface3DSeriesPrivateCall3 call = reinterpret_cast<CuteQSurface3DSeriesPrivateCall3>(taken[3]);
      call(this, graph, &handled);
      if (handled) return;
    }
    QAbstract3DSeriesPrivate::setGraph(graph);
  }
};

//  QSurface3DSeries *QSurface3DSeriesPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSurface3DSeries *ritual_ZN23QSurface3DSeriesPrivate6q_funcEv(
    QSurface3DSeriesPrivate *self) {
  return self->q_func();
}

//  const QSurface3DSeries *QSurface3DSeriesPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSurface3DSeries *ritual_ZNK23QSurface3DSeriesPrivate6q_funcEv(
    const QSurface3DSeriesPrivate *self) {
  return self->q_func();
}

//  QSurface3DSeriesPrivate::~QSurface3DSeriesPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivateD1Ev(QSurface3DSeriesPrivate *self) {
  delete self;
}

//  void QSurface3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy(
    QSurface3DSeriesPrivate *self,
    QAbstractDataProxy *proxy) {
  self->setDataProxy(proxy);
}

//  void QSurface3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem
//      *newGraph)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate20connectGraphAndProxyEP16QQuickGraphsItem(
    QSurface3DSeriesPrivate *self,
    QQuickGraphsItem *newGraph) {
  self->connectGraphAndProxy(newGraph);
}

//  void QSurface3DSeriesPrivate::createItemLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate15createItemLabelEv(
    QSurface3DSeriesPrivate *self) {
  self->createItemLabel();
}

//  void QSurface3DSeriesPrivate::setTexture(const QImage &texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate10setTextureERK6QImage(
    QSurface3DSeriesPrivate *self,
    const QImage *texture) {
  self->setTexture(*texture);
}

//  void QSurface3DSeriesPrivate::setWireframeColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate17setWireframeColorE6QColor(
    QSurface3DSeriesPrivate *self,
    const QColor *color) {
  self->setWireframeColor(*color);
}

//  void QSurface3DSeriesPrivate::setRowsSanitized(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate16setRowsSanitizedEb(
    QSurface3DSeriesPrivate *self,
    bool enabled) {
  self->setRowsSanitized(enabled);
}

//  void QSurface3DSeriesPrivate::clearRow(qsizetype rowIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate8clearRowEx(
    QSurface3DSeriesPrivate *self,
    qsizetype rowIndex) {
  self->clearRow(rowIndex);
}

//  void QSurface3DSeriesPrivate::clearArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate10clearArrayEv(
    QSurface3DSeriesPrivate *self) {
  self->clearArray();
}

//  void QSurface3DSeriesPrivate::setAxisX(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate8setAxisXEP12QValue3DAxis(
    QSurface3DSeriesPrivate *self,
    QValue3DAxis *axis) {
  self->setAxisX(axis);
}

//  void QSurface3DSeriesPrivate::setAxisY(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate8setAxisYEP12QValue3DAxis(
    QSurface3DSeriesPrivate *self,
    QValue3DAxis *axis) {
  self->setAxisY(axis);
}

//  void QSurface3DSeriesPrivate::setAxisZ(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate8setAxisZEP12QValue3DAxis(
    QSurface3DSeriesPrivate *self,
    QValue3DAxis *axis) {
  self->setAxisZ(axis);
}

//  void QSurface3DSeriesPrivate::resetAxisX()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate10resetAxisXEv(
    QSurface3DSeriesPrivate *self) {
  self->resetAxisX();
}

//  void QSurface3DSeriesPrivate::resetAxisY()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate10resetAxisYEv(
    QSurface3DSeriesPrivate *self) {
  self->resetAxisY();
}

//  void QSurface3DSeriesPrivate::resetAxisZ()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSurface3DSeriesPrivate10resetAxisZEv(
    QSurface3DSeriesPrivate *self) {
  self->resetAxisZ();
}

//  a Python function taken by a CuteQSurface3DSeriesPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSurface3DSeriesPrivate(
    QSurface3DSeriesPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSurface3DSeriesPrivate *>(self)->take(key, call);
}

//  void QSurface3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSurface3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy(
    QSurface3DSeriesPrivate *self,
    QAbstractDataProxy *proxy) {
  self->QSurface3DSeriesPrivate::setDataProxy(proxy);
}

//  void QSurface3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem
//      *newGraph)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSurface3DSeriesPrivate20connectGraphAndProxyEP16QQuickGraphsItem(
    QSurface3DSeriesPrivate *self,
    QQuickGraphsItem *newGraph) {
  self->QSurface3DSeriesPrivate::connectGraphAndProxy(newGraph);
}

//  void QSurface3DSeriesPrivate::createItemLabel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSurface3DSeriesPrivate15createItemLabelEv(
    QSurface3DSeriesPrivate *self) {
  self->QSurface3DSeriesPrivate::createItemLabel();
}

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
