//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsgridlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicsgridlayout.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QGraphicsGridLayout that Python can take functions over in. Every QGraphicsGridLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef int (*CuteQGraphicsGridLayoutCall0)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void * (*CuteQGraphicsGridLayoutCall1)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsGridLayoutCall2)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsGridLayoutCall3)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsGridLayoutCall4)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QSizeF * (*CuteQGraphicsGridLayoutCall5)(const void *, int, const QSizeF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsGridLayoutCall6)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsGridLayoutCall7)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsGridLayoutCall8)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteQGraphicsGridLayout : public QGraphicsGridLayout {
public:
  using QGraphicsGridLayout::QGraphicsGridLayout;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGraphicsLayout5countEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGraphicsLayout6itemAtEi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsLayout8removeAtEi")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGraphicsLayout10invalidateEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem11setGeometryERK6QRectF")) {
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
  //  int QGraphicsGridLayout::count() const
  int count() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsGridLayoutCall0 call = reinterpret_cast<CuteQGraphicsGridLayoutCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsGridLayout::count();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QGraphicsLayoutItem *QGraphicsGridLayout::itemAt(int index) const
  QGraphicsLayoutItem *itemAt(int index) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsGridLayoutCall1 call = reinterpret_cast<CuteQGraphicsGridLayoutCall1>(taken[1]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QGraphicsLayoutItem *>(given);
    }
    return QGraphicsGridLayout::itemAt(index);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsGridLayout::removeAt(int index)
  void removeAt(int index) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsGridLayoutCall2 call = reinterpret_cast<CuteQGraphicsGridLayoutCall2>(taken[2]);
      call(this, index, &handled);
      if (handled) return;
    }
    QGraphicsGridLayout::removeAt(index);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsGridLayout::invalidate()
  void invalidate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsGridLayoutCall3 call = reinterpret_cast<CuteQGraphicsGridLayoutCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsGridLayout::invalidate();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsGridLayout::setGeometry(const QRectF &rect)
  void setGeometry(const QRectF &rect) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsGridLayoutCall4 call = reinterpret_cast<CuteQGraphicsGridLayoutCall4>(taken[4]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QGraphicsGridLayout::setGeometry(rect);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QSizeF QGraphicsGridLayout::sizeHint(Qt::SizeHint which, const QSizeF
  //      &constraint) const
  QSizeF sizeHint(
      Qt::SizeHint which,
      const QSizeF &constraint) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsGridLayoutCall5 call = reinterpret_cast<CuteQGraphicsGridLayoutCall5>(taken[5]);
      const QSizeF * given = call(this, static_cast<int>(which), &constraint, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsGridLayout::sizeHint(which, constraint);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsLayout::updateGeometry()
  void updateGeometry() override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsGridLayoutCall6 call = reinterpret_cast<CuteQGraphicsGridLayoutCall6>(taken[6]);
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
      CuteQGraphicsGridLayoutCall7 call = reinterpret_cast<CuteQGraphicsGridLayoutCall7>(taken[7]);
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
      CuteQGraphicsGridLayoutCall8 call = reinterpret_cast<CuteQGraphicsGridLayoutCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsLayoutItem::isEmpty();
  }
#endif  // QT_CONFIG(graphicsview)
};

//  QGraphicsGridLayout::QGraphicsGridLayout(QGraphicsLayoutItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsGridLayout *ritual_ZN19QGraphicsGridLayoutC1EP19QGraphicsLayoutItem(
    QGraphicsLayoutItem *parent) {
  return new CuteQGraphicsGridLayout(parent);
}

//  QGraphicsGridLayout::~QGraphicsGridLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayoutD1Ev(QGraphicsGridLayout *self) {
  delete self;
}

//  void QGraphicsGridLayout::addItem(QGraphicsLayoutItem *item, int row, int
//      column, int rowSpan, int columnSpan, Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout7addItemEP19QGraphicsLayoutItemiiii6QFlagsIN2Qt13AlignmentFlagEE(
    QGraphicsGridLayout *self,
    QGraphicsLayoutItem *item,
    int row,
    int column,
    int rowSpan,
    int columnSpan,
    int alignment) {
  self->addItem(
      item,
      row,
      column,
      rowSpan,
      columnSpan,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void QGraphicsGridLayout::addItem(QGraphicsLayoutItem *item, int row, int
//      column, Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout7addItemEP19QGraphicsLayoutItemii6QFlagsIN2Qt13AlignmentFlagEE(
    QGraphicsGridLayout *self,
    QGraphicsLayoutItem *item,
    int row,
    int column,
    int alignment) {
  self->addItem(
      item,
      row,
      column,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void QGraphicsGridLayout::setHorizontalSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout20setHorizontalSpacingEd(
    QGraphicsGridLayout *self,
    qreal spacing) {
  self->setHorizontalSpacing(spacing);
}

//  qreal QGraphicsGridLayout::horizontalSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsGridLayout17horizontalSpacingEv(
    const QGraphicsGridLayout *self) {
  return self->horizontalSpacing();
}

//  void QGraphicsGridLayout::setVerticalSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout18setVerticalSpacingEd(
    QGraphicsGridLayout *self,
    qreal spacing) {
  self->setVerticalSpacing(spacing);
}

//  qreal QGraphicsGridLayout::verticalSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsGridLayout15verticalSpacingEv(
    const QGraphicsGridLayout *self) {
  return self->verticalSpacing();
}

//  void QGraphicsGridLayout::setSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout10setSpacingEd(
    QGraphicsGridLayout *self,
    qreal spacing) {
  self->setSpacing(spacing);
}

//  void QGraphicsGridLayout::setRowSpacing(int row, qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout13setRowSpacingEid(
    QGraphicsGridLayout *self,
    int row,
    qreal spacing) {
  self->setRowSpacing(row, spacing);
}

//  qreal QGraphicsGridLayout::rowSpacing(int row) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsGridLayout10rowSpacingEi(
    const QGraphicsGridLayout *self,
    int row) {
  return self->rowSpacing(row);
}

//  void QGraphicsGridLayout::setColumnSpacing(int column, qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout16setColumnSpacingEid(
    QGraphicsGridLayout *self,
    int column,
    qreal spacing) {
  self->setColumnSpacing(column, spacing);
}

//  qreal QGraphicsGridLayout::columnSpacing(int column) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsGridLayout13columnSpacingEi(
    const QGraphicsGridLayout *self,
    int column) {
  return self->columnSpacing(column);
}

//  void QGraphicsGridLayout::setRowStretchFactor(int row, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout19setRowStretchFactorEii(
    QGraphicsGridLayout *self,
    int row,
    int stretch) {
  self->setRowStretchFactor(row, stretch);
}

//  int QGraphicsGridLayout::rowStretchFactor(int row) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGraphicsGridLayout16rowStretchFactorEi(
    const QGraphicsGridLayout *self,
    int row) {
  return self->rowStretchFactor(row);
}

//  void QGraphicsGridLayout::setColumnStretchFactor(int column, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout22setColumnStretchFactorEii(
    QGraphicsGridLayout *self,
    int column,
    int stretch) {
  self->setColumnStretchFactor(column, stretch);
}

//  int QGraphicsGridLayout::columnStretchFactor(int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGraphicsGridLayout19columnStretchFactorEi(
    const QGraphicsGridLayout *self,
    int column) {
  return self->columnStretchFactor(column);
}

//  void QGraphicsGridLayout::setRowMinimumHeight(int row, qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout19setRowMinimumHeightEid(
    QGraphicsGridLayout *self,
    int row,
    qreal height) {
  self->setRowMinimumHeight(row, height);
}

//  qreal QGraphicsGridLayout::rowMinimumHeight(int row) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsGridLayout16rowMinimumHeightEi(
    const QGraphicsGridLayout *self,
    int row) {
  return self->rowMinimumHeight(row);
}

//  void QGraphicsGridLayout::setRowPreferredHeight(int row, qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout21setRowPreferredHeightEid(
    QGraphicsGridLayout *self,
    int row,
    qreal height) {
  self->setRowPreferredHeight(row, height);
}

//  qreal QGraphicsGridLayout::rowPreferredHeight(int row) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsGridLayout18rowPreferredHeightEi(
    const QGraphicsGridLayout *self,
    int row) {
  return self->rowPreferredHeight(row);
}

//  void QGraphicsGridLayout::setRowMaximumHeight(int row, qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout19setRowMaximumHeightEid(
    QGraphicsGridLayout *self,
    int row,
    qreal height) {
  self->setRowMaximumHeight(row, height);
}

//  qreal QGraphicsGridLayout::rowMaximumHeight(int row) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsGridLayout16rowMaximumHeightEi(
    const QGraphicsGridLayout *self,
    int row) {
  return self->rowMaximumHeight(row);
}

//  void QGraphicsGridLayout::setRowFixedHeight(int row, qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout17setRowFixedHeightEid(
    QGraphicsGridLayout *self,
    int row,
    qreal height) {
  self->setRowFixedHeight(row, height);
}

//  void QGraphicsGridLayout::setColumnMinimumWidth(int column, qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout21setColumnMinimumWidthEid(
    QGraphicsGridLayout *self,
    int column,
    qreal width) {
  self->setColumnMinimumWidth(column, width);
}

//  qreal QGraphicsGridLayout::columnMinimumWidth(int column) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsGridLayout18columnMinimumWidthEi(
    const QGraphicsGridLayout *self,
    int column) {
  return self->columnMinimumWidth(column);
}

//  void QGraphicsGridLayout::setColumnPreferredWidth(int column, qreal
//      width)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout23setColumnPreferredWidthEid(
    QGraphicsGridLayout *self,
    int column,
    qreal width) {
  self->setColumnPreferredWidth(column, width);
}

//  qreal QGraphicsGridLayout::columnPreferredWidth(int column) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsGridLayout20columnPreferredWidthEi(
    const QGraphicsGridLayout *self,
    int column) {
  return self->columnPreferredWidth(column);
}

//  void QGraphicsGridLayout::setColumnMaximumWidth(int column, qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout21setColumnMaximumWidthEid(
    QGraphicsGridLayout *self,
    int column,
    qreal width) {
  self->setColumnMaximumWidth(column, width);
}

//  qreal QGraphicsGridLayout::columnMaximumWidth(int column) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsGridLayout18columnMaximumWidthEi(
    const QGraphicsGridLayout *self,
    int column) {
  return self->columnMaximumWidth(column);
}

//  void QGraphicsGridLayout::setColumnFixedWidth(int column, qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout19setColumnFixedWidthEid(
    QGraphicsGridLayout *self,
    int column,
    qreal width) {
  self->setColumnFixedWidth(column, width);
}

//  void QGraphicsGridLayout::setRowAlignment(int row, Qt::Alignment
//      alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout15setRowAlignmentEi6QFlagsIN2Qt13AlignmentFlagEE(
    QGraphicsGridLayout *self,
    int row,
    int alignment) {
  self->setRowAlignment(row, QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  Qt::Alignment QGraphicsGridLayout::rowAlignment(int row) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGraphicsGridLayout12rowAlignmentEi(
    const QGraphicsGridLayout *self,
    int row) {
  return static_cast<int>(self->rowAlignment(row).toInt());
}

//  void QGraphicsGridLayout::setColumnAlignment(int column, Qt::Alignment
//      alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout18setColumnAlignmentEi6QFlagsIN2Qt13AlignmentFlagEE(
    QGraphicsGridLayout *self,
    int column,
    int alignment) {
  self->setColumnAlignment(
      column,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  Qt::Alignment QGraphicsGridLayout::columnAlignment(int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGraphicsGridLayout15columnAlignmentEi(
    const QGraphicsGridLayout *self,
    int column) {
  return static_cast<int>(self->columnAlignment(column).toInt());
}

//  void QGraphicsGridLayout::setAlignment(QGraphicsLayoutItem *item,
//      Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout12setAlignmentEP19QGraphicsLayoutItem6QFlagsIN2Qt13AlignmentFlagEE(
    QGraphicsGridLayout *self,
    QGraphicsLayoutItem *item,
    int alignment) {
  self->setAlignment(item, QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  Qt::Alignment QGraphicsGridLayout::alignment(QGraphicsLayoutItem *item)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGraphicsGridLayout9alignmentEP19QGraphicsLayoutItem(
    const QGraphicsGridLayout *self,
    QGraphicsLayoutItem *item) {
  return static_cast<int>(self->alignment(item).toInt());
}

//  int QGraphicsGridLayout::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGraphicsGridLayout8rowCountEv(
    const QGraphicsGridLayout *self) {
  return self->rowCount();
}

//  int QGraphicsGridLayout::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGraphicsGridLayout11columnCountEv(
    const QGraphicsGridLayout *self) {
  return self->columnCount();
}

//  QGraphicsLayoutItem *QGraphicsGridLayout::itemAt(int row, int column)
//      const
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_ZNK19QGraphicsGridLayout6itemAtEii(
    const QGraphicsGridLayout *self,
    int row,
    int column) {
  return self->itemAt(row, column);
}

//  int QGraphicsGridLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGraphicsGridLayout5countEv(
    const QGraphicsGridLayout *self) {
  return self->count();
}

//  QGraphicsLayoutItem *QGraphicsGridLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_ZNK19QGraphicsGridLayout6itemAtEi(
    const QGraphicsGridLayout *self,
    int index) {
  return self->itemAt(index);
}

//  void QGraphicsGridLayout::removeAt(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout8removeAtEi(
    QGraphicsGridLayout *self,
    int index) {
  self->removeAt(index);
}

//  void QGraphicsGridLayout::removeItem(QGraphicsLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout10removeItemEP19QGraphicsLayoutItem(
    QGraphicsGridLayout *self,
    QGraphicsLayoutItem *item) {
  self->removeItem(item);
}

//  void QGraphicsGridLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout10invalidateEv(
    QGraphicsGridLayout *self) {
  self->invalidate();
}

//  void QGraphicsGridLayout::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout11setGeometryERK6QRectF(
    QGraphicsGridLayout *self,
    const QRectF *rect) {
  self->setGeometry(*rect);
}

//  QSizeF QGraphicsGridLayout::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK19QGraphicsGridLayout8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const QGraphicsGridLayout *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->sizeHint(which, *constraint));
}

//  QGraphicsGridLayoutPrivate *QGraphicsGridLayout::d_func()
extern "C" Q_DECL_EXPORT
QGraphicsGridLayoutPrivate *ritual_ZN19QGraphicsGridLayout6d_funcEv(
    QGraphicsGridLayout *self) {
  return self->d_func();
}

//  const QGraphicsGridLayoutPrivate *QGraphicsGridLayout::d_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsGridLayoutPrivate *ritual_ZNK19QGraphicsGridLayout6d_funcEv(
    const QGraphicsGridLayout *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQGraphicsGridLayout, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsGridLayout(
    QGraphicsGridLayout *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsGridLayout *>(self)->take(key, call);
}

//  int QGraphicsGridLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QGraphicsGridLayout5countEv(
    const QGraphicsGridLayout *self) {
  return self->QGraphicsGridLayout::count();
}

//  QGraphicsLayoutItem *QGraphicsGridLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_own_ZNK19QGraphicsGridLayout6itemAtEi(
    const QGraphicsGridLayout *self,
    int index) {
  return self->QGraphicsGridLayout::itemAt(index);
}

//  void QGraphicsGridLayout::removeAt(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGraphicsGridLayout8removeAtEi(
    QGraphicsGridLayout *self,
    int index) {
  self->QGraphicsGridLayout::removeAt(index);
}

//  void QGraphicsGridLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGraphicsGridLayout10invalidateEv(
    QGraphicsGridLayout *self) {
  self->QGraphicsGridLayout::invalidate();
}

//  void QGraphicsGridLayout::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGraphicsGridLayout11setGeometryERK6QRectF(
    QGraphicsGridLayout *self,
    const QRectF *rect) {
  self->QGraphicsGridLayout::setGeometry(*rect);
}

//  QSizeF QGraphicsGridLayout::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK19QGraphicsGridLayout8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const QGraphicsGridLayout *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->QGraphicsGridLayout::sizeHint(which, *constraint));
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
