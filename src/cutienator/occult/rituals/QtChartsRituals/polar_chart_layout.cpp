//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/polarchartlayout_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/polarchartlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/chartaxiselement_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmargins.h>
#include <QtCore/qsize.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A PolarChartLayout that Python can take functions over in. Every PolarChartLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CutePolarChartLayoutCall0)(const void *, const QMargins *, int *);
typedef const QMargins * (*CutePolarChartLayoutCall1)(const void *, int *);
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartLayoutCall2)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef const QRectF * (*CutePolarChartLayoutCall3)(const void *, const QRectF *, ChartBackground *, bool, int *);
typedef const QRectF * (*CutePolarChartLayoutCall4)(const void *, const QRectF *, int *);
typedef const QRectF * (*CutePolarChartLayoutCall5)(const void *, const QRectF *, int *);
typedef const QRectF * (*CutePolarChartLayoutCall6)(const void *, const QRectF *, int *);
typedef const QRectF * (*CutePolarChartLayoutCall7)(const void *, const QRectF *, ChartTitle *, bool, int *);
typedef const QRectF * (*CutePolarChartLayoutCall8)(const void *, const QRectF *, ChartTitle *, int *);
typedef const QRectF * (*CutePolarChartLayoutCall9)(const void *, const QRectF *, QLegend *, bool, int *);
typedef const QRectF * (*CutePolarChartLayoutCall10)(const void *, const QRectF *, QLegend *, int *);
#if QT_CONFIG(graphicsview)
typedef const QSizeF * (*CutePolarChartLayoutCall11)(const void *, int, const QSizeF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CutePolarChartLayoutCall12)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void * (*CutePolarChartLayoutCall13)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartLayoutCall14)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartLayoutCall15)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartLayoutCall16)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CutePolarChartLayoutCall17)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CutePolarChartLayoutCall18)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
class CutePolarChartLayout : public PolarChartLayout {
public:
  using PolarChartLayout::PolarChartLayout;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19AbstractChartLayout10setMarginsERK8QMargins")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19AbstractChartLayout7marginsEv")) {
      taken[1] = call;
      return true;
    }
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem11setGeometryERK6QRectF")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK19AbstractChartLayout27calculateBackgroundGeometryERK6QRectFP15ChartBackgroundb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19AbstractChartLayout26calculateBackgroundMinimumERK6QRectF")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19AbstractChartLayout24calculateContentGeometryERK6QRectF")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19AbstractChartLayout23calculateContentMinimumERK6QRectF")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19AbstractChartLayout22calculateTitleGeometryERK6QRectFP10ChartTitleb")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19AbstractChartLayout21calculateTitleMinimumERK6QRectFP10ChartTitle")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19AbstractChartLayout23calculateLegendGeometryERK6QRectFP7QLegendb")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19AbstractChartLayout22calculateLegendMinimumERK6QRectFP7QLegend")) {
      taken[10] = call;
      return true;
    }
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGraphicsLayout5countEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGraphicsLayout6itemAtEi")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsLayout8removeAtEi")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsLayout10invalidateEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem14updateGeometryEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsLayout11widgetEventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem7isEmptyEv")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    return false;
  }

  //  void AbstractChartLayout::setMargins(const QMargins &margins)
  void setMargins(const QMargins &margins) override {
    if (taken[0]) {
      int handled = 0;
      CutePolarChartLayoutCall0 call = reinterpret_cast<CutePolarChartLayoutCall0>(taken[0]);
      call(this, &margins, &handled);
      if (handled) return;
    }
    AbstractChartLayout::setMargins(margins);
  }

  //  QMargins AbstractChartLayout::margins() const
  QMargins margins() const override {
    if (taken[1]) {
      int handled = 0;
      CutePolarChartLayoutCall1 call = reinterpret_cast<CutePolarChartLayoutCall1>(taken[1]);
      const QMargins * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return AbstractChartLayout::margins();
  }

#if QT_CONFIG(graphicsview)
  //  void AbstractChartLayout::setGeometry(const QRectF &rect)
  void setGeometry(const QRectF &rect) override {
    if (taken[2]) {
      int handled = 0;
      CutePolarChartLayoutCall2 call = reinterpret_cast<CutePolarChartLayoutCall2>(taken[2]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    AbstractChartLayout::setGeometry(rect);
  }
#endif  // QT_CONFIG(graphicsview)

  //  QRectF AbstractChartLayout::calculateBackgroundGeometry(const QRectF
  //      &geometry, ChartBackground *background, bool update) const
  QRectF calculateBackgroundGeometry(
      const QRectF &geometry,
      ChartBackground *background,
      bool update) const override {
    if (taken[3]) {
      int handled = 0;
      CutePolarChartLayoutCall3 call = reinterpret_cast<CutePolarChartLayoutCall3>(taken[3]);
      const QRectF * given = call(this, &geometry, background, update, &handled);
      if (handled && given) return *given;
    }
    return AbstractChartLayout::calculateBackgroundGeometry(geometry, background, update);
  }

  //  QRectF AbstractChartLayout::calculateBackgroundMinimum(const QRectF
  //      &minimum) const
  QRectF calculateBackgroundMinimum(const QRectF &minimum) const override {
    if (taken[4]) {
      int handled = 0;
      CutePolarChartLayoutCall4 call = reinterpret_cast<CutePolarChartLayoutCall4>(taken[4]);
      const QRectF * given = call(this, &minimum, &handled);
      if (handled && given) return *given;
    }
    return AbstractChartLayout::calculateBackgroundMinimum(minimum);
  }

  //  QRectF AbstractChartLayout::calculateContentGeometry(const QRectF
  //      &geometry) const
  QRectF calculateContentGeometry(const QRectF &geometry) const override {
    if (taken[5]) {
      int handled = 0;
      CutePolarChartLayoutCall5 call = reinterpret_cast<CutePolarChartLayoutCall5>(taken[5]);
      const QRectF * given = call(this, &geometry, &handled);
      if (handled && given) return *given;
    }
    return AbstractChartLayout::calculateContentGeometry(geometry);
  }

  //  QRectF AbstractChartLayout::calculateContentMinimum(const QRectF
  //      &minimum) const
  QRectF calculateContentMinimum(const QRectF &minimum) const override {
    if (taken[6]) {
      int handled = 0;
      CutePolarChartLayoutCall6 call = reinterpret_cast<CutePolarChartLayoutCall6>(taken[6]);
      const QRectF * given = call(this, &minimum, &handled);
      if (handled && given) return *given;
    }
    return AbstractChartLayout::calculateContentMinimum(minimum);
  }

  //  QRectF AbstractChartLayout::calculateTitleGeometry(const QRectF
  //      &geometry, ChartTitle *title, bool update) const
  QRectF calculateTitleGeometry(
      const QRectF &geometry,
      ChartTitle *title,
      bool update) const override {
    if (taken[7]) {
      int handled = 0;
      CutePolarChartLayoutCall7 call = reinterpret_cast<CutePolarChartLayoutCall7>(taken[7]);
      const QRectF * given = call(this, &geometry, title, update, &handled);
      if (handled && given) return *given;
    }
    return AbstractChartLayout::calculateTitleGeometry(geometry, title, update);
  }

  //  QRectF AbstractChartLayout::calculateTitleMinimum(const QRectF
  //      &minimum, ChartTitle *title) const
  QRectF calculateTitleMinimum(
      const QRectF &minimum,
      ChartTitle *title) const override {
    if (taken[8]) {
      int handled = 0;
      CutePolarChartLayoutCall8 call = reinterpret_cast<CutePolarChartLayoutCall8>(taken[8]);
      const QRectF * given = call(this, &minimum, title, &handled);
      if (handled && given) return *given;
    }
    return AbstractChartLayout::calculateTitleMinimum(minimum, title);
  }

  //  QRectF AbstractChartLayout::calculateLegendGeometry(const QRectF
  //      &geometry, QLegend *legend, bool update) const
  QRectF calculateLegendGeometry(
      const QRectF &geometry,
      QLegend *legend,
      bool update) const override {
    if (taken[9]) {
      int handled = 0;
      CutePolarChartLayoutCall9 call = reinterpret_cast<CutePolarChartLayoutCall9>(taken[9]);
      const QRectF * given = call(this, &geometry, legend, update, &handled);
      if (handled && given) return *given;
    }
    return AbstractChartLayout::calculateLegendGeometry(geometry, legend, update);
  }

  //  QRectF AbstractChartLayout::calculateLegendMinimum(const QRectF
  //      &minimum, QLegend *legend) const
  QRectF calculateLegendMinimum(
      const QRectF &minimum,
      QLegend *legend) const override {
    if (taken[10]) {
      int handled = 0;
      CutePolarChartLayoutCall10 call = reinterpret_cast<CutePolarChartLayoutCall10>(taken[10]);
      const QRectF * given = call(this, &minimum, legend, &handled);
      if (handled && given) return *given;
    }
    return AbstractChartLayout::calculateLegendMinimum(minimum, legend);
  }

#if QT_CONFIG(graphicsview)
  //  QSizeF AbstractChartLayout::sizeHint(Qt::SizeHint which, const QSizeF
  //      &constraint) const
  QSizeF sizeHint(
      Qt::SizeHint which,
      const QSizeF &constraint) const override {
    if (taken[11]) {
      int handled = 0;
      CutePolarChartLayoutCall11 call = reinterpret_cast<CutePolarChartLayoutCall11>(taken[11]);
      const QSizeF * given = call(this, static_cast<int>(which), &constraint, &handled);
      if (handled && given) return *given;
    }
    return AbstractChartLayout::sizeHint(which, constraint);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  int AbstractChartLayout::count() const
  int count() const override {
    if (taken[12]) {
      int handled = 0;
      CutePolarChartLayoutCall12 call = reinterpret_cast<CutePolarChartLayoutCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return AbstractChartLayout::count();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QGraphicsLayoutItem *AbstractChartLayout::itemAt(int a0) const
  QGraphicsLayoutItem *itemAt(int a0) const override {
    if (taken[13]) {
      int handled = 0;
      CutePolarChartLayoutCall13 call = reinterpret_cast<CutePolarChartLayoutCall13>(taken[13]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QGraphicsLayoutItem *>(given);
    }
    return AbstractChartLayout::itemAt(a0);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void AbstractChartLayout::removeAt(int a0)
  void removeAt(int a0) override {
    if (taken[14]) {
      int handled = 0;
      CutePolarChartLayoutCall14 call = reinterpret_cast<CutePolarChartLayoutCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    AbstractChartLayout::removeAt(a0);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsLayout::invalidate()
  void invalidate() override {
    if (taken[15]) {
      int handled = 0;
      CutePolarChartLayoutCall15 call = reinterpret_cast<CutePolarChartLayoutCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsLayout::invalidate();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsLayout::updateGeometry()
  void updateGeometry() override {
    if (taken[16]) {
      int handled = 0;
      CutePolarChartLayoutCall16 call = reinterpret_cast<CutePolarChartLayoutCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsLayout::updateGeometry();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsLayout::widgetEvent(QEvent *e)
  void widgetEvent(QEvent *e) override {
    if (taken[17]) {
      int handled = 0;
      CutePolarChartLayoutCall17 call = reinterpret_cast<CutePolarChartLayoutCall17>(taken[17]);
      call(this, e, &handled);
      if (handled) return;
    }
    QGraphicsLayout::widgetEvent(e);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsLayoutItem::isEmpty() const
  bool isEmpty() const override {
    if (taken[18]) {
      int handled = 0;
      CutePolarChartLayoutCall18 call = reinterpret_cast<CutePolarChartLayoutCall18>(taken[18]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsLayoutItem::isEmpty();
  }
#endif  // QT_CONFIG(graphicsview)
};

//  PolarChartLayout::PolarChartLayout(ChartPresenter *presenter)
extern "C" Q_DECL_EXPORT
PolarChartLayout *ritual_ZN16PolarChartLayoutC1EP14ChartPresenter(
    ChartPresenter *presenter) {
  return new CutePolarChartLayout(presenter);
}

//  PolarChartLayout::~PolarChartLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN16PolarChartLayoutD1Ev(PolarChartLayout *self) {
  delete self;
}

//  QRectF PolarChartLayout::calculateAxisMinimum(const QRectF &minimum,
//      const QList<ChartAxisElement *> &axes) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK16PolarChartLayout20calculateAxisMinimumERK6QRectFRK5QListIP16ChartAxisElementE(
    const PolarChartLayout *self,
    const QRectF *minimum,
    const QList<ChartAxisElement *> *axes) {
  return new QRectF(self->calculateAxisMinimum(*minimum, *axes));
}

//  QRectF PolarChartLayout::calculateAxisGeometry(const QRectF &geometry,
//      const QList<ChartAxisElement *> &axes, bool update) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK16PolarChartLayout21calculateAxisGeometryERK6QRectFRK5QListIP16ChartAxisElementEb(
    const PolarChartLayout *self,
    const QRectF *geometry,
    const QList<ChartAxisElement *> *axes,
    bool update) {
  return new QRectF(self->calculateAxisGeometry(*geometry, *axes, update));
}

//  a Python function taken by a CutePolarChartLayout, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_PolarChartLayout(
    PolarChartLayout *self,
    const char *key,
    void *call) {
  return static_cast<CutePolarChartLayout *>(self)->take(key, call);
}
