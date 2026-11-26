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
#include <cstring>

//  A QSvgFillStyle that Python can take functions over in. Every QSvgFillStyle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgFillStyleCall0)(const void *, int *);
typedef bool (*CuteQSvgFillStyleCall1)(const void *, int *);
class CuteQSvgFillStyle : public QSvgFillStyle {
public:
  using QSvgFillStyle::QSvgFillStyle;
  CuteQSvgFillStyle(const QSvgFillStyle & other) : QSvgFillStyle(other) {}
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

  //  Type QSvgFillStyle::type() const
  QSvgStyleProperty::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgFillStyleCall0 call = reinterpret_cast<CuteQSvgFillStyleCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgStyleProperty::Type>(given);
    }
    return QSvgFillStyle::type();
  }

  //  bool QSvgStyleProperty::isDefault() const
  bool isDefault() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgFillStyleCall1 call = reinterpret_cast<CuteQSvgFillStyleCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgStyleProperty::isDefault();
  }
};

//  QSvgFillStyle::QSvgFillStyle()
extern "C" Q_DECL_EXPORT
QSvgFillStyle *ritual_ZN13QSvgFillStyleC1Ev() {
  return new CuteQSvgFillStyle();
}

//  QSvgFillStyle::~QSvgFillStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgFillStyleD1Ev(QSvgFillStyle *self) {
  delete self;
}

//  void QSvgFillStyle::apply(QPainter *p, const QSvgNode *node,
//      QSvgExtraStates &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgFillStyle5applyEP8QPainterPK8QSvgNodeR15QSvgExtraStates(
    QSvgFillStyle *self,
    QPainter *p,
    const QSvgNode *node,
    QSvgExtraStates *states) {
  self->apply(p, node, *states);
}

//  void QSvgFillStyle::revert(QPainter *p, QSvgExtraStates &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgFillStyle6revertEP8QPainterR15QSvgExtraStates(
    QSvgFillStyle *self,
    QPainter *p,
    QSvgExtraStates *states) {
  self->revert(p, *states);
}

//  Type QSvgFillStyle::type() const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty::Type ritual_ZNK13QSvgFillStyle4typeEv(
    const QSvgFillStyle *self) {
  return self->type();
}

//  void QSvgFillStyle::setFillRule(Qt::FillRule f)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgFillStyle11setFillRuleEN2Qt8FillRuleE(
    QSvgFillStyle *self,
    Qt::FillRule f) {
  self->setFillRule(f);
}

//  void QSvgFillStyle::setFillOpacity(qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgFillStyle14setFillOpacityEd(
    QSvgFillStyle *self,
    qreal opacity) {
  self->setFillOpacity(opacity);
}

//  void QSvgFillStyle::setPaintServer(QSvgPaintServerSharedPtr paintServer)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgFillStyle14setPaintServerESt10shared_ptrI15QSvgPaintServerE(
    QSvgFillStyle *self,
    const QSvgPaintServerSharedPtr *paintServer) {
  self->setPaintServer(*paintServer);
}

//  void QSvgFillStyle::setBrush(QBrush brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgFillStyle8setBrushE6QBrush(
    QSvgFillStyle *self,
    const QBrush *brush) {
  self->setBrush(*brush);
}

//  const QBrush &QSvgFillStyle::qbrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK13QSvgFillStyle6qbrushEv(const QSvgFillStyle *self) {
  return new QBrush(self->qbrush());
}

//  qreal QSvgFillStyle::fillOpacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QSvgFillStyle11fillOpacityEv(const QSvgFillStyle *self) {
  return self->fillOpacity();
}

//  Qt::FillRule QSvgFillStyle::fillRule() const
extern "C" Q_DECL_EXPORT
Qt::FillRule ritual_ZNK13QSvgFillStyle8fillRuleEv(
    const QSvgFillStyle *self) {
  return self->fillRule();
}

//  QSvgPaintServer *QSvgFillStyle::paintServer() const
extern "C" Q_DECL_EXPORT
QSvgPaintServer *ritual_ZNK13QSvgFillStyle11paintServerEv(
    const QSvgFillStyle *self) {
  return self->paintServer();
}

//  void QSvgFillStyle::setPaintStyleId(const QString &Id)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgFillStyle15setPaintStyleIdERK7QString(
    QSvgFillStyle *self,
    const QString *Id) {
  self->setPaintStyleId(*Id);
}

//  QString QSvgFillStyle::paintStyleId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QSvgFillStyle12paintStyleIdEv(
    const QSvgFillStyle *self) {
  return new QString(self->paintStyleId());
}

//  a Python function taken by a CuteQSvgFillStyle, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgFillStyle(
    QSvgFillStyle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgFillStyle *>(self)->take(key, call);
}

//  Type QSvgFillStyle::type() const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty::Type ritual_own_ZNK13QSvgFillStyle4typeEv(
    const QSvgFillStyle *self) {
  return self->QSvgFillStyle::type();
}
