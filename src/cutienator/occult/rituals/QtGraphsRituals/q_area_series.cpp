//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qareaseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_area))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qareaseries.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAreaSeries that Python can take functions over in. Every QAreaSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQAreaSeriesCall0)(const void *, int *);
typedef void (*CuteQAreaSeriesCall1)(const void *, int *);
typedef void (*CuteQAreaSeriesCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAreaSeriesCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAreaSeriesCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAreaSeriesCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAreaSeriesCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAreaSeriesCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAreaSeriesCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAreaSeriesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAreaSeries : public QAreaSeries {
public:
  using QAreaSeries::QAreaSeries;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QAbstractSeries4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QAbstractSeries::SeriesType QAreaSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAreaSeriesCall0 call = reinterpret_cast<CuteQAreaSeriesCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QAreaSeries::type();
  }

  //  void QAbstractSeries::classBegin()
  void classBegin() override {
    if (taken[1]) {
      int handled = 0;
      CuteQAreaSeriesCall1 call = reinterpret_cast<CuteQAreaSeriesCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSeries::classBegin();
  }

  //  void QAbstractSeries::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQAreaSeriesCall2 call = reinterpret_cast<CuteQAreaSeriesCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSeries::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAreaSeriesCall3 call = reinterpret_cast<CuteQAreaSeriesCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAreaSeriesCall4 call = reinterpret_cast<CuteQAreaSeriesCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAreaSeriesCall5 call = reinterpret_cast<CuteQAreaSeriesCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAreaSeriesCall6 call = reinterpret_cast<CuteQAreaSeriesCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAreaSeriesCall7 call = reinterpret_cast<CuteQAreaSeriesCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAreaSeriesCall8 call = reinterpret_cast<CuteQAreaSeriesCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAreaSeriesCall9 call = reinterpret_cast<CuteQAreaSeriesCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAreaSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QAreaSeries10metaObjectEv(
    const QAreaSeries *self) {
  return self->metaObject();
}

//  void *QAreaSeries::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QAreaSeries11qt_metacastEPKc(
    QAreaSeries *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAreaSeries::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QAreaSeries11qt_metacallEN11QMetaObject4CallEiPPv(
    QAreaSeries *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAreaSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QAreaSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAreaSeries::tr(s, c, n));
}

//  QAreaSeries::QAreaSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
QAreaSeries *ritual_ZN11QAreaSeriesC1EP7QObject(QObject *parent) {
  return new CuteQAreaSeries(parent);
}

//  QAreaSeries::~QAreaSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeriesD1Ev(QAreaSeries *self) {
  delete self;
}

//  QAbstractSeries::SeriesType QAreaSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_ZNK11QAreaSeries4typeEv(
    const QAreaSeries *self) {
  return self->type();
}

//  QColor QAreaSeries::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QAreaSeries5colorEv(const QAreaSeries *self) {
  return new QColor(self->color());
}

//  void QAreaSeries::setColor(QColor newColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries8setColorE6QColor(
    QAreaSeries *self,
    const QColor *newColor) {
  self->setColor(*newColor);
}

//  QColor QAreaSeries::selectedColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QAreaSeries13selectedColorEv(const QAreaSeries *self) {
  return new QColor(self->selectedColor());
}

//  void QAreaSeries::setSelectedColor(QColor newColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries16setSelectedColorE6QColor(
    QAreaSeries *self,
    const QColor *newColor) {
  self->setSelectedColor(*newColor);
}

//  QColor QAreaSeries::borderColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QAreaSeries11borderColorEv(const QAreaSeries *self) {
  return new QColor(self->borderColor());
}

//  void QAreaSeries::setBorderColor(QColor newBorderColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries14setBorderColorE6QColor(
    QAreaSeries *self,
    const QColor *newBorderColor) {
  self->setBorderColor(*newBorderColor);
}

//  QColor QAreaSeries::selectedBorderColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QAreaSeries19selectedBorderColorEv(
    const QAreaSeries *self) {
  return new QColor(self->selectedBorderColor());
}

//  void QAreaSeries::setSelectedBorderColor(QColor newSelectedBorderColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries22setSelectedBorderColorE6QColor(
    QAreaSeries *self,
    const QColor *newSelectedBorderColor) {
  self->setSelectedBorderColor(*newSelectedBorderColor);
}

//  qreal QAreaSeries::borderWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QAreaSeries11borderWidthEv(const QAreaSeries *self) {
  return self->borderWidth();
}

//  void QAreaSeries::setBorderWidth(qreal newBorderWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries14setBorderWidthEd(
    QAreaSeries *self,
    qreal newBorderWidth) {
  self->setBorderWidth(newBorderWidth);
}

//  bool QAreaSeries::isSelected() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QAreaSeries10isSelectedEv(const QAreaSeries *self) {
  return self->isSelected();
}

//  void QAreaSeries::setSelected(bool newSelected)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries11setSelectedEb(
    QAreaSeries *self,
    bool newSelected) {
  self->setSelected(newSelected);
}

//  QXYSeries *QAreaSeries::upperSeries() const
extern "C" Q_DECL_EXPORT
QXYSeries *ritual_ZNK11QAreaSeries11upperSeriesEv(const QAreaSeries *self) {
  return self->upperSeries();
}

//  void QAreaSeries::setUpperSeries(QXYSeries *newUpperSeries)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries14setUpperSeriesEP9QXYSeries(
    QAreaSeries *self,
    QXYSeries *newUpperSeries) {
  self->setUpperSeries(newUpperSeries);
}

//  QXYSeries *QAreaSeries::lowerSeries() const
extern "C" Q_DECL_EXPORT
QXYSeries *ritual_ZNK11QAreaSeries11lowerSeriesEv(const QAreaSeries *self) {
  return self->lowerSeries();
}

//  void QAreaSeries::setLowerSeries(QXYSeries *newLowerSeries)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries14setLowerSeriesEP9QXYSeries(
    QAreaSeries *self,
    QXYSeries *newLowerSeries) {
  self->setLowerSeries(newLowerSeries);
}

//  QQuickShapeGradient *QAreaSeries::gradient() const
extern "C" Q_DECL_EXPORT
QQuickShapeGradient *ritual_ZNK11QAreaSeries8gradientEv(
    const QAreaSeries *self) {
  return self->gradient();
}

//  void QAreaSeries::setGradient(QQuickShapeGradient *newGradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries11setGradientEP19QQuickShapeGradient(
    QAreaSeries *self,
    QQuickShapeGradient *newGradient) {
  self->setGradient(newGradient);
}

//  QQuickShapeGradient *QAreaSeries::selectedGradient() const
extern "C" Q_DECL_EXPORT
QQuickShapeGradient *ritual_ZNK11QAreaSeries16selectedGradientEv(
    const QAreaSeries *self) {
  return self->selectedGradient();
}

//  void QAreaSeries::setSelectedGradient(QQuickShapeGradient
//      *newSelectedGradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries19setSelectedGradientEP19QQuickShapeGradient(
    QAreaSeries *self,
    QQuickShapeGradient *newSelectedGradient) {
  self->setSelectedGradient(newSelectedGradient);
}

//  void QAreaSeries::colorChanged(QColor newColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries12colorChangedE6QColor(
    QAreaSeries *self,
    const QColor *newColor) {
  self->colorChanged(*newColor);
}

//  void QAreaSeries::selectedColorChanged(QColor newSelectedColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries20selectedColorChangedE6QColor(
    QAreaSeries *self,
    const QColor *newSelectedColor) {
  self->selectedColorChanged(*newSelectedColor);
}

//  void QAreaSeries::borderColorChanged(QColor newBorderColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries18borderColorChangedE6QColor(
    QAreaSeries *self,
    const QColor *newBorderColor) {
  self->borderColorChanged(*newBorderColor);
}

//  void QAreaSeries::selectedBorderColorChanged(QColor
//      newSelectedBorderColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries26selectedBorderColorChangedE6QColor(
    QAreaSeries *self,
    const QColor *newSelectedBorderColor) {
  self->selectedBorderColorChanged(*newSelectedBorderColor);
}

//  void QAreaSeries::borderWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries18borderWidthChangedEv(QAreaSeries *self) {
  self->borderWidthChanged();
}

//  void QAreaSeries::selectedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries15selectedChangedEv(QAreaSeries *self) {
  self->selectedChanged();
}

//  void QAreaSeries::upperSeriesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries18upperSeriesChangedEv(QAreaSeries *self) {
  self->upperSeriesChanged();
}

//  void QAreaSeries::lowerSeriesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries18lowerSeriesChangedEv(QAreaSeries *self) {
  self->lowerSeriesChanged();
}

//  void QAreaSeries::gradientChanged(QQuickShapeGradient *newGradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries15gradientChangedEP19QQuickShapeGradient(
    QAreaSeries *self,
    QQuickShapeGradient *newGradient) {
  self->gradientChanged(newGradient);
}

//  void QAreaSeries::selectedGradientChanged(QQuickShapeGradient
//      *newGradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries23selectedGradientChangedEP19QQuickShapeGradient(
    QAreaSeries *self,
    QQuickShapeGradient *newGradient) {
  self->selectedGradientChanged(newGradient);
}

//  void QAreaSeries::clicked(QPoint point)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries7clickedE6QPoint(
    QAreaSeries *self,
    const QPoint *point) {
  self->clicked(*point);
}

//  void QAreaSeries::doubleClicked(QPoint point)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries13doubleClickedE6QPoint(
    QAreaSeries *self,
    const QPoint *point) {
  self->doubleClicked(*point);
}

//  void QAreaSeries::pressed(QPoint point)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries7pressedE6QPoint(
    QAreaSeries *self,
    const QPoint *point) {
  self->pressed(*point);
}

//  void QAreaSeries::released(QPoint point)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAreaSeries8releasedE6QPoint(
    QAreaSeries *self,
    const QPoint *point) {
  self->released(*point);
}

//  QAreaSeries::QAreaSeries(QAreaSeriesPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QAreaSeries *ritual_ZN11QAreaSeriesC1ER18QAreaSeriesPrivateP7QObject(
    QAreaSeriesPrivate *dd,
    QObject *parent) {
  return new CuteQAreaSeries(*dd, parent);
}

//  QAreaSeriesPrivate *QAreaSeries::d_func()
extern "C" Q_DECL_EXPORT
QAreaSeriesPrivate *ritual_ZN11QAreaSeries6d_funcEv(QAreaSeries *self) {
  return self->d_func();
}

//  const QAreaSeriesPrivate *QAreaSeries::d_func() const
extern "C" Q_DECL_EXPORT
const QAreaSeriesPrivate *ritual_ZNK11QAreaSeries6d_funcEv(
    const QAreaSeries *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAreaSeries, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAreaSeries(
    QAreaSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAreaSeries *>(self)->take(key, call);
}

//  QAbstractSeries::SeriesType QAreaSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_own_ZNK11QAreaSeries4typeEv(
    const QAreaSeries *self) {
  return self->QAreaSeries::type();
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_area))
