//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qsurfacedataproxy_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qsurfacedataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/qsurfacedataitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/qabstractdataproxy_p.h>
#include <QtDataVisualization/private/qabstract3dseries_p.h>
#include <QtDataVisualization/private/qsurfacedataproxy_p.h>
#include <QtDataVisualization/private/qsurface3dseries_p.h>
#include <QtDataVisualization/private/qabstract3daxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/data/qabstractdataproxy.cpp, line 97, as _ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QAbstractDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    q_ptr->setParent(series);
    m_series = series;
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 442, as _ZN24QSurfaceDataProxyPrivate7setItemEiiRK16QSurfaceDataItem
inline void QSurfaceDataProxyPrivate::setItem(int rowIndex, int columnIndex, const QSurfaceDataItem &item)
{
    Q_ASSERT(rowIndex >= 0 && rowIndex < m_dataArray->size());
    QSurfaceDataRow &row = *(*m_dataArray)[rowIndex];
    Q_ASSERT(columnIndex < row.size());
    row[columnIndex] = item;
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 489, as _ZN24QSurfaceDataProxyPrivate10removeRowsEii
inline void QSurfaceDataProxyPrivate::removeRows(int rowIndex, int removeCount)
{
    Q_ASSERT(rowIndex >= 0);
    int maxRemoveCount = m_dataArray->size() - rowIndex;
    removeCount = qMin(removeCount, maxRemoveCount);
    for (int i = 0; i < removeCount; i++) {
        clearRow(rowIndex);
        m_dataArray->removeAt(rowIndex);
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 614, as _ZNK24QSurfaceDataProxyPrivate12isValidValueEfP15QAbstract3DAxis
inline bool QSurfaceDataProxyPrivate::isValidValue(float value, QAbstract3DAxis *axis) const
{
    return (value > 0.0f || (value == 0.0f && axis->d_ptr->allowZero())
            || (value < 0.0f && axis->d_ptr->allowNegatives()));
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 636, as _ZN24QSurfaceDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QSurfaceDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    QAbstractDataProxyPrivate::setSeries(series);
    QSurface3DSeries *surfaceSeries = static_cast<QSurface3DSeries *>(series);
    emit qptr()->seriesChanged(surfaceSeries);
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 500, as _ZN24QSurfaceDataProxyPrivate4qptrEv
inline QSurfaceDataProxy *QSurfaceDataProxyPrivate::qptr()
{
    return static_cast<QSurfaceDataProxy *>(q_ptr);
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 620, as _ZN24QSurfaceDataProxyPrivate8clearRowEi
inline void QSurfaceDataProxyPrivate::clearRow(int rowIndex)
{
    if (m_dataArray->at(rowIndex)) {
        delete m_dataArray->at(rowIndex);
        (*m_dataArray)[rowIndex] = 0;
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/qsurfacedataproxy.cpp, line 628, as _ZN24QSurfaceDataProxyPrivate10clearArrayEv
inline void QSurfaceDataProxyPrivate::clearArray()
{
    for (int i = 0; i < m_dataArray->size(); i++)
        clearRow(i);
    m_dataArray->clear();
    delete m_dataArray;
}
//  -----------------------------------------------------------------------

//  A QSurfaceDataProxyPrivate that Python can take functions over in. Every QSurfaceDataProxyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSurfaceDataProxyPrivateCall0)(const void *, QAbstract3DSeries *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSurfaceDataProxyPrivateCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSurfaceDataProxyPrivateCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurfaceDataProxyPrivateCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurfaceDataProxyPrivateCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurfaceDataProxyPrivateCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurfaceDataProxyPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurfaceDataProxyPrivateCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSurfaceDataProxyPrivate : public QSurfaceDataProxyPrivate {
public:
  using QSurfaceDataProxyPrivate::QSurfaceDataProxyPrivate;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QSurfaceDataProxyPrivate::setSeries(QAbstract3DSeries *series)
  void setSeries(QAbstract3DSeries *series) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSurfaceDataProxyPrivateCall0 call = reinterpret_cast<CuteQSurfaceDataProxyPrivateCall0>(taken[0]);
      call(this, series, &handled);
      if (handled) return;
    }
    QSurfaceDataProxyPrivate::setSeries(series);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSurfaceDataProxyPrivateCall1 call = reinterpret_cast<CuteQSurfaceDataProxyPrivateCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSurfaceDataProxyPrivateCall2 call = reinterpret_cast<CuteQSurfaceDataProxyPrivateCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSurfaceDataProxyPrivateCall3 call = reinterpret_cast<CuteQSurfaceDataProxyPrivateCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSurfaceDataProxyPrivateCall4 call = reinterpret_cast<CuteQSurfaceDataProxyPrivateCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSurfaceDataProxyPrivateCall5 call = reinterpret_cast<CuteQSurfaceDataProxyPrivateCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSurfaceDataProxyPrivateCall6 call = reinterpret_cast<CuteQSurfaceDataProxyPrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSurfaceDataProxyPrivateCall7 call = reinterpret_cast<CuteQSurfaceDataProxyPrivateCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSurfaceDataProxyPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QSurfaceDataProxyPrivate10metaObjectEv(
    const QSurfaceDataProxyPrivate *self) {
  return self->metaObject();
}

//  QSurfaceDataProxyPrivate::~QSurfaceDataProxyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivateD1Ev(
    QSurfaceDataProxyPrivate *self) {
  delete self;
}

//  void QSurfaceDataProxyPrivate::setItem(int rowIndex, int columnIndex,
//      const QSurfaceDataItem &item)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate7setItemEiiRK16QSurfaceDataItem(
    QSurfaceDataProxyPrivate *self,
    int rowIndex,
    int columnIndex,
    const QSurfaceDataItem *item) {
  self->setItem(rowIndex, columnIndex, *item);
}

//  void QSurfaceDataProxyPrivate::removeRows(int rowIndex, int removeCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate10removeRowsEii(
    QSurfaceDataProxyPrivate *self,
    int rowIndex,
    int removeCount) {
  self->removeRows(rowIndex, removeCount);
}

//  bool QSurfaceDataProxyPrivate::isValidValue(float value, QAbstract3DAxis
//      *axis) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QSurfaceDataProxyPrivate12isValidValueEfP15QAbstract3DAxis(
    const QSurfaceDataProxyPrivate *self,
    float value,
    QAbstract3DAxis *axis) {
  return self->isValidValue(value, axis);
}

//  void QSurfaceDataProxyPrivate::setSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate9setSeriesEP17QAbstract3DSeries(
    QSurfaceDataProxyPrivate *self,
    QAbstract3DSeries *series) {
  self->setSeries(series);
}

//  QSurfaceDataProxy *QSurfaceDataProxyPrivate::qptr()
extern "C" Q_DECL_EXPORT
QSurfaceDataProxy *ritual_ZN24QSurfaceDataProxyPrivate4qptrEv(
    QSurfaceDataProxyPrivate *self) {
  return self->qptr();
}

//  void QSurfaceDataProxyPrivate::clearRow(int rowIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate8clearRowEi(
    QSurfaceDataProxyPrivate *self,
    int rowIndex) {
  self->clearRow(rowIndex);
}

//  void QSurfaceDataProxyPrivate::clearArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate10clearArrayEv(
    QSurfaceDataProxyPrivate *self) {
  self->clearArray();
}

//  a Python function taken by a CuteQSurfaceDataProxyPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSurfaceDataProxyPrivate(
    QSurfaceDataProxyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSurfaceDataProxyPrivate *>(self)->take(key, call);
}

//  void QSurfaceDataProxyPrivate::setSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QSurfaceDataProxyPrivate9setSeriesEP17QAbstract3DSeries(
    QSurfaceDataProxyPrivate *self,
    QAbstract3DSeries *series) {
  self->QSurfaceDataProxyPrivate::setSeries(series);
}
