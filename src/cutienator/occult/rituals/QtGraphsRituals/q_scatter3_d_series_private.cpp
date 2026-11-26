//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qscatter3dseries_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qscatter3dseries.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qscatter3dseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/qscatterdataitem.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/qcategory3daxis.h>
#include <QtGraphs/private/qquickgraphsscatter_p.h>
#include <QtGraphs/private/qscatter3dseries_p.h>
#include <QtGraphs/qvalue3daxis.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#include <QtGraphs/private/qabstract3dseries_p.h>
#include <QtGraphs/private/qabstractdataproxy_p.h>
#include <QtGraphs/private/qquickgraphsitem_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qtgraphs/src/graphs3d/data/qscatter3dseries.cpp, line 534, as _ZN23QScatter3DSeriesPrivateD2Ev
inline QScatter3DSeriesPrivate::~QScatter3DSeriesPrivate()
{
    clearArray();
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

//  from ../qtgraphs/src/graphs3d/utils/qgraphs3dlogging.cpp, line 13, as _Z14lcProperties3Dv
inline const QLoggingCategory &lcProperties3D()
{
    static const QLoggingCategory category("qt.graphs3d.properties");
    return category;
}

//  from ../qtgraphs/src/graphs3d/data/qabstract3dseries.cpp, line 1117, as _ZN24QAbstract3DSeriesPrivate18markItemLabelDirtyEv
inline void QAbstract3DSeriesPrivate::markItemLabelDirty()
{
    m_itemLabelDirty = true;
    m_changeTracker.itemLabelChanged = true;
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

//  from ../qtgraphs/src/graphs3d/data/qscatter3dseries.cpp, line 525, as _ZN23QScatter3DSeriesPrivateC1Ev
inline QScatter3DSeriesPrivate::QScatter3DSeriesPrivate()
    : QAbstract3DSeriesPrivate(QAbstract3DSeries::SeriesType::Scatter)
    , m_selectedItem(QQuickGraphsScatter::invalidSelectionIndex())
    , m_itemSize(0.0f)
{
    m_itemLabelFormat = QStringLiteral("@xLabel, @yLabel, @zLabel");
    m_mesh = QAbstract3DSeries::Mesh::Sphere;
}

//  from ../qtgraphs/src/graphs3d/data/qscatter3dseries.cpp, line 634, as _ZN23QScatter3DSeriesPrivate15setSelectedItemEx
inline void QScatter3DSeriesPrivate::setSelectedItem(qsizetype index)
{
    Q_Q(QScatter3DSeries);
    if (index == m_selectedItem) {
        qCDebug(lcProperties3D, "%s Value is already set to: %" PRIdQSIZETYPE,
                qUtf8Printable(QLatin1String(__FUNCTION__)), index);
        return;
    }
    markItemLabelDirty();
    m_selectedItem = index;
    emit q->selectedItemChanged(m_selectedItem);
}

//  from ../qtgraphs/src/graphs3d/data/qscatter3dseries.cpp, line 647, as _ZN23QScatter3DSeriesPrivate11setItemSizeEf
inline void QScatter3DSeriesPrivate::setItemSize(float size)
{
    m_itemSize = size;
    if (m_graph)
        m_graph->markSeriesVisualsDirty();
}

//  from ../qtgraphs/src/graphs3d/data/qscatter3dseries.cpp, line 654, as _ZN23QScatter3DSeriesPrivate12setDataArrayERK5QListI16QScatterDataItemE
inline void QScatter3DSeriesPrivate::setDataArray(const QScatterDataArray &newDataArray)
{
    m_dataArray = newDataArray;
}

//  from ../qtgraphs/src/graphs3d/data/qscatter3dseries.cpp, line 659, as _ZN23QScatter3DSeriesPrivate10clearArrayEv
inline void QScatter3DSeriesPrivate::clearArray()
{
    m_dataArray.clear();
}

//  from ../qtgraphs/src/graphs3d/data/qscatter3dseries.cpp, line 664, as _ZN23QScatter3DSeriesPrivate13setScaleArrayERK5QListI9QVector3DE
inline void QScatter3DSeriesPrivate::setScaleArray(const QList<QVector3D> &newScaleArray)
{
    m_scaleArray = newScaleArray;
}

//  from ../qtgraphs/src/graphs3d/data/qscatter3dseries.cpp, line 669, as _ZN23QScatter3DSeriesPrivate15clearScaleArrayEv
inline void QScatter3DSeriesPrivate::clearScaleArray()
{
    m_scaleArray.clear();
}

//  from ../qtgraphs/src/graphs3d/data/qscatter3dseries.cpp, line 674, as _ZN23QScatter3DSeriesPrivate8setAxisXEP12QValue3DAxis
inline void QScatter3DSeriesPrivate::setAxisX(QValue3DAxis *axis)
{
    m_axisX = axis;
}

//  from ../qtgraphs/src/graphs3d/data/qscatter3dseries.cpp, line 684, as _ZN23QScatter3DSeriesPrivate8setAxisYEP12QValue3DAxis
inline void QScatter3DSeriesPrivate::setAxisY(QValue3DAxis *axis)
{
    m_axisY = axis;
}

//  from ../qtgraphs/src/graphs3d/data/qscatter3dseries.cpp, line 694, as _ZN23QScatter3DSeriesPrivate8setAxisZEP12QValue3DAxis
inline void QScatter3DSeriesPrivate::setAxisZ(QValue3DAxis *axis)
{
    m_axisZ = axis;
}

//  from ../qtgraphs/src/graphs3d/data/qscatter3dseries.cpp, line 679, as _ZN23QScatter3DSeriesPrivate10resetAxisXEv
inline void QScatter3DSeriesPrivate::resetAxisX()
{
    m_axisX = nullptr;
}

//  from ../qtgraphs/src/graphs3d/data/qscatter3dseries.cpp, line 689, as _ZN23QScatter3DSeriesPrivate10resetAxisYEv
inline void QScatter3DSeriesPrivate::resetAxisY()
{
    m_axisY = nullptr;
}

//  from ../qtgraphs/src/graphs3d/data/qscatter3dseries.cpp, line 699, as _ZN23QScatter3DSeriesPrivate10resetAxisZEv
inline void QScatter3DSeriesPrivate::resetAxisZ()
{
    m_axisZ = nullptr;
}
//  -----------------------------------------------------------------------

//  A QScatter3DSeriesPrivate that Python can take functions over in. Every QScatter3DSeriesPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQScatter3DSeriesPrivateCall0)(const void *, QAbstractDataProxy *, int *);
typedef void (*CuteQScatter3DSeriesPrivateCall1)(const void *, QQuickGraphsItem *, int *);
typedef void (*CuteQScatter3DSeriesPrivateCall2)(const void *, int *);
typedef void (*CuteQScatter3DSeriesPrivateCall3)(const void *, QQuickGraphsItem *, int *);
class CuteQScatter3DSeriesPrivate : public QScatter3DSeriesPrivate {
public:
  using QScatter3DSeriesPrivate::QScatter3DSeriesPrivate;
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
      CuteQScatter3DSeriesPrivateCall0 call = reinterpret_cast<CuteQScatter3DSeriesPrivateCall0>(taken[0]);
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
      CuteQScatter3DSeriesPrivateCall1 call = reinterpret_cast<CuteQScatter3DSeriesPrivateCall1>(taken[1]);
      call(this, newGraph, &handled);
      if (handled) return;
    }
    QScatter3DSeriesPrivate::connectGraphAndProxy(newGraph);
  }

  //  void QScatter3DSeriesPrivate::createItemLabel()
  void createItemLabel() override {
    if (taken[2]) {
      int handled = 0;
      CuteQScatter3DSeriesPrivateCall2 call = reinterpret_cast<CuteQScatter3DSeriesPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QScatter3DSeriesPrivate::createItemLabel();
  }

  //  void QAbstract3DSeriesPrivate::setGraph(QQuickGraphsItem *graph)
  void setGraph(QQuickGraphsItem *graph) override {
    if (taken[3]) {
      int handled = 0;
      CuteQScatter3DSeriesPrivateCall3 call = reinterpret_cast<CuteQScatter3DSeriesPrivateCall3>(taken[3]);
      call(this, graph, &handled);
      if (handled) return;
    }
    QAbstract3DSeriesPrivate::setGraph(graph);
  }
};

//  QScatter3DSeries *QScatter3DSeriesPrivate::q_func()
extern "C" Q_DECL_EXPORT
QScatter3DSeries *ritual_ZN23QScatter3DSeriesPrivate6q_funcEv(
    QScatter3DSeriesPrivate *self) {
  return self->q_func();
}

//  const QScatter3DSeries *QScatter3DSeriesPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QScatter3DSeries *ritual_ZNK23QScatter3DSeriesPrivate6q_funcEv(
    const QScatter3DSeriesPrivate *self) {
  return self->q_func();
}

//  QScatter3DSeriesPrivate::QScatter3DSeriesPrivate()
extern "C" Q_DECL_EXPORT
QScatter3DSeriesPrivate *ritual_ZN23QScatter3DSeriesPrivateC1Ev() {
  return new CuteQScatter3DSeriesPrivate();
}

//  QScatter3DSeriesPrivate::~QScatter3DSeriesPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivateD1Ev(QScatter3DSeriesPrivate *self) {
  delete self;
}

//  void QScatter3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy(
    QScatter3DSeriesPrivate *self,
    QAbstractDataProxy *proxy) {
  self->setDataProxy(proxy);
}

//  void QScatter3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem
//      *newGraph)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivate20connectGraphAndProxyEP16QQuickGraphsItem(
    QScatter3DSeriesPrivate *self,
    QQuickGraphsItem *newGraph) {
  self->connectGraphAndProxy(newGraph);
}

//  void QScatter3DSeriesPrivate::createItemLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivate15createItemLabelEv(
    QScatter3DSeriesPrivate *self) {
  self->createItemLabel();
}

//  void QScatter3DSeriesPrivate::setSelectedItem(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivate15setSelectedItemEx(
    QScatter3DSeriesPrivate *self,
    qsizetype index) {
  self->setSelectedItem(index);
}

//  void QScatter3DSeriesPrivate::setItemSize(float size)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivate11setItemSizeEf(
    QScatter3DSeriesPrivate *self,
    float size) {
  self->setItemSize(size);
}

//  void QScatter3DSeriesPrivate::setDataArray(const QScatterDataArray
//      &newDataArray)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivate12setDataArrayERK5QListI16QScatterDataItemE(
    QScatter3DSeriesPrivate *self,
    const QList<QScatterDataItem> *newDataArray) {
  self->setDataArray(*newDataArray);
}

//  void QScatter3DSeriesPrivate::clearArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivate10clearArrayEv(
    QScatter3DSeriesPrivate *self) {
  self->clearArray();
}

//  void QScatter3DSeriesPrivate::setScaleArray(const QList<QVector3D>
//      &newScaleArray)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivate13setScaleArrayERK5QListI9QVector3DE(
    QScatter3DSeriesPrivate *self,
    const QList<QVector3D> *newScaleArray) {
  self->setScaleArray(*newScaleArray);
}

//  void QScatter3DSeriesPrivate::clearScaleArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivate15clearScaleArrayEv(
    QScatter3DSeriesPrivate *self) {
  self->clearScaleArray();
}

//  void QScatter3DSeriesPrivate::setAxisX(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivate8setAxisXEP12QValue3DAxis(
    QScatter3DSeriesPrivate *self,
    QValue3DAxis *axis) {
  self->setAxisX(axis);
}

//  void QScatter3DSeriesPrivate::setAxisY(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivate8setAxisYEP12QValue3DAxis(
    QScatter3DSeriesPrivate *self,
    QValue3DAxis *axis) {
  self->setAxisY(axis);
}

//  void QScatter3DSeriesPrivate::setAxisZ(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivate8setAxisZEP12QValue3DAxis(
    QScatter3DSeriesPrivate *self,
    QValue3DAxis *axis) {
  self->setAxisZ(axis);
}

//  void QScatter3DSeriesPrivate::resetAxisX()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivate10resetAxisXEv(
    QScatter3DSeriesPrivate *self) {
  self->resetAxisX();
}

//  void QScatter3DSeriesPrivate::resetAxisY()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivate10resetAxisYEv(
    QScatter3DSeriesPrivate *self) {
  self->resetAxisY();
}

//  void QScatter3DSeriesPrivate::resetAxisZ()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QScatter3DSeriesPrivate10resetAxisZEv(
    QScatter3DSeriesPrivate *self) {
  self->resetAxisZ();
}

//  a Python function taken by a CuteQScatter3DSeriesPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScatter3DSeriesPrivate(
    QScatter3DSeriesPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScatter3DSeriesPrivate *>(self)->take(key, call);
}

//  void QScatter3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QScatter3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy(
    QScatter3DSeriesPrivate *self,
    QAbstractDataProxy *proxy) {
  self->QScatter3DSeriesPrivate::setDataProxy(proxy);
}

//  void QScatter3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem
//      *newGraph)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QScatter3DSeriesPrivate20connectGraphAndProxyEP16QQuickGraphsItem(
    QScatter3DSeriesPrivate *self,
    QQuickGraphsItem *newGraph) {
  self->QScatter3DSeriesPrivate::connectGraphAndProxy(newGraph);
}

//  void QScatter3DSeriesPrivate::createItemLabel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QScatter3DSeriesPrivate15createItemLabelEv(
    QScatter3DSeriesPrivate *self) {
  self->QScatter3DSeriesPrivate::createItemLabel();
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
