//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qabstractdataproxy_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qabstractdataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/qabstractdataproxy_p.h>
#include <QtDataVisualization/private/qabstract3dseries_p.h>
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
//  -----------------------------------------------------------------------

//  A QAbstractDataProxyPrivate that Python can take functions over in. Every QAbstractDataProxyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractDataProxyPrivateCall0)(const void *, QAbstract3DSeries *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractDataProxyPrivateCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractDataProxyPrivateCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractDataProxyPrivateCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractDataProxyPrivateCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractDataProxyPrivateCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractDataProxyPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractDataProxyPrivateCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractDataProxyPrivate : public QAbstractDataProxyPrivate {
public:
  using QAbstractDataProxyPrivate::QAbstractDataProxyPrivate;
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

  //  void QAbstractDataProxyPrivate::setSeries(QAbstract3DSeries *series)
  void setSeries(QAbstract3DSeries *series) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractDataProxyPrivateCall0 call = reinterpret_cast<CuteQAbstractDataProxyPrivateCall0>(taken[0]);
      call(this, series, &handled);
      if (handled) return;
    }
    QAbstractDataProxyPrivate::setSeries(series);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractDataProxyPrivateCall1 call = reinterpret_cast<CuteQAbstractDataProxyPrivateCall1>(taken[1]);
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
      CuteQAbstractDataProxyPrivateCall2 call = reinterpret_cast<CuteQAbstractDataProxyPrivateCall2>(taken[2]);
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
      CuteQAbstractDataProxyPrivateCall3 call = reinterpret_cast<CuteQAbstractDataProxyPrivateCall3>(taken[3]);
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
      CuteQAbstractDataProxyPrivateCall4 call = reinterpret_cast<CuteQAbstractDataProxyPrivateCall4>(taken[4]);
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
      CuteQAbstractDataProxyPrivateCall5 call = reinterpret_cast<CuteQAbstractDataProxyPrivateCall5>(taken[5]);
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
      CuteQAbstractDataProxyPrivateCall6 call = reinterpret_cast<CuteQAbstractDataProxyPrivateCall6>(taken[6]);
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
      CuteQAbstractDataProxyPrivateCall7 call = reinterpret_cast<CuteQAbstractDataProxyPrivateCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractDataProxyPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QAbstractDataProxyPrivate10metaObjectEv(
    const QAbstractDataProxyPrivate *self) {
  return self->metaObject();
}

//  void *QAbstractDataProxyPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QAbstractDataProxyPrivate11qt_metacastEPKc(
    QAbstractDataProxyPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractDataProxyPrivate::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QAbstractDataProxyPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractDataProxyPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QAbstractDataProxyPrivate::~QAbstractDataProxyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractDataProxyPrivateD1Ev(
    QAbstractDataProxyPrivate *self) {
  delete self;
}

//  QAbstract3DSeries *QAbstractDataProxyPrivate::series()
extern "C" Q_DECL_EXPORT
QAbstract3DSeries *ritual_ZN25QAbstractDataProxyPrivate6seriesEv(
    QAbstractDataProxyPrivate *self) {
  return self->series();
}

//  void QAbstractDataProxyPrivate::setSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries(
    QAbstractDataProxyPrivate *self,
    QAbstract3DSeries *series) {
  self->setSeries(series);
}

//  a Python function taken by a CuteQAbstractDataProxyPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractDataProxyPrivate(
    QAbstractDataProxyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractDataProxyPrivate *>(self)->take(key, call);
}

//  void QAbstractDataProxyPrivate::setSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries(
    QAbstractDataProxyPrivate *self,
    QAbstract3DSeries *series) {
  self->QAbstractDataProxyPrivate::setSeries(series);
}
