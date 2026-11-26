//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/qsurfacedataproxy.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtDataVisualization/qsurfacedataproxy.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtDataVisualization/qsurfacedataitem.h>
#include <QtCore/qmetaobject.h>
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

//  void *QSurfaceDataProxy::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QSurfaceDataProxy11qt_metacastEPKc(
    QSurfaceDataProxy *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSurfaceDataProxy::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QSurfaceDataProxy11qt_metacallEN11QMetaObject4CallEiPPv(
    QSurfaceDataProxy *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSurfaceDataProxy::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QSurfaceDataProxy2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSurfaceDataProxy::tr(s, c, n));
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

//  int QSurfaceDataProxy::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QSurfaceDataProxy8rowCountEv(const QSurfaceDataProxy *self) {
  return self->rowCount();
}

//  int QSurfaceDataProxy::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QSurfaceDataProxy11columnCountEv(
    const QSurfaceDataProxy *self) {
  return self->columnCount();
}

//  const QSurfaceDataArray *QSurfaceDataProxy::array() const
extern "C" Q_DECL_EXPORT
const QSurfaceDataArray *ritual_ZNK17QSurfaceDataProxy5arrayEv(
    const QSurfaceDataProxy *self) {
  return self->array();
}

//  const QSurfaceDataItem *QSurfaceDataProxy::itemAt(int rowIndex, int
//      columnIndex) const
extern "C" Q_DECL_EXPORT
const QSurfaceDataItem *ritual_ZNK17QSurfaceDataProxy6itemAtEii(
    const QSurfaceDataProxy *self,
    int rowIndex,
    int columnIndex) {
  return self->itemAt(rowIndex, columnIndex);
}

//  const QSurfaceDataItem *QSurfaceDataProxy::itemAt(const QPoint &position)
//      const
extern "C" Q_DECL_EXPORT
const QSurfaceDataItem *ritual_ZNK17QSurfaceDataProxy6itemAtERK6QPoint(
    const QSurfaceDataProxy *self,
    const QPoint *position) {
  return self->itemAt(*position);
}

//  void QSurfaceDataProxy::resetArray(QSurfaceDataArray *newArray)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy10resetArrayEP5QListIPS0_I16QSurfaceDataItemEE(
    QSurfaceDataProxy *self,
    QSurfaceDataArray *newArray) {
  self->resetArray(newArray);
}

//  void QSurfaceDataProxy::setRow(int rowIndex, QSurfaceDataRow *row)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy6setRowEiP5QListI16QSurfaceDataItemE(
    QSurfaceDataProxy *self,
    int rowIndex,
    QSurfaceDataRow *row) {
  self->setRow(rowIndex, row);
}

//  void QSurfaceDataProxy::setRows(int rowIndex, const QSurfaceDataArray
//      &rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy7setRowsEiRK5QListIPS0_I16QSurfaceDataItemEE(
    QSurfaceDataProxy *self,
    int rowIndex,
    const QSurfaceDataArray *rows) {
  self->setRows(rowIndex, *rows);
}

//  void QSurfaceDataProxy::setItem(int rowIndex, int columnIndex, const
//      QSurfaceDataItem &item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy7setItemEiiRK16QSurfaceDataItem(
    QSurfaceDataProxy *self,
    int rowIndex,
    int columnIndex,
    const QSurfaceDataItem *item) {
  self->setItem(rowIndex, columnIndex, *item);
}

//  void QSurfaceDataProxy::setItem(const QPoint &position, const
//      QSurfaceDataItem &item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy7setItemERK6QPointRK16QSurfaceDataItem(
    QSurfaceDataProxy *self,
    const QPoint *position,
    const QSurfaceDataItem *item) {
  self->setItem(*position, *item);
}

//  int QSurfaceDataProxy::addRow(QSurfaceDataRow *row)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QSurfaceDataProxy6addRowEP5QListI16QSurfaceDataItemE(
    QSurfaceDataProxy *self,
    QSurfaceDataRow *row) {
  return self->addRow(row);
}

//  int QSurfaceDataProxy::addRows(const QSurfaceDataArray &rows)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QSurfaceDataProxy7addRowsERK5QListIPS0_I16QSurfaceDataItemEE(
    QSurfaceDataProxy *self,
    const QSurfaceDataArray *rows) {
  return self->addRows(*rows);
}

//  void QSurfaceDataProxy::insertRow(int rowIndex, QSurfaceDataRow *row)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy9insertRowEiP5QListI16QSurfaceDataItemE(
    QSurfaceDataProxy *self,
    int rowIndex,
    QSurfaceDataRow *row) {
  self->insertRow(rowIndex, row);
}

//  void QSurfaceDataProxy::insertRows(int rowIndex, const QSurfaceDataArray
//      &rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy10insertRowsEiRK5QListIPS0_I16QSurfaceDataItemEE(
    QSurfaceDataProxy *self,
    int rowIndex,
    const QSurfaceDataArray *rows) {
  self->insertRows(rowIndex, *rows);
}

//  void QSurfaceDataProxy::removeRows(int rowIndex, int removeCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy10removeRowsEii(
    QSurfaceDataProxy *self,
    int rowIndex,
    int removeCount) {
  self->removeRows(rowIndex, removeCount);
}

//  void QSurfaceDataProxy::arrayReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy10arrayResetEv(QSurfaceDataProxy *self) {
  self->arrayReset();
}

//  void QSurfaceDataProxy::rowsAdded(int startIndex, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy9rowsAddedEii(
    QSurfaceDataProxy *self,
    int startIndex,
    int count) {
  self->rowsAdded(startIndex, count);
}

//  void QSurfaceDataProxy::rowsChanged(int startIndex, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy11rowsChangedEii(
    QSurfaceDataProxy *self,
    int startIndex,
    int count) {
  self->rowsChanged(startIndex, count);
}

//  void QSurfaceDataProxy::rowsRemoved(int startIndex, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy11rowsRemovedEii(
    QSurfaceDataProxy *self,
    int startIndex,
    int count) {
  self->rowsRemoved(startIndex, count);
}

//  void QSurfaceDataProxy::rowsInserted(int startIndex, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy12rowsInsertedEii(
    QSurfaceDataProxy *self,
    int startIndex,
    int count) {
  self->rowsInserted(startIndex, count);
}

//  void QSurfaceDataProxy::itemChanged(int rowIndex, int columnIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy11itemChangedEii(
    QSurfaceDataProxy *self,
    int rowIndex,
    int columnIndex) {
  self->itemChanged(rowIndex, columnIndex);
}

//  void QSurfaceDataProxy::rowCountChanged(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy15rowCountChangedEi(
    QSurfaceDataProxy *self,
    int count) {
  self->rowCountChanged(count);
}

//  void QSurfaceDataProxy::columnCountChanged(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy18columnCountChangedEi(
    QSurfaceDataProxy *self,
    int count) {
  self->columnCountChanged(count);
}

//  void QSurfaceDataProxy::seriesChanged(QSurface3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSurfaceDataProxy13seriesChangedEP16QSurface3DSeries(
    QSurfaceDataProxy *self,
    QSurface3DSeries *series) {
  self->seriesChanged(series);
}

//  QSurfaceDataProxy::QSurfaceDataProxy(QSurfaceDataProxyPrivate *d, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QSurfaceDataProxy *ritual_ZN17QSurfaceDataProxyC1EP24QSurfaceDataProxyPrivateP7QObject(
    QSurfaceDataProxyPrivate *d,
    QObject *parent) {
  return new CuteQSurfaceDataProxy(d, parent);
}

//  QSurfaceDataProxyPrivate *QSurfaceDataProxy::dptr()
extern "C" Q_DECL_EXPORT
QSurfaceDataProxyPrivate *ritual_ZN17QSurfaceDataProxy4dptrEv(
    QSurfaceDataProxy *self) {
  return self->dptr();
}

//  const QSurfaceDataProxyPrivate *QSurfaceDataProxy::dptrc() const
extern "C" Q_DECL_EXPORT
const QSurfaceDataProxyPrivate *ritual_ZNK17QSurfaceDataProxy5dptrcEv(
    const QSurfaceDataProxy *self) {
  return self->dptrc();
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
