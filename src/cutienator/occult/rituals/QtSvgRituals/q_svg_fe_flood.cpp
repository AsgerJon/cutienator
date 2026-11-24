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
#include <QtGui/qcolor.h>
#include <QtGui/qimage.h>
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QSvgFeFlood that Python can take functions over in. Every QSvgFeFlood
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgFeFloodCall0)(const void *, int *);
typedef bool (*CuteQSvgFeFloodCall1)(const void *, int *);
typedef bool (*CuteQSvgFeFloodCall2)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgFeFloodCall3)(const void *, int *);
class CuteQSvgFeFlood : public QSvgFeFlood {
public:
  using QSvgFeFlood::QSvgFeFlood;
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

  //  Type QSvgFeFlood::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgFeFloodCall0 call = reinterpret_cast<CuteQSvgFeFloodCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgFeFlood::type();
  }

  //  bool QSvgFeFilterPrimitive::requiresSourceAlpha() const
  bool requiresSourceAlpha() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgFeFloodCall1 call = reinterpret_cast<CuteQSvgFeFloodCall1>(taken[1]);
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
      CuteQSvgFeFloodCall2 call = reinterpret_cast<CuteQSvgFeFloodCall2>(taken[2]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSvgFeFloodCall3 call = reinterpret_cast<CuteQSvgFeFloodCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgFeFlood::QSvgFeFlood(QSvgNode *parent, const QString &input, const
//      QString &result, const QSvgRectF &rect, const QColor &color)
extern "C" Q_DECL_EXPORT
QSvgFeFlood *ritual_ZN11QSvgFeFloodC1EP8QSvgNodeRK7QStringS4_RK9QSvgRectFRK6QColor(
    QSvgNode *parent,
    const QString *input,
    const QString *result,
    const QSvgRectF *rect,
    const QColor *color) {
  return new CuteQSvgFeFlood(parent, *input, *result, *rect, *color);
}

//  QSvgFeFlood::~QSvgFeFlood()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgFeFloodD1Ev(QSvgFeFlood *self) {
  delete self;
}

//  Type QSvgFeFlood::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK11QSvgFeFlood4typeEv(const QSvgFeFlood *self) {
  return self->type();
}

//  QImage QSvgFeFlood::apply(const QMap<QString, QImage> &sources, QPainter
//      *p, const QRectF &itemBounds, const QRectF &filterBounds,
//      QtSvg::UnitTypes primitiveUnits, QtSvg::UnitTypes filterUnits) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK11QSvgFeFlood5applyERK4QMapI7QString6QImageEP8QPainterRK6QRectFSA_N5QtSvg9UnitTypesESC_(
    const QSvgFeFlood *self,
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

//  QColor QSvgFeFlood::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QSvgFeFlood5colorEv(const QSvgFeFlood *self) {
  return new QColor(self->color());
}

//  a Python function taken by a CuteQSvgFeFlood, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgFeFlood(
    QSvgFeFlood *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgFeFlood *>(self)->take(key, call);
}

//  Type QSvgFeFlood::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK11QSvgFeFlood4typeEv(const QSvgFeFlood *self) {
  return self->QSvgFeFlood::type();
}
