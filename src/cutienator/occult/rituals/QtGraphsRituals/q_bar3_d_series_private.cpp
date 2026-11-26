//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qbar3dseries_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qbar3dseries.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qbar3dseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qcolor.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmath.h>
#include <QtGraphs/private/qabstract3daxis_p.h>
#include <QtGraphs/private/qbar3dseries_p.h>
#include <QtGraphs/private/qcategory3daxis_p.h>
#include <QtGraphs/private/qquickgraphsbars_p.h>
#include <QtGraphs/private/qvalue3daxis_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#include <QtGui/qquaternion.h>
#include <QtGraphs/private/qabstract3dseries_p.h>
#include <QtGraphs/private/qabstractdataproxy_p.h>
#include <QtGraphs/private/qquickgraphsitem_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 828, as _ZN19QBar3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy
inline void QBar3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
{
    Q_ASSERT(proxy->type() == QAbstractDataProxy::DataType::Bar);
    Q_Q(QBar3DSeries);

    QAbstract3DSeriesPrivate::setDataProxy(proxy);

    emit q->dataProxyChanged(static_cast<QBarDataProxy *>(proxy));
}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 894, as _ZN19QBar3DSeriesPrivate15createItemLabelEv
inline void QBar3DSeriesPrivate::createItemLabel()
{
    Q_Q(QBar3DSeries);
    static const QString rowIndexTag(QStringLiteral("@rowIdx"));
    static const QString rowLabelTag(QStringLiteral("@rowLabel"));
    static const QString rowTitleTag(QStringLiteral("@rowTitle"));
    static const QString colIndexTag(QStringLiteral("@colIdx"));
    static const QString colLabelTag(QStringLiteral("@colLabel"));
    static const QString colTitleTag(QStringLiteral("@colTitle"));
    static const QString valueTitleTag(QStringLiteral("@valueTitle"));
    static const QString valueLabelTag(QStringLiteral("@valueLabel"));
    static const QString seriesNameTag(QStringLiteral("@seriesName"));

    if (m_selectedBar == QBar3DSeries::invalidSelectionPosition()) {
        m_itemLabel = QString(hiddenLabelTag);
        return;
    }

    QLocale locale(QLocale::c());
    if (m_graph)
        locale = m_graph->locale();
    else
        return;

    QCategory3DAxis *categoryAxisZ = static_cast<QCategory3DAxis *>(m_graph->axisZ());
    QCategory3DAxis *categoryAxisX = static_cast<QCategory3DAxis *>(m_graph->axisX());
    QValue3DAxis *valueAxis = static_cast<QValue3DAxis *>(m_graph->axisY());
    qreal selectedBarValue = qreal(q->dataProxy()->itemAt(m_selectedBar).value());

    // Custom format expects printf format specifier. There is no tag for it.
    m_itemLabel = valueAxis->formatter()->stringForValue(selectedBarValue, m_itemLabelFormat);

    int selBarPosRow = m_selectedBar.x();
    int selBarPosCol = m_selectedBar.y();
    m_itemLabel.replace(rowIndexTag, locale.toString(selBarPosRow));
    if (categoryAxisZ->labels().size() > selBarPosRow)
        m_itemLabel.replace(rowLabelTag, categoryAxisZ->labels().at(selBarPosRow));
    else
        m_itemLabel.replace(rowLabelTag, QString());
    m_itemLabel.replace(rowTitleTag, categoryAxisZ->title());
    m_itemLabel.replace(colIndexTag, locale.toString(selBarPosCol));
    if (categoryAxisX->labels().size() > selBarPosCol)
        m_itemLabel.replace(colLabelTag, categoryAxisX->labels().at(selBarPosCol));
    else
        m_itemLabel.replace(colLabelTag, QString());
    m_itemLabel.replace(colTitleTag, categoryAxisX->title());
    m_itemLabel.replace(valueTitleTag, valueAxis->title());

    if (m_itemLabel.contains(valueLabelTag)) {
        QString valueLabelText = valueAxis->formatter()->stringForValue(selectedBarValue,
                                                                        valueAxis->labelFormat());
        m_itemLabel.replace(valueLabelTag, valueLabelText);
    }

    m_itemLabel.replace(seriesNameTag, m_name);
}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 838, as _ZN19QBar3DSeriesPrivate20connectGraphAndProxyEP16QQuickGraphsItem
inline void QBar3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem *newGraph)
{
    Q_Q(QBar3DSeries);
    QBarDataProxy *barDataProxy = static_cast<QBarDataProxy *>(m_dataProxy);

    if (m_graph && barDataProxy) {
        // Disconnect old graph/old proxy
        QObject::disconnect(barDataProxy, 0, m_graph, 0);
        QObject::disconnect(q, 0, m_graph, 0);
    }

    if (newGraph && barDataProxy) {
        QQuickGraphsBars *graph = static_cast<QQuickGraphsBars *>(newGraph);
        QObject::connect(barDataProxy,
                         &QBarDataProxy::arrayReset,
                         graph,
                         &QQuickGraphsBars::handleArrayReset);
        QObject::connect(barDataProxy,
                         &QBarDataProxy::rowsAdded,
                         graph,
                         &QQuickGraphsBars::handleRowsAdded);
        QObject::connect(barDataProxy,
                         &QBarDataProxy::rowsChanged,
                         graph,
                         &QQuickGraphsBars::handleRowsChanged);
        QObject::connect(barDataProxy,
                         &QBarDataProxy::rowsRemoved,
                         graph,
                         &QQuickGraphsBars::handleRowsRemoved);
        QObject::connect(barDataProxy,
                         &QBarDataProxy::rowsInserted,
                         graph,
                         &QQuickGraphsBars::handleRowsInserted);
        QObject::connect(barDataProxy,
                         &QBarDataProxy::itemChanged,
                         graph,
                         &QQuickGraphsBars::handleItemChanged);
        QObject::connect(q,
                         &QBar3DSeries::rowLabelsChanged,
                         graph,
                         &QQuickGraphsBars::handleDataRowLabelsChanged);
        QObject::connect(q,
                         &QBar3DSeries::columnLabelsChanged,
                         graph,
                         &QQuickGraphsBars::handleDataColumnLabelsChanged);
        QObject::connect(q,
                         &QBar3DSeries::dataProxyChanged,
                         graph,
                         &QQuickGraphsBars::handleArrayReset);
        QObject::connect(q,
                         &QBar3DSeries::rowColorsChanged,
                         graph,
                         &QQuickGraphsBars::handleRowColorsChanged);
    }
}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 757, as _ZN19QBar3DSeriesPrivateD2Ev
inline QBar3DSeriesPrivate::~QBar3DSeriesPrivate() {}

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

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 748, as _ZN19QBar3DSeriesPrivateC1Ev
inline QBar3DSeriesPrivate::QBar3DSeriesPrivate()
    : QAbstract3DSeriesPrivate(QAbstract3DSeries::SeriesType::Bar)
    , m_selectedBar(QQuickGraphsBars::invalidSelectionPosition())
{
    m_itemLabelFormat = QStringLiteral("@valueLabel");
    m_mesh = QAbstract3DSeries::Mesh::BevelBar;
    m_valueColoring = false;
}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 951, as _ZN19QBar3DSeriesPrivate14setSelectedBarE6QPoint
inline void QBar3DSeriesPrivate::setSelectedBar(QPoint position)
{
    Q_Q(QBar3DSeries);
    if (position == m_selectedBar) {
        qCDebug(lcProperties3D, "%s value is already set to: %d %d",
                qUtf8Printable(QLatin1String(__FUNCTION__)), position.x(), position.y());
        return;
    }

    markItemLabelDirty();
    m_selectedBar = position;
    emit q->selectedBarChanged(m_selectedBar);
}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 965, as _ZN19QBar3DSeriesPrivate12setRowColorsERK5QListI6QColorE
inline void QBar3DSeriesPrivate::setRowColors(const QList<QColor> &colors)
{
    Q_Q(QBar3DSeries);
    if (m_rowColors == colors) {
        qCDebug(lcProperties3D) << __FUNCTION__
            << "value is already set to:" << colors;
        return;
    }

    m_rowColors = colors;
    emit q->rowColorsChanged(m_rowColors);
}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 978, as _ZN19QBar3DSeriesPrivate23setValueColoringEnabledEb
inline void QBar3DSeriesPrivate::setValueColoringEnabled(bool enabled)
{
    Q_Q(QBar3DSeries);
    if (m_valueColoring == enabled) {
        qCDebug(lcProperties3D) << __FUNCTION__
            << "value is already set to:" << enabled;
        return;
    }
    m_valueColoring = enabled;
    emit q->valueColoringEnabledChanged(enabled);
}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 990, as _ZN19QBar3DSeriesPrivate12setDataArrayERK5QListIS0_I12QBarDataItemEE
inline void QBar3DSeriesPrivate::setDataArray(const QBarDataArray &newDataArray)
{
    m_dataArray = newDataArray;
}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 995, as _ZN19QBar3DSeriesPrivate8clearRowEx
inline void QBar3DSeriesPrivate::clearRow(qsizetype rowIndex)
{
    m_dataArray[rowIndex].clear();
}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 1000, as _ZN19QBar3DSeriesPrivate10clearArrayEv
inline void QBar3DSeriesPrivate::clearArray()
{
    m_dataArray.clear();
}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 1005, as _ZN19QBar3DSeriesPrivate12setRowLabelsERK5QListI7QStringE
inline void QBar3DSeriesPrivate::setRowLabels(const QStringList &labels)
{
    m_rowLabels = labels;
}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 1010, as _ZN19QBar3DSeriesPrivate15setColumnLabelsERK5QListI7QStringE
inline void QBar3DSeriesPrivate::setColumnLabels(const QStringList &labels)
{
    m_columnLabels = labels;
}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 1015, as _ZN19QBar3DSeriesPrivate18setCustomRowLabelsERK5QListI7QStringE
inline void QBar3DSeriesPrivate::setCustomRowLabels(const QStringList &labels)
{
    m_customRowLabels = labels;
}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 1020, as _ZN19QBar3DSeriesPrivate21setCustomColumnLabelsERK5QListI7QStringE
inline void QBar3DSeriesPrivate::setCustomColumnLabels(const QStringList &labels)
{
    m_customColumnLabels = labels;
}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 759, as _ZN19QBar3DSeriesPrivate12fixRowLabelsExxRK5QListI7QStringEb
inline void QBar3DSeriesPrivate::fixRowLabels(qsizetype startIndex,
                                       qsizetype count,
                                       const QStringList &newLabels,
                                       bool isInsert)
{
    bool changed = false;
    qsizetype currentSize = m_rowLabels.size();

    qsizetype newSize = newLabels.size();
    if (startIndex >= currentSize) {
        // Adding labels past old label array, create empty strings to fill
        // intervening space
        if (newSize) {
            for (qsizetype i = currentSize; i < startIndex; i++)
                m_rowLabels << QString();
            // Doesn't matter if insert, append, or just change when there were no
            // existing strings, just append new strings.
            m_rowLabels << newLabels;
            changed = true;
        }
    } else {
        if (isInsert) {
            qsizetype insertIndex = startIndex;
            if (count)
                changed = true;
            for (qsizetype i = 0; i < count; i++) {
                if (i < newSize)
                    m_rowLabels.insert(insertIndex++, newLabels.at(i));
                else
                    m_rowLabels.insert(insertIndex++, QString());
            }
        } else {
            // Either append or change, replace labels up to array end and then add
            // new ones
            qsizetype lastChangeIndex = count + startIndex;
            qsizetype newIndex = 0;
            for (qsizetype i = startIndex; i < lastChangeIndex; i++) {
                if (i >= currentSize) {
                    // Label past the current size, so just append the new label
                    if (newSize < newIndex) {
                        changed = true;
                        m_rowLabels << newLabels.at(newIndex);
                    } else {
                        break; // No point appending empty strings, so just exit
                    }
                } else if (newSize > newIndex) {
                    // Replace existing label
                    if (m_rowLabels.at(i) != newLabels.at(newIndex)) {
                        changed = true;
                        m_rowLabels[i] = newLabels.at(newIndex);
                    }
                } else {
                    // No more new labels, so clear existing label
                    if (!m_rowLabels.at(i).isEmpty()) {
                        changed = true;
                        m_rowLabels[i] = QString();
                    }
                }
                newIndex++;
            }
        }
    }

    if (changed) {
        Q_Q(QBar3DSeries);
        emit q->rowLabelsChanged();
    }
}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 1025, as _ZN19QBar3DSeriesPrivate10setRowAxisEP15QCategory3DAxis
inline void QBar3DSeriesPrivate::setRowAxis(QCategory3DAxis *axis)
{
    m_rowAxis = axis;
}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 1035, as _ZN19QBar3DSeriesPrivate12setValueAxisEP12QValue3DAxis
inline void QBar3DSeriesPrivate::setValueAxis(QValue3DAxis *axis)
{
    m_valueAxis = axis;
}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 1045, as _ZN19QBar3DSeriesPrivate13setColumnAxisEP15QCategory3DAxis
inline void QBar3DSeriesPrivate::setColumnAxis(QCategory3DAxis *axis)
{
    m_columnAxis = axis;
}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 1030, as _ZN19QBar3DSeriesPrivate12resetRowAxisEv
inline void QBar3DSeriesPrivate::resetRowAxis()
{
    m_rowAxis = nullptr;
}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 1040, as _ZN19QBar3DSeriesPrivate14resetValueAxisEv
inline void QBar3DSeriesPrivate::resetValueAxis()
{
    m_valueAxis = nullptr;
}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 1050, as _ZN19QBar3DSeriesPrivate15resetColumnAxisEv
inline void QBar3DSeriesPrivate::resetColumnAxis()
{
    m_columnAxis = nullptr;
}
//  -----------------------------------------------------------------------

//  A QBar3DSeriesPrivate that Python can take functions over in. Every QBar3DSeriesPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQBar3DSeriesPrivateCall0)(const void *, QAbstractDataProxy *, int *);
typedef void (*CuteQBar3DSeriesPrivateCall1)(const void *, QQuickGraphsItem *, int *);
typedef void (*CuteQBar3DSeriesPrivateCall2)(const void *, int *);
typedef void (*CuteQBar3DSeriesPrivateCall3)(const void *, QQuickGraphsItem *, int *);
class CuteQBar3DSeriesPrivate : public QBar3DSeriesPrivate {
public:
  using QBar3DSeriesPrivate::QBar3DSeriesPrivate;
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

  //  void QBar3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
  void setDataProxy(QAbstractDataProxy *proxy) override {
    if (taken[0]) {
      int handled = 0;
      CuteQBar3DSeriesPrivateCall0 call = reinterpret_cast<CuteQBar3DSeriesPrivateCall0>(taken[0]);
      call(this, proxy, &handled);
      if (handled) return;
    }
    QBar3DSeriesPrivate::setDataProxy(proxy);
  }

  //  void QBar3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem
  //      *newGraph)
  void connectGraphAndProxy(QQuickGraphsItem *newGraph) override {
    if (taken[1]) {
      int handled = 0;
      CuteQBar3DSeriesPrivateCall1 call = reinterpret_cast<CuteQBar3DSeriesPrivateCall1>(taken[1]);
      call(this, newGraph, &handled);
      if (handled) return;
    }
    QBar3DSeriesPrivate::connectGraphAndProxy(newGraph);
  }

  //  void QBar3DSeriesPrivate::createItemLabel()
  void createItemLabel() override {
    if (taken[2]) {
      int handled = 0;
      CuteQBar3DSeriesPrivateCall2 call = reinterpret_cast<CuteQBar3DSeriesPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QBar3DSeriesPrivate::createItemLabel();
  }

  //  void QAbstract3DSeriesPrivate::setGraph(QQuickGraphsItem *graph)
  void setGraph(QQuickGraphsItem *graph) override {
    if (taken[3]) {
      int handled = 0;
      CuteQBar3DSeriesPrivateCall3 call = reinterpret_cast<CuteQBar3DSeriesPrivateCall3>(taken[3]);
      call(this, graph, &handled);
      if (handled) return;
    }
    QAbstract3DSeriesPrivate::setGraph(graph);
  }
};

//  QBar3DSeries *QBar3DSeriesPrivate::q_func()
extern "C" Q_DECL_EXPORT
QBar3DSeries *ritual_ZN19QBar3DSeriesPrivate6q_funcEv(
    QBar3DSeriesPrivate *self) {
  return self->q_func();
}

//  const QBar3DSeries *QBar3DSeriesPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QBar3DSeries *ritual_ZNK19QBar3DSeriesPrivate6q_funcEv(
    const QBar3DSeriesPrivate *self) {
  return self->q_func();
}

//  QBar3DSeriesPrivate *QBar3DSeriesPrivate::get(QBar3DSeries *item)
extern "C" Q_DECL_EXPORT
QBar3DSeriesPrivate *ritual_ZN19QBar3DSeriesPrivate3getEP12QBar3DSeries(
    QBar3DSeries *item) {
  return QBar3DSeriesPrivate::get(item);
}

//  QBar3DSeriesPrivate::QBar3DSeriesPrivate()
extern "C" Q_DECL_EXPORT
QBar3DSeriesPrivate *ritual_ZN19QBar3DSeriesPrivateC1Ev() {
  return new CuteQBar3DSeriesPrivate();
}

//  QBar3DSeriesPrivate::~QBar3DSeriesPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivateD1Ev(QBar3DSeriesPrivate *self) {
  delete self;
}

//  void QBar3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy(
    QBar3DSeriesPrivate *self,
    QAbstractDataProxy *proxy) {
  self->setDataProxy(proxy);
}

//  void QBar3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem
//      *newGraph)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate20connectGraphAndProxyEP16QQuickGraphsItem(
    QBar3DSeriesPrivate *self,
    QQuickGraphsItem *newGraph) {
  self->connectGraphAndProxy(newGraph);
}

//  void QBar3DSeriesPrivate::createItemLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate15createItemLabelEv(
    QBar3DSeriesPrivate *self) {
  self->createItemLabel();
}

//  void QBar3DSeriesPrivate::setSelectedBar(QPoint position)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate14setSelectedBarE6QPoint(
    QBar3DSeriesPrivate *self,
    const QPoint *position) {
  self->setSelectedBar(*position);
}

//  void QBar3DSeriesPrivate::setRowColors(const QList<QColor> &colors)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate12setRowColorsERK5QListI6QColorE(
    QBar3DSeriesPrivate *self,
    const QList<QColor> *colors) {
  self->setRowColors(*colors);
}

//  void QBar3DSeriesPrivate::setValueColoringEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate23setValueColoringEnabledEb(
    QBar3DSeriesPrivate *self,
    bool enabled) {
  self->setValueColoringEnabled(enabled);
}

//  void QBar3DSeriesPrivate::setDataArray(const QBarDataArray &newDataArray)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate12setDataArrayERK5QListIS0_I12QBarDataItemEE(
    QBar3DSeriesPrivate *self,
    const QBarDataArray *newDataArray) {
  self->setDataArray(*newDataArray);
}

//  void QBar3DSeriesPrivate::clearRow(qsizetype rowIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate8clearRowEx(
    QBar3DSeriesPrivate *self,
    qsizetype rowIndex) {
  self->clearRow(rowIndex);
}

//  void QBar3DSeriesPrivate::clearArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate10clearArrayEv(
    QBar3DSeriesPrivate *self) {
  self->clearArray();
}

//  void QBar3DSeriesPrivate::setRowLabels(const QStringList &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate12setRowLabelsERK5QListI7QStringE(
    QBar3DSeriesPrivate *self,
    const QList<QString> *labels) {
  self->setRowLabels(*labels);
}

//  void QBar3DSeriesPrivate::setColumnLabels(const QStringList &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate15setColumnLabelsERK5QListI7QStringE(
    QBar3DSeriesPrivate *self,
    const QList<QString> *labels) {
  self->setColumnLabels(*labels);
}

//  void QBar3DSeriesPrivate::setCustomRowLabels(const QStringList &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate18setCustomRowLabelsERK5QListI7QStringE(
    QBar3DSeriesPrivate *self,
    const QList<QString> *labels) {
  self->setCustomRowLabels(*labels);
}

//  void QBar3DSeriesPrivate::setCustomColumnLabels(const QStringList
//      &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate21setCustomColumnLabelsERK5QListI7QStringE(
    QBar3DSeriesPrivate *self,
    const QList<QString> *labels) {
  self->setCustomColumnLabels(*labels);
}

//  void QBar3DSeriesPrivate::fixRowLabels(qsizetype startIndex, qsizetype
//      count, const QStringList &newLabels, bool isInsert)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate12fixRowLabelsExxRK5QListI7QStringEb(
    QBar3DSeriesPrivate *self,
    qsizetype startIndex,
    qsizetype count,
    const QList<QString> *newLabels,
    bool isInsert) {
  self->fixRowLabels(startIndex, count, *newLabels, isInsert);
}

//  void QBar3DSeriesPrivate::setRowAxis(QCategory3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate10setRowAxisEP15QCategory3DAxis(
    QBar3DSeriesPrivate *self,
    QCategory3DAxis *axis) {
  self->setRowAxis(axis);
}

//  void QBar3DSeriesPrivate::setValueAxis(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate12setValueAxisEP12QValue3DAxis(
    QBar3DSeriesPrivate *self,
    QValue3DAxis *axis) {
  self->setValueAxis(axis);
}

//  void QBar3DSeriesPrivate::setColumnAxis(QCategory3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate13setColumnAxisEP15QCategory3DAxis(
    QBar3DSeriesPrivate *self,
    QCategory3DAxis *axis) {
  self->setColumnAxis(axis);
}

//  void QBar3DSeriesPrivate::resetRowAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate12resetRowAxisEv(
    QBar3DSeriesPrivate *self) {
  self->resetRowAxis();
}

//  void QBar3DSeriesPrivate::resetValueAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate14resetValueAxisEv(
    QBar3DSeriesPrivate *self) {
  self->resetValueAxis();
}

//  void QBar3DSeriesPrivate::resetColumnAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBar3DSeriesPrivate15resetColumnAxisEv(
    QBar3DSeriesPrivate *self) {
  self->resetColumnAxis();
}

//  a Python function taken by a CuteQBar3DSeriesPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBar3DSeriesPrivate(
    QBar3DSeriesPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBar3DSeriesPrivate *>(self)->take(key, call);
}

//  void QBar3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBar3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy(
    QBar3DSeriesPrivate *self,
    QAbstractDataProxy *proxy) {
  self->QBar3DSeriesPrivate::setDataProxy(proxy);
}

//  void QBar3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem
//      *newGraph)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBar3DSeriesPrivate20connectGraphAndProxyEP16QQuickGraphsItem(
    QBar3DSeriesPrivate *self,
    QQuickGraphsItem *newGraph) {
  self->QBar3DSeriesPrivate::connectGraphAndProxy(newGraph);
}

//  void QBar3DSeriesPrivate::createItemLabel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QBar3DSeriesPrivate15createItemLabelEv(
    QBar3DSeriesPrivate *self) {
  self->QBar3DSeriesPrivate::createItemLabel();
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
