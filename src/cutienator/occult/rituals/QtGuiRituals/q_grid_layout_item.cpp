//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qgridlayoutengine_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qgridlayoutengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QGridLayoutItem that Python can take functions over in. Every QGridLayoutItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQGridLayoutItemCall0)(const void *, int, int *);
typedef const QSizeF * (*CuteQGridLayoutItemCall1)(const void *, int, const QSizeF *, int *);
typedef bool (*CuteQGridLayoutItemCall2)(const void *, int *);
typedef void (*CuteQGridLayoutItemCall3)(const void *, const QRectF *, int *);
typedef bool (*CuteQGridLayoutItemCall4)(const void *, int *);
typedef int (*CuteQGridLayoutItemCall5)(const void *, int *);
typedef int (*CuteQGridLayoutItemCall6)(const void *, int, int *);
typedef QString * (*CuteQGridLayoutItemCall7)(const void *, int *);
class CuteQGridLayoutItem : public QGridLayoutItem {
public:
  using QGridLayoutItem::QGridLayoutItem;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QGridLayoutItem10sizePolicyEN2Qt11OrientationE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QGridLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QGridLayoutItem7isEmptyEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGridLayoutItem11setGeometryERK6QRectF")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QGridLayoutItem20hasDynamicConstraintEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QGridLayoutItem28dynamicConstraintOrientationEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QGridLayoutItem12controlTypesE10LayoutSide")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QGridLayoutItem8toStringEv")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  QLayoutPolicy::Policy QGridLayoutItem::sizePolicy(Qt::Orientation
  //      orientation) const
  QLayoutPolicy::Policy sizePolicy(
      Qt::Orientation orientation) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGridLayoutItemCall0 call = reinterpret_cast<CuteQGridLayoutItemCall0>(taken[0]);
      int given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return QFlags<QLayoutPolicy::PolicyFlag>::fromInt(given);
    }
    return {};
  }

  //  QSizeF QGridLayoutItem::sizeHint(Qt::SizeHint which, const QSizeF
  //      &constraint) const
  QSizeF sizeHint(
      Qt::SizeHint which,
      const QSizeF &constraint) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGridLayoutItemCall1 call = reinterpret_cast<CuteQGridLayoutItemCall1>(taken[1]);
      const QSizeF * given = call(this, static_cast<int>(which), &constraint, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QGridLayoutItem::isEmpty() const
  bool isEmpty() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGridLayoutItemCall2 call = reinterpret_cast<CuteQGridLayoutItemCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGridLayoutItem::isEmpty();
  }

  //  void QGridLayoutItem::setGeometry(const QRectF &rect)
  void setGeometry(const QRectF &rect) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGridLayoutItemCall3 call = reinterpret_cast<CuteQGridLayoutItemCall3>(taken[3]);
      call(this, &rect, &handled);
      if (handled) return;
    }
  }

  //  bool QGridLayoutItem::hasDynamicConstraint() const
  bool hasDynamicConstraint() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGridLayoutItemCall4 call = reinterpret_cast<CuteQGridLayoutItemCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGridLayoutItem::hasDynamicConstraint();
  }

  //  Qt::Orientation QGridLayoutItem::dynamicConstraintOrientation() const
  Qt::Orientation dynamicConstraintOrientation() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGridLayoutItemCall5 call = reinterpret_cast<CuteQGridLayoutItemCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::Orientation>(given);
    }
    return QGridLayoutItem::dynamicConstraintOrientation();
  }

  //  QLayoutPolicy::ControlTypes QGridLayoutItem::controlTypes(LayoutSide
  //      side) const
  QLayoutPolicy::ControlTypes controlTypes(LayoutSide side) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGridLayoutItemCall6 call = reinterpret_cast<CuteQGridLayoutItemCall6>(taken[6]);
      int given = call(this, static_cast<int>(side), &handled);
      if (handled) return QFlags<QLayoutPolicy::ControlType>::fromInt(given);
    }
    return QGridLayoutItem::controlTypes(side);
  }

  //  QString QGridLayoutItem::toString() const
  QString toString() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGridLayoutItemCall7 call = reinterpret_cast<CuteQGridLayoutItemCall7>(taken[7]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QGridLayoutItem::toString();
  }
};

//  QGridLayoutItem::~QGridLayoutItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGridLayoutItemD1Ev(QGridLayoutItem *self) {
  delete self;
}

//  int QGridLayoutItem::firstRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGridLayoutItem8firstRowEv(const QGridLayoutItem *self) {
  return self->firstRow();
}

//  int QGridLayoutItem::firstColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGridLayoutItem11firstColumnEv(const QGridLayoutItem *self) {
  return self->firstColumn();
}

//  int QGridLayoutItem::rowSpan() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGridLayoutItem7rowSpanEv(const QGridLayoutItem *self) {
  return self->rowSpan();
}

//  int QGridLayoutItem::columnSpan() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGridLayoutItem10columnSpanEv(const QGridLayoutItem *self) {
  return self->columnSpan();
}

//  int QGridLayoutItem::lastRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGridLayoutItem7lastRowEv(const QGridLayoutItem *self) {
  return self->lastRow();
}

//  int QGridLayoutItem::lastColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGridLayoutItem10lastColumnEv(const QGridLayoutItem *self) {
  return self->lastColumn();
}

//  int QGridLayoutItem::firstRow(Qt::Orientation orientation) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGridLayoutItem8firstRowEN2Qt11OrientationE(
    const QGridLayoutItem *self,
    Qt::Orientation orientation) {
  return self->firstRow(orientation);
}

//  int QGridLayoutItem::firstColumn(Qt::Orientation orientation) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGridLayoutItem11firstColumnEN2Qt11OrientationE(
    const QGridLayoutItem *self,
    Qt::Orientation orientation) {
  return self->firstColumn(orientation);
}

//  int QGridLayoutItem::lastRow(Qt::Orientation orientation) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGridLayoutItem7lastRowEN2Qt11OrientationE(
    const QGridLayoutItem *self,
    Qt::Orientation orientation) {
  return self->lastRow(orientation);
}

//  int QGridLayoutItem::lastColumn(Qt::Orientation orientation) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGridLayoutItem10lastColumnEN2Qt11OrientationE(
    const QGridLayoutItem *self,
    Qt::Orientation orientation) {
  return self->lastColumn(orientation);
}

//  int QGridLayoutItem::rowSpan(Qt::Orientation orientation) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGridLayoutItem7rowSpanEN2Qt11OrientationE(
    const QGridLayoutItem *self,
    Qt::Orientation orientation) {
  return self->rowSpan(orientation);
}

//  int QGridLayoutItem::columnSpan(Qt::Orientation orientation) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGridLayoutItem10columnSpanEN2Qt11OrientationE(
    const QGridLayoutItem *self,
    Qt::Orientation orientation) {
  return self->columnSpan(orientation);
}

//  void QGridLayoutItem::setFirstRow(int row, Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGridLayoutItem11setFirstRowEiN2Qt11OrientationE(
    QGridLayoutItem *self,
    int row,
    Qt::Orientation orientation) {
  self->setFirstRow(row, orientation);
}

//  void QGridLayoutItem::setRowSpan(int rowSpan, Qt::Orientation
//      orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGridLayoutItem10setRowSpanEiN2Qt11OrientationE(
    QGridLayoutItem *self,
    int rowSpan,
    Qt::Orientation orientation) {
  self->setRowSpan(rowSpan, orientation);
}

//  int QGridLayoutItem::stretchFactor(Qt::Orientation orientation) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGridLayoutItem13stretchFactorEN2Qt11OrientationE(
    const QGridLayoutItem *self,
    Qt::Orientation orientation) {
  return self->stretchFactor(orientation);
}

//  void QGridLayoutItem::setStretchFactor(int stretch, Qt::Orientation
//      orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGridLayoutItem16setStretchFactorEiN2Qt11OrientationE(
    QGridLayoutItem *self,
    int stretch,
    Qt::Orientation orientation) {
  self->setStretchFactor(stretch, orientation);
}

//  Qt::Alignment QGridLayoutItem::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGridLayoutItem9alignmentEv(const QGridLayoutItem *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QGridLayoutItem::setAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGridLayoutItem12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QGridLayoutItem *self,
    int alignment) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  QLayoutPolicy::Policy QGridLayoutItem::sizePolicy(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGridLayoutItem10sizePolicyEN2Qt11OrientationE(
    const QGridLayoutItem *self,
    Qt::Orientation orientation) {
  return static_cast<int>(self->sizePolicy(orientation).toInt());
}

//  QSizeF QGridLayoutItem::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK15QGridLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const QGridLayoutItem *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->sizeHint(which, *constraint));
}

//  bool QGridLayoutItem::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QGridLayoutItem7isEmptyEv(const QGridLayoutItem *self) {
  return self->isEmpty();
}

//  void QGridLayoutItem::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGridLayoutItem11setGeometryERK6QRectF(
    QGridLayoutItem *self,
    const QRectF *rect) {
  self->setGeometry(*rect);
}

//  bool QGridLayoutItem::hasDynamicConstraint() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QGridLayoutItem20hasDynamicConstraintEv(
    const QGridLayoutItem *self) {
  return self->hasDynamicConstraint();
}

//  Qt::Orientation QGridLayoutItem::dynamicConstraintOrientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK15QGridLayoutItem28dynamicConstraintOrientationEv(
    const QGridLayoutItem *self) {
  return self->dynamicConstraintOrientation();
}

//  QLayoutPolicy::ControlTypes QGridLayoutItem::controlTypes(LayoutSide
//      side) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QGridLayoutItem12controlTypesE10LayoutSide(
    const QGridLayoutItem *self,
    LayoutSide side) {
  return static_cast<int>(self->controlTypes(side).toInt());
}

//  QString QGridLayoutItem::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QGridLayoutItem8toStringEv(
    const QGridLayoutItem *self) {
  return new QString(self->toString());
}

//  QRectF QGridLayoutItem::geometryWithin(qreal x, qreal y, qreal width,
//      qreal height, qreal rowDescent, Qt::Alignment align, bool
//      snapToPixelGrid) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QGridLayoutItem14geometryWithinEddddd6QFlagsIN2Qt13AlignmentFlagEEb(
    const QGridLayoutItem *self,
    qreal x,
    qreal y,
    qreal width,
    qreal height,
    qreal rowDescent,
    int align,
    bool snapToPixelGrid) {
  return new QRectF(
      self->geometryWithin(
          x,
          y,
          width,
          height,
          rowDescent,
          QFlags<Qt::AlignmentFlag>::fromInt(align),
          snapToPixelGrid));
}

//  QGridLayoutBox QGridLayoutItem::box(Qt::Orientation orientation, bool
//      snapToPixelGrid, qreal constraint) const
extern "C" Q_DECL_EXPORT
QGridLayoutBox *ritual_ZNK15QGridLayoutItem3boxEN2Qt11OrientationEbd(
    const QGridLayoutItem *self,
    Qt::Orientation orientation,
    bool snapToPixelGrid,
    qreal constraint) {
  return new QGridLayoutBox(
      self->box(
          orientation,
          snapToPixelGrid,
          constraint));
}

//  void QGridLayoutItem::transpose()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGridLayoutItem9transposeEv(QGridLayoutItem *self) {
  self->transpose();
}

//  void QGridLayoutItem::insertOrRemoveRows(int row, int delta,
//      Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGridLayoutItem18insertOrRemoveRowsEiiN2Qt11OrientationE(
    QGridLayoutItem *self,
    int row,
    int delta,
    Qt::Orientation orientation) {
  self->insertOrRemoveRows(row, delta, orientation);
}

//  QSizeF QGridLayoutItem::effectiveMaxSize(const QSizeF &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK15QGridLayoutItem16effectiveMaxSizeERK6QSizeF(
    const QGridLayoutItem *self,
    const QSizeF *constraint) {
  return new QSizeF(self->effectiveMaxSize(*constraint));
}

//  a Python function taken by a CuteQGridLayoutItem, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGridLayoutItem(
    QGridLayoutItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGridLayoutItem *>(self)->take(key, call);
}

//  bool QGridLayoutItem::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QGridLayoutItem7isEmptyEv(const QGridLayoutItem *self) {
  return self->QGridLayoutItem::isEmpty();
}

//  bool QGridLayoutItem::hasDynamicConstraint() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QGridLayoutItem20hasDynamicConstraintEv(
    const QGridLayoutItem *self) {
  return self->QGridLayoutItem::hasDynamicConstraint();
}

//  Qt::Orientation QGridLayoutItem::dynamicConstraintOrientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_own_ZNK15QGridLayoutItem28dynamicConstraintOrientationEv(
    const QGridLayoutItem *self) {
  return self->QGridLayoutItem::dynamicConstraintOrientation();
}

//  QLayoutPolicy::ControlTypes QGridLayoutItem::controlTypes(LayoutSide
//      side) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QGridLayoutItem12controlTypesE10LayoutSide(
    const QGridLayoutItem *self,
    LayoutSide side) {
  return static_cast<int>(self->QGridLayoutItem::controlTypes(side).toInt());
}

//  QString QGridLayoutItem::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK15QGridLayoutItem8toStringEv(
    const QGridLayoutItem *self) {
  return new QString(self->QGridLayoutItem::toString());
}
