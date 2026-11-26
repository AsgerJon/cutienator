//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qspline3dseries_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qspline3dseries.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qspline3dseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/private/qspline3dseries_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#include <QtGraphs/qcategory3daxis.h>
#include <QtGraphs/private/qquickgraphsscatter_p.h>
#include <QtGraphs/private/qscatter3dseries_p.h>
#include <QtGraphs/qvalue3daxis.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
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

//  from ../qtgraphs/src/graphs3d/data/qspline3dseries.cpp, line 365, as _ZN22QSpline3DSeriesPrivateD2Ev
inline QSpline3DSeriesPrivate::~QSpline3DSeriesPrivate() {}

//  from ../qtgraphs/src/graphs3d/data/qscatter3dseries.cpp, line 539, as _ZN23QScatter3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy
inline void QScatter3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
{
    Q_Q(QScatter3DSeries);
    Q_ASSERT(proxy->type() == QAbstractDataProxy::DataType::Scatter);

    QAbstract3DSeriesPrivate::setDataProxy(proxy);

    emit q->dataProxyChanged(static_cast<QScatterDataProxy *>(proxy));
}

//  from ../qtgraphs/src/graphs3d/data/qscatter3dseries.cpp, line 589, as _ZN23QScatter3DSeriesPrivate15createItemLabelEv
inline void QScatter3DSeriesPrivate::createItemLabel()
{
    Q_Q(QScatter3DSeries);
    static const QString xTitleTag(QStringLiteral("@xTitle"));
    static const QString yTitleTag(QStringLiteral("@yTitle"));
    static const QString zTitleTag(QStringLiteral("@zTitle"));
    static const QString xLabelTag(QStringLiteral("@xLabel"));
    static const QString yLabelTag(QStringLiteral("@yLabel"));
    static const QString zLabelTag(QStringLiteral("@zLabel"));
    static const QString seriesNameTag(QStringLiteral("@seriesName"));

    if (m_selectedItem == QScatter3DSeries::invalidSelectionIndex()) {
        m_itemLabel = QString(hiddenLabelTag);
        return;
    }

    QValue3DAxis *axisX = static_cast<QValue3DAxis *>(m_graph->axisX());
    QValue3DAxis *axisY = static_cast<QValue3DAxis *>(m_graph->axisY());
    QValue3DAxis *axisZ = static_cast<QValue3DAxis *>(m_graph->axisZ());
    QVector3D selectedPosition = q->dataProxy()->itemAt(m_selectedItem).position();

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

//  from ../qtgraphs/src/graphs3d/data/qscatter3dseries.cpp, line 549, as _ZN23QScatter3DSeriesPrivate20connectGraphAndProxyEP16QQuickGraphsItem
inline void QScatter3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem *newGraph)
{
    Q_Q(QScatter3DSeries);
    QScatterDataProxy *scatterDataProxy = static_cast<QScatterDataProxy *>(m_dataProxy);

    if (m_graph && scatterDataProxy) {
        // Disconnect old graph/old proxy
        QObject::disconnect(scatterDataProxy, 0, m_graph, 0);
        QObject::disconnect(q, 0, m_graph, 0);
    }

    if (newGraph && scatterDataProxy) {
        QQuickGraphsScatter *graph = static_cast<QQuickGraphsScatter *>(newGraph);
        QObject::connect(scatterDataProxy,
                         &QScatterDataProxy::arrayReset,
                         graph,
                         &QQuickGraphsScatter::handleArrayReset);
        QObject::connect(scatterDataProxy,
                         &QScatterDataProxy::itemsAdded,
                         graph,
                         &QQuickGraphsScatter::handleItemsAdded);
        QObject::connect(scatterDataProxy,
                         &QScatterDataProxy::itemsChanged,
                         graph,
                         &QQuickGraphsScatter::handleItemsChanged);
        QObject::connect(scatterDataProxy,
                         &QScatterDataProxy::itemsRemoved,
                         graph,
                         &QQuickGraphsScatter::handleItemsRemoved);
        QObject::connect(scatterDataProxy,
                         &QScatterDataProxy::itemsInserted,
                         graph,
                         &QQuickGraphsScatter::handleItemsInserted);
        QObject::connect(q,
                         &QScatter3DSeries::dataProxyChanged,
                         graph,
                         &QQuickGraphsScatter::handleArrayReset);
    }
}

//  from ../qtgraphs/src/graphs3d/data/qscatter3dseries.cpp, line 525, as _ZN23QScatter3DSeriesPrivateC2Ev
inline QScatter3DSeriesPrivate::QScatter3DSeriesPrivate()
    : QAbstract3DSeriesPrivate(QAbstract3DSeries::SeriesType::Scatter)
    , m_selectedItem(QQuickGraphsScatter::invalidSelectionIndex())
    , m_itemSize(0.0f)
{
    m_itemLabelFormat = QStringLiteral("@xLabel, @yLabel, @zLabel");
    m_mesh = QAbstract3DSeries::Mesh::Sphere;
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

//  from ../qtgraphs/src/graphs3d/data/qscatter3dseries.cpp, line 534, as _ZN23QScatter3DSeriesPrivateD2Ev
inline QScatter3DSeriesPrivate::~QScatter3DSeriesPrivate()
{
    clearArray();
}

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

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 1117, as _ZN24QAbstract3DSeriesPrivate18markItemLabelDirtyEv
inline void QAbstract3DSeriesPrivate::markItemLabelDirty()
{
    m_itemLabelDirty = true;
    m_changeTracker.itemLabelChanged = true;
}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 879, as _ZN24QAbstract3DSeriesPrivateC2EN17QAbstract3DSeries10SeriesTypeE
inline QAbstract3DSeriesPrivate::QAbstract3DSeriesPrivate(QAbstract3DSeries::SeriesType type)
    : m_type(type)
    , m_dataProxy(0)
    , m_visible(true)
    , m_graph(0)
    , m_mesh(QAbstract3DSeries::Mesh::Cube)
    , m_meshSmooth(false)
    , m_colorStyle(QGraphsTheme::ColorStyle::Uniform)
    , m_baseColor(Qt::black)
    , m_singleHighlightColor(Qt::black)
    , m_multiHighlightColor(Qt::black)
    , m_itemLabelDirty(true)
    , m_itemLabelVisible(true)
    , m_lightingMode(QAbstract3DSeries::LightingMode::Shaded)
{}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 895, as _ZN24QAbstract3DSeriesPrivateD2Ev
inline QAbstract3DSeriesPrivate::~QAbstract3DSeriesPrivate() {}

//  from ../qtgraphs/src/graphs3d/data/qscatter3dseries.cpp, line 659, as _ZN23QScatter3DSeriesPrivate10clearArrayEv
inline void QScatter3DSeriesPrivate::clearArray()
{
    m_dataArray.clear();
}

//  from ../qtgraphs/src/graphs3d/data/qspline3dseries.cpp, line 361, as _ZN22QSpline3DSeriesPrivateC1Ev
inline QSpline3DSeriesPrivate::QSpline3DSeriesPrivate()
    : QScatter3DSeriesPrivate()
{}
//  -----------------------------------------------------------------------

//  A QSpline3DSeriesPrivate that Python can take functions over in. Every QSpline3DSeriesPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSpline3DSeriesPrivateCall0)(const void *, QAbstractDataProxy *, int *);
typedef void (*CuteQSpline3DSeriesPrivateCall1)(const void *, QQuickGraphsItem *, int *);
typedef void (*CuteQSpline3DSeriesPrivateCall2)(const void *, int *);
typedef void (*CuteQSpline3DSeriesPrivateCall3)(const void *, QQuickGraphsItem *, int *);
class CuteQSpline3DSeriesPrivate : public QSpline3DSeriesPrivate {
public:
  using QSpline3DSeriesPrivate::QSpline3DSeriesPrivate;
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

  //  void QScatter3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
  void setDataProxy(QAbstractDataProxy *proxy) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSpline3DSeriesPrivateCall0 call = reinterpret_cast<CuteQSpline3DSeriesPrivateCall0>(taken[0]);
      call(this, proxy, &handled);
      if (handled) return;
    }
    QScatter3DSeriesPrivate::setDataProxy(proxy);
  }

  //  void QScatter3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem
  //      *newGraph)
  void connectGraphAndProxy(QQuickGraphsItem *newGraph) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSpline3DSeriesPrivateCall1 call = reinterpret_cast<CuteQSpline3DSeriesPrivateCall1>(taken[1]);
      call(this, newGraph, &handled);
      if (handled) return;
    }
    QScatter3DSeriesPrivate::connectGraphAndProxy(newGraph);
  }

  //  void QScatter3DSeriesPrivate::createItemLabel()
  void createItemLabel() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSpline3DSeriesPrivateCall2 call = reinterpret_cast<CuteQSpline3DSeriesPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QScatter3DSeriesPrivate::createItemLabel();
  }

  //  void QAbstract3DSeriesPrivate::setGraph(QQuickGraphsItem *graph)
  void setGraph(QQuickGraphsItem *graph) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSpline3DSeriesPrivateCall3 call = reinterpret_cast<CuteQSpline3DSeriesPrivateCall3>(taken[3]);
      call(this, graph, &handled);
      if (handled) return;
    }
    QAbstract3DSeriesPrivate::setGraph(graph);
  }
};

//  QSpline3DSeries *QSpline3DSeriesPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSpline3DSeries *ritual_ZN22QSpline3DSeriesPrivate6q_funcEv(
    QSpline3DSeriesPrivate *self) {
  return self->q_func();
}

//  const QSpline3DSeries *QSpline3DSeriesPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSpline3DSeries *ritual_ZNK22QSpline3DSeriesPrivate6q_funcEv(
    const QSpline3DSeriesPrivate *self) {
  return self->q_func();
}

//  QSpline3DSeriesPrivate::QSpline3DSeriesPrivate()
extern "C" Q_DECL_EXPORT
QSpline3DSeriesPrivate *ritual_ZN22QSpline3DSeriesPrivateC1Ev() {
  return new CuteQSpline3DSeriesPrivate();
}

//  QSpline3DSeriesPrivate::~QSpline3DSeriesPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSpline3DSeriesPrivateD1Ev(QSpline3DSeriesPrivate *self) {
  delete self;
}

//  a Python function taken by a CuteQSpline3DSeriesPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSpline3DSeriesPrivate(
    QSpline3DSeriesPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSpline3DSeriesPrivate *>(self)->take(key, call);
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
