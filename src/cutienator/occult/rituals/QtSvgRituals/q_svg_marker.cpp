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

//  A QSvgMarker that Python can take functions over in. Every QSvgMarker
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgMarkerCall0)(const void *, int *);
typedef bool (*CuteQSvgMarkerCall1)(const void *, int *);
typedef bool (*CuteQSvgMarkerCall2)(const void *, const QPainter *, const QSvgExtraStates *, int *);
class CuteQSvgMarker : public QSvgMarker {
public:
  using QSvgMarker::QSvgMarker;
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

  //  Type QSvgMarker::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgMarkerCall0 call = reinterpret_cast<CuteQSvgMarkerCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgMarker::type();
  }

  //  bool QSvgSymbolLike::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgMarkerCall1 call = reinterpret_cast<CuteQSvgMarkerCall1>(taken[1]);
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
      CuteQSvgMarkerCall2 call = reinterpret_cast<CuteQSvgMarkerCall2>(taken[2]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }
};

//  QSvgMarker::QSvgMarker(QSvgNode *parent, QRectF bounds, QRectF viewBox,
//      QPointF refP, QSvgSymbolLike::PreserveAspectRatios pAspectRatios,
//      QSvgSymbolLike::Overflow overflow, Orientation orientation, qreal
//      orientationAngle, MarkerUnits markerUnits)
extern "C" Q_DECL_EXPORT
QSvgMarker *ritual_ZN10QSvgMarkerC1EP8QSvgNode6QRectFS2_7QPointF6QFlagsIN14QSvgSymbolLike19PreserveAspectRatioEENS5_8OverflowENS_11OrientationEdNS_11MarkerUnitsE(
    QSvgNode *parent,
    const QRectF *bounds,
    const QRectF *viewBox,
    const QPointF *refP,
    int pAspectRatios,
    QSvgSymbolLike::Overflow overflow,
    QSvgMarker::Orientation orientation,
    qreal orientationAngle,
    QSvgMarker::MarkerUnits markerUnits) {
  return new CuteQSvgMarker(
      parent,
      *bounds,
      *viewBox,
      *refP,
      QFlags<QSvgSymbolLike::PreserveAspectRatio>::fromInt(pAspectRatios),
      overflow,
      orientation,
      orientationAngle,
      markerUnits);
}

//  QSvgMarker::~QSvgMarker()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSvgMarkerD1Ev(QSvgMarker *self) {
  delete self;
}

//  Orientation QSvgMarker::orientation() const
extern "C" Q_DECL_EXPORT
QSvgMarker::Orientation ritual_ZNK10QSvgMarker11orientationEv(
    const QSvgMarker *self) {
  return self->orientation();
}

//  qreal QSvgMarker::orientationAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QSvgMarker16orientationAngleEv(const QSvgMarker *self) {
  return self->orientationAngle();
}

//  MarkerUnits QSvgMarker::markerUnits() const
extern "C" Q_DECL_EXPORT
QSvgMarker::MarkerUnits ritual_ZNK10QSvgMarker11markerUnitsEv(
    const QSvgMarker *self) {
  return self->markerUnits();
}

//  Type QSvgMarker::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK10QSvgMarker4typeEv(const QSvgMarker *self) {
  return self->type();
}

//  a Python function taken by a CuteQSvgMarker, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgMarker(QSvgMarker *self, const char *key, void *call) {
  return static_cast<CuteQSvgMarker *>(self)->take(key, call);
}

//  Type QSvgMarker::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK10QSvgMarker4typeEv(const QSvgMarker *self) {
  return self->QSvgMarker::type();
}
