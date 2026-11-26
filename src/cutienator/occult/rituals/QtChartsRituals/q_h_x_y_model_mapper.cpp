//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qhxymodelmapper.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qhxymodelmapper.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QHXYModelMapper that Python can take functions over in. Every QHXYModelMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHXYModelMapperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHXYModelMapperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHXYModelMapperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHXYModelMapperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHXYModelMapperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHXYModelMapperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHXYModelMapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHXYModelMapper : public QHXYModelMapper {
public:
  using QHXYModelMapper::QHXYModelMapper;
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
      CuteQHXYModelMapperCall0 call = reinterpret_cast<CuteQHXYModelMapperCall0>(taken[0]);
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
      CuteQHXYModelMapperCall1 call = reinterpret_cast<CuteQHXYModelMapperCall1>(taken[1]);
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
      CuteQHXYModelMapperCall2 call = reinterpret_cast<CuteQHXYModelMapperCall2>(taken[2]);
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
      CuteQHXYModelMapperCall3 call = reinterpret_cast<CuteQHXYModelMapperCall3>(taken[3]);
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
      CuteQHXYModelMapperCall4 call = reinterpret_cast<CuteQHXYModelMapperCall4>(taken[4]);
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
      CuteQHXYModelMapperCall5 call = reinterpret_cast<CuteQHXYModelMapperCall5>(taken[5]);
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
      CuteQHXYModelMapperCall6 call = reinterpret_cast<CuteQHXYModelMapperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHXYModelMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QHXYModelMapper10metaObjectEv(
    const QHXYModelMapper *self) {
  return self->metaObject();
}

//  void *QHXYModelMapper::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QHXYModelMapper11qt_metacastEPKc(
    QHXYModelMapper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QHXYModelMapper::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QHXYModelMapper11qt_metacallEN11QMetaObject4CallEiPPv(
    QHXYModelMapper *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QHXYModelMapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QHXYModelMapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHXYModelMapper::tr(s, c, n));
}

//  QHXYModelMapper::QHXYModelMapper(QObject *parent)
extern "C" Q_DECL_EXPORT
QHXYModelMapper *ritual_ZN15QHXYModelMapperC1EP7QObject(QObject *parent) {
  return new CuteQHXYModelMapper(parent);
}

//  QAbstractItemModel *QHXYModelMapper::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK15QHXYModelMapper5modelEv(
    const QHXYModelMapper *self) {
  return self->model();
}

//  void QHXYModelMapper::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHXYModelMapper8setModelEP18QAbstractItemModel(
    QHXYModelMapper *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  QXYSeries *QHXYModelMapper::series() const
extern "C" Q_DECL_EXPORT
QXYSeries *ritual_ZNK15QHXYModelMapper6seriesEv(
    const QHXYModelMapper *self) {
  return self->series();
}

//  void QHXYModelMapper::setSeries(QXYSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHXYModelMapper9setSeriesEP9QXYSeries(
    QHXYModelMapper *self,
    QXYSeries *series) {
  self->setSeries(series);
}

//  int QHXYModelMapper::xRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QHXYModelMapper4xRowEv(const QHXYModelMapper *self) {
  return self->xRow();
}

//  void QHXYModelMapper::setXRow(int xRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHXYModelMapper7setXRowEi(QHXYModelMapper *self, int xRow) {
  self->setXRow(xRow);
}

//  int QHXYModelMapper::yRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QHXYModelMapper4yRowEv(const QHXYModelMapper *self) {
  return self->yRow();
}

//  void QHXYModelMapper::setYRow(int yRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHXYModelMapper7setYRowEi(QHXYModelMapper *self, int yRow) {
  self->setYRow(yRow);
}

//  int QHXYModelMapper::firstColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QHXYModelMapper11firstColumnEv(const QHXYModelMapper *self) {
  return self->firstColumn();
}

//  void QHXYModelMapper::setFirstColumn(int firstColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHXYModelMapper14setFirstColumnEi(
    QHXYModelMapper *self,
    int firstColumn) {
  self->setFirstColumn(firstColumn);
}

//  int QHXYModelMapper::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QHXYModelMapper11columnCountEv(const QHXYModelMapper *self) {
  return self->columnCount();
}

//  void QHXYModelMapper::setColumnCount(int columnCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHXYModelMapper14setColumnCountEi(
    QHXYModelMapper *self,
    int columnCount) {
  self->setColumnCount(columnCount);
}

//  void QHXYModelMapper::seriesReplaced()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHXYModelMapper14seriesReplacedEv(QHXYModelMapper *self) {
  self->seriesReplaced();
}

//  void QHXYModelMapper::modelReplaced()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHXYModelMapper13modelReplacedEv(QHXYModelMapper *self) {
  self->modelReplaced();
}

//  void QHXYModelMapper::xRowChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHXYModelMapper11xRowChangedEv(QHXYModelMapper *self) {
  self->xRowChanged();
}

//  void QHXYModelMapper::yRowChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHXYModelMapper11yRowChangedEv(QHXYModelMapper *self) {
  self->yRowChanged();
}

//  void QHXYModelMapper::firstColumnChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHXYModelMapper18firstColumnChangedEv(
    QHXYModelMapper *self) {
  self->firstColumnChanged();
}

//  void QHXYModelMapper::columnCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHXYModelMapper18columnCountChangedEv(
    QHXYModelMapper *self) {
  self->columnCountChanged();
}

//  a Python function taken by a CuteQHXYModelMapper, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHXYModelMapper(
    QHXYModelMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHXYModelMapper *>(self)->take(key, call);
}
