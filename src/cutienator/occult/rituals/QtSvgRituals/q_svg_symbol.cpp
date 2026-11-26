//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgstructure_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstructure_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgSymbol that Python can take functions over in. Every QSvgSymbol
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgSymbolCall0)(const void *, int *);
typedef bool (*CuteQSvgSymbolCall1)(const void *, int *);
typedef bool (*CuteQSvgSymbolCall2)(const void *, const QPainter *, const QSvgExtraStates *, int *);
class CuteQSvgSymbol : public QSvgSymbol {
public:
  using QSvgSymbol::QSvgSymbol;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8QSvgNode4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode22requiresGroupRenderingEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgExtraStates")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  Type QSvgSymbol::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgSymbolCall0 call = reinterpret_cast<CuteQSvgSymbolCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgSymbol::type();
  }

  //  bool QSvgSymbolLike::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgSymbolCall1 call = reinterpret_cast<CuteQSvgSymbolCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgSymbolLike::requiresGroupRendering();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgSymbolCall2 call = reinterpret_cast<CuteQSvgSymbolCall2>(taken[2]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }
};

//  QSvgSymbol::QSvgSymbol(QSvgNode *parent, QRectF bounds, QRectF viewBox,
//      QPointF refP, QSvgSymbolLike::PreserveAspectRatios pAspectRatios,
//      QSvgSymbolLike::Overflow overflow)
extern "C" Q_DECL_EXPORT
QSvgSymbol *ritual_ZN10QSvgSymbolC1EP8QSvgNode6QRectFS2_7QPointF6QFlagsIN14QSvgSymbolLike19PreserveAspectRatioEENS5_8OverflowE(
    QSvgNode *parent,
    const QRectF *bounds,
    const QRectF *viewBox,
    const QPointF *refP,
    int pAspectRatios,
    QSvgSymbolLike::Overflow overflow) {
  return new CuteQSvgSymbol(
      parent,
      *bounds,
      *viewBox,
      *refP,
      QFlags<QSvgSymbolLike::PreserveAspectRatio>::fromInt(pAspectRatios),
      overflow);
}

//  QSvgSymbol::~QSvgSymbol()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSvgSymbolD1Ev(QSvgSymbol *self) {
  delete self;
}

//  void QSvgSymbol::drawCommand(QPainter *p, QSvgExtraStates &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSvgSymbol11drawCommandEP8QPainterR15QSvgExtraStates(
    QSvgSymbol *self,
    QPainter *p,
    QSvgExtraStates *states) {
  self->drawCommand(p, *states);
}

//  Type QSvgSymbol::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK10QSvgSymbol4typeEv(const QSvgSymbol *self) {
  return self->type();
}

//  a Python function taken by a CuteQSvgSymbol, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgSymbol(QSvgSymbol *self, const char *key, void *call) {
  return static_cast<CuteQSvgSymbol *>(self)->take(key, call);
}

//  Type QSvgSymbol::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK10QSvgSymbol4typeEv(const QSvgSymbol *self) {
  return self->QSvgSymbol::type();
}
