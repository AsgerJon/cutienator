//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qitemmodelbardataproxy_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qitemmodelbardataproxy.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qitemmodelbardataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/private/baritemmodelhandler_p.h>
#include <QtGraphs/private/qbar3dseries_p.h>
#include <QtGraphs/private/qbar3dseries_p.h>
#include <QtGraphs/private/qbardataproxy_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#include <QtGraphs/private/baritemmodelhandler_p.h>
#include <QtGraphs/private/qitemmodelbardataproxy_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#include <QtGraphs/private/abstractitemmodelhandler_p.h>
#include <QtGraphs/private/qabstract3dseries_p.h>
#include <QtGraphs/private/qabstractdataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs3d/data/baritemmodelhandler.cpp, line 30, as _ZN19BarItemModelHandlerC1EP22QItemModelBarDataProxyP7QObject
inline BarItemModelHandler::BarItemModelHandler(QItemModelBarDataProxy *proxy, QObject *parent)
    : AbstractItemModelHandler(parent)
    , m_proxy(proxy)
    , m_proxyArray(0)
    , m_columnCount(0)
    , m_valueRole(noRoleIndex)
    , m_rotationRole(noRoleIndex)
    , m_haveValuePattern(false)
    , m_haveRotationPattern(false)
{}

//  from ../qtgraphs/src/graphs3d/data/qbardataproxy.cpp, line 698, as _ZN20QBarDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QBarDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    Q_Q(QBarDataProxy);
    QAbstractDataProxyPrivate::setSeries(series);
    QBar3DSeries *barSeries = static_cast<QBar3DSeries *>(series);
    emit q->seriesChanged(barSeries);
}

//  from ../qtgraphs/src/graphs3d/data/qbardataproxy.cpp, line 545, as _ZN20QBarDataProxyPrivateC2Ev
inline QBarDataProxyPrivate::QBarDataProxyPrivate()
    : QAbstractDataProxyPrivate(QAbstractDataProxy::DataType::Bar)
{}

//  from ../qtgraphs/src/graphs3d/data/qbardataproxy.cpp, line 549, as _ZN20QBarDataProxyPrivateD2Ev
inline QBarDataProxyPrivate::~QBarDataProxyPrivate() {}

//  from ../qtgraphs/src/graphs3d/data/qitemmodelbardataproxy.cpp, line 1093, as _ZN29QItemModelBarDataProxyPrivateD2Ev
inline QItemModelBarDataProxyPrivate::~QItemModelBarDataProxyPrivate()
{
    delete m_itemModelHandler;
}

//  from ../qtgraphs/src/graphs3d/data/abstractitemmodelhandler.cpp, line 10, as _ZN24AbstractItemModelHandlerC2EP7QObject
inline AbstractItemModelHandler::AbstractItemModelHandler(QObject *parent)
    : QObject(parent)
    , resolvePending(0)
    , m_fullReset(true)
{
    m_resolveTimer.setSingleShot(true);
    QObject::connect(&m_resolveTimer,
                     &QTimer::timeout,
                     this,
                     &AbstractItemModelHandler::handlePendingResolve);
}

//  from ../qtgraphs/src/graphs3d/data/abstractitemmodelhandler.cpp, line 22, as _ZN24AbstractItemModelHandlerD2Ev
inline AbstractItemModelHandler::~AbstractItemModelHandler() {}

//  from ../qtgraphs/src/graphs3d/data/qabstractdataproxy.cpp, line 89, as _ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QAbstractDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    Q_Q(QAbstractDataProxy);
    q->setParent(series);
    m_series = series;
}

//  from ../qtgraphs/src/graphs3d/data/qabstractdataproxy.cpp, line 82, as _ZN25QAbstractDataProxyPrivateC2EN18QAbstractDataProxy8DataTypeE
inline QAbstractDataProxyPrivate::QAbstractDataProxyPrivate(QAbstractDataProxy::DataType type)
    : m_type(type)
    , m_series(0)
{}

//  from ../qtgraphs/src/graphs3d/data/qabstractdataproxy.cpp, line 87, as _ZN25QAbstractDataProxyPrivateD2Ev
inline QAbstractDataProxyPrivate::~QAbstractDataProxyPrivate() {}
//  -----------------------------------------------------------------------

//  A QItemModelBarDataProxyPrivate that Python can take functions over in. Every QItemModelBarDataProxyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQItemModelBarDataProxyPrivateCall0)(const void *, QAbstract3DSeries *, int *);
class CuteQItemModelBarDataProxyPrivate : public QItemModelBarDataProxyPrivate {
public:
  using QItemModelBarDataProxyPrivate::QItemModelBarDataProxyPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QBarDataProxyPrivate::setSeries(QAbstract3DSeries *series)
  void setSeries(QAbstract3DSeries *series) override {
    if (taken[0]) {
      int handled = 0;
      CuteQItemModelBarDataProxyPrivateCall0 call = reinterpret_cast<CuteQItemModelBarDataProxyPrivateCall0>(taken[0]);
      call(this, series, &handled);
      if (handled) return;
    }
    QBarDataProxyPrivate::setSeries(series);
  }
};

//  QItemModelBarDataProxy *QItemModelBarDataProxyPrivate::q_func()
extern "C" Q_DECL_EXPORT
QItemModelBarDataProxy *ritual_ZN29QItemModelBarDataProxyPrivate6q_funcEv(
    QItemModelBarDataProxyPrivate *self) {
  return self->q_func();
}

//  const QItemModelBarDataProxy *QItemModelBarDataProxyPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QItemModelBarDataProxy *ritual_ZNK29QItemModelBarDataProxyPrivate6q_funcEv(
    const QItemModelBarDataProxyPrivate *self) {
  return self->q_func();
}

//  QItemModelBarDataProxyPrivate::~QItemModelBarDataProxyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QItemModelBarDataProxyPrivateD1Ev(
    QItemModelBarDataProxyPrivate *self) {
  delete self;
}

//  a Python function taken by a CuteQItemModelBarDataProxyPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QItemModelBarDataProxyPrivate(
    QItemModelBarDataProxyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQItemModelBarDataProxyPrivate *>(self)->take(key, call);
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
