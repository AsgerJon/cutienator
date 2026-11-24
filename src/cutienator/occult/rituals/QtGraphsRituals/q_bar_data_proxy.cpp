//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qbardataproxy.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qbardataproxy.h>
#include <QtCore/qstring.h>
#include <QtGraphs/qbardataitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QBarDataProxy that Python can take functions over in. Every QBarDataProxy
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBarDataProxyCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBarDataProxyCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarDataProxyCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarDataProxyCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarDataProxyCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarDataProxyCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarDataProxyCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBarDataProxy : public QBarDataProxy {
public:
  using QBarDataProxy::QBarDataProxy;
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
      CuteQBarDataProxyCall0 call = reinterpret_cast<CuteQBarDataProxyCall0>(taken[0]);
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
      CuteQBarDataProxyCall1 call = reinterpret_cast<CuteQBarDataProxyCall1>(taken[1]);
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
      CuteQBarDataProxyCall2 call = reinterpret_cast<CuteQBarDataProxyCall2>(taken[2]);
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
      CuteQBarDataProxyCall3 call = reinterpret_cast<CuteQBarDataProxyCall3>(taken[3]);
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
      CuteQBarDataProxyCall4 call = reinterpret_cast<CuteQBarDataProxyCall4>(taken[4]);
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
      CuteQBarDataProxyCall5 call = reinterpret_cast<CuteQBarDataProxyCall5>(taken[5]);
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
      CuteQBarDataProxyCall6 call = reinterpret_cast<CuteQBarDataProxyCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBarDataProxy::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QBarDataProxy10metaObjectEv(
    const QBarDataProxy *self) {
  return self->metaObject();
}

//  QString QBarDataProxy::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QBarDataProxy2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBarDataProxy::tr(s, c, n));
}

//  void QBarDataProxy::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy24qt_qmlMarker_uncreatableEv(
    QBarDataProxy *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QBarDataProxy::QBarDataProxy(QObject *parent)
extern "C" Q_DECL_EXPORT
QBarDataProxy *ritual_ZN13QBarDataProxyC1EP7QObject(QObject *parent) {
  return new CuteQBarDataProxy(parent);
}

//  QBarDataProxy::~QBarDataProxy()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxyD1Ev(QBarDataProxy *self) {
  delete self;
}

//  QBar3DSeries *QBarDataProxy::series() const
extern "C" Q_DECL_EXPORT
QBar3DSeries *ritual_ZNK13QBarDataProxy6seriesEv(const QBarDataProxy *self) {
  return self->series();
}

//  qsizetype QBarDataProxy::rowCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QBarDataProxy8rowCountEv(const QBarDataProxy *self) {
  return self->rowCount();
}

//  qsizetype QBarDataProxy::colCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QBarDataProxy8colCountEv(const QBarDataProxy *self) {
  return self->colCount();
}

//  const QBarDataRow &QBarDataProxy::rowAt(qsizetype rowIndex) const
extern "C" Q_DECL_EXPORT
QList<QBarDataItem> *ritual_ZNK13QBarDataProxy5rowAtEx(
    const QBarDataProxy *self,
    qsizetype rowIndex) {
  return new QList<QBarDataItem>(self->rowAt(rowIndex));
}

//  const QBarDataItem &QBarDataProxy::itemAt(qsizetype rowIndex, qsizetype
//      columnIndex) const
extern "C" Q_DECL_EXPORT
QBarDataItem *ritual_ZNK13QBarDataProxy6itemAtExx(
    const QBarDataProxy *self,
    qsizetype rowIndex,
    qsizetype columnIndex) {
  return new QBarDataItem(self->itemAt(rowIndex, columnIndex));
}

//  const QBarDataItem &QBarDataProxy::itemAt(QPoint position) const
extern "C" Q_DECL_EXPORT
QBarDataItem *ritual_ZNK13QBarDataProxy6itemAtE6QPoint(
    const QBarDataProxy *self,
    const QPoint *position) {
  return new QBarDataItem(self->itemAt(*position));
}

//  void QBarDataProxy::resetArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy10resetArrayEv(QBarDataProxy *self) {
  self->resetArray();
}

//  void QBarDataProxy::setRow(qsizetype rowIndex, QBarDataRow row)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy6setRowEx5QListI12QBarDataItemE(
    QBarDataProxy *self,
    qsizetype rowIndex,
    const QList<QBarDataItem> *row) {
  self->setRow(rowIndex, *row);
}

//  void QBarDataProxy::setRow(qsizetype rowIndex, QBarDataRow row, QString
//      label)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy6setRowEx5QListI12QBarDataItemE7QString(
    QBarDataProxy *self,
    qsizetype rowIndex,
    const QList<QBarDataItem> *row,
    const QString *label) {
  self->setRow(rowIndex, *row, *label);
}

//  void QBarDataProxy::setItem(qsizetype rowIndex, qsizetype columnIndex,
//      QBarDataItem item)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy7setItemExx12QBarDataItem(
    QBarDataProxy *self,
    qsizetype rowIndex,
    qsizetype columnIndex,
    const QBarDataItem *item) {
  self->setItem(rowIndex, columnIndex, *item);
}

//  void QBarDataProxy::setItem(QPoint position, QBarDataItem item)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy7setItemE6QPoint12QBarDataItem(
    QBarDataProxy *self,
    const QPoint *position,
    const QBarDataItem *item) {
  self->setItem(*position, *item);
}

//  qsizetype QBarDataProxy::addRow(QBarDataRow row)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN13QBarDataProxy6addRowE5QListI12QBarDataItemE(
    QBarDataProxy *self,
    const QList<QBarDataItem> *row) {
  return self->addRow(*row);
}

//  qsizetype QBarDataProxy::addRow(QBarDataRow row, QString label)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN13QBarDataProxy6addRowE5QListI12QBarDataItemE7QString(
    QBarDataProxy *self,
    const QList<QBarDataItem> *row,
    const QString *label) {
  return self->addRow(*row, *label);
}

//  void QBarDataProxy::insertRow(qsizetype rowIndex, QBarDataRow row)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy9insertRowEx5QListI12QBarDataItemE(
    QBarDataProxy *self,
    qsizetype rowIndex,
    const QList<QBarDataItem> *row) {
  self->insertRow(rowIndex, *row);
}

//  void QBarDataProxy::insertRow(qsizetype rowIndex, QBarDataRow row,
//      QString label)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy9insertRowEx5QListI12QBarDataItemE7QString(
    QBarDataProxy *self,
    qsizetype rowIndex,
    const QList<QBarDataItem> *row,
    const QString *label) {
  self->insertRow(rowIndex, *row, *label);
}

//  void QBarDataProxy::removeRows(qsizetype rowIndex, qsizetype removeCount,
//      RemoveLabels removeLabels)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy10removeRowsExxNS_12RemoveLabelsE(
    QBarDataProxy *self,
    qsizetype rowIndex,
    qsizetype removeCount,
    QBarDataProxy::RemoveLabels removeLabels) {
  self->removeRows(rowIndex, removeCount, removeLabels);
}

//  a Python function taken by a CuteQBarDataProxy, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBarDataProxy(
    QBarDataProxy *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBarDataProxy *>(self)->take(key, call);
}

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
