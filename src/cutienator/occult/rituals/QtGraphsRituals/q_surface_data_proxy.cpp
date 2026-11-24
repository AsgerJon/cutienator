//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qsurfacedataproxy.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qsurfacedataproxy.h>
#include <QtCore/qstring.h>
#include <QtGraphs/qsurfacedataitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QSurfaceDataProxy that Python can take functions over in. Every QSurfaceDataProxy
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSurfaceDataProxyCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSurfaceDataProxyCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurfaceDataProxyCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurfaceDataProxyCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurfaceDataProxyCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurfaceDataProxyCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurfaceDataProxyCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSurfaceDataProxy : public QSurfaceDataProxy {
public:
  using QSurfaceDataProxy::QSurfaceDataProxy;
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
      CuteQSurfaceDataProxyCall0 call = reinterpret_cast<CuteQSurfaceDataProxyCall0>(taken[0]);
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
      CuteQSurfaceDataProxyCall1 call = reinterpret_cast<CuteQSurfaceDataProxyCall1>(taken[1]);
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
      CuteQSurfaceDataProxyCall2 call = reinterpret_cast<CuteQSurfaceDataProxyCall2>(taken[2]);
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
      CuteQSurfaceDataProxyCall3 call = reinterpret_cast<CuteQSurfaceDataProxyCall3>(taken[3]);
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
      CuteQSurfaceDataProxyCall4 call = reinterpret_cast<CuteQSurfaceDataProxyCall4>(taken[4]);
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
      CuteQSurfaceDataProxyCall5 call = reinterpret_cast<CuteQSurfaceDataProxyCall5>(taken[5]);
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
      CuteQSurfaceDataProxyCall6 call = reinterpret_cast<CuteQSurfaceDataProxyCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSurfaceDataProxy::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QSurfaceDataProxy10metaObjectEv(
    const QSurfaceDataProxy *self) {
  return self->metaObject();
}

//  QString QSurfaceDataProxy::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QSurfaceDataProxy2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSurfaceDataProxy::tr(s, c, n));
}

//  void QSurfaceDataProxy::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy24qt_qmlMarker_uncreatableEv(
    QSurfaceDataProxy *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QSurfaceDataProxy::QSurfaceDataProxy(QObject *parent)
extern "C" Q_DECL_EXPORT
QSurfaceDataProxy *ritual_ZN17QSurfaceDataProxyC1EP7QObject(
    QObject *parent) {
  return new CuteQSurfaceDataProxy(parent);
}

//  QSurfaceDataProxy::~QSurfaceDataProxy()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxyD1Ev(QSurfaceDataProxy *self) {
  delete self;
}

//  QSurface3DSeries *QSurfaceDataProxy::series() const
extern "C" Q_DECL_EXPORT
QSurface3DSeries *ritual_ZNK17QSurfaceDataProxy6seriesEv(
    const QSurfaceDataProxy *self) {
  return self->series();
}

//  qsizetype QSurfaceDataProxy::rowCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK17QSurfaceDataProxy8rowCountEv(
    const QSurfaceDataProxy *self) {
  return self->rowCount();
}

//  qsizetype QSurfaceDataProxy::columnCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK17QSurfaceDataProxy11columnCountEv(
    const QSurfaceDataProxy *self) {
  return self->columnCount();
}

//  const QSurfaceDataItem &QSurfaceDataProxy::itemAt(qsizetype rowIndex,
//      qsizetype columnIndex) const
extern "C" Q_DECL_EXPORT
QSurfaceDataItem *ritual_ZNK17QSurfaceDataProxy6itemAtExx(
    const QSurfaceDataProxy *self,
    qsizetype rowIndex,
    qsizetype columnIndex) {
  return new QSurfaceDataItem(self->itemAt(rowIndex, columnIndex));
}

//  const QSurfaceDataItem &QSurfaceDataProxy::itemAt(QPoint position) const
extern "C" Q_DECL_EXPORT
QSurfaceDataItem *ritual_ZNK17QSurfaceDataProxy6itemAtE6QPoint(
    const QSurfaceDataProxy *self,
    const QPoint *position) {
  return new QSurfaceDataItem(self->itemAt(*position));
}

//  void QSurfaceDataProxy::resetArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy10resetArrayEv(QSurfaceDataProxy *self) {
  self->resetArray();
}

//  void QSurfaceDataProxy::setRow(qsizetype rowIndex, QSurfaceDataRow row)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy6setRowEx5QListI16QSurfaceDataItemE(
    QSurfaceDataProxy *self,
    qsizetype rowIndex,
    const QList<QSurfaceDataItem> *row) {
  self->setRow(rowIndex, *row);
}

//  void QSurfaceDataProxy::setItem(qsizetype rowIndex, qsizetype
//      columnIndex, QSurfaceDataItem item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy7setItemExx16QSurfaceDataItem(
    QSurfaceDataProxy *self,
    qsizetype rowIndex,
    qsizetype columnIndex,
    const QSurfaceDataItem *item) {
  self->setItem(rowIndex, columnIndex, *item);
}

//  void QSurfaceDataProxy::setItem(QPoint position, QSurfaceDataItem item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy7setItemE6QPoint16QSurfaceDataItem(
    QSurfaceDataProxy *self,
    const QPoint *position,
    const QSurfaceDataItem *item) {
  self->setItem(*position, *item);
}

//  qsizetype QSurfaceDataProxy::addRow(QSurfaceDataRow row)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN17QSurfaceDataProxy6addRowE5QListI16QSurfaceDataItemE(
    QSurfaceDataProxy *self,
    const QList<QSurfaceDataItem> *row) {
  return self->addRow(*row);
}

//  void QSurfaceDataProxy::insertRow(qsizetype rowIndex, QSurfaceDataRow
//      row)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy9insertRowEx5QListI16QSurfaceDataItemE(
    QSurfaceDataProxy *self,
    qsizetype rowIndex,
    const QList<QSurfaceDataItem> *row) {
  self->insertRow(rowIndex, *row);
}

//  void QSurfaceDataProxy::removeRows(qsizetype rowIndex, qsizetype
//      removeCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy10removeRowsExx(
    QSurfaceDataProxy *self,
    qsizetype rowIndex,
    qsizetype removeCount) {
  self->removeRows(rowIndex, removeCount);
}

//  a Python function taken by a CuteQSurfaceDataProxy, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSurfaceDataProxy(
    QSurfaceDataProxy *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSurfaceDataProxy *>(self)->take(key, call);
}

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
