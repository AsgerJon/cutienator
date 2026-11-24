//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/qscatterdataproxy.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtDataVisualization/qscatterdataproxy.h>
#include <QtCore/qstring.h>
#include <QtDataVisualization/qscatterdataitem.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QScatterDataProxy that Python can take functions over in. Every QScatterDataProxy
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScatterDataProxyCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScatterDataProxyCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatterDataProxyCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatterDataProxyCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatterDataProxyCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatterDataProxyCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatterDataProxyCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScatterDataProxy : public QScatterDataProxy {
public:
  using QScatterDataProxy::QScatterDataProxy;
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
      CuteQScatterDataProxyCall0 call = reinterpret_cast<CuteQScatterDataProxyCall0>(taken[0]);
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
      CuteQScatterDataProxyCall1 call = reinterpret_cast<CuteQScatterDataProxyCall1>(taken[1]);
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
      CuteQScatterDataProxyCall2 call = reinterpret_cast<CuteQScatterDataProxyCall2>(taken[2]);
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
      CuteQScatterDataProxyCall3 call = reinterpret_cast<CuteQScatterDataProxyCall3>(taken[3]);
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
      CuteQScatterDataProxyCall4 call = reinterpret_cast<CuteQScatterDataProxyCall4>(taken[4]);
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
      CuteQScatterDataProxyCall5 call = reinterpret_cast<CuteQScatterDataProxyCall5>(taken[5]);
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
      CuteQScatterDataProxyCall6 call = reinterpret_cast<CuteQScatterDataProxyCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScatterDataProxy::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QScatterDataProxy10metaObjectEv(
    const QScatterDataProxy *self) {
  return self->metaObject();
}

//  QString QScatterDataProxy::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QScatterDataProxy2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScatterDataProxy::tr(s, c, n));
}

//  QScatterDataProxy::QScatterDataProxy(QObject *parent)
extern "C" Q_DECL_EXPORT
QScatterDataProxy *ritual_ZN17QScatterDataProxyC1EP7QObject(
    QObject *parent) {
  return new CuteQScatterDataProxy(parent);
}

//  QScatterDataProxy::~QScatterDataProxy()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QScatterDataProxyD1Ev(QScatterDataProxy *self) {
  delete self;
}

//  QScatter3DSeries *QScatterDataProxy::series() const
extern "C" Q_DECL_EXPORT
QScatter3DSeries *ritual_ZNK17QScatterDataProxy6seriesEv(
    const QScatterDataProxy *self) {
  return self->series();
}

//  int QScatterDataProxy::itemCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QScatterDataProxy9itemCountEv(
    const QScatterDataProxy *self) {
  return self->itemCount();
}

//  const QScatterDataItem *QScatterDataProxy::itemAt(int index) const
extern "C" Q_DECL_EXPORT
const QScatterDataItem *ritual_ZNK17QScatterDataProxy6itemAtEi(
    const QScatterDataProxy *self,
    int index) {
  return self->itemAt(index);
}

//  void QScatterDataProxy::setItem(int index, const QScatterDataItem &item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QScatterDataProxy7setItemEiRK16QScatterDataItem(
    QScatterDataProxy *self,
    int index,
    const QScatterDataItem *item) {
  self->setItem(index, *item);
}

//  void QScatterDataProxy::setItems(int index, const QScatterDataArray
//      &items)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QScatterDataProxy8setItemsEiRK5QListI16QScatterDataItemE(
    QScatterDataProxy *self,
    int index,
    const QList<QScatterDataItem> *items) {
  self->setItems(index, *items);
}

//  int QScatterDataProxy::addItem(const QScatterDataItem &item)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QScatterDataProxy7addItemERK16QScatterDataItem(
    QScatterDataProxy *self,
    const QScatterDataItem *item) {
  return self->addItem(*item);
}

//  int QScatterDataProxy::addItems(const QScatterDataArray &items)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QScatterDataProxy8addItemsERK5QListI16QScatterDataItemE(
    QScatterDataProxy *self,
    const QList<QScatterDataItem> *items) {
  return self->addItems(*items);
}

//  void QScatterDataProxy::insertItem(int index, const QScatterDataItem
//      &item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QScatterDataProxy10insertItemEiRK16QScatterDataItem(
    QScatterDataProxy *self,
    int index,
    const QScatterDataItem *item) {
  self->insertItem(index, *item);
}

//  void QScatterDataProxy::insertItems(int index, const QScatterDataArray
//      &items)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QScatterDataProxy11insertItemsEiRK5QListI16QScatterDataItemE(
    QScatterDataProxy *self,
    int index,
    const QList<QScatterDataItem> *items) {
  self->insertItems(index, *items);
}

//  void QScatterDataProxy::removeItems(int index, int removeCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QScatterDataProxy11removeItemsEii(
    QScatterDataProxy *self,
    int index,
    int removeCount) {
  self->removeItems(index, removeCount);
}

//  QScatterDataProxy::QScatterDataProxy(QScatterDataProxyPrivate *d, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QScatterDataProxy *ritual_ZN17QScatterDataProxyC1EP24QScatterDataProxyPrivateP7QObject(
    QScatterDataProxyPrivate *d,
    QObject *parent) {
  return new CuteQScatterDataProxy(d, parent);
}

//  QScatterDataProxyPrivate *QScatterDataProxy::dptr()
extern "C" Q_DECL_EXPORT
QScatterDataProxyPrivate *ritual_ZN17QScatterDataProxy4dptrEv(
    QScatterDataProxy *self) {
  return self->dptr();
}

//  const QScatterDataProxyPrivate *QScatterDataProxy::dptrc() const
extern "C" Q_DECL_EXPORT
const QScatterDataProxyPrivate *ritual_ZNK17QScatterDataProxy5dptrcEv(
    const QScatterDataProxy *self) {
  return self->dptrc();
}

//  a Python function taken by a CuteQScatterDataProxy, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScatterDataProxy(
    QScatterDataProxy *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScatterDataProxy *>(self)->take(key, call);
}
