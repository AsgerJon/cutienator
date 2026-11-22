//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicslayoutitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicslayoutitem.h>
#include <QtWidgets/qsizepolicy.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QGraphicsLayoutItem that Python can take functions over in. Every QGraphicsLayoutItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphicsLayoutItemCall0)(const void *, const QRectF *, int *);
typedef void (*CuteQGraphicsLayoutItemCall1)(const void *, int *);
typedef bool (*CuteQGraphicsLayoutItemCall2)(const void *, int *);
typedef const QSizeF * (*CuteQGraphicsLayoutItemCall3)(const void *, int, const QSizeF *, int *);
class CuteQGraphicsLayoutItem : public QGraphicsLayoutItem {
public:
  using QGraphicsLayoutItem::QGraphicsLayoutItem;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem11setGeometryERK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGraphicsLayoutItem14updateGeometryEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem7isEmptyEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QGraphicsLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QGraphicsLayoutItem::setGeometry(const QRectF &rect)
  void setGeometry(const QRectF &rect) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsLayoutItemCall0 call = reinterpret_cast<CuteQGraphicsLayoutItemCall0>(taken[0]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QGraphicsLayoutItem::setGeometry(rect);
  }

  //  void QGraphicsLayoutItem::updateGeometry()
  void updateGeometry() override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsLayoutItemCall1 call = reinterpret_cast<CuteQGraphicsLayoutItemCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsLayoutItem::updateGeometry();
  }

  //  bool QGraphicsLayoutItem::isEmpty() const
  bool isEmpty() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsLayoutItemCall2 call = reinterpret_cast<CuteQGraphicsLayoutItemCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsLayoutItemCall3 call = reinterpret_cast<CuteQGraphicsLayoutItemCall3>(taken[3]);
      const QSizeF * given = call(this, static_cast<int>(which), &constraint, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QGraphicsLayoutItem::~QGraphicsLayoutItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsLayoutItemD1Ev(QGraphicsLayoutItem *self) {
  delete self;
}

//  void QGraphicsLayoutItem::setSizePolicy(const QSizePolicy &policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsLayoutItem13setSizePolicyERK11QSizePolicy(
    QGraphicsLayoutItem *self,
    const QSizePolicy *policy) {
  self->setSizePolicy(*policy);
}

//  void QGraphicsLayoutItem::setSizePolicy(QSizePolicy::Policy hPolicy,
//      QSizePolicy::Policy vPolicy, QSizePolicy::ControlType controlType)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsLayoutItem13setSizePolicyEN11QSizePolicy6PolicyES1_NS0_11ControlTypeE(
    QGraphicsLayoutItem *self,
    QSizePolicy::Policy hPolicy,
    QSizePolicy::Policy vPolicy,
    QSizePolicy::ControlType controlType) {
  self->setSizePolicy(hPolicy, vPolicy, controlType);
}

//  QSizePolicy QGraphicsLayoutItem::sizePolicy() const
extern "C" Q_DECL_EXPORT
QSizePolicy *ritual_ZNK19QGraphicsLayoutItem10sizePolicyEv(
    const QGraphicsLayoutItem *self) {
  return new QSizePolicy(self->sizePolicy());
}

//  void QGraphicsLayoutItem::setMinimumSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsLayoutItem14setMinimumSizeERK6QSizeF(
    QGraphicsLayoutItem *self,
    const QSizeF *size) {
  self->setMinimumSize(*size);
}

//  void QGraphicsLayoutItem::setMinimumSize(qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsLayoutItem14setMinimumSizeEdd(
    QGraphicsLayoutItem *self,
    qreal w,
    qreal h) {
  self->setMinimumSize(w, h);
}

//  QSizeF QGraphicsLayoutItem::minimumSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK19QGraphicsLayoutItem11minimumSizeEv(
    const QGraphicsLayoutItem *self) {
  return new QSizeF(self->minimumSize());
}

//  void QGraphicsLayoutItem::setMinimumWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsLayoutItem15setMinimumWidthEd(
    QGraphicsLayoutItem *self,
    qreal width) {
  self->setMinimumWidth(width);
}

//  qreal QGraphicsLayoutItem::minimumWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsLayoutItem12minimumWidthEv(
    const QGraphicsLayoutItem *self) {
  return self->minimumWidth();
}

//  void QGraphicsLayoutItem::setMinimumHeight(qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsLayoutItem16setMinimumHeightEd(
    QGraphicsLayoutItem *self,
    qreal height) {
  self->setMinimumHeight(height);
}

//  qreal QGraphicsLayoutItem::minimumHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsLayoutItem13minimumHeightEv(
    const QGraphicsLayoutItem *self) {
  return self->minimumHeight();
}

//  void QGraphicsLayoutItem::setPreferredSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsLayoutItem16setPreferredSizeERK6QSizeF(
    QGraphicsLayoutItem *self,
    const QSizeF *size) {
  self->setPreferredSize(*size);
}

//  void QGraphicsLayoutItem::setPreferredSize(qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsLayoutItem16setPreferredSizeEdd(
    QGraphicsLayoutItem *self,
    qreal w,
    qreal h) {
  self->setPreferredSize(w, h);
}

//  QSizeF QGraphicsLayoutItem::preferredSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK19QGraphicsLayoutItem13preferredSizeEv(
    const QGraphicsLayoutItem *self) {
  return new QSizeF(self->preferredSize());
}

//  void QGraphicsLayoutItem::setPreferredWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsLayoutItem17setPreferredWidthEd(
    QGraphicsLayoutItem *self,
    qreal width) {
  self->setPreferredWidth(width);
}

//  qreal QGraphicsLayoutItem::preferredWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsLayoutItem14preferredWidthEv(
    const QGraphicsLayoutItem *self) {
  return self->preferredWidth();
}

//  void QGraphicsLayoutItem::setPreferredHeight(qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsLayoutItem18setPreferredHeightEd(
    QGraphicsLayoutItem *self,
    qreal height) {
  self->setPreferredHeight(height);
}

//  qreal QGraphicsLayoutItem::preferredHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsLayoutItem15preferredHeightEv(
    const QGraphicsLayoutItem *self) {
  return self->preferredHeight();
}

//  void QGraphicsLayoutItem::setMaximumSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsLayoutItem14setMaximumSizeERK6QSizeF(
    QGraphicsLayoutItem *self,
    const QSizeF *size) {
  self->setMaximumSize(*size);
}

//  void QGraphicsLayoutItem::setMaximumSize(qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsLayoutItem14setMaximumSizeEdd(
    QGraphicsLayoutItem *self,
    qreal w,
    qreal h) {
  self->setMaximumSize(w, h);
}

//  QSizeF QGraphicsLayoutItem::maximumSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK19QGraphicsLayoutItem11maximumSizeEv(
    const QGraphicsLayoutItem *self) {
  return new QSizeF(self->maximumSize());
}

//  void QGraphicsLayoutItem::setMaximumWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsLayoutItem15setMaximumWidthEd(
    QGraphicsLayoutItem *self,
    qreal width) {
  self->setMaximumWidth(width);
}

//  qreal QGraphicsLayoutItem::maximumWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsLayoutItem12maximumWidthEv(
    const QGraphicsLayoutItem *self) {
  return self->maximumWidth();
}

//  void QGraphicsLayoutItem::setMaximumHeight(qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsLayoutItem16setMaximumHeightEd(
    QGraphicsLayoutItem *self,
    qreal height) {
  self->setMaximumHeight(height);
}

//  qreal QGraphicsLayoutItem::maximumHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsLayoutItem13maximumHeightEv(
    const QGraphicsLayoutItem *self) {
  return self->maximumHeight();
}

//  void QGraphicsLayoutItem::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsLayoutItem11setGeometryERK6QRectF(
    QGraphicsLayoutItem *self,
    const QRectF *rect) {
  self->setGeometry(*rect);
}

//  QRectF QGraphicsLayoutItem::geometry() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19QGraphicsLayoutItem8geometryEv(
    const QGraphicsLayoutItem *self) {
  return new QRectF(self->geometry());
}

//  void QGraphicsLayoutItem::getContentsMargins(qreal *left, qreal *top,
//      qreal *right, qreal *bottom) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QGraphicsLayoutItem18getContentsMarginsEPdS0_S0_S0_(
    const QGraphicsLayoutItem *self,
    qreal *left,
    qreal *top,
    qreal *right,
    qreal *bottom) {
  self->getContentsMargins(left, top, right, bottom);
}

//  QRectF QGraphicsLayoutItem::contentsRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19QGraphicsLayoutItem12contentsRectEv(
    const QGraphicsLayoutItem *self) {
  return new QRectF(self->contentsRect());
}

//  QSizeF QGraphicsLayoutItem::effectiveSizeHint(Qt::SizeHint which, const
//      QSizeF &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK19QGraphicsLayoutItem17effectiveSizeHintEN2Qt8SizeHintERK6QSizeF(
    const QGraphicsLayoutItem *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->effectiveSizeHint(which, *constraint));
}

//  void QGraphicsLayoutItem::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsLayoutItem14updateGeometryEv(
    QGraphicsLayoutItem *self) {
  self->updateGeometry();
}

//  bool QGraphicsLayoutItem::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGraphicsLayoutItem7isEmptyEv(
    const QGraphicsLayoutItem *self) {
  return self->isEmpty();
}

//  QGraphicsLayoutItem *QGraphicsLayoutItem::parentLayoutItem() const
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_ZNK19QGraphicsLayoutItem16parentLayoutItemEv(
    const QGraphicsLayoutItem *self) {
  return self->parentLayoutItem();
}

//  void QGraphicsLayoutItem::setParentLayoutItem(QGraphicsLayoutItem
//      *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsLayoutItem19setParentLayoutItemEPS_(
    QGraphicsLayoutItem *self,
    QGraphicsLayoutItem *parent) {
  self->setParentLayoutItem(parent);
}

//  bool QGraphicsLayoutItem::isLayout() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGraphicsLayoutItem8isLayoutEv(
    const QGraphicsLayoutItem *self) {
  return self->isLayout();
}

//  QGraphicsItem *QGraphicsLayoutItem::graphicsItem() const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK19QGraphicsLayoutItem12graphicsItemEv(
    const QGraphicsLayoutItem *self) {
  return self->graphicsItem();
}

//  bool QGraphicsLayoutItem::ownedByLayout() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGraphicsLayoutItem13ownedByLayoutEv(
    const QGraphicsLayoutItem *self) {
  return self->ownedByLayout();
}

//  a Python function taken by a CuteQGraphicsLayoutItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsLayoutItem(
    QGraphicsLayoutItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsLayoutItem *>(self)->take(key, call);
}

//  void QGraphicsLayoutItem::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGraphicsLayoutItem11setGeometryERK6QRectF(
    QGraphicsLayoutItem *self,
    const QRectF *rect) {
  self->QGraphicsLayoutItem::setGeometry(*rect);
}

//  void QGraphicsLayoutItem::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGraphicsLayoutItem14updateGeometryEv(
    QGraphicsLayoutItem *self) {
  self->QGraphicsLayoutItem::updateGeometry();
}

//  bool QGraphicsLayoutItem::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QGraphicsLayoutItem7isEmptyEv(
    const QGraphicsLayoutItem *self) {
  return self->QGraphicsLayoutItem::isEmpty();
}
