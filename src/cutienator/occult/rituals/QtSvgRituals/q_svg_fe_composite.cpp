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
#include <QtGui/qvectornd.h>
#include <QtGui/qimage.h>
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QSvgFeComposite that Python can take functions over in. Every QSvgFeComposite
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgFeCompositeCall0)(const void *, int *);
typedef bool (*CuteQSvgFeCompositeCall1)(const void *, int *);
typedef bool (*CuteQSvgFeCompositeCall2)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgFeCompositeCall3)(const void *, int *);
class CuteQSvgFeComposite : public QSvgFeComposite {
public:
  using QSvgFeComposite::QSvgFeComposite;
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

  //  Type QSvgFeComposite::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgFeCompositeCall0 call = reinterpret_cast<CuteQSvgFeCompositeCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgFeComposite::type();
  }

  //  bool QSvgFeComposite::requiresSourceAlpha() const
  bool requiresSourceAlpha() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgFeCompositeCall1 call = reinterpret_cast<CuteQSvgFeCompositeCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgFeComposite::requiresSourceAlpha();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgFeCompositeCall2 call = reinterpret_cast<CuteQSvgFeCompositeCall2>(taken[2]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSvgFeCompositeCall3 call = reinterpret_cast<CuteQSvgFeCompositeCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgFeComposite::QSvgFeComposite(QSvgNode *parent, const QString &input,
//      const QString &result, const QSvgRectF &rect, const QString &input2,
//      Operator op, const QVector4D &k)
extern "C" Q_DECL_EXPORT
QSvgFeComposite *ritual_ZN15QSvgFeCompositeC1EP8QSvgNodeRK7QStringS4_RK9QSvgRectFS4_NS_8OperatorERK9QVector4D(
    QSvgNode *parent,
    const QString *input,
    const QString *result,
    const QSvgRectF *rect,
    const QString *input2,
    QSvgFeComposite::Operator op,
    const QVector4D *k) {
  return new CuteQSvgFeComposite(
      parent,
      *input,
      *result,
      *rect,
      *input2,
      op,
      *k);
}

//  QSvgFeComposite::~QSvgFeComposite()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgFeCompositeD1Ev(QSvgFeComposite *self) {
  delete self;
}

//  Type QSvgFeComposite::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK15QSvgFeComposite4typeEv(
    const QSvgFeComposite *self) {
  return self->type();
}

//  QImage QSvgFeComposite::apply(const QMap<QString, QImage> &sources,
//      QPainter *p, const QRectF &itemBounds, const QRectF &filterBounds,
//      QtSvg::UnitTypes primitiveUnits, QtSvg::UnitTypes filterUnits) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK15QSvgFeComposite5applyERK4QMapI7QString6QImageEP8QPainterRK6QRectFSA_N5QtSvg9UnitTypesESC_(
    const QSvgFeComposite *self,
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

//  bool QSvgFeComposite::requiresSourceAlpha() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSvgFeComposite19requiresSourceAlphaEv(
    const QSvgFeComposite *self) {
  return self->requiresSourceAlpha();
}

//  QString QSvgFeComposite::input2() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QSvgFeComposite6input2Ev(const QSvgFeComposite *self) {
  return new QString(self->input2());
}

//  Operator QSvgFeComposite::compositionOperator() const
extern "C" Q_DECL_EXPORT
QSvgFeComposite::Operator ritual_ZNK15QSvgFeComposite19compositionOperatorEv(
    const QSvgFeComposite *self) {
  return self->compositionOperator();
}

//  QVector4D QSvgFeComposite::k() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK15QSvgFeComposite1kEv(const QSvgFeComposite *self) {
  return new QVector4D(self->k());
}

//  a Python function taken by a CuteQSvgFeComposite, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgFeComposite(
    QSvgFeComposite *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgFeComposite *>(self)->take(key, call);
}

//  Type QSvgFeComposite::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK15QSvgFeComposite4typeEv(
    const QSvgFeComposite *self) {
  return self->QSvgFeComposite::type();
}

//  bool QSvgFeComposite::requiresSourceAlpha() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QSvgFeComposite19requiresSourceAlphaEv(
    const QSvgFeComposite *self) {
  return self->QSvgFeComposite::requiresSourceAlpha();
}
