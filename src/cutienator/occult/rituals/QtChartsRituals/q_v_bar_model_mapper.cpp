//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qvbarmodelmapper.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qvbarmodelmapper.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QVBarModelMapper that Python can take functions over in. Every QVBarModelMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVBarModelMapperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVBarModelMapperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVBarModelMapperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVBarModelMapperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVBarModelMapperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVBarModelMapperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVBarModelMapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQVBarModelMapper : public QVBarModelMapper {
public:
  using QVBarModelMapper::QVBarModelMapper;
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
      CuteQVBarModelMapperCall0 call = reinterpret_cast<CuteQVBarModelMapperCall0>(taken[0]);
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
      CuteQVBarModelMapperCall1 call = reinterpret_cast<CuteQVBarModelMapperCall1>(taken[1]);
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
      CuteQVBarModelMapperCall2 call = reinterpret_cast<CuteQVBarModelMapperCall2>(taken[2]);
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
      CuteQVBarModelMapperCall3 call = reinterpret_cast<CuteQVBarModelMapperCall3>(taken[3]);
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
      CuteQVBarModelMapperCall4 call = reinterpret_cast<CuteQVBarModelMapperCall4>(taken[4]);
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
      CuteQVBarModelMapperCall5 call = reinterpret_cast<CuteQVBarModelMapperCall5>(taken[5]);
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
      CuteQVBarModelMapperCall6 call = reinterpret_cast<CuteQVBarModelMapperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QVBarModelMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QVBarModelMapper10metaObjectEv(
    const QVBarModelMapper *self) {
  return self->metaObject();
}

//  QString QVBarModelMapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QVBarModelMapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVBarModelMapper::tr(s, c, n));
}

//  QVBarModelMapper::QVBarModelMapper(QObject *parent)
extern "C" Q_DECL_EXPORT
QVBarModelMapper *ritual_ZN16QVBarModelMapperC1EP7QObject(QObject *parent) {
  return new CuteQVBarModelMapper(parent);
}

//  QAbstractItemModel *QVBarModelMapper::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK16QVBarModelMapper5modelEv(
    const QVBarModelMapper *self) {
  return self->model();
}

//  void QVBarModelMapper::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVBarModelMapper8setModelEP18QAbstractItemModel(
    QVBarModelMapper *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  QAbstractBarSeries *QVBarModelMapper::series() const
extern "C" Q_DECL_EXPORT
QAbstractBarSeries *ritual_ZNK16QVBarModelMapper6seriesEv(
    const QVBarModelMapper *self) {
  return self->series();
}

//  void QVBarModelMapper::setSeries(QAbstractBarSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVBarModelMapper9setSeriesEP18QAbstractBarSeries(
    QVBarModelMapper *self,
    QAbstractBarSeries *series) {
  self->setSeries(series);
}

//  int QVBarModelMapper::firstBarSetColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QVBarModelMapper17firstBarSetColumnEv(
    const QVBarModelMapper *self) {
  return self->firstBarSetColumn();
}

//  void QVBarModelMapper::setFirstBarSetColumn(int firstBarSetColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVBarModelMapper20setFirstBarSetColumnEi(
    QVBarModelMapper *self,
    int firstBarSetColumn) {
  self->setFirstBarSetColumn(firstBarSetColumn);
}

//  int QVBarModelMapper::lastBarSetColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QVBarModelMapper16lastBarSetColumnEv(
    const QVBarModelMapper *self) {
  return self->lastBarSetColumn();
}

//  void QVBarModelMapper::setLastBarSetColumn(int lastBarSetColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVBarModelMapper19setLastBarSetColumnEi(
    QVBarModelMapper *self,
    int lastBarSetColumn) {
  self->setLastBarSetColumn(lastBarSetColumn);
}

//  int QVBarModelMapper::firstRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QVBarModelMapper8firstRowEv(const QVBarModelMapper *self) {
  return self->firstRow();
}

//  void QVBarModelMapper::setFirstRow(int firstRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVBarModelMapper11setFirstRowEi(
    QVBarModelMapper *self,
    int firstRow) {
  self->setFirstRow(firstRow);
}

//  int QVBarModelMapper::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QVBarModelMapper8rowCountEv(const QVBarModelMapper *self) {
  return self->rowCount();
}

//  void QVBarModelMapper::setRowCount(int rowCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVBarModelMapper11setRowCountEi(
    QVBarModelMapper *self,
    int rowCount) {
  self->setRowCount(rowCount);
}

//  a Python function taken by a CuteQVBarModelMapper, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVBarModelMapper(
    QVBarModelMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVBarModelMapper *>(self)->take(key, call);
}
