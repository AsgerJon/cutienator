//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qbarmodelmapper.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_bar))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qbarmodelmapper.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QBarModelMapper that Python can take functions over in. Every QBarModelMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBarModelMapperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBarModelMapperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarModelMapperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarModelMapperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarModelMapperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarModelMapperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarModelMapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBarModelMapper : public QBarModelMapper {
public:
  using QBarModelMapper::QBarModelMapper;
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
      CuteQBarModelMapperCall0 call = reinterpret_cast<CuteQBarModelMapperCall0>(taken[0]);
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
      CuteQBarModelMapperCall1 call = reinterpret_cast<CuteQBarModelMapperCall1>(taken[1]);
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
      CuteQBarModelMapperCall2 call = reinterpret_cast<CuteQBarModelMapperCall2>(taken[2]);
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
      CuteQBarModelMapperCall3 call = reinterpret_cast<CuteQBarModelMapperCall3>(taken[3]);
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
      CuteQBarModelMapperCall4 call = reinterpret_cast<CuteQBarModelMapperCall4>(taken[4]);
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
      CuteQBarModelMapperCall5 call = reinterpret_cast<CuteQBarModelMapperCall5>(taken[5]);
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
      CuteQBarModelMapperCall6 call = reinterpret_cast<CuteQBarModelMapperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBarModelMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QBarModelMapper10metaObjectEv(
    const QBarModelMapper *self) {
  return self->metaObject();
}

//  void *QBarModelMapper::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QBarModelMapper11qt_metacastEPKc(
    QBarModelMapper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QBarModelMapper::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QBarModelMapper11qt_metacallEN11QMetaObject4CallEiPPv(
    QBarModelMapper *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QBarModelMapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QBarModelMapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBarModelMapper::tr(s, c, n));
}

//  QBarModelMapperPrivate *QBarModelMapper::d_func()
extern "C" Q_DECL_EXPORT
QBarModelMapperPrivate *ritual_ZN15QBarModelMapper6d_funcEv(
    QBarModelMapper *self) {
  return self->d_func();
}

//  const QBarModelMapperPrivate *QBarModelMapper::d_func() const
extern "C" Q_DECL_EXPORT
const QBarModelMapperPrivate *ritual_ZNK15QBarModelMapper6d_funcEv(
    const QBarModelMapper *self) {
  return self->d_func();
}

//  QBarModelMapper::QBarModelMapper(QObject *parent)
extern "C" Q_DECL_EXPORT
QBarModelMapper *ritual_ZN15QBarModelMapperC1EP7QObject(QObject *parent) {
  return new CuteQBarModelMapper(parent);
}

//  QBarModelMapper::~QBarModelMapper()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBarModelMapperD1Ev(QBarModelMapper *self) {
  delete self;
}

//  QAbstractItemModel *QBarModelMapper::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK15QBarModelMapper5modelEv(
    const QBarModelMapper *self) {
  return self->model();
}

//  void QBarModelMapper::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBarModelMapper8setModelEP18QAbstractItemModel(
    QBarModelMapper *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  QBarSeries *QBarModelMapper::series() const
extern "C" Q_DECL_EXPORT
QBarSeries *ritual_ZNK15QBarModelMapper6seriesEv(
    const QBarModelMapper *self) {
  return self->series();
}

//  void QBarModelMapper::setSeries(QBarSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBarModelMapper9setSeriesEP10QBarSeries(
    QBarModelMapper *self,
    QBarSeries *series) {
  self->setSeries(series);
}

//  qsizetype QBarModelMapper::firstBarSetSection() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK15QBarModelMapper18firstBarSetSectionEv(
    const QBarModelMapper *self) {
  return self->firstBarSetSection();
}

//  void QBarModelMapper::setFirstBarSetSection(qsizetype
//      newFirstBarSetSection)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBarModelMapper21setFirstBarSetSectionEx(
    QBarModelMapper *self,
    qsizetype newFirstBarSetSection) {
  self->setFirstBarSetSection(newFirstBarSetSection);
}

//  qsizetype QBarModelMapper::lastBarSetSection() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK15QBarModelMapper17lastBarSetSectionEv(
    const QBarModelMapper *self) {
  return self->lastBarSetSection();
}

//  void QBarModelMapper::setLastBarSetSection(qsizetype
//      newLastBarSetSection)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBarModelMapper20setLastBarSetSectionEx(
    QBarModelMapper *self,
    qsizetype newLastBarSetSection) {
  self->setLastBarSetSection(newLastBarSetSection);
}

//  qsizetype QBarModelMapper::count() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK15QBarModelMapper5countEv(const QBarModelMapper *self) {
  return self->count();
}

//  void QBarModelMapper::setCount(qsizetype newCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBarModelMapper8setCountEx(
    QBarModelMapper *self,
    qsizetype newCount) {
  self->setCount(newCount);
}

//  qsizetype QBarModelMapper::first() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK15QBarModelMapper5firstEv(const QBarModelMapper *self) {
  return self->first();
}

//  void QBarModelMapper::setFirst(qsizetype newFirst)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBarModelMapper8setFirstEx(
    QBarModelMapper *self,
    qsizetype newFirst) {
  self->setFirst(newFirst);
}

//  Qt::Orientation QBarModelMapper::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK15QBarModelMapper11orientationEv(
    const QBarModelMapper *self) {
  return self->orientation();
}

//  void QBarModelMapper::setOrientation(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBarModelMapper14setOrientationEN2Qt11OrientationE(
    QBarModelMapper *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  void QBarModelMapper::seriesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBarModelMapper13seriesChangedEv(QBarModelMapper *self) {
  self->seriesChanged();
}

//  void QBarModelMapper::modelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBarModelMapper12modelChangedEv(QBarModelMapper *self) {
  self->modelChanged();
}

//  void QBarModelMapper::firstBarSetSectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBarModelMapper25firstBarSetSectionChangedEv(
    QBarModelMapper *self) {
  self->firstBarSetSectionChanged();
}

//  void QBarModelMapper::lastBarSetSectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBarModelMapper24lastBarSetSectionChangedEv(
    QBarModelMapper *self) {
  self->lastBarSetSectionChanged();
}

//  void QBarModelMapper::firstChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBarModelMapper12firstChangedEv(QBarModelMapper *self) {
  self->firstChanged();
}

//  void QBarModelMapper::countChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBarModelMapper12countChangedEv(QBarModelMapper *self) {
  self->countChanged();
}

//  void QBarModelMapper::orientationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBarModelMapper18orientationChangedEv(
    QBarModelMapper *self) {
  self->orientationChanged();
}

//  QBarModelMapper::QBarModelMapper(QBarModelMapperPrivate &dd, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QBarModelMapper *ritual_ZN15QBarModelMapperC1ER22QBarModelMapperPrivateP7QObject(
    QBarModelMapperPrivate *dd,
    QObject *parent) {
  return new CuteQBarModelMapper(*dd, parent);
}

//  void QBarModelMapper::onValuesAdded(qsizetype index, qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBarModelMapper13onValuesAddedExx(
    QBarModelMapper *self,
    qsizetype index,
    qsizetype count) {
  self->onValuesAdded(index, count);
}

//  void QBarModelMapper::onBarLabelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBarModelMapper17onBarLabelChangedEv(QBarModelMapper *self) {
  self->onBarLabelChanged();
}

//  void QBarModelMapper::onBarValueChanged(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QBarModelMapper17onBarValueChangedEx(
    QBarModelMapper *self,
    qsizetype index) {
  self->onBarValueChanged(index);
}

//  a Python function taken by a CuteQBarModelMapper, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBarModelMapper(
    QBarModelMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBarModelMapper *>(self)->take(key, call);
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_bar))
