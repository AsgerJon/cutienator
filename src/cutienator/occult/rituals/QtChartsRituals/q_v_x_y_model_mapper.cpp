//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qvxymodelmapper.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qvxymodelmapper.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QVXYModelMapper that Python can take functions over in. Every QVXYModelMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVXYModelMapperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVXYModelMapperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVXYModelMapperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVXYModelMapperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVXYModelMapperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVXYModelMapperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVXYModelMapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQVXYModelMapper : public QVXYModelMapper {
public:
  using QVXYModelMapper::QVXYModelMapper;
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
      CuteQVXYModelMapperCall0 call = reinterpret_cast<CuteQVXYModelMapperCall0>(taken[0]);
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
      CuteQVXYModelMapperCall1 call = reinterpret_cast<CuteQVXYModelMapperCall1>(taken[1]);
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
      CuteQVXYModelMapperCall2 call = reinterpret_cast<CuteQVXYModelMapperCall2>(taken[2]);
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
      CuteQVXYModelMapperCall3 call = reinterpret_cast<CuteQVXYModelMapperCall3>(taken[3]);
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
      CuteQVXYModelMapperCall4 call = reinterpret_cast<CuteQVXYModelMapperCall4>(taken[4]);
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
      CuteQVXYModelMapperCall5 call = reinterpret_cast<CuteQVXYModelMapperCall5>(taken[5]);
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
      CuteQVXYModelMapperCall6 call = reinterpret_cast<CuteQVXYModelMapperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QVXYModelMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QVXYModelMapper10metaObjectEv(
    const QVXYModelMapper *self) {
  return self->metaObject();
}

//  void *QVXYModelMapper::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QVXYModelMapper11qt_metacastEPKc(
    QVXYModelMapper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QVXYModelMapper::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QVXYModelMapper11qt_metacallEN11QMetaObject4CallEiPPv(
    QVXYModelMapper *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QVXYModelMapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QVXYModelMapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVXYModelMapper::tr(s, c, n));
}

//  QVXYModelMapper::QVXYModelMapper(QObject *parent)
extern "C" Q_DECL_EXPORT
QVXYModelMapper *ritual_ZN15QVXYModelMapperC1EP7QObject(QObject *parent) {
  return new CuteQVXYModelMapper(parent);
}

//  QAbstractItemModel *QVXYModelMapper::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK15QVXYModelMapper5modelEv(
    const QVXYModelMapper *self) {
  return self->model();
}

//  void QVXYModelMapper::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVXYModelMapper8setModelEP18QAbstractItemModel(
    QVXYModelMapper *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  QXYSeries *QVXYModelMapper::series() const
extern "C" Q_DECL_EXPORT
QXYSeries *ritual_ZNK15QVXYModelMapper6seriesEv(
    const QVXYModelMapper *self) {
  return self->series();
}

//  void QVXYModelMapper::setSeries(QXYSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVXYModelMapper9setSeriesEP9QXYSeries(
    QVXYModelMapper *self,
    QXYSeries *series) {
  self->setSeries(series);
}

//  int QVXYModelMapper::xColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QVXYModelMapper7xColumnEv(const QVXYModelMapper *self) {
  return self->xColumn();
}

//  void QVXYModelMapper::setXColumn(int xColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVXYModelMapper10setXColumnEi(
    QVXYModelMapper *self,
    int xColumn) {
  self->setXColumn(xColumn);
}

//  int QVXYModelMapper::yColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QVXYModelMapper7yColumnEv(const QVXYModelMapper *self) {
  return self->yColumn();
}

//  void QVXYModelMapper::setYColumn(int yColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVXYModelMapper10setYColumnEi(
    QVXYModelMapper *self,
    int yColumn) {
  self->setYColumn(yColumn);
}

//  int QVXYModelMapper::firstRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QVXYModelMapper8firstRowEv(const QVXYModelMapper *self) {
  return self->firstRow();
}

//  void QVXYModelMapper::setFirstRow(int firstRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVXYModelMapper11setFirstRowEi(
    QVXYModelMapper *self,
    int firstRow) {
  self->setFirstRow(firstRow);
}

//  int QVXYModelMapper::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QVXYModelMapper8rowCountEv(const QVXYModelMapper *self) {
  return self->rowCount();
}

//  void QVXYModelMapper::setRowCount(int rowCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVXYModelMapper11setRowCountEi(
    QVXYModelMapper *self,
    int rowCount) {
  self->setRowCount(rowCount);
}

//  void QVXYModelMapper::seriesReplaced()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVXYModelMapper14seriesReplacedEv(QVXYModelMapper *self) {
  self->seriesReplaced();
}

//  void QVXYModelMapper::modelReplaced()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVXYModelMapper13modelReplacedEv(QVXYModelMapper *self) {
  self->modelReplaced();
}

//  void QVXYModelMapper::xColumnChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVXYModelMapper14xColumnChangedEv(QVXYModelMapper *self) {
  self->xColumnChanged();
}

//  void QVXYModelMapper::yColumnChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVXYModelMapper14yColumnChangedEv(QVXYModelMapper *self) {
  self->yColumnChanged();
}

//  void QVXYModelMapper::firstRowChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVXYModelMapper15firstRowChangedEv(QVXYModelMapper *self) {
  self->firstRowChanged();
}

//  void QVXYModelMapper::rowCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QVXYModelMapper15rowCountChangedEv(QVXYModelMapper *self) {
  self->rowCountChanged();
}

//  a Python function taken by a CuteQVXYModelMapper, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVXYModelMapper(
    QVXYModelMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVXYModelMapper *>(self)->take(key, call);
}
