//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qitemmodelbardataproxy_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qitemmodelbardataproxy.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qitemmodelbardataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "baritemmodelhandler_p.h"
#include "qitemmodelbardataproxy_p.h"
#include "qgraphs3dlogging_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs3d/data/qitemmodelbardataproxy.cpp, line 1093, as _ZN29QItemModelBarDataProxyPrivateD1Ev
inline QItemModelBarDataProxyPrivate::~QItemModelBarDataProxyPrivate()
{
    delete m_itemModelHandler;
}
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

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
