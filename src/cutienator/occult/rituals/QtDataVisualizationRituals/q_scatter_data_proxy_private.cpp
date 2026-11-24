//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qscatterdataproxy_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qscatterdataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/qscatterdataitem.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qabstractdataproxy_p.h"
#include "qabstract3dseries_p.h"
#include "qscatterdataproxy_p.h"
#include "qscatter3dseries_p.h"
#include "qabstract3daxis_p.h"
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

//  from ../qtdatavis3d/src/datavisualization/data/qscatterdataproxy.cpp, line 305, as _ZN24QScatterDataProxyPrivate7setItemEiRK16QScatterDataItem
inline void QScatterDataProxyPrivate::setItem(int index, const QScatterDataItem &item)
{
    Q_ASSERT(index >= 0 && index < m_dataArray->size());
    (*m_dataArray)[index] = item;
}

//  from ../qtdatavis3d/src/datavisualization/data/qscatterdataproxy.cpp, line 311, as _ZN24QScatterDataProxyPrivate8setItemsEiRK5QListI16QScatterDataItemE
inline void QScatterDataProxyPrivate::setItems(int index, const QScatterDataArray &items)
{
    Q_ASSERT(index >= 0 && (index + items.size()) <= m_dataArray->size());
    for (int i = 0; i < items.size(); i++)
        (*m_dataArray)[index++] = items[i];
}

//  from ../qtdatavis3d/src/datavisualization/data/qscatterdataproxy.cpp, line 318, as _ZN24QScatterDataProxyPrivate7addItemERK16QScatterDataItem
inline int QScatterDataProxyPrivate::addItem(const QScatterDataItem &item)
{
    int currentSize = m_dataArray->size();
    m_dataArray->append(item);
    return currentSize;
}

//  from ../qtdatavis3d/src/datavisualization/data/qscatterdataproxy.cpp, line 325, as _ZN24QScatterDataProxyPrivate8addItemsERK5QListI16QScatterDataItemE
inline int QScatterDataProxyPrivate::addItems(const QScatterDataArray &items)
{
    int currentSize = m_dataArray->size();
    (*m_dataArray) += items;
    return currentSize;
}

//  from ../qtdatavis3d/src/datavisualization/data/qscatterdataproxy.cpp, line 332, as _ZN24QScatterDataProxyPrivate10insertItemEiRK16QScatterDataItem
inline void QScatterDataProxyPrivate::insertItem(int index, const QScatterDataItem &item)
{
    Q_ASSERT(index >= 0 && index <= m_dataArray->size());
    m_dataArray->insert(index, item);
}

//  from ../qtdatavis3d/src/datavisualization/data/qscatterdataproxy.cpp, line 338, as _ZN24QScatterDataProxyPrivate11insertItemsEiRK5QListI16QScatterDataItemE
inline void QScatterDataProxyPrivate::insertItems(int index, const QScatterDataArray &items)
{
    Q_ASSERT(index >= 0 && index <= m_dataArray->size());
    for (int i = 0; i < items.size(); i++)
        m_dataArray->insert(index++, items.at(i));
}

//  from ../qtdatavis3d/src/datavisualization/data/qscatterdataproxy.cpp, line 345, as _ZN24QScatterDataProxyPrivate11removeItemsEii
inline void QScatterDataProxyPrivate::removeItems(int index, int removeCount)
{
    Q_ASSERT(index >= 0);
    int maxRemoveCount = m_dataArray->size() - index;
    removeCount = qMin(removeCount, maxRemoveCount);
    m_dataArray->remove(index, removeCount);
}

//  from ../qtdatavis3d/src/datavisualization/data/qscatterdataproxy.cpp, line 408, as _ZNK24QScatterDataProxyPrivate12isValidValueEffP15QAbstract3DAxis
inline bool QScatterDataProxyPrivate::isValidValue(float axisValue, float value,
                                            QAbstract3DAxis *axis) const
{
    return (axisValue > value && (value > 0.0f
                                  || (value == 0.0f && axis->d_ptr->allowZero())
                                  || (value < 0.0f && axis->d_ptr->allowNegatives())));
}

//  from ../qtdatavis3d/src/datavisualization/data/qscatterdataproxy.cpp, line 416, as _ZN24QScatterDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QScatterDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    QAbstractDataProxyPrivate::setSeries(series);
    QScatter3DSeries *scatterSeries = static_cast<QScatter3DSeries *>(series);
    emit qptr()->seriesChanged(scatterSeries);
}

//  from ../qtdatavis3d/src/datavisualization/data/qscatterdataproxy.cpp, line 423, as _ZN24QScatterDataProxyPrivate4qptrEv
inline QScatterDataProxy *QScatterDataProxyPrivate::qptr()
{
    return static_cast<QScatterDataProxy *>(q_ptr);
}
//  -----------------------------------------------------------------------

//  A QScatterDataProxyPrivate that Python can take functions over in. Every QScatterDataProxyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQScatterDataProxyPrivateCall0)(const void *, QAbstract3DSeries *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScatterDataProxyPrivateCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScatterDataProxyPrivateCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatterDataProxyPrivateCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatterDataProxyPrivateCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatterDataProxyPrivateCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatterDataProxyPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatterDataProxyPrivateCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScatterDataProxyPrivate : public QScatterDataProxyPrivate {
public:
  using QScatterDataProxyPrivate::QScatterDataProxyPrivate;
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

  //  void QScatterDataProxyPrivate::setSeries(QAbstract3DSeries *series)
  void setSeries(QAbstract3DSeries *series) override {
    if (taken[0]) {
      int handled = 0;
      CuteQScatterDataProxyPrivateCall0 call = reinterpret_cast<CuteQScatterDataProxyPrivateCall0>(taken[0]);
      call(this, series, &handled);
      if (handled) return;
    }
    QScatterDataProxyPrivate::setSeries(series);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQScatterDataProxyPrivateCall1 call = reinterpret_cast<CuteQScatterDataProxyPrivateCall1>(taken[1]);
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
      CuteQScatterDataProxyPrivateCall2 call = reinterpret_cast<CuteQScatterDataProxyPrivateCall2>(taken[2]);
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
      CuteQScatterDataProxyPrivateCall3 call = reinterpret_cast<CuteQScatterDataProxyPrivateCall3>(taken[3]);
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
      CuteQScatterDataProxyPrivateCall4 call = reinterpret_cast<CuteQScatterDataProxyPrivateCall4>(taken[4]);
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
      CuteQScatterDataProxyPrivateCall5 call = reinterpret_cast<CuteQScatterDataProxyPrivateCall5>(taken[5]);
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
      CuteQScatterDataProxyPrivateCall6 call = reinterpret_cast<CuteQScatterDataProxyPrivateCall6>(taken[6]);
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
      CuteQScatterDataProxyPrivateCall7 call = reinterpret_cast<CuteQScatterDataProxyPrivateCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScatterDataProxyPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QScatterDataProxyPrivate10metaObjectEv(
    const QScatterDataProxyPrivate *self) {
  return self->metaObject();
}

//  QScatterDataProxyPrivate::~QScatterDataProxyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScatterDataProxyPrivateD1Ev(
    QScatterDataProxyPrivate *self) {
  delete self;
}

//  void QScatterDataProxyPrivate::setItem(int index, const QScatterDataItem
//      &item)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScatterDataProxyPrivate7setItemEiRK16QScatterDataItem(
    QScatterDataProxyPrivate *self,
    int index,
    const QScatterDataItem *item) {
  self->setItem(index, *item);
}

//  void QScatterDataProxyPrivate::setItems(int index, const
//      QScatterDataArray &items)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScatterDataProxyPrivate8setItemsEiRK5QListI16QScatterDataItemE(
    QScatterDataProxyPrivate *self,
    int index,
    const QList<QScatterDataItem> *items) {
  self->setItems(index, *items);
}

//  int QScatterDataProxyPrivate::addItem(const QScatterDataItem &item)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QScatterDataProxyPrivate7addItemERK16QScatterDataItem(
    QScatterDataProxyPrivate *self,
    const QScatterDataItem *item) {
  return self->addItem(*item);
}

//  int QScatterDataProxyPrivate::addItems(const QScatterDataArray &items)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QScatterDataProxyPrivate8addItemsERK5QListI16QScatterDataItemE(
    QScatterDataProxyPrivate *self,
    const QList<QScatterDataItem> *items) {
  return self->addItems(*items);
}

//  void QScatterDataProxyPrivate::insertItem(int index, const
//      QScatterDataItem &item)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScatterDataProxyPrivate10insertItemEiRK16QScatterDataItem(
    QScatterDataProxyPrivate *self,
    int index,
    const QScatterDataItem *item) {
  self->insertItem(index, *item);
}

//  void QScatterDataProxyPrivate::insertItems(int index, const
//      QScatterDataArray &items)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScatterDataProxyPrivate11insertItemsEiRK5QListI16QScatterDataItemE(
    QScatterDataProxyPrivate *self,
    int index,
    const QList<QScatterDataItem> *items) {
  self->insertItems(index, *items);
}

//  void QScatterDataProxyPrivate::removeItems(int index, int removeCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScatterDataProxyPrivate11removeItemsEii(
    QScatterDataProxyPrivate *self,
    int index,
    int removeCount) {
  self->removeItems(index, removeCount);
}

//  bool QScatterDataProxyPrivate::isValidValue(float axisValue, float value,
//      QAbstract3DAxis *axis) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QScatterDataProxyPrivate12isValidValueEffP15QAbstract3DAxis(
    const QScatterDataProxyPrivate *self,
    float axisValue,
    float value,
    QAbstract3DAxis *axis) {
  return self->isValidValue(axisValue, value, axis);
}

//  void QScatterDataProxyPrivate::setSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScatterDataProxyPrivate9setSeriesEP17QAbstract3DSeries(
    QScatterDataProxyPrivate *self,
    QAbstract3DSeries *series) {
  self->setSeries(series);
}

//  QScatterDataProxy *QScatterDataProxyPrivate::qptr()
extern "C" Q_DECL_EXPORT
QScatterDataProxy *ritual_ZN24QScatterDataProxyPrivate4qptrEv(
    QScatterDataProxyPrivate *self) {
  return self->qptr();
}

//  a Python function taken by a CuteQScatterDataProxyPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScatterDataProxyPrivate(
    QScatterDataProxyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScatterDataProxyPrivate *>(self)->take(key, call);
}

//  void QScatterDataProxyPrivate::setSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QScatterDataProxyPrivate9setSeriesEP17QAbstract3DSeries(
    QScatterDataProxyPrivate *self,
    QAbstract3DSeries *series) {
  self->QScatterDataProxyPrivate::setSeries(series);
}
