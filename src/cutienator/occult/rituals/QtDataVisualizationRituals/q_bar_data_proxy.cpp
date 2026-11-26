//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/qbardataproxy.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtDataVisualization/qbardataproxy.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtDataVisualization/qbardataitem.h>
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

//  void *QBarDataProxy::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QBarDataProxy11qt_metacastEPKc(
    QBarDataProxy *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QBarDataProxy::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QBarDataProxy11qt_metacallEN11QMetaObject4CallEiPPv(
    QBarDataProxy *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QBarDataProxy::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QBarDataProxy2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBarDataProxy::tr(s, c, n));
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

//  int QBarDataProxy::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QBarDataProxy8rowCountEv(const QBarDataProxy *self) {
  return self->rowCount();
}

//  QStringList QBarDataProxy::rowLabels() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK13QBarDataProxy9rowLabelsEv(
    const QBarDataProxy *self) {
  return new QList<QString>(self->rowLabels());
}

//  void QBarDataProxy::setRowLabels(const QStringList &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy12setRowLabelsERK5QListI7QStringE(
    QBarDataProxy *self,
    const QList<QString> *labels) {
  self->setRowLabels(*labels);
}

//  QStringList QBarDataProxy::columnLabels() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK13QBarDataProxy12columnLabelsEv(
    const QBarDataProxy *self) {
  return new QList<QString>(self->columnLabels());
}

//  void QBarDataProxy::setColumnLabels(const QStringList &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy15setColumnLabelsERK5QListI7QStringE(
    QBarDataProxy *self,
    const QList<QString> *labels) {
  self->setColumnLabels(*labels);
}

//  const QBarDataArray *QBarDataProxy::array() const
extern "C" Q_DECL_EXPORT
const QBarDataArray *ritual_ZNK13QBarDataProxy5arrayEv(
    const QBarDataProxy *self) {
  return self->array();
}

//  const QBarDataRow *QBarDataProxy::rowAt(int rowIndex) const
extern "C" Q_DECL_EXPORT
const QBarDataRow *ritual_ZNK13QBarDataProxy5rowAtEi(
    const QBarDataProxy *self,
    int rowIndex) {
  return self->rowAt(rowIndex);
}

//  const QBarDataItem *QBarDataProxy::itemAt(int rowIndex, int columnIndex)
//      const
extern "C" Q_DECL_EXPORT
const QBarDataItem *ritual_ZNK13QBarDataProxy6itemAtEii(
    const QBarDataProxy *self,
    int rowIndex,
    int columnIndex) {
  return self->itemAt(rowIndex, columnIndex);
}

//  const QBarDataItem *QBarDataProxy::itemAt(const QPoint &position) const
extern "C" Q_DECL_EXPORT
const QBarDataItem *ritual_ZNK13QBarDataProxy6itemAtERK6QPoint(
    const QBarDataProxy *self,
    const QPoint *position) {
  return self->itemAt(*position);
}

//  void QBarDataProxy::resetArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy10resetArrayEv(QBarDataProxy *self) {
  self->resetArray();
}

//  void QBarDataProxy::resetArray(QBarDataArray *newArray)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy10resetArrayEP5QListIPS0_I12QBarDataItemEE(
    QBarDataProxy *self,
    QBarDataArray *newArray) {
  self->resetArray(newArray);
}

//  void QBarDataProxy::resetArray(QBarDataArray *newArray, const QStringList
//      &rowLabels, const QStringList &columnLabels)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy10resetArrayEP5QListIPS0_I12QBarDataItemEERKS0_I7QStringES9_(
    QBarDataProxy *self,
    QBarDataArray *newArray,
    const QList<QString> *rowLabels,
    const QList<QString> *columnLabels) {
  self->resetArray(newArray, *rowLabels, *columnLabels);
}

//  void QBarDataProxy::setRow(int rowIndex, QBarDataRow *row)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy6setRowEiP5QListI12QBarDataItemE(
    QBarDataProxy *self,
    int rowIndex,
    QBarDataRow *row) {
  self->setRow(rowIndex, row);
}

//  void QBarDataProxy::setRow(int rowIndex, QBarDataRow *row, const QString
//      &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy6setRowEiP5QListI12QBarDataItemERK7QString(
    QBarDataProxy *self,
    int rowIndex,
    QBarDataRow *row,
    const QString *label) {
  self->setRow(rowIndex, row, *label);
}

//  void QBarDataProxy::setRows(int rowIndex, const QBarDataArray &rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy7setRowsEiRK5QListIPS0_I12QBarDataItemEE(
    QBarDataProxy *self,
    int rowIndex,
    const QBarDataArray *rows) {
  self->setRows(rowIndex, *rows);
}

//  void QBarDataProxy::setRows(int rowIndex, const QBarDataArray &rows,
//      const QStringList &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy7setRowsEiRK5QListIPS0_I12QBarDataItemEERKS0_I7QStringE(
    QBarDataProxy *self,
    int rowIndex,
    const QBarDataArray *rows,
    const QList<QString> *labels) {
  self->setRows(rowIndex, *rows, *labels);
}

//  void QBarDataProxy::setItem(int rowIndex, int columnIndex, const
//      QBarDataItem &item)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy7setItemEiiRK12QBarDataItem(
    QBarDataProxy *self,
    int rowIndex,
    int columnIndex,
    const QBarDataItem *item) {
  self->setItem(rowIndex, columnIndex, *item);
}

//  void QBarDataProxy::setItem(const QPoint &position, const QBarDataItem
//      &item)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy7setItemERK6QPointRK12QBarDataItem(
    QBarDataProxy *self,
    const QPoint *position,
    const QBarDataItem *item) {
  self->setItem(*position, *item);
}

//  int QBarDataProxy::addRow(QBarDataRow *row)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QBarDataProxy6addRowEP5QListI12QBarDataItemE(
    QBarDataProxy *self,
    QBarDataRow *row) {
  return self->addRow(row);
}

//  int QBarDataProxy::addRow(QBarDataRow *row, const QString &label)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QBarDataProxy6addRowEP5QListI12QBarDataItemERK7QString(
    QBarDataProxy *self,
    QBarDataRow *row,
    const QString *label) {
  return self->addRow(row, *label);
}

//  int QBarDataProxy::addRows(const QBarDataArray &rows)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QBarDataProxy7addRowsERK5QListIPS0_I12QBarDataItemEE(
    QBarDataProxy *self,
    const QBarDataArray *rows) {
  return self->addRows(*rows);
}

//  int QBarDataProxy::addRows(const QBarDataArray &rows, const QStringList
//      &labels)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QBarDataProxy7addRowsERK5QListIPS0_I12QBarDataItemEERKS0_I7QStringE(
    QBarDataProxy *self,
    const QBarDataArray *rows,
    const QList<QString> *labels) {
  return self->addRows(*rows, *labels);
}

//  void QBarDataProxy::insertRow(int rowIndex, QBarDataRow *row)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy9insertRowEiP5QListI12QBarDataItemE(
    QBarDataProxy *self,
    int rowIndex,
    QBarDataRow *row) {
  self->insertRow(rowIndex, row);
}

//  void QBarDataProxy::insertRow(int rowIndex, QBarDataRow *row, const
//      QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy9insertRowEiP5QListI12QBarDataItemERK7QString(
    QBarDataProxy *self,
    int rowIndex,
    QBarDataRow *row,
    const QString *label) {
  self->insertRow(rowIndex, row, *label);
}

//  void QBarDataProxy::insertRows(int rowIndex, const QBarDataArray &rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy10insertRowsEiRK5QListIPS0_I12QBarDataItemEE(
    QBarDataProxy *self,
    int rowIndex,
    const QBarDataArray *rows) {
  self->insertRows(rowIndex, *rows);
}

//  void QBarDataProxy::insertRows(int rowIndex, const QBarDataArray &rows,
//      const QStringList &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy10insertRowsEiRK5QListIPS0_I12QBarDataItemEERKS0_I7QStringE(
    QBarDataProxy *self,
    int rowIndex,
    const QBarDataArray *rows,
    const QList<QString> *labels) {
  self->insertRows(rowIndex, *rows, *labels);
}

//  void QBarDataProxy::removeRows(int rowIndex, int removeCount, bool
//      removeLabels)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy10removeRowsEiib(
    QBarDataProxy *self,
    int rowIndex,
    int removeCount,
    bool removeLabels) {
  self->removeRows(rowIndex, removeCount, removeLabels);
}

//  void QBarDataProxy::arrayReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy10arrayResetEv(QBarDataProxy *self) {
  self->arrayReset();
}

//  void QBarDataProxy::rowsAdded(int startIndex, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy9rowsAddedEii(
    QBarDataProxy *self,
    int startIndex,
    int count) {
  self->rowsAdded(startIndex, count);
}

//  void QBarDataProxy::rowsChanged(int startIndex, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy11rowsChangedEii(
    QBarDataProxy *self,
    int startIndex,
    int count) {
  self->rowsChanged(startIndex, count);
}

//  void QBarDataProxy::rowsRemoved(int startIndex, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy11rowsRemovedEii(
    QBarDataProxy *self,
    int startIndex,
    int count) {
  self->rowsRemoved(startIndex, count);
}

//  void QBarDataProxy::rowsInserted(int startIndex, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy12rowsInsertedEii(
    QBarDataProxy *self,
    int startIndex,
    int count) {
  self->rowsInserted(startIndex, count);
}

//  void QBarDataProxy::itemChanged(int rowIndex, int columnIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy11itemChangedEii(
    QBarDataProxy *self,
    int rowIndex,
    int columnIndex) {
  self->itemChanged(rowIndex, columnIndex);
}

//  void QBarDataProxy::rowCountChanged(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy15rowCountChangedEi(
    QBarDataProxy *self,
    int count) {
  self->rowCountChanged(count);
}

//  void QBarDataProxy::rowLabelsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy16rowLabelsChangedEv(QBarDataProxy *self) {
  self->rowLabelsChanged();
}

//  void QBarDataProxy::columnLabelsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy19columnLabelsChangedEv(QBarDataProxy *self) {
  self->columnLabelsChanged();
}

//  void QBarDataProxy::seriesChanged(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QBarDataProxy13seriesChangedEP12QBar3DSeries(
    QBarDataProxy *self,
    QBar3DSeries *series) {
  self->seriesChanged(series);
}

//  QBarDataProxy::QBarDataProxy(QBarDataProxyPrivate *d, QObject *parent)
extern "C" Q_DECL_EXPORT
QBarDataProxy *ritual_ZN13QBarDataProxyC1EP20QBarDataProxyPrivateP7QObject(
    QBarDataProxyPrivate *d,
    QObject *parent) {
  return new CuteQBarDataProxy(d, parent);
}

//  QBarDataProxyPrivate *QBarDataProxy::dptr()
extern "C" Q_DECL_EXPORT
QBarDataProxyPrivate *ritual_ZN13QBarDataProxy4dptrEv(QBarDataProxy *self) {
  return self->dptr();
}

//  const QBarDataProxyPrivate *QBarDataProxy::dptrc() const
extern "C" Q_DECL_EXPORT
const QBarDataProxyPrivate *ritual_ZNK13QBarDataProxy5dptrcEv(
    const QBarDataProxy *self) {
  return self->dptrc();
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
