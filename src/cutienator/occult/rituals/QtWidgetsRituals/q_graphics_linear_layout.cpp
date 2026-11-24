//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicslinearlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicslinearlayout.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QGraphicsLinearLayout that Python can take functions over in. Every QGraphicsLinearLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLinearLayoutCall0)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLinearLayoutCall1)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteQGraphicsLinearLayoutCall2)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void * (*CuteQGraphicsLinearLayoutCall3)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLinearLayoutCall4)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QSizeF * (*CuteQGraphicsLinearLayoutCall5)(const void *, int, const QSizeF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLinearLayoutCall6)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLinearLayoutCall7)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsLinearLayoutCall8)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteQGraphicsLinearLayout : public QGraphicsLinearLayout {
public:
  using QGraphicsLinearLayout::QGraphicsLinearLayout;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsLayout8removeAtEi")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem11setGeometryERK6QRectF")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGraphicsLayout5countEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGraphicsLayout6itemAtEi")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsLayout10invalidateEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF")) {
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
  //  void QGraphicsLinearLayout::removeAt(int index)
  void removeAt(int index) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsLinearLayoutCall0 call = reinterpret_cast<CuteQGraphicsLinearLayoutCall0>(taken[0]);
      call(this, index, &handled);
      if (handled) return;
    }
    QGraphicsLinearLayout::removeAt(index);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsLinearLayout::setGeometry(const QRectF &rect)
  void setGeometry(const QRectF &rect) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsLinearLayoutCall1 call = reinterpret_cast<CuteQGraphicsLinearLayoutCall1>(taken[1]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QGraphicsLinearLayout::setGeometry(rect);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  int QGraphicsLinearLayout::count() const
  int count() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsLinearLayoutCall2 call = reinterpret_cast<CuteQGraphicsLinearLayoutCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsLinearLayout::count();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QGraphicsLayoutItem *QGraphicsLinearLayout::itemAt(int index) const
  QGraphicsLayoutItem *itemAt(int index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsLinearLayoutCall3 call = reinterpret_cast<CuteQGraphicsLinearLayoutCall3>(taken[3]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QGraphicsLayoutItem *>(given);
    }
    return QGraphicsLinearLayout::itemAt(index);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsLinearLayout::invalidate()
  void invalidate() override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsLinearLayoutCall4 call = reinterpret_cast<CuteQGraphicsLinearLayoutCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsLinearLayout::invalidate();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QSizeF QGraphicsLinearLayout::sizeHint(Qt::SizeHint which, const
  //      QSizeF &constraint) const
  QSizeF sizeHint(
      Qt::SizeHint which,
      const QSizeF &constraint) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsLinearLayoutCall5 call = reinterpret_cast<CuteQGraphicsLinearLayoutCall5>(taken[5]);
      const QSizeF * given = call(this, static_cast<int>(which), &constraint, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsLinearLayout::sizeHint(which, constraint);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsLayout::updateGeometry()
  void updateGeometry() override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsLinearLayoutCall6 call = reinterpret_cast<CuteQGraphicsLinearLayoutCall6>(taken[6]);
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
      CuteQGraphicsLinearLayoutCall7 call = reinterpret_cast<CuteQGraphicsLinearLayoutCall7>(taken[7]);
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
      CuteQGraphicsLinearLayoutCall8 call = reinterpret_cast<CuteQGraphicsLinearLayoutCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsLayoutItem::isEmpty();
  }
#endif  // QT_CONFIG(graphicsview)
};

//  QGraphicsLinearLayout::QGraphicsLinearLayout(QGraphicsLayoutItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsLinearLayout *ritual_ZN21QGraphicsLinearLayoutC1EP19QGraphicsLayoutItem(
    QGraphicsLayoutItem *parent) {
  return new CuteQGraphicsLinearLayout(parent);
}

//  QGraphicsLinearLayout::QGraphicsLinearLayout(Qt::Orientation orientation,
//      QGraphicsLayoutItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsLinearLayout *ritual_ZN21QGraphicsLinearLayoutC1EN2Qt11OrientationEP19QGraphicsLayoutItem(
    Qt::Orientation orientation,
    QGraphicsLayoutItem *parent) {
  return new CuteQGraphicsLinearLayout(orientation, parent);
}

//  QGraphicsLinearLayout::~QGraphicsLinearLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayoutD1Ev(QGraphicsLinearLayout *self) {
  delete self;
}

//  void QGraphicsLinearLayout::setOrientation(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout14setOrientationEN2Qt11OrientationE(
    QGraphicsLinearLayout *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  Qt::Orientation QGraphicsLinearLayout::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK21QGraphicsLinearLayout11orientationEv(
    const QGraphicsLinearLayout *self) {
  return self->orientation();
}

//  void QGraphicsLinearLayout::addItem(QGraphicsLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout7addItemEP19QGraphicsLayoutItem(
    QGraphicsLinearLayout *self,
    QGraphicsLayoutItem *item) {
  self->addItem(item);
}

//  void QGraphicsLinearLayout::addStretch(int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout10addStretchEi(
    QGraphicsLinearLayout *self,
    int stretch) {
  self->addStretch(stretch);
}

//  void QGraphicsLinearLayout::insertItem(int index, QGraphicsLayoutItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout10insertItemEiP19QGraphicsLayoutItem(
    QGraphicsLinearLayout *self,
    int index,
    QGraphicsLayoutItem *item) {
  self->insertItem(index, item);
}

//  void QGraphicsLinearLayout::insertStretch(int index, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout13insertStretchEii(
    QGraphicsLinearLayout *self,
    int index,
    int stretch) {
  self->insertStretch(index, stretch);
}

//  void QGraphicsLinearLayout::removeItem(QGraphicsLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout10removeItemEP19QGraphicsLayoutItem(
    QGraphicsLinearLayout *self,
    QGraphicsLayoutItem *item) {
  self->removeItem(item);
}

//  void QGraphicsLinearLayout::removeAt(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout8removeAtEi(
    QGraphicsLinearLayout *self,
    int index) {
  self->removeAt(index);
}

//  void QGraphicsLinearLayout::setSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout10setSpacingEd(
    QGraphicsLinearLayout *self,
    qreal spacing) {
  self->setSpacing(spacing);
}

//  qreal QGraphicsLinearLayout::spacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QGraphicsLinearLayout7spacingEv(
    const QGraphicsLinearLayout *self) {
  return self->spacing();
}

//  void QGraphicsLinearLayout::setItemSpacing(int index, qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout14setItemSpacingEid(
    QGraphicsLinearLayout *self,
    int index,
    qreal spacing) {
  self->setItemSpacing(index, spacing);
}

//  qreal QGraphicsLinearLayout::itemSpacing(int index) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QGraphicsLinearLayout11itemSpacingEi(
    const QGraphicsLinearLayout *self,
    int index) {
  return self->itemSpacing(index);
}

//  void QGraphicsLinearLayout::setStretchFactor(QGraphicsLayoutItem *item,
//      int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout16setStretchFactorEP19QGraphicsLayoutItemi(
    QGraphicsLinearLayout *self,
    QGraphicsLayoutItem *item,
    int stretch) {
  self->setStretchFactor(item, stretch);
}

//  int QGraphicsLinearLayout::stretchFactor(QGraphicsLayoutItem *item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QGraphicsLinearLayout13stretchFactorEP19QGraphicsLayoutItem(
    const QGraphicsLinearLayout *self,
    QGraphicsLayoutItem *item) {
  return self->stretchFactor(item);
}

//  void QGraphicsLinearLayout::setAlignment(QGraphicsLayoutItem *item,
//      Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout12setAlignmentEP19QGraphicsLayoutItem6QFlagsIN2Qt13AlignmentFlagEE(
    QGraphicsLinearLayout *self,
    QGraphicsLayoutItem *item,
    int alignment) {
  self->setAlignment(item, QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  Qt::Alignment QGraphicsLinearLayout::alignment(QGraphicsLayoutItem *item)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QGraphicsLinearLayout9alignmentEP19QGraphicsLayoutItem(
    const QGraphicsLinearLayout *self,
    QGraphicsLayoutItem *item) {
  return static_cast<int>(self->alignment(item).toInt());
}

//  void QGraphicsLinearLayout::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout11setGeometryERK6QRectF(
    QGraphicsLinearLayout *self,
    const QRectF *rect) {
  self->setGeometry(*rect);
}

//  int QGraphicsLinearLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QGraphicsLinearLayout5countEv(
    const QGraphicsLinearLayout *self) {
  return self->count();
}

//  QGraphicsLayoutItem *QGraphicsLinearLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_ZNK21QGraphicsLinearLayout6itemAtEi(
    const QGraphicsLinearLayout *self,
    int index) {
  return self->itemAt(index);
}

//  void QGraphicsLinearLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsLinearLayout10invalidateEv(
    QGraphicsLinearLayout *self) {
  self->invalidate();
}

//  QSizeF QGraphicsLinearLayout::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK21QGraphicsLinearLayout8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const QGraphicsLinearLayout *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->sizeHint(which, *constraint));
}

//  void QGraphicsLinearLayout::dump(int indent) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QGraphicsLinearLayout4dumpEi(
    const QGraphicsLinearLayout *self,
    int indent) {
  self->dump(indent);
}

//  a Python function taken by a CuteQGraphicsLinearLayout, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsLinearLayout(
    QGraphicsLinearLayout *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsLinearLayout *>(self)->take(key, call);
}

//  void QGraphicsLinearLayout::removeAt(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QGraphicsLinearLayout8removeAtEi(
    QGraphicsLinearLayout *self,
    int index) {
  self->QGraphicsLinearLayout::removeAt(index);
}

//  void QGraphicsLinearLayout::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QGraphicsLinearLayout11setGeometryERK6QRectF(
    QGraphicsLinearLayout *self,
    const QRectF *rect) {
  self->QGraphicsLinearLayout::setGeometry(*rect);
}

//  int QGraphicsLinearLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QGraphicsLinearLayout5countEv(
    const QGraphicsLinearLayout *self) {
  return self->QGraphicsLinearLayout::count();
}

//  QGraphicsLayoutItem *QGraphicsLinearLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_own_ZNK21QGraphicsLinearLayout6itemAtEi(
    const QGraphicsLinearLayout *self,
    int index) {
  return self->QGraphicsLinearLayout::itemAt(index);
}

//  void QGraphicsLinearLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QGraphicsLinearLayout10invalidateEv(
    QGraphicsLinearLayout *self) {
  self->QGraphicsLinearLayout::invalidate();
}

//  QSizeF QGraphicsLinearLayout::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK21QGraphicsLinearLayout8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const QGraphicsLinearLayout *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(
      self->QGraphicsLinearLayout::sizeHint(
          which,
          *constraint));
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
