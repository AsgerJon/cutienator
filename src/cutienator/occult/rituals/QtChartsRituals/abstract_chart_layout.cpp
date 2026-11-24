//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/abstractchartlayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/abstractchartlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmargins.h>
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/chartaxiselement_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on AbstractChartLayout may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnAbstractChartLayout : AbstractChartLayout {
  using AbstractChartLayout::calculateBackgroundGeometry;
  using AbstractChartLayout::calculateBackgroundMinimum;
  using AbstractChartLayout::calculateContentGeometry;
  using AbstractChartLayout::calculateContentMinimum;
  using AbstractChartLayout::calculateTitleGeometry;
  using AbstractChartLayout::calculateTitleMinimum;
  using AbstractChartLayout::calculateLegendGeometry;
  using AbstractChartLayout::calculateLegendMinimum;
  using AbstractChartLayout::sizeHint;
  using AbstractChartLayout::count;
  using AbstractChartLayout::itemAt;
  using AbstractChartLayout::removeAt;
};

//  A AbstractChartLayout that Python can take functions over in. Every AbstractChartLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteAbstractChartLayoutCall0)(const void *, const QMargins *, int *);
typedef const QMargins * (*CuteAbstractChartLayoutCall1)(const void *, int *);
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractChartLayoutCall2)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef const QRectF * (*CuteAbstractChartLayoutCall3)(const void *, const QRectF *, ChartBackground *, bool, int *);
typedef const QRectF * (*CuteAbstractChartLayoutCall4)(const void *, const QRectF *, int *);
typedef const QRectF * (*CuteAbstractChartLayoutCall5)(const void *, const QRectF *, int *);
typedef const QRectF * (*CuteAbstractChartLayoutCall6)(const void *, const QRectF *, int *);
typedef const QRectF * (*CuteAbstractChartLayoutCall7)(const void *, const QRectF *, ChartTitle *, bool, int *);
typedef const QRectF * (*CuteAbstractChartLayoutCall8)(const void *, const QRectF *, ChartTitle *, int *);
typedef const QRectF * (*CuteAbstractChartLayoutCall9)(const void *, const QRectF *, QLegend *, bool, int *);
typedef const QRectF * (*CuteAbstractChartLayoutCall10)(const void *, const QRectF *, QLegend *, int *);
#if QT_CONFIG(graphicsview)
typedef const QSizeF * (*CuteAbstractChartLayoutCall11)(const void *, int, const QSizeF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteAbstractChartLayoutCall12)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void * (*CuteAbstractChartLayoutCall13)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractChartLayoutCall14)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractChartLayoutCall15)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractChartLayoutCall16)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteAbstractChartLayoutCall17)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteAbstractChartLayoutCall18)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteAbstractChartLayout : public AbstractChartLayout {
public:
  using AbstractChartLayout::AbstractChartLayout;
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
      CuteAbstractChartLayoutCall0 call = reinterpret_cast<CuteAbstractChartLayoutCall0>(taken[0]);
      call(this, &margins, &handled);
      if (handled) return;
    }
    AbstractChartLayout::setMargins(margins);
  }

  //  QMargins AbstractChartLayout::margins() const
  QMargins margins() const override {
    if (taken[1]) {
      int handled = 0;
      CuteAbstractChartLayoutCall1 call = reinterpret_cast<CuteAbstractChartLayoutCall1>(taken[1]);
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
      CuteAbstractChartLayoutCall2 call = reinterpret_cast<CuteAbstractChartLayoutCall2>(taken[2]);
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
      CuteAbstractChartLayoutCall3 call = reinterpret_cast<CuteAbstractChartLayoutCall3>(taken[3]);
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
      CuteAbstractChartLayoutCall4 call = reinterpret_cast<CuteAbstractChartLayoutCall4>(taken[4]);
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
      CuteAbstractChartLayoutCall5 call = reinterpret_cast<CuteAbstractChartLayoutCall5>(taken[5]);
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
      CuteAbstractChartLayoutCall6 call = reinterpret_cast<CuteAbstractChartLayoutCall6>(taken[6]);
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
      CuteAbstractChartLayoutCall7 call = reinterpret_cast<CuteAbstractChartLayoutCall7>(taken[7]);
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
      CuteAbstractChartLayoutCall8 call = reinterpret_cast<CuteAbstractChartLayoutCall8>(taken[8]);
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
      CuteAbstractChartLayoutCall9 call = reinterpret_cast<CuteAbstractChartLayoutCall9>(taken[9]);
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
      CuteAbstractChartLayoutCall10 call = reinterpret_cast<CuteAbstractChartLayoutCall10>(taken[10]);
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
      CuteAbstractChartLayoutCall11 call = reinterpret_cast<CuteAbstractChartLayoutCall11>(taken[11]);
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
      CuteAbstractChartLayoutCall12 call = reinterpret_cast<CuteAbstractChartLayoutCall12>(taken[12]);
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
      CuteAbstractChartLayoutCall13 call = reinterpret_cast<CuteAbstractChartLayoutCall13>(taken[13]);
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
      CuteAbstractChartLayoutCall14 call = reinterpret_cast<CuteAbstractChartLayoutCall14>(taken[14]);
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
      CuteAbstractChartLayoutCall15 call = reinterpret_cast<CuteAbstractChartLayoutCall15>(taken[15]);
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
      CuteAbstractChartLayoutCall16 call = reinterpret_cast<CuteAbstractChartLayoutCall16>(taken[16]);
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
      CuteAbstractChartLayoutCall17 call = reinterpret_cast<CuteAbstractChartLayoutCall17>(taken[17]);
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
      CuteAbstractChartLayoutCall18 call = reinterpret_cast<CuteAbstractChartLayoutCall18>(taken[18]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsLayoutItem::isEmpty();
  }
#endif  // QT_CONFIG(graphicsview)
};

//  AbstractChartLayout::~AbstractChartLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractChartLayoutD1Ev(AbstractChartLayout *self) {
  delete self;
}

//  void AbstractChartLayout::setMargins(const QMargins &margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractChartLayout10setMarginsERK8QMargins(
    AbstractChartLayout *self,
    const QMargins *margins) {
  self->setMargins(*margins);
}

//  QMargins AbstractChartLayout::margins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK19AbstractChartLayout7marginsEv(
    const AbstractChartLayout *self) {
  return new QMargins(self->margins());
}

//  void AbstractChartLayout::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractChartLayout11setGeometryERK6QRectF(
    AbstractChartLayout *self,
    const QRectF *rect) {
  self->setGeometry(*rect);
}

//  QRectF AbstractChartLayout::calculateBackgroundGeometry(const QRectF
//      &geometry, ChartBackground *background, bool update) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19AbstractChartLayout27calculateBackgroundGeometryERK6QRectFP15ChartBackgroundb(
    const AbstractChartLayout *self,
    const QRectF *geometry,
    ChartBackground *background,
    bool update) {
  return new QRectF(
      self->calculateBackgroundGeometry(
          *geometry,
          background,
          update));
}

//  QRectF AbstractChartLayout::calculateBackgroundMinimum(const QRectF
//      &minimum) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19AbstractChartLayout26calculateBackgroundMinimumERK6QRectF(
    const AbstractChartLayout *self,
    const QRectF *minimum) {
  return new QRectF(self->calculateBackgroundMinimum(*minimum));
}

//  QRectF AbstractChartLayout::calculateContentGeometry(const QRectF
//      &geometry) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19AbstractChartLayout24calculateContentGeometryERK6QRectF(
    const AbstractChartLayout *self,
    const QRectF *geometry) {
  return new QRectF(self->calculateContentGeometry(*geometry));
}

//  QRectF AbstractChartLayout::calculateContentMinimum(const QRectF
//      &minimum) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19AbstractChartLayout23calculateContentMinimumERK6QRectF(
    const AbstractChartLayout *self,
    const QRectF *minimum) {
  return new QRectF(self->calculateContentMinimum(*minimum));
}

//  QRectF AbstractChartLayout::calculateTitleGeometry(const QRectF
//      &geometry, ChartTitle *title, bool update) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19AbstractChartLayout22calculateTitleGeometryERK6QRectFP10ChartTitleb(
    const AbstractChartLayout *self,
    const QRectF *geometry,
    ChartTitle *title,
    bool update) {
  return new QRectF(self->calculateTitleGeometry(*geometry, title, update));
}

//  QRectF AbstractChartLayout::calculateTitleMinimum(const QRectF &minimum,
//      ChartTitle *title) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19AbstractChartLayout21calculateTitleMinimumERK6QRectFP10ChartTitle(
    const AbstractChartLayout *self,
    const QRectF *minimum,
    ChartTitle *title) {
  return new QRectF(self->calculateTitleMinimum(*minimum, title));
}

//  QRectF AbstractChartLayout::calculateLegendGeometry(const QRectF
//      &geometry, QLegend *legend, bool update) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19AbstractChartLayout23calculateLegendGeometryERK6QRectFP7QLegendb(
    const AbstractChartLayout *self,
    const QRectF *geometry,
    QLegend *legend,
    bool update) {
  return new QRectF(
      self->calculateLegendGeometry(
          *geometry,
          legend,
          update));
}

//  QRectF AbstractChartLayout::calculateLegendMinimum(const QRectF &minimum,
//      QLegend *legend) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19AbstractChartLayout22calculateLegendMinimumERK6QRectFP7QLegend(
    const AbstractChartLayout *self,
    const QRectF *minimum,
    QLegend *legend) {
  return new QRectF(self->calculateLegendMinimum(*minimum, legend));
}

//  QRectF AbstractChartLayout::calculateAxisGeometry(const QRectF &geometry,
//      const QList<ChartAxisElement *> &axes, bool update) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19AbstractChartLayout21calculateAxisGeometryERK6QRectFRK5QListIP16ChartAxisElementEb(
    const AbstractChartLayout *self,
    const QRectF *geometry,
    const QList<ChartAxisElement *> *axes,
    bool update) {
  return new QRectF(self->calculateAxisGeometry(*geometry, *axes, update));
}

//  QRectF AbstractChartLayout::calculateAxisMinimum(const QRectF &minimum,
//      const QList<ChartAxisElement *> &axes) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19AbstractChartLayout20calculateAxisMinimumERK6QRectFRK5QListIP16ChartAxisElementE(
    const AbstractChartLayout *self,
    const QRectF *minimum,
    const QList<ChartAxisElement *> *axes) {
  return new QRectF(self->calculateAxisMinimum(*minimum, *axes));
}

//  QSizeF AbstractChartLayout::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK19AbstractChartLayout8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const AbstractChartLayout *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->sizeHint(which, *constraint));
}

//  int AbstractChartLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19AbstractChartLayout5countEv(
    const AbstractChartLayout *self) {
  return self->count();
}

//  QGraphicsLayoutItem *AbstractChartLayout::itemAt(int a0) const
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_ZNK19AbstractChartLayout6itemAtEi(
    const AbstractChartLayout *self,
    int a0) {
  return self->itemAt(a0);
}

//  void AbstractChartLayout::removeAt(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19AbstractChartLayout8removeAtEi(
    AbstractChartLayout *self,
    int a0) {
  self->removeAt(a0);
}

//  a Python function taken by a CuteAbstractChartLayout, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_AbstractChartLayout(
    AbstractChartLayout *self,
    const char *key,
    void *call) {
  return static_cast<CuteAbstractChartLayout *>(self)->take(key, call);
}

//  void AbstractChartLayout::setMargins(const QMargins &margins)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19AbstractChartLayout10setMarginsERK8QMargins(
    AbstractChartLayout *self,
    const QMargins *margins) {
  self->AbstractChartLayout::setMargins(*margins);
}

//  QMargins AbstractChartLayout::margins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_own_ZNK19AbstractChartLayout7marginsEv(
    const AbstractChartLayout *self) {
  return new QMargins(self->AbstractChartLayout::margins());
}

//  void AbstractChartLayout::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19AbstractChartLayout11setGeometryERK6QRectF(
    AbstractChartLayout *self,
    const QRectF *rect) {
  self->AbstractChartLayout::setGeometry(*rect);
}

//  QRectF AbstractChartLayout::calculateBackgroundGeometry(const QRectF
//      &geometry, ChartBackground *background, bool update) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK19AbstractChartLayout27calculateBackgroundGeometryERK6QRectFP15ChartBackgroundb(
    const AbstractChartLayout *self,
    const QRectF *geometry,
    ChartBackground *background,
    bool update) {
  return new QRectF(
      static_cast<const OwnAbstractChartLayout *>(self)->OwnAbstractChartLayout::calculateBackgroundGeometry(
          *geometry,
          background,
          update));
}

//  QRectF AbstractChartLayout::calculateBackgroundMinimum(const QRectF
//      &minimum) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK19AbstractChartLayout26calculateBackgroundMinimumERK6QRectF(
    const AbstractChartLayout *self,
    const QRectF *minimum) {
  return new QRectF(
      static_cast<const OwnAbstractChartLayout *>(self)->OwnAbstractChartLayout::calculateBackgroundMinimum(
          *minimum));
}

//  QRectF AbstractChartLayout::calculateContentGeometry(const QRectF
//      &geometry) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK19AbstractChartLayout24calculateContentGeometryERK6QRectF(
    const AbstractChartLayout *self,
    const QRectF *geometry) {
  return new QRectF(
      static_cast<const OwnAbstractChartLayout *>(self)->OwnAbstractChartLayout::calculateContentGeometry(
          *geometry));
}

//  QRectF AbstractChartLayout::calculateContentMinimum(const QRectF
//      &minimum) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK19AbstractChartLayout23calculateContentMinimumERK6QRectF(
    const AbstractChartLayout *self,
    const QRectF *minimum) {
  return new QRectF(
      static_cast<const OwnAbstractChartLayout *>(self)->OwnAbstractChartLayout::calculateContentMinimum(
          *minimum));
}

//  QRectF AbstractChartLayout::calculateTitleGeometry(const QRectF
//      &geometry, ChartTitle *title, bool update) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK19AbstractChartLayout22calculateTitleGeometryERK6QRectFP10ChartTitleb(
    const AbstractChartLayout *self,
    const QRectF *geometry,
    ChartTitle *title,
    bool update) {
  return new QRectF(
      static_cast<const OwnAbstractChartLayout *>(self)->OwnAbstractChartLayout::calculateTitleGeometry(
          *geometry,
          title,
          update));
}

//  QRectF AbstractChartLayout::calculateTitleMinimum(const QRectF &minimum,
//      ChartTitle *title) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK19AbstractChartLayout21calculateTitleMinimumERK6QRectFP10ChartTitle(
    const AbstractChartLayout *self,
    const QRectF *minimum,
    ChartTitle *title) {
  return new QRectF(
      static_cast<const OwnAbstractChartLayout *>(self)->OwnAbstractChartLayout::calculateTitleMinimum(
          *minimum,
          title));
}

//  QRectF AbstractChartLayout::calculateLegendGeometry(const QRectF
//      &geometry, QLegend *legend, bool update) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK19AbstractChartLayout23calculateLegendGeometryERK6QRectFP7QLegendb(
    const AbstractChartLayout *self,
    const QRectF *geometry,
    QLegend *legend,
    bool update) {
  return new QRectF(
      static_cast<const OwnAbstractChartLayout *>(self)->OwnAbstractChartLayout::calculateLegendGeometry(
          *geometry,
          legend,
          update));
}

//  QRectF AbstractChartLayout::calculateLegendMinimum(const QRectF &minimum,
//      QLegend *legend) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK19AbstractChartLayout22calculateLegendMinimumERK6QRectFP7QLegend(
    const AbstractChartLayout *self,
    const QRectF *minimum,
    QLegend *legend) {
  return new QRectF(
      static_cast<const OwnAbstractChartLayout *>(self)->OwnAbstractChartLayout::calculateLegendMinimum(
          *minimum,
          legend));
}

//  QSizeF AbstractChartLayout::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK19AbstractChartLayout8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const AbstractChartLayout *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(
      static_cast<const OwnAbstractChartLayout *>(self)->OwnAbstractChartLayout::sizeHint(
          which,
          *constraint));
}

//  int AbstractChartLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19AbstractChartLayout5countEv(
    const AbstractChartLayout *self) {
  return static_cast<const OwnAbstractChartLayout *>(self)->OwnAbstractChartLayout::count();
}

//  QGraphicsLayoutItem *AbstractChartLayout::itemAt(int a0) const
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_own_ZNK19AbstractChartLayout6itemAtEi(
    const AbstractChartLayout *self,
    int a0) {
  return static_cast<const OwnAbstractChartLayout *>(self)->OwnAbstractChartLayout::itemAt(
      a0);
}

//  void AbstractChartLayout::removeAt(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19AbstractChartLayout8removeAtEi(
    AbstractChartLayout *self,
    int a0) {
  static_cast<OwnAbstractChartLayout *>(self)->OwnAbstractChartLayout::removeAt(
      a0);
}
