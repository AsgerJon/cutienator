//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qpiemodelmapper.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_donut_pie))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qpiemodelmapper.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPieModelMapper that Python can take functions over in. Every QPieModelMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPieModelMapperCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPieModelMapperCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieModelMapperCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieModelMapperCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieModelMapperCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieModelMapperCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieModelMapperCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPieModelMapper : public QPieModelMapper {
public:
  using QPieModelMapper::QPieModelMapper;
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
      CuteQPieModelMapperCall0 call = reinterpret_cast<CuteQPieModelMapperCall0>(taken[0]);
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
      CuteQPieModelMapperCall1 call = reinterpret_cast<CuteQPieModelMapperCall1>(taken[1]);
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
      CuteQPieModelMapperCall2 call = reinterpret_cast<CuteQPieModelMapperCall2>(taken[2]);
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
      CuteQPieModelMapperCall3 call = reinterpret_cast<CuteQPieModelMapperCall3>(taken[3]);
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
      CuteQPieModelMapperCall4 call = reinterpret_cast<CuteQPieModelMapperCall4>(taken[4]);
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
      CuteQPieModelMapperCall5 call = reinterpret_cast<CuteQPieModelMapperCall5>(taken[5]);
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
      CuteQPieModelMapperCall6 call = reinterpret_cast<CuteQPieModelMapperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPieModelMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QPieModelMapper10metaObjectEv(
    const QPieModelMapper *self) {
  return self->metaObject();
}

//  void *QPieModelMapper::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QPieModelMapper11qt_metacastEPKc(
    QPieModelMapper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPieModelMapper::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QPieModelMapper11qt_metacallEN11QMetaObject4CallEiPPv(
    QPieModelMapper *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPieModelMapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QPieModelMapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPieModelMapper::tr(s, c, n));
}

//  QPieModelMapperPrivate *QPieModelMapper::d_func()
extern "C" Q_DECL_EXPORT
QPieModelMapperPrivate *ritual_ZN15QPieModelMapper6d_funcEv(
    QPieModelMapper *self) {
  return self->d_func();
}

//  const QPieModelMapperPrivate *QPieModelMapper::d_func() const
extern "C" Q_DECL_EXPORT
const QPieModelMapperPrivate *ritual_ZNK15QPieModelMapper6d_funcEv(
    const QPieModelMapper *self) {
  return self->d_func();
}

//  QPieModelMapper::QPieModelMapper(QObject *parent)
extern "C" Q_DECL_EXPORT
QPieModelMapper *ritual_ZN15QPieModelMapperC1EP7QObject(QObject *parent) {
  return new CuteQPieModelMapper(parent);
}

//  QPieModelMapper::~QPieModelMapper()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPieModelMapperD1Ev(QPieModelMapper *self) {
  delete self;
}

//  QPieSeries *QPieModelMapper::series() const
extern "C" Q_DECL_EXPORT
QPieSeries *ritual_ZNK15QPieModelMapper6seriesEv(
    const QPieModelMapper *self) {
  return self->series();
}

//  void QPieModelMapper::setSeries(QPieSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPieModelMapper9setSeriesEP10QPieSeries(
    QPieModelMapper *self,
    QPieSeries *series) {
  self->setSeries(series);
}

//  qsizetype QPieModelMapper::first() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK15QPieModelMapper5firstEv(const QPieModelMapper *self) {
  return self->first();
}

//  void QPieModelMapper::setFirst(qsizetype first)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPieModelMapper8setFirstEx(
    QPieModelMapper *self,
    qsizetype first) {
  self->setFirst(first);
}

//  qsizetype QPieModelMapper::count() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK15QPieModelMapper5countEv(const QPieModelMapper *self) {
  return self->count();
}

//  void QPieModelMapper::setCount(qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPieModelMapper8setCountEx(
    QPieModelMapper *self,
    qsizetype count) {
  self->setCount(count);
}

//  qsizetype QPieModelMapper::valuesSection() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK15QPieModelMapper13valuesSectionEv(
    const QPieModelMapper *self) {
  return self->valuesSection();
}

//  void QPieModelMapper::setValuesSection(qsizetype valuesSection)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPieModelMapper16setValuesSectionEx(
    QPieModelMapper *self,
    qsizetype valuesSection) {
  self->setValuesSection(valuesSection);
}

//  qsizetype QPieModelMapper::labelsSection() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK15QPieModelMapper13labelsSectionEv(
    const QPieModelMapper *self) {
  return self->labelsSection();
}

//  void QPieModelMapper::setLabelsSection(qsizetype labelsSection)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPieModelMapper16setLabelsSectionEx(
    QPieModelMapper *self,
    qsizetype labelsSection) {
  self->setLabelsSection(labelsSection);
}

//  Qt::Orientation QPieModelMapper::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK15QPieModelMapper11orientationEv(
    const QPieModelMapper *self) {
  return self->orientation();
}

//  void QPieModelMapper::setOrientation(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPieModelMapper14setOrientationEN2Qt11OrientationE(
    QPieModelMapper *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  QAbstractItemModel *QPieModelMapper::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK15QPieModelMapper5modelEv(
    const QPieModelMapper *self) {
  return self->model();
}

//  void QPieModelMapper::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPieModelMapper8setModelEP18QAbstractItemModel(
    QPieModelMapper *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  void QPieModelMapper::seriesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPieModelMapper13seriesChangedEv(QPieModelMapper *self) {
  self->seriesChanged();
}

//  void QPieModelMapper::modelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPieModelMapper12modelChangedEv(QPieModelMapper *self) {
  self->modelChanged();
}

//  void QPieModelMapper::valuesSectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPieModelMapper20valuesSectionChangedEv(
    QPieModelMapper *self) {
  self->valuesSectionChanged();
}

//  void QPieModelMapper::labelsSectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPieModelMapper20labelsSectionChangedEv(
    QPieModelMapper *self) {
  self->labelsSectionChanged();
}

//  void QPieModelMapper::firstChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPieModelMapper12firstChangedEv(QPieModelMapper *self) {
  self->firstChanged();
}

//  void QPieModelMapper::countChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPieModelMapper12countChangedEv(QPieModelMapper *self) {
  self->countChanged();
}

//  void QPieModelMapper::orientationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPieModelMapper18orientationChangedEv(
    QPieModelMapper *self) {
  self->orientationChanged();
}

//  void QPieModelMapper::onSliceLabelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPieModelMapper19onSliceLabelChangedEv(
    QPieModelMapper *self) {
  self->onSliceLabelChanged();
}

//  void QPieModelMapper::onSliceValueChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPieModelMapper19onSliceValueChangedEv(
    QPieModelMapper *self) {
  self->onSliceValueChanged();
}

//  QPieModelMapper::QPieModelMapper(QPieModelMapperPrivate &dd, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QPieModelMapper *ritual_ZN15QPieModelMapperC1ER22QPieModelMapperPrivateP7QObject(
    QPieModelMapperPrivate *dd,
    QObject *parent) {
  return new CuteQPieModelMapper(*dd, parent);
}

//  a Python function taken by a CuteQPieModelMapper, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPieModelMapper(
    QPieModelMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPieModelMapper *>(self)->take(key, call);
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_donut_pie))
