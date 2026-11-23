//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsanchorlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsanchorlayout.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <cstring>

//  Only a class built on QGraphicsAnchorLayout may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsAnchorLayout : QGraphicsAnchorLayout {
  using QGraphicsAnchorLayout::sizeHint;
};

//  A QGraphicsAnchorLayout that Python can take functions over in. Every QGraphicsAnchorLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphicsAnchorLayoutCall0)(const void *, int, int *);
typedef void (*CuteQGraphicsAnchorLayoutCall1)(const void *, const QRectF *, int *);
typedef int (*CuteQGraphicsAnchorLayoutCall2)(const void *, int *);
typedef void * (*CuteQGraphicsAnchorLayoutCall3)(const void *, int, int *);
typedef void (*CuteQGraphicsAnchorLayoutCall4)(const void *, int *);
typedef const QSizeF * (*CuteQGraphicsAnchorLayoutCall5)(const void *, int, const QSizeF *, int *);
typedef void (*CuteQGraphicsAnchorLayoutCall6)(const void *, int *);
typedef void (*CuteQGraphicsAnchorLayoutCall7)(const void *, QEvent *, int *);
typedef bool (*CuteQGraphicsAnchorLayoutCall8)(const void *, int *);
class CuteQGraphicsAnchorLayout : public QGraphicsAnchorLayout {
public:
  using QGraphicsAnchorLayout::QGraphicsAnchorLayout;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QGraphicsLayout8removeAtEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem11setGeometryERK6QRectF")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QGraphicsLayout5countEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QGraphicsLayout6itemAtEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsLayout10invalidateEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem14updateGeometryEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsLayout11widgetEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem7isEmptyEv")) {
      taken[8] = call;
      return true;
    }
    return false;
  }

  //  void QGraphicsAnchorLayout::removeAt(int index)
  void removeAt(int index) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsAnchorLayoutCall0 call = reinterpret_cast<CuteQGraphicsAnchorLayoutCall0>(taken[0]);
      call(this, index, &handled);
      if (handled) return;
    }
    QGraphicsAnchorLayout::removeAt(index);
  }

  //  void QGraphicsAnchorLayout::setGeometry(const QRectF &rect)
  void setGeometry(const QRectF &rect) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsAnchorLayoutCall1 call = reinterpret_cast<CuteQGraphicsAnchorLayoutCall1>(taken[1]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QGraphicsAnchorLayout::setGeometry(rect);
  }

  //  int QGraphicsAnchorLayout::count() const
  int count() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsAnchorLayoutCall2 call = reinterpret_cast<CuteQGraphicsAnchorLayoutCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsAnchorLayout::count();
  }

  //  QGraphicsLayoutItem *QGraphicsAnchorLayout::itemAt(int index) const
  QGraphicsLayoutItem *itemAt(int index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsAnchorLayoutCall3 call = reinterpret_cast<CuteQGraphicsAnchorLayoutCall3>(taken[3]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QGraphicsLayoutItem *>(given);
    }
    return QGraphicsAnchorLayout::itemAt(index);
  }

  //  void QGraphicsAnchorLayout::invalidate()
  void invalidate() override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsAnchorLayoutCall4 call = reinterpret_cast<CuteQGraphicsAnchorLayoutCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsAnchorLayout::invalidate();
  }

  //  QSizeF QGraphicsAnchorLayout::sizeHint(Qt::SizeHint which, const
  //      QSizeF &constraint) const
  QSizeF sizeHint(
      Qt::SizeHint which,
      const QSizeF &constraint) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsAnchorLayoutCall5 call = reinterpret_cast<CuteQGraphicsAnchorLayoutCall5>(taken[5]);
      const QSizeF * given = call(this, static_cast<int>(which), &constraint, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsAnchorLayout::sizeHint(which, constraint);
  }

  //  void QGraphicsLayout::updateGeometry()
  void updateGeometry() override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsAnchorLayoutCall6 call = reinterpret_cast<CuteQGraphicsAnchorLayoutCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsLayout::updateGeometry();
  }

  //  void QGraphicsLayout::widgetEvent(QEvent *e)
  void widgetEvent(QEvent *e) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsAnchorLayoutCall7 call = reinterpret_cast<CuteQGraphicsAnchorLayoutCall7>(taken[7]);
      call(this, e, &handled);
      if (handled) return;
    }
    QGraphicsLayout::widgetEvent(e);
  }

  //  bool QGraphicsLayoutItem::isEmpty() const
  bool isEmpty() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsAnchorLayoutCall8 call = reinterpret_cast<CuteQGraphicsAnchorLayoutCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsLayoutItem::isEmpty();
  }
};

//  QGraphicsAnchorLayout::QGraphicsAnchorLayout(QGraphicsLayoutItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsAnchorLayout *ritual_ZN21QGraphicsAnchorLayoutC1EP19QGraphicsLayoutItem(
    QGraphicsLayoutItem *parent) {
  return new CuteQGraphicsAnchorLayout(parent);
}

//  QGraphicsAnchorLayout::~QGraphicsAnchorLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsAnchorLayoutD1Ev(QGraphicsAnchorLayout *self) {
  delete self;
}

//  QGraphicsAnchor *QGraphicsAnchorLayout::addAnchor(QGraphicsLayoutItem
//      *firstItem, Qt::AnchorPoint firstEdge, QGraphicsLayoutItem
//      *secondItem, Qt::AnchorPoint secondEdge)
extern "C" Q_DECL_EXPORT
QGraphicsAnchor *ritual_ZN21QGraphicsAnchorLayout9addAnchorEP19QGraphicsLayoutItemN2Qt11AnchorPointES1_S3_(
    QGraphicsAnchorLayout *self,
    QGraphicsLayoutItem *firstItem,
    Qt::AnchorPoint firstEdge,
    QGraphicsLayoutItem *secondItem,
    Qt::AnchorPoint secondEdge) {
  return self->addAnchor(firstItem, firstEdge, secondItem, secondEdge);
}

//  QGraphicsAnchor *QGraphicsAnchorLayout::anchor(QGraphicsLayoutItem
//      *firstItem, Qt::AnchorPoint firstEdge, QGraphicsLayoutItem
//      *secondItem, Qt::AnchorPoint secondEdge)
extern "C" Q_DECL_EXPORT
QGraphicsAnchor *ritual_ZN21QGraphicsAnchorLayout6anchorEP19QGraphicsLayoutItemN2Qt11AnchorPointES1_S3_(
    QGraphicsAnchorLayout *self,
    QGraphicsLayoutItem *firstItem,
    Qt::AnchorPoint firstEdge,
    QGraphicsLayoutItem *secondItem,
    Qt::AnchorPoint secondEdge) {
  return self->anchor(firstItem, firstEdge, secondItem, secondEdge);
}

//  void QGraphicsAnchorLayout::addCornerAnchors(QGraphicsLayoutItem
//      *firstItem, Qt::Corner firstCorner, QGraphicsLayoutItem *secondItem,
//      Qt::Corner secondCorner)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsAnchorLayout16addCornerAnchorsEP19QGraphicsLayoutItemN2Qt6CornerES1_S3_(
    QGraphicsAnchorLayout *self,
    QGraphicsLayoutItem *firstItem,
    Qt::Corner firstCorner,
    QGraphicsLayoutItem *secondItem,
    Qt::Corner secondCorner) {
  self->addCornerAnchors(firstItem, firstCorner, secondItem, secondCorner);
}

//  void QGraphicsAnchorLayout::addAnchors(QGraphicsLayoutItem *firstItem,
//      QGraphicsLayoutItem *secondItem, Qt::Orientations orientations)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsAnchorLayout10addAnchorsEP19QGraphicsLayoutItemS1_6QFlagsIN2Qt11OrientationEE(
    QGraphicsAnchorLayout *self,
    QGraphicsLayoutItem *firstItem,
    QGraphicsLayoutItem *secondItem,
    int orientations) {
  self->addAnchors(
      firstItem,
      secondItem,
      QFlags<Qt::Orientation>::fromInt(orientations));
}

//  void QGraphicsAnchorLayout::setHorizontalSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsAnchorLayout20setHorizontalSpacingEd(
    QGraphicsAnchorLayout *self,
    qreal spacing) {
  self->setHorizontalSpacing(spacing);
}

//  void QGraphicsAnchorLayout::setVerticalSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsAnchorLayout18setVerticalSpacingEd(
    QGraphicsAnchorLayout *self,
    qreal spacing) {
  self->setVerticalSpacing(spacing);
}

//  void QGraphicsAnchorLayout::setSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsAnchorLayout10setSpacingEd(
    QGraphicsAnchorLayout *self,
    qreal spacing) {
  self->setSpacing(spacing);
}

//  qreal QGraphicsAnchorLayout::horizontalSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QGraphicsAnchorLayout17horizontalSpacingEv(
    const QGraphicsAnchorLayout *self) {
  return self->horizontalSpacing();
}

//  qreal QGraphicsAnchorLayout::verticalSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QGraphicsAnchorLayout15verticalSpacingEv(
    const QGraphicsAnchorLayout *self) {
  return self->verticalSpacing();
}

//  void QGraphicsAnchorLayout::removeAt(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsAnchorLayout8removeAtEi(
    QGraphicsAnchorLayout *self,
    int index) {
  self->removeAt(index);
}

//  void QGraphicsAnchorLayout::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsAnchorLayout11setGeometryERK6QRectF(
    QGraphicsAnchorLayout *self,
    const QRectF *rect) {
  self->setGeometry(*rect);
}

//  int QGraphicsAnchorLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QGraphicsAnchorLayout5countEv(
    const QGraphicsAnchorLayout *self) {
  return self->count();
}

//  QGraphicsLayoutItem *QGraphicsAnchorLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_ZNK21QGraphicsAnchorLayout6itemAtEi(
    const QGraphicsAnchorLayout *self,
    int index) {
  return self->itemAt(index);
}

//  void QGraphicsAnchorLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsAnchorLayout10invalidateEv(
    QGraphicsAnchorLayout *self) {
  self->invalidate();
}

//  QSizeF QGraphicsAnchorLayout::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK21QGraphicsAnchorLayout8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const QGraphicsAnchorLayout *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->sizeHint(which, *constraint));
}

//  QGraphicsAnchorLayoutPrivate *QGraphicsAnchorLayout::d_func()
extern "C" Q_DECL_EXPORT
QGraphicsAnchorLayoutPrivate *ritual_ZN21QGraphicsAnchorLayout6d_funcEv(
    QGraphicsAnchorLayout *self) {
  return self->d_func();
}

//  const QGraphicsAnchorLayoutPrivate *QGraphicsAnchorLayout::d_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsAnchorLayoutPrivate *ritual_ZNK21QGraphicsAnchorLayout6d_funcEv(
    const QGraphicsAnchorLayout *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQGraphicsAnchorLayout, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsAnchorLayout(
    QGraphicsAnchorLayout *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsAnchorLayout *>(self)->take(key, call);
}

//  void QGraphicsAnchorLayout::removeAt(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QGraphicsAnchorLayout8removeAtEi(
    QGraphicsAnchorLayout *self,
    int index) {
  self->QGraphicsAnchorLayout::removeAt(index);
}

//  void QGraphicsAnchorLayout::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QGraphicsAnchorLayout11setGeometryERK6QRectF(
    QGraphicsAnchorLayout *self,
    const QRectF *rect) {
  self->QGraphicsAnchorLayout::setGeometry(*rect);
}

//  int QGraphicsAnchorLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QGraphicsAnchorLayout5countEv(
    const QGraphicsAnchorLayout *self) {
  return self->QGraphicsAnchorLayout::count();
}

//  QGraphicsLayoutItem *QGraphicsAnchorLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_own_ZNK21QGraphicsAnchorLayout6itemAtEi(
    const QGraphicsAnchorLayout *self,
    int index) {
  return self->QGraphicsAnchorLayout::itemAt(index);
}

//  void QGraphicsAnchorLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QGraphicsAnchorLayout10invalidateEv(
    QGraphicsAnchorLayout *self) {
  self->QGraphicsAnchorLayout::invalidate();
}

//  QSizeF QGraphicsAnchorLayout::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK21QGraphicsAnchorLayout8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const QGraphicsAnchorLayout *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(
      static_cast<const OwnQGraphicsAnchorLayout *>(self)->OwnQGraphicsAnchorLayout::sizeHint(
          which,
          *constraint));
}
