//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qbrush.h>
#include <QtCore/qstring.h>
#include <QtGui/qpen.h>
#include <cstring>

//  A QSvgStrokeStyle that Python can take functions over in. Every QSvgStrokeStyle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgStrokeStyleCall0)(const void *, int *);
typedef bool (*CuteQSvgStrokeStyleCall1)(const void *, int *);
class CuteQSvgStrokeStyle : public QSvgStrokeStyle {
public:
  using QSvgStrokeStyle::QSvgStrokeStyle;
  CuteQSvgStrokeStyle(const QSvgStrokeStyle & other) : QSvgStrokeStyle(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK17QSvgStyleProperty4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QSvgStyleProperty9isDefaultEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  Type QSvgStrokeStyle::type() const
  QSvgStyleProperty::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgStrokeStyleCall0 call = reinterpret_cast<CuteQSvgStrokeStyleCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgStyleProperty::Type>(given);
    }
    return QSvgStrokeStyle::type();
  }

  //  bool QSvgStyleProperty::isDefault() const
  bool isDefault() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgStrokeStyleCall1 call = reinterpret_cast<CuteQSvgStrokeStyleCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgStyleProperty::isDefault();
  }
};

//  QSvgStrokeStyle::QSvgStrokeStyle()
extern "C" Q_DECL_EXPORT
QSvgStrokeStyle *ritual_ZN15QSvgStrokeStyleC1Ev() {
  return new CuteQSvgStrokeStyle();
}

//  QSvgStrokeStyle::~QSvgStrokeStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgStrokeStyleD1Ev(QSvgStrokeStyle *self) {
  delete self;
}

//  void QSvgStrokeStyle::apply(QPainter *p, const QSvgNode *node,
//      QSvgExtraStates &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgStrokeStyle5applyEP8QPainterPK8QSvgNodeR15QSvgExtraStates(
    QSvgStrokeStyle *self,
    QPainter *p,
    const QSvgNode *node,
    QSvgExtraStates *states) {
  self->apply(p, node, *states);
}

//  void QSvgStrokeStyle::revert(QPainter *p, QSvgExtraStates &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgStrokeStyle6revertEP8QPainterR15QSvgExtraStates(
    QSvgStrokeStyle *self,
    QPainter *p,
    QSvgExtraStates *states) {
  self->revert(p, *states);
}

//  Type QSvgStrokeStyle::type() const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty::Type ritual_ZNK15QSvgStrokeStyle4typeEv(
    const QSvgStrokeStyle *self) {
  return self->type();
}

//  void QSvgStrokeStyle::setStroke(QBrush brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgStrokeStyle9setStrokeE6QBrush(
    QSvgStrokeStyle *self,
    const QBrush *brush) {
  self->setStroke(*brush);
}

//  void QSvgStrokeStyle::setPaintServer(QSvgPaintServerSharedPtr
//      paintServer)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgStrokeStyle14setPaintServerESt10shared_ptrI15QSvgPaintServerE(
    QSvgStrokeStyle *self,
    const QSvgPaintServerSharedPtr *paintServer) {
  self->setPaintServer(*paintServer);
}

//  void QSvgStrokeStyle::setDashArray(const QList<qreal> &dashes)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgStrokeStyle12setDashArrayERK5QListIdE(
    QSvgStrokeStyle *self,
    const QList<qreal> *dashes) {
  self->setDashArray(*dashes);
}

//  void QSvgStrokeStyle::setDashArrayNone()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgStrokeStyle16setDashArrayNoneEv(QSvgStrokeStyle *self) {
  self->setDashArrayNone();
}

//  void QSvgStrokeStyle::setDashOffset(qreal offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgStrokeStyle13setDashOffsetEd(
    QSvgStrokeStyle *self,
    qreal offset) {
  self->setDashOffset(offset);
}

//  void QSvgStrokeStyle::setLineCap(Qt::PenCapStyle cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgStrokeStyle10setLineCapEN2Qt11PenCapStyleE(
    QSvgStrokeStyle *self,
    Qt::PenCapStyle cap) {
  self->setLineCap(cap);
}

//  void QSvgStrokeStyle::setLineJoin(Qt::PenJoinStyle join)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgStrokeStyle11setLineJoinEN2Qt12PenJoinStyleE(
    QSvgStrokeStyle *self,
    Qt::PenJoinStyle join) {
  self->setLineJoin(join);
}

//  void QSvgStrokeStyle::setMiterLimit(qreal limit)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgStrokeStyle13setMiterLimitEd(
    QSvgStrokeStyle *self,
    qreal limit) {
  self->setMiterLimit(limit);
}

//  void QSvgStrokeStyle::setOpacity(qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgStrokeStyle10setOpacityEd(
    QSvgStrokeStyle *self,
    qreal opacity) {
  self->setOpacity(opacity);
}

//  void QSvgStrokeStyle::setWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgStrokeStyle8setWidthEd(
    QSvgStrokeStyle *self,
    qreal width) {
  self->setWidth(width);
}

//  qreal QSvgStrokeStyle::width()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN15QSvgStrokeStyle5widthEv(QSvgStrokeStyle *self) {
  return self->width();
}

//  void QSvgStrokeStyle::setVectorEffect(bool nonScalingStroke)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgStrokeStyle15setVectorEffectEb(
    QSvgStrokeStyle *self,
    bool nonScalingStroke) {
  self->setVectorEffect(nonScalingStroke);
}

//  QSvgPaintServer *QSvgStrokeStyle::paintServer() const
extern "C" Q_DECL_EXPORT
QSvgPaintServer *ritual_ZNK15QSvgStrokeStyle11paintServerEv(
    const QSvgStrokeStyle *self) {
  return self->paintServer();
}

//  void QSvgStrokeStyle::setPaintStyleId(const QString &Id)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgStrokeStyle15setPaintStyleIdERK7QString(
    QSvgStrokeStyle *self,
    const QString *Id) {
  self->setPaintStyleId(*Id);
}

//  QString QSvgStrokeStyle::paintStyleId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QSvgStrokeStyle12paintStyleIdEv(
    const QSvgStrokeStyle *self) {
  return new QString(self->paintStyleId());
}

//  QPen QSvgStrokeStyle::stroke() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK15QSvgStrokeStyle6strokeEv(const QSvgStrokeStyle *self) {
  return new QPen(self->stroke());
}

//  a Python function taken by a CuteQSvgStrokeStyle, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgStrokeStyle(
    QSvgStrokeStyle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgStrokeStyle *>(self)->take(key, call);
}

//  Type QSvgStrokeStyle::type() const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty::Type ritual_own_ZNK15QSvgStrokeStyle4typeEv(
    const QSvgStrokeStyle *self) {
  return self->QSvgStrokeStyle::type();
}
