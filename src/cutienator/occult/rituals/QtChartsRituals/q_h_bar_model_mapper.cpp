//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qhbarmodelmapper.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qhbarmodelmapper.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QHBarModelMapper that Python can take functions over in. Every QHBarModelMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHBarModelMapperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHBarModelMapperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHBarModelMapperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHBarModelMapperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHBarModelMapperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHBarModelMapperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHBarModelMapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHBarModelMapper : public QHBarModelMapper {
public:
  using QHBarModelMapper::QHBarModelMapper;
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
      CuteQHBarModelMapperCall0 call = reinterpret_cast<CuteQHBarModelMapperCall0>(taken[0]);
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
      CuteQHBarModelMapperCall1 call = reinterpret_cast<CuteQHBarModelMapperCall1>(taken[1]);
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
      CuteQHBarModelMapperCall2 call = reinterpret_cast<CuteQHBarModelMapperCall2>(taken[2]);
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
      CuteQHBarModelMapperCall3 call = reinterpret_cast<CuteQHBarModelMapperCall3>(taken[3]);
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
      CuteQHBarModelMapperCall4 call = reinterpret_cast<CuteQHBarModelMapperCall4>(taken[4]);
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
      CuteQHBarModelMapperCall5 call = reinterpret_cast<CuteQHBarModelMapperCall5>(taken[5]);
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
      CuteQHBarModelMapperCall6 call = reinterpret_cast<CuteQHBarModelMapperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHBarModelMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QHBarModelMapper10metaObjectEv(
    const QHBarModelMapper *self) {
  return self->metaObject();
}

//  QString QHBarModelMapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QHBarModelMapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHBarModelMapper::tr(s, c, n));
}

//  QHBarModelMapper::QHBarModelMapper(QObject *parent)
extern "C" Q_DECL_EXPORT
QHBarModelMapper *ritual_ZN16QHBarModelMapperC1EP7QObject(QObject *parent) {
  return new CuteQHBarModelMapper(parent);
}

//  QAbstractItemModel *QHBarModelMapper::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK16QHBarModelMapper5modelEv(
    const QHBarModelMapper *self) {
  return self->model();
}

//  void QHBarModelMapper::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHBarModelMapper8setModelEP18QAbstractItemModel(
    QHBarModelMapper *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  QAbstractBarSeries *QHBarModelMapper::series() const
extern "C" Q_DECL_EXPORT
QAbstractBarSeries *ritual_ZNK16QHBarModelMapper6seriesEv(
    const QHBarModelMapper *self) {
  return self->series();
}

//  void QHBarModelMapper::setSeries(QAbstractBarSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHBarModelMapper9setSeriesEP18QAbstractBarSeries(
    QHBarModelMapper *self,
    QAbstractBarSeries *series) {
  self->setSeries(series);
}

//  int QHBarModelMapper::firstBarSetRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QHBarModelMapper14firstBarSetRowEv(
    const QHBarModelMapper *self) {
  return self->firstBarSetRow();
}

//  void QHBarModelMapper::setFirstBarSetRow(int firstBarSetRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHBarModelMapper17setFirstBarSetRowEi(
    QHBarModelMapper *self,
    int firstBarSetRow) {
  self->setFirstBarSetRow(firstBarSetRow);
}

//  int QHBarModelMapper::lastBarSetRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QHBarModelMapper13lastBarSetRowEv(
    const QHBarModelMapper *self) {
  return self->lastBarSetRow();
}

//  void QHBarModelMapper::setLastBarSetRow(int lastBarSetRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHBarModelMapper16setLastBarSetRowEi(
    QHBarModelMapper *self,
    int lastBarSetRow) {
  self->setLastBarSetRow(lastBarSetRow);
}

//  int QHBarModelMapper::firstColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QHBarModelMapper11firstColumnEv(
    const QHBarModelMapper *self) {
  return self->firstColumn();
}

//  void QHBarModelMapper::setFirstColumn(int firstColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHBarModelMapper14setFirstColumnEi(
    QHBarModelMapper *self,
    int firstColumn) {
  self->setFirstColumn(firstColumn);
}

//  int QHBarModelMapper::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QHBarModelMapper11columnCountEv(
    const QHBarModelMapper *self) {
  return self->columnCount();
}

//  void QHBarModelMapper::setColumnCount(int columnCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHBarModelMapper14setColumnCountEi(
    QHBarModelMapper *self,
    int columnCount) {
  self->setColumnCount(columnCount);
}

//  a Python function taken by a CuteQHBarModelMapper, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHBarModelMapper(
    QHBarModelMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHBarModelMapper *>(self)->take(key, call);
}
