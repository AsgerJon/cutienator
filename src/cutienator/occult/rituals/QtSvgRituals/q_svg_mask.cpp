//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgstructure_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstructure_p.h>
#include <QtSvg/6.12.0/QtSvg/private/qsvghelper_p.h>
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgMask that Python can take functions over in. Every QSvgMask
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgMaskCall0)(const void *, int *);
typedef bool (*CuteQSvgMaskCall1)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgMaskCall2)(const void *, int *);
class CuteQSvgMask : public QSvgMask {
public:
  using QSvgMask::QSvgMask;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8QSvgNode4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgExtraStates")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode22requiresGroupRenderingEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  Type QSvgMask::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgMaskCall0 call = reinterpret_cast<CuteQSvgMaskCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgMask::type();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgMaskCall1 call = reinterpret_cast<CuteQSvgMaskCall1>(taken[1]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgMaskCall2 call = reinterpret_cast<CuteQSvgMaskCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgMask::QSvgMask(QSvgNode *parent, QSvgRectF bounds, QtSvg::UnitTypes
//      contentsUnits)
extern "C" Q_DECL_EXPORT
QSvgMask *ritual_ZN8QSvgMaskC1EP8QSvgNode9QSvgRectFN5QtSvg9UnitTypesE(
    QSvgNode *parent,
    const QSvgRectF *bounds,
    QtSvg::UnitTypes contentsUnits) {
  return new CuteQSvgMask(parent, *bounds, contentsUnits);
}

//  QSvgMask::~QSvgMask()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgMaskD1Ev(QSvgMask *self) {
  delete self;
}

//  Type QSvgMask::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK8QSvgMask4typeEv(const QSvgMask *self) {
  return self->type();
}

//  QSvgRectF QSvgMask::rect() const
extern "C" Q_DECL_EXPORT
QSvgRectF *ritual_ZNK8QSvgMask4rectEv(const QSvgMask *self) {
  return new QSvgRectF(self->rect());
}

//  QtSvg::UnitTypes QSvgMask::contentUnits() const
extern "C" Q_DECL_EXPORT
QtSvg::UnitTypes ritual_ZNK8QSvgMask12contentUnitsEv(const QSvgMask *self) {
  return self->contentUnits();
}

//  a Python function taken by a CuteQSvgMask, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgMask(QSvgMask *self, const char *key, void *call) {
  return static_cast<CuteQSvgMask *>(self)->take(key, call);
}

//  Type QSvgMask::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK8QSvgMask4typeEv(const QSvgMask *self) {
  return self->QSvgMask::type();
}
