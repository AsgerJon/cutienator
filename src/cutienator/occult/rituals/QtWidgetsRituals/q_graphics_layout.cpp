//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicslayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicslayout.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QGraphicsLayout that Python can take functions over in. Every QGraphicsLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphicsLayoutCall0)(const void *, int *);
typedef void (*CuteQGraphicsLayoutCall1)(const void *, int *);
typedef void (*CuteQGraphicsLayoutCall2)(const void *, QEvent *, int *);
typedef int (*CuteQGraphicsLayoutCall3)(const void *, int *);
typedef void * (*CuteQGraphicsLayoutCall4)(const void *, int, int *);
typedef void (*CuteQGraphicsLayoutCall5)(const void *, int, int *);
typedef void (*CuteQGraphicsLayoutCall6)(const void *, const QRectF *, int *);
typedef bool (*CuteQGraphicsLayoutCall7)(const void *, int *);
typedef const QSizeF * (*CuteQGraphicsLayoutCall8)(const void *, int, const QSizeF *, int *);
class CuteQGraphicsLayout : public QGraphicsLayout {
public:
  using QGraphicsLayout::QGraphicsLayout;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QGraphicsLayout10invalidateEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem14updateGeometryEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsLayout11widgetEventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QGraphicsLayout5countEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QGraphicsLayout6itemAtEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsLayout8removeAtEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem11setGeometryERK6QRectF")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem7isEmptyEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF")) {
      taken[8] = call;
      return true;
    }
    return false;
  }

  //  void QGraphicsLayout::invalidate()
  void invalidate() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsLayoutCall0 call = reinterpret_cast<CuteQGraphicsLayoutCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsLayout::invalidate();
  }

  //  void QGraphicsLayout::updateGeometry()
  void updateGeometry() override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsLayoutCall1 call = reinterpret_cast<CuteQGraphicsLayoutCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsLayout::updateGeometry();
  }

  //  void QGraphicsLayout::widgetEvent(QEvent *e)
  void widgetEvent(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsLayoutCall2 call = reinterpret_cast<CuteQGraphicsLayoutCall2>(taken[2]);
      call(this, e, &handled);
      if (handled) return;
    }
    QGraphicsLayout::widgetEvent(e);
  }

  //  int QGraphicsLayout::count() const
  int count() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsLayoutCall3 call = reinterpret_cast<CuteQGraphicsLayoutCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QGraphicsLayoutItem *QGraphicsLayout::itemAt(int i) const
  QGraphicsLayoutItem *itemAt(int i) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsLayoutCall4 call = reinterpret_cast<CuteQGraphicsLayoutCall4>(taken[4]);
      void * given = call(this, i, &handled);
      if (handled) return static_cast<QGraphicsLayoutItem *>(given);
    }
    return {};
  }

  //  void QGraphicsLayout::removeAt(int index)
  void removeAt(int index) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsLayoutCall5 call = reinterpret_cast<CuteQGraphicsLayoutCall5>(taken[5]);
      call(this, index, &handled);
      if (handled) return;
    }
  }

  //  void QGraphicsLayoutItem::setGeometry(const QRectF &rect)
  void setGeometry(const QRectF &rect) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsLayoutCall6 call = reinterpret_cast<CuteQGraphicsLayoutCall6>(taken[6]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QGraphicsLayoutItem::setGeometry(rect);
  }

  //  bool QGraphicsLayoutItem::isEmpty() const
  bool isEmpty() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsLayoutCall7 call = reinterpret_cast<CuteQGraphicsLayoutCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsLayoutItem::isEmpty();
  }

  //  QSizeF QGraphicsLayoutItem::sizeHint(Qt::SizeHint which, const QSizeF
  //      &constraint) const
  QSizeF sizeHint(
      Qt::SizeHint which,
      const QSizeF &constraint) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsLayoutCall8 call = reinterpret_cast<CuteQGraphicsLayoutCall8>(taken[8]);
      const QSizeF * given = call(this, static_cast<int>(which), &constraint, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QGraphicsLayout::~QGraphicsLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsLayoutD1Ev(QGraphicsLayout *self) {
  delete self;
}

//  void QGraphicsLayout::setContentsMargins(qreal left, qreal top, qreal
//      right, qreal bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsLayout18setContentsMarginsEdddd(
    QGraphicsLayout *self,
    qreal left,
    qreal top,
    qreal right,
    qreal bottom) {
  self->setContentsMargins(left, top, right, bottom);
}

//  void QGraphicsLayout::getContentsMargins(qreal *left, qreal *top, qreal
//      *right, qreal *bottom) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QGraphicsLayout18getContentsMarginsEPdS0_S0_S0_(
    const QGraphicsLayout *self,
    qreal *left,
    qreal *top,
    qreal *right,
    qreal *bottom) {
  self->getContentsMargins(left, top, right, bottom);
}

//  void QGraphicsLayout::activate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsLayout8activateEv(QGraphicsLayout *self) {
  self->activate();
}

//  bool QGraphicsLayout::isActivated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QGraphicsLayout11isActivatedEv(
    const QGraphicsLayout *self) {
  return self->isActivated();
}

//  void QGraphicsLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsLayout10invalidateEv(QGraphicsLayout *self) {
  self->invalidate();
}

//  void QGraphicsLayout::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsLayout14updateGeometryEv(QGraphicsLayout *self) {
  self->updateGeometry();
}

//  void QGraphicsLayout::widgetEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsLayout11widgetEventEP6QEvent(
    QGraphicsLayout *self,
    QEvent *e) {
  self->widgetEvent(e);
}

//  int QGraphicsLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGraphicsLayout5countEv(const QGraphicsLayout *self) {
  return self->count();
}

//  QGraphicsLayoutItem *QGraphicsLayout::itemAt(int i) const
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_ZNK15QGraphicsLayout6itemAtEi(
    const QGraphicsLayout *self,
    int i) {
  return self->itemAt(i);
}

//  void QGraphicsLayout::removeAt(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsLayout8removeAtEi(
    QGraphicsLayout *self,
    int index) {
  self->removeAt(index);
}

//  void QGraphicsLayout::setInstantInvalidatePropagation(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsLayout31setInstantInvalidatePropagationEb(
    bool enable) {
  QGraphicsLayout::setInstantInvalidatePropagation(enable);
}

//  bool QGraphicsLayout::instantInvalidatePropagation()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QGraphicsLayout28instantInvalidatePropagationEv() {
  return QGraphicsLayout::instantInvalidatePropagation();
}

//  void QGraphicsLayout::addChildLayoutItem(QGraphicsLayoutItem *layoutItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsLayout18addChildLayoutItemEP19QGraphicsLayoutItem(
    QGraphicsLayout *self,
    QGraphicsLayoutItem *layoutItem) {
  self->addChildLayoutItem(layoutItem);
}

//  a Python function taken by a CuteQGraphicsLayout, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsLayout(
    QGraphicsLayout *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsLayout *>(self)->take(key, call);
}

//  void QGraphicsLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsLayout10invalidateEv(QGraphicsLayout *self) {
  self->QGraphicsLayout::invalidate();
}

//  void QGraphicsLayout::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsLayout14updateGeometryEv(
    QGraphicsLayout *self) {
  self->QGraphicsLayout::updateGeometry();
}

//  void QGraphicsLayout::widgetEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsLayout11widgetEventEP6QEvent(
    QGraphicsLayout *self,
    QEvent *e) {
  self->QGraphicsLayout::widgetEvent(e);
}
