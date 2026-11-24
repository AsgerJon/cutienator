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

//  A QSvgFeMergeNode that Python can take functions over in. Every QSvgFeMergeNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgFeMergeNodeCall0)(const void *, int *);
typedef bool (*CuteQSvgFeMergeNodeCall1)(const void *, int *);
typedef bool (*CuteQSvgFeMergeNodeCall2)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgFeMergeNodeCall3)(const void *, int *);
class CuteQSvgFeMergeNode : public QSvgFeMergeNode {
public:
  using QSvgFeMergeNode::QSvgFeMergeNode;
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

  //  Type QSvgFeMergeNode::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgFeMergeNodeCall0 call = reinterpret_cast<CuteQSvgFeMergeNodeCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgFeMergeNode::type();
  }

  //  bool QSvgFeFilterPrimitive::requiresSourceAlpha() const
  bool requiresSourceAlpha() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgFeMergeNodeCall1 call = reinterpret_cast<CuteQSvgFeMergeNodeCall1>(taken[1]);
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
      CuteQSvgFeMergeNodeCall2 call = reinterpret_cast<CuteQSvgFeMergeNodeCall2>(taken[2]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSvgFeMergeNodeCall3 call = reinterpret_cast<CuteQSvgFeMergeNodeCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgFeMergeNode::QSvgFeMergeNode(QSvgNode *parent, const QString &input,
//      const QString &result, const QSvgRectF &rect)
extern "C" Q_DECL_EXPORT
QSvgFeMergeNode *ritual_ZN15QSvgFeMergeNodeC1EP8QSvgNodeRK7QStringS4_RK9QSvgRectF(
    QSvgNode *parent,
    const QString *input,
    const QString *result,
    const QSvgRectF *rect) {
  return new CuteQSvgFeMergeNode(parent, *input, *result, *rect);
}

//  QSvgFeMergeNode::~QSvgFeMergeNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgFeMergeNodeD1Ev(QSvgFeMergeNode *self) {
  delete self;
}

//  Type QSvgFeMergeNode::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK15QSvgFeMergeNode4typeEv(
    const QSvgFeMergeNode *self) {
  return self->type();
}

//  QImage QSvgFeMergeNode::apply(const QMap<QString, QImage> &sources,
//      QPainter *p, const QRectF &itemBounds, const QRectF &filterBounds,
//      QtSvg::UnitTypes primitiveUnits, QtSvg::UnitTypes filterUnits) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK15QSvgFeMergeNode5applyERK4QMapI7QString6QImageEP8QPainterRK6QRectFSA_N5QtSvg9UnitTypesESC_(
    const QSvgFeMergeNode *self,
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

//  a Python function taken by a CuteQSvgFeMergeNode, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgFeMergeNode(
    QSvgFeMergeNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgFeMergeNode *>(self)->take(key, call);
}

//  Type QSvgFeMergeNode::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK15QSvgFeMergeNode4typeEv(
    const QSvgFeMergeNode *self) {
  return self->QSvgFeMergeNode::type();
}
