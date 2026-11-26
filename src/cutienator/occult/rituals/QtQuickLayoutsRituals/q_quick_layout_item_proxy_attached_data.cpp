//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutitemproxy_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutglobal_p.h>
#include <QtQuickLayouts/QtQuickLayouts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutitemproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickLayouts/private/qquicklayoutitemproxy_p.h>
#include <QtQuickLayouts/private/qquicklayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicklayouts/qquicklayoutitemproxy.cpp, line 518, as _ZNK33QQuickLayoutItemProxyAttachedData19getControllingProxyEv
inline QQuickLayoutItemProxy *QQuickLayoutItemProxyAttachedData::getControllingProxy() const
{
    return controllingProxy;
}

//  from ../qtdeclarative/src/quicklayouts/qquicklayoutitemproxy.cpp, line 527, as _ZN33QQuickLayoutItemProxyAttachedData10getProxiesEv
inline QQmlListProperty<QQuickLayoutItemProxy> QQuickLayoutItemProxyAttachedData::getProxies()
{
    using Type = QQuickLayoutItemProxy;
    using Property = QQmlListProperty<Type>;

    return Property(
        this, &proxies,
        [](Property *p) { return static_cast<QList<Type *> *>(p->data)->size(); },
        [](Property *p, qsizetype i) { return static_cast<QList<Type *> *>(p->data)->at(i); }
    );
}

//  from ../qtdeclarative/src/quicklayouts/qquicklayoutitemproxy.cpp, line 543, as _ZNK33QQuickLayoutItemProxyAttachedData15proxyHasControlEv
inline bool QQuickLayoutItemProxyAttachedData::proxyHasControl() const
{
    return controllingProxy != nullptr;
}
//  -----------------------------------------------------------------------

//  A QQuickLayoutItemProxyAttachedData that Python can take functions over in. Every QQuickLayoutItemProxyAttachedData
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLayoutItemProxyAttachedDataCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLayoutItemProxyAttachedDataCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLayoutItemProxyAttachedDataCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLayoutItemProxyAttachedDataCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLayoutItemProxyAttachedDataCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLayoutItemProxyAttachedDataCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLayoutItemProxyAttachedDataCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickLayoutItemProxyAttachedData : public QQuickLayoutItemProxyAttachedData {
public:
  using QQuickLayoutItemProxyAttachedData::QQuickLayoutItemProxyAttachedData;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyAttachedDataCall0 call = reinterpret_cast<CuteQQuickLayoutItemProxyAttachedDataCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyAttachedDataCall1 call = reinterpret_cast<CuteQQuickLayoutItemProxyAttachedDataCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyAttachedDataCall2 call = reinterpret_cast<CuteQQuickLayoutItemProxyAttachedDataCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyAttachedDataCall3 call = reinterpret_cast<CuteQQuickLayoutItemProxyAttachedDataCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyAttachedDataCall4 call = reinterpret_cast<CuteQQuickLayoutItemProxyAttachedDataCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyAttachedDataCall5 call = reinterpret_cast<CuteQQuickLayoutItemProxyAttachedDataCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickLayoutItemProxyAttachedDataCall6 call = reinterpret_cast<CuteQQuickLayoutItemProxyAttachedDataCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickLayoutItemProxyAttachedData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK33QQuickLayoutItemProxyAttachedData10metaObjectEv(
    const QQuickLayoutItemProxyAttachedData *self) {
  return self->metaObject();
}

//  void *QQuickLayoutItemProxyAttachedData::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN33QQuickLayoutItemProxyAttachedData11qt_metacastEPKc(
    QQuickLayoutItemProxyAttachedData *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickLayoutItemProxyAttachedData::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN33QQuickLayoutItemProxyAttachedData11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickLayoutItemProxyAttachedData *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQuickLayoutItemProxyAttachedData::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickLayoutItemProxyAttachedData22qt_qmlMarker_anonymousEv(
    QQuickLayoutItemProxyAttachedData *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickLayoutItemProxyAttachedData::~QQuickLayoutItemProxyAttachedData()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickLayoutItemProxyAttachedDataD1Ev(
    QQuickLayoutItemProxyAttachedData *self) {
  delete self;
}

//  QQuickLayoutItemProxy
//      *QQuickLayoutItemProxyAttachedData::getControllingProxy() const
extern "C" Q_DECL_EXPORT
QQuickLayoutItemProxy *ritual_ZNK33QQuickLayoutItemProxyAttachedData19getControllingProxyEv(
    const QQuickLayoutItemProxyAttachedData *self) {
  return self->getControllingProxy();
}

//  QQmlListProperty<QQuickLayoutItemProxy>
//      QQuickLayoutItemProxyAttachedData::getProxies()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuickLayoutItemProxy> *ritual_ZN33QQuickLayoutItemProxyAttachedData10getProxiesEv(
    QQuickLayoutItemProxyAttachedData *self) {
  return new QQmlListProperty<QQuickLayoutItemProxy>(self->getProxies());
}

//  bool QQuickLayoutItemProxyAttachedData::proxyHasControl() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK33QQuickLayoutItemProxyAttachedData15proxyHasControlEv(
    const QQuickLayoutItemProxyAttachedData *self) {
  return self->proxyHasControl();
}

//  void QQuickLayoutItemProxyAttachedData::controlTaken()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickLayoutItemProxyAttachedData12controlTakenEv(
    QQuickLayoutItemProxyAttachedData *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxyAttachedData")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "controlTaken()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "controlTaken()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxyAttachedData::controlReleased()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickLayoutItemProxyAttachedData15controlReleasedEv(
    QQuickLayoutItemProxyAttachedData *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxyAttachedData")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "controlReleased()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "controlReleased()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxyAttachedData::controllingProxyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickLayoutItemProxyAttachedData23controllingProxyChangedEv(
    QQuickLayoutItemProxyAttachedData *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxyAttachedData")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "controllingProxyChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "controllingProxyChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLayoutItemProxyAttachedData::proxiesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickLayoutItemProxyAttachedData14proxiesChangedEv(
    QQuickLayoutItemProxyAttachedData *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLayoutItemProxyAttachedData")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "proxiesChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "proxiesChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQQuickLayoutItemProxyAttachedData, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickLayoutItemProxyAttachedData(
    QQuickLayoutItemProxyAttachedData *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickLayoutItemProxyAttachedData *>(self)->take(key, call);
}

//  a QQmlListProperty<QQuickLayoutItemProxy> a ritual of
//      QQuickLayoutItemProxyAttachedData gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickLayoutItemProxyAttachedData__QQmlListProperty_QQuickLayoutItemProxy(
    QQmlListProperty<QQuickLayoutItemProxy> *self) {
  delete self;
}
