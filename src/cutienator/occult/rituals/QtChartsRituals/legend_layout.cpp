//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/legendlayout_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/legendlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <cstring>

//  Only a class built on LegendLayout may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnLegendLayout : LegendLayout {
  using LegendLayout::sizeHint;
  using LegendLayout::count;
  using LegendLayout::itemAt;
  using LegendLayout::removeAt;
};

//  A LegendLayout that Python can take functions over in. Every LegendLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendLayoutCall0)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendLayoutCall1)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QSizeF * (*CuteLegendLayoutCall2)(const void *, int, const QSizeF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteLegendLayoutCall3)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void * (*CuteLegendLayoutCall4)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendLayoutCall5)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendLayoutCall6)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteLegendLayoutCall7)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteLegendLayoutCall8)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteLegendLayout : public LegendLayout {
public:
  using LegendLayout::LegendLayout;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem11setGeometryERK6QRectF")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsLayout10invalidateEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGraphicsLayout5countEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGraphicsLayout6itemAtEi")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsLayout8removeAtEi")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem14updateGeometryEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsLayout11widgetEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem7isEmptyEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    return false;
  }

#if QT_CONFIG(graphicsview)
  //  void LegendLayout::setGeometry(const QRectF &rect)
  void setGeometry(const QRectF &rect) override {
    if (taken[0]) {
      int handled = 0;
      CuteLegendLayoutCall0 call = reinterpret_cast<CuteLegendLayoutCall0>(taken[0]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    LegendLayout::setGeometry(rect);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void LegendLayout::invalidate()
  void invalidate() override {
    if (taken[1]) {
      int handled = 0;
      CuteLegendLayoutCall1 call = reinterpret_cast<CuteLegendLayoutCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    LegendLayout::invalidate();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QSizeF LegendLayout::sizeHint(Qt::SizeHint which, const QSizeF
  //      &constraint) const
  QSizeF sizeHint(
      Qt::SizeHint which,
      const QSizeF &constraint) const override {
    if (taken[2]) {
      int handled = 0;
      CuteLegendLayoutCall2 call = reinterpret_cast<CuteLegendLayoutCall2>(taken[2]);
      const QSizeF * given = call(this, static_cast<int>(which), &constraint, &handled);
      if (handled && given) return *given;
    }
    return LegendLayout::sizeHint(which, constraint);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  int LegendLayout::count() const
  int count() const override {
    if (taken[3]) {
      int handled = 0;
      CuteLegendLayoutCall3 call = reinterpret_cast<CuteLegendLayoutCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return LegendLayout::count();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QGraphicsLayoutItem *LegendLayout::itemAt(int a0) const
  QGraphicsLayoutItem *itemAt(int a0) const override {
    if (taken[4]) {
      int handled = 0;
      CuteLegendLayoutCall4 call = reinterpret_cast<CuteLegendLayoutCall4>(taken[4]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QGraphicsLayoutItem *>(given);
    }
    return LegendLayout::itemAt(a0);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void LegendLayout::removeAt(int a0)
  void removeAt(int a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteLegendLayoutCall5 call = reinterpret_cast<CuteLegendLayoutCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    LegendLayout::removeAt(a0);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsLayout::updateGeometry()
  void updateGeometry() override {
    if (taken[6]) {
      int handled = 0;
      CuteLegendLayoutCall6 call = reinterpret_cast<CuteLegendLayoutCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsLayout::updateGeometry();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsLayout::widgetEvent(QEvent *e)
  void widgetEvent(QEvent *e) override {
    if (taken[7]) {
      int handled = 0;
      CuteLegendLayoutCall7 call = reinterpret_cast<CuteLegendLayoutCall7>(taken[7]);
      call(this, e, &handled);
      if (handled) return;
    }
    QGraphicsLayout::widgetEvent(e);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsLayoutItem::isEmpty() const
  bool isEmpty() const override {
    if (taken[8]) {
      int handled = 0;
      CuteLegendLayoutCall8 call = reinterpret_cast<CuteLegendLayoutCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsLayoutItem::isEmpty();
  }
#endif  // QT_CONFIG(graphicsview)
};

//  LegendLayout::LegendLayout(QLegend *legend)
extern "C" Q_DECL_EXPORT
LegendLayout *ritual_ZN12LegendLayoutC1EP7QLegend(QLegend *legend) {
  return new CuteLegendLayout(legend);
}

//  LegendLayout::~LegendLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN12LegendLayoutD1Ev(LegendLayout *self) {
  delete self;
}

//  void LegendLayout::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN12LegendLayout11setGeometryERK6QRectF(
    LegendLayout *self,
    const QRectF *rect) {
  self->setGeometry(*rect);
}

//  void LegendLayout::setOffset(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN12LegendLayout9setOffsetEdd(
    LegendLayout *self,
    qreal x,
    qreal y) {
  self->setOffset(x, y);
}

//  QPointF LegendLayout::offset() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK12LegendLayout6offsetEv(const LegendLayout *self) {
  return new QPointF(self->offset());
}

//  void LegendLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN12LegendLayout10invalidateEv(LegendLayout *self) {
  self->invalidate();
}

//  QSizeF LegendLayout::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK12LegendLayout8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const LegendLayout *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->sizeHint(which, *constraint));
}

//  int LegendLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12LegendLayout5countEv(const LegendLayout *self) {
  return self->count();
}

//  QGraphicsLayoutItem *LegendLayout::itemAt(int a0) const
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_ZNK12LegendLayout6itemAtEi(
    const LegendLayout *self,
    int a0) {
  return self->itemAt(a0);
}

//  void LegendLayout::removeAt(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12LegendLayout8removeAtEi(LegendLayout *self, int a0) {
  self->removeAt(a0);
}

//  void LegendLayout::setAttachedGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN12LegendLayout19setAttachedGeometryERK6QRectF(
    LegendLayout *self,
    const QRectF *rect) {
  self->setAttachedGeometry(*rect);
}

//  void LegendLayout::setDettachedGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN12LegendLayout20setDettachedGeometryERK6QRectF(
    LegendLayout *self,
    const QRectF *rect) {
  self->setDettachedGeometry(*rect);
}

//  bool LegendLayout::widthLongerThan(const LegendWidthStruct *item1, const
//      LegendWidthStruct *item2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12LegendLayout15widthLongerThanEPKNS_17LegendWidthStructES2_(
    const LegendLayout::LegendWidthStruct *item1,
    const LegendLayout::LegendWidthStruct *item2) {
  return LegendLayout::widthLongerThan(item1, item2);
}

//  a Python function taken by a CuteLegendLayout, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_LegendLayout(
    LegendLayout *self,
    const char *key,
    void *call) {
  return static_cast<CuteLegendLayout *>(self)->take(key, call);
}

//  void LegendLayout::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12LegendLayout11setGeometryERK6QRectF(
    LegendLayout *self,
    const QRectF *rect) {
  self->LegendLayout::setGeometry(*rect);
}

//  void LegendLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12LegendLayout10invalidateEv(LegendLayout *self) {
  self->LegendLayout::invalidate();
}

//  QSizeF LegendLayout::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK12LegendLayout8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const LegendLayout *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(
      static_cast<const OwnLegendLayout *>(self)->OwnLegendLayout::sizeHint(
          which,
          *constraint));
}

//  int LegendLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK12LegendLayout5countEv(const LegendLayout *self) {
  return static_cast<const OwnLegendLayout *>(self)->OwnLegendLayout::count();
}

//  QGraphicsLayoutItem *LegendLayout::itemAt(int a0) const
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_own_ZNK12LegendLayout6itemAtEi(
    const LegendLayout *self,
    int a0) {
  return static_cast<const OwnLegendLayout *>(self)->OwnLegendLayout::itemAt(
      a0);
}

//  void LegendLayout::removeAt(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12LegendLayout8removeAtEi(LegendLayout *self, int a0) {
  static_cast<OwnLegendLayout *>(self)->OwnLegendLayout::removeAt(a0);
}
