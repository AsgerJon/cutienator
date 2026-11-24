//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgfilter_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgfilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvghelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QSvgFeGaussianBlur that Python can take functions over in. Every QSvgFeGaussianBlur
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgFeGaussianBlurCall0)(const void *, int *);
typedef bool (*CuteQSvgFeGaussianBlurCall1)(const void *, int *);
typedef bool (*CuteQSvgFeGaussianBlurCall2)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgFeGaussianBlurCall3)(const void *, int *);
class CuteQSvgFeGaussianBlur : public QSvgFeGaussianBlur {
public:
  using QSvgFeGaussianBlur::QSvgFeGaussianBlur;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8QSvgNode4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QSvgFeFilterPrimitive19requiresSourceAlphaEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgExtraStates")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode22requiresGroupRenderingEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  Type QSvgFeGaussianBlur::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgFeGaussianBlurCall0 call = reinterpret_cast<CuteQSvgFeGaussianBlurCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgFeGaussianBlur::type();
  }

  //  bool QSvgFeFilterPrimitive::requiresSourceAlpha() const
  bool requiresSourceAlpha() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgFeGaussianBlurCall1 call = reinterpret_cast<CuteQSvgFeGaussianBlurCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgFeFilterPrimitive::requiresSourceAlpha();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgFeGaussianBlurCall2 call = reinterpret_cast<CuteQSvgFeGaussianBlurCall2>(taken[2]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSvgFeGaussianBlurCall3 call = reinterpret_cast<CuteQSvgFeGaussianBlurCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgFeGaussianBlur::QSvgFeGaussianBlur(QSvgNode *parent, const QString
//      &input, const QString &result, const QSvgRectF &rect, qreal
//      stdDeviationX, qreal stdDeviationY, EdgeMode edgemode)
extern "C" Q_DECL_EXPORT
QSvgFeGaussianBlur *ritual_ZN18QSvgFeGaussianBlurC1EP8QSvgNodeRK7QStringS4_RK9QSvgRectFddNS_8EdgeModeE(
    QSvgNode *parent,
    const QString *input,
    const QString *result,
    const QSvgRectF *rect,
    qreal stdDeviationX,
    qreal stdDeviationY,
    QSvgFeGaussianBlur::EdgeMode edgemode) {
  return new CuteQSvgFeGaussianBlur(
      parent,
      *input,
      *result,
      *rect,
      stdDeviationX,
      stdDeviationY,
      edgemode);
}

//  QSvgFeGaussianBlur::~QSvgFeGaussianBlur()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSvgFeGaussianBlurD1Ev(QSvgFeGaussianBlur *self) {
  delete self;
}

//  Type QSvgFeGaussianBlur::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK18QSvgFeGaussianBlur4typeEv(
    const QSvgFeGaussianBlur *self) {
  return self->type();
}

//  QImage QSvgFeGaussianBlur::apply(const QMap<QString, QImage> &sources,
//      QPainter *p, const QRectF &itemBounds, const QRectF &filterBounds,
//      QtSvg::UnitTypes primitiveUnits, QtSvg::UnitTypes filterUnits) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK18QSvgFeGaussianBlur5applyERK4QMapI7QString6QImageEP8QPainterRK6QRectFSA_N5QtSvg9UnitTypesESC_(
    const QSvgFeGaussianBlur *self,
    const QMap<QString, QImage> *sources,
    QPainter *p,
    const QRectF *itemBounds,
    const QRectF *filterBounds,
    QtSvg::UnitTypes primitiveUnits,
    QtSvg::UnitTypes filterUnits) {
  return new QImage(
      self->apply(
          *sources,
          p,
          *itemBounds,
          *filterBounds,
          primitiveUnits,
          filterUnits));
}

//  qreal QSvgFeGaussianBlur::stdDeviationX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QSvgFeGaussianBlur13stdDeviationXEv(
    const QSvgFeGaussianBlur *self) {
  return self->stdDeviationX();
}

//  qreal QSvgFeGaussianBlur::stdDeviationY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QSvgFeGaussianBlur13stdDeviationYEv(
    const QSvgFeGaussianBlur *self) {
  return self->stdDeviationY();
}

//  EdgeMode QSvgFeGaussianBlur::edgeMode() const
extern "C" Q_DECL_EXPORT
QSvgFeGaussianBlur::EdgeMode ritual_ZNK18QSvgFeGaussianBlur8edgeModeEv(
    const QSvgFeGaussianBlur *self) {
  return self->edgeMode();
}

//  a Python function taken by a CuteQSvgFeGaussianBlur, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgFeGaussianBlur(
    QSvgFeGaussianBlur *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgFeGaussianBlur *>(self)->take(key, call);
}

//  Type QSvgFeGaussianBlur::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK18QSvgFeGaussianBlur4typeEv(
    const QSvgFeGaussianBlur *self) {
  return self->QSvgFeGaussianBlur::type();
}
