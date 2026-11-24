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

//  A QSvgFeMerge that Python can take functions over in. Every QSvgFeMerge
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgFeMergeCall0)(const void *, int *);
typedef bool (*CuteQSvgFeMergeCall1)(const void *, int *);
typedef bool (*CuteQSvgFeMergeCall2)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgFeMergeCall3)(const void *, int *);
class CuteQSvgFeMerge : public QSvgFeMerge {
public:
  using QSvgFeMerge::QSvgFeMerge;
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

  //  Type QSvgFeMerge::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgFeMergeCall0 call = reinterpret_cast<CuteQSvgFeMergeCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgFeMerge::type();
  }

  //  bool QSvgFeMerge::requiresSourceAlpha() const
  bool requiresSourceAlpha() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgFeMergeCall1 call = reinterpret_cast<CuteQSvgFeMergeCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgFeMerge::requiresSourceAlpha();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgFeMergeCall2 call = reinterpret_cast<CuteQSvgFeMergeCall2>(taken[2]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSvgFeMergeCall3 call = reinterpret_cast<CuteQSvgFeMergeCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgFeMerge::QSvgFeMerge(QSvgNode *parent, const QString &input, const
//      QString &result, const QSvgRectF &rect)
extern "C" Q_DECL_EXPORT
QSvgFeMerge *ritual_ZN11QSvgFeMergeC1EP8QSvgNodeRK7QStringS4_RK9QSvgRectF(
    QSvgNode *parent,
    const QString *input,
    const QString *result,
    const QSvgRectF *rect) {
  return new CuteQSvgFeMerge(parent, *input, *result, *rect);
}

//  QSvgFeMerge::~QSvgFeMerge()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgFeMergeD1Ev(QSvgFeMerge *self) {
  delete self;
}

//  Type QSvgFeMerge::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK11QSvgFeMerge4typeEv(const QSvgFeMerge *self) {
  return self->type();
}

//  QImage QSvgFeMerge::apply(const QMap<QString, QImage> &sources, QPainter
//      *p, const QRectF &itemBounds, const QRectF &filterBounds,
//      QtSvg::UnitTypes primitiveUnits, QtSvg::UnitTypes filterUnits) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK11QSvgFeMerge5applyERK4QMapI7QString6QImageEP8QPainterRK6QRectFSA_N5QtSvg9UnitTypesESC_(
    const QSvgFeMerge *self,
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

//  bool QSvgFeMerge::requiresSourceAlpha() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSvgFeMerge19requiresSourceAlphaEv(
    const QSvgFeMerge *self) {
  return self->requiresSourceAlpha();
}

//  a Python function taken by a CuteQSvgFeMerge, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgFeMerge(
    QSvgFeMerge *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgFeMerge *>(self)->take(key, call);
}

//  Type QSvgFeMerge::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK11QSvgFeMerge4typeEv(const QSvgFeMerge *self) {
  return self->QSvgFeMerge::type();
}

//  bool QSvgFeMerge::requiresSourceAlpha() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QSvgFeMerge19requiresSourceAlphaEv(
    const QSvgFeMerge *self) {
  return self->QSvgFeMerge::requiresSourceAlpha();
}
