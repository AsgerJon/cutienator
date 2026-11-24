//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgfilter_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgfilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qimage.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvghelper_p.h>
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QSvgFeFilterPrimitive that Python can take functions over in. Every QSvgFeFilterPrimitive
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSvgFeFilterPrimitiveCall0)(const void *, int *);
typedef bool (*CuteQSvgFeFilterPrimitiveCall1)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef int (*CuteQSvgFeFilterPrimitiveCall2)(const void *, int *);
typedef bool (*CuteQSvgFeFilterPrimitiveCall3)(const void *, int *);
class CuteQSvgFeFilterPrimitive : public QSvgFeFilterPrimitive {
public:
  using QSvgFeFilterPrimitive::QSvgFeFilterPrimitive;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK21QSvgFeFilterPrimitive19requiresSourceAlphaEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgExtraStates")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode4typeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode22requiresGroupRenderingEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  bool QSvgFeFilterPrimitive::requiresSourceAlpha() const
  bool requiresSourceAlpha() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgFeFilterPrimitiveCall0 call = reinterpret_cast<CuteQSvgFeFilterPrimitiveCall0>(taken[0]);
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
    if (taken[1]) {
      int handled = 0;
      CuteQSvgFeFilterPrimitiveCall1 call = reinterpret_cast<CuteQSvgFeFilterPrimitiveCall1>(taken[1]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  Type QSvgNode::type() const
  QSvgNode::Type type() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgFeFilterPrimitiveCall2 call = reinterpret_cast<CuteQSvgFeFilterPrimitiveCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return {};
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSvgFeFilterPrimitiveCall3 call = reinterpret_cast<CuteQSvgFeFilterPrimitiveCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgFeFilterPrimitive::~QSvgFeFilterPrimitive()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSvgFeFilterPrimitiveD1Ev(QSvgFeFilterPrimitive *self) {
  delete self;
}

//  QRectF QSvgFeFilterPrimitive::localSubRegion(const QRectF &itemBounds,
//      const QRectF &filterBounds, QtSvg::UnitTypes primitiveUnits,
//      QtSvg::UnitTypes filterUnits) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK21QSvgFeFilterPrimitive14localSubRegionERK6QRectFS2_N5QtSvg9UnitTypesES4_(
    const QSvgFeFilterPrimitive *self,
    const QRectF *itemBounds,
    const QRectF *filterBounds,
    QtSvg::UnitTypes primitiveUnits,
    QtSvg::UnitTypes filterUnits) {
  return new QRectF(
      self->localSubRegion(
          *itemBounds,
          *filterBounds,
          primitiveUnits,
          filterUnits));
}

//  QRectF QSvgFeFilterPrimitive::globalSubRegion(QPainter *p, const QRectF
//      &itemBounds, const QRectF &filterBounds, QtSvg::UnitTypes
//      primitiveUnits, QtSvg::UnitTypes filterUnits) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK21QSvgFeFilterPrimitive15globalSubRegionEP8QPainterRK6QRectFS4_N5QtSvg9UnitTypesES6_(
    const QSvgFeFilterPrimitive *self,
    QPainter *p,
    const QRectF *itemBounds,
    const QRectF *filterBounds,
    QtSvg::UnitTypes primitiveUnits,
    QtSvg::UnitTypes filterUnits) {
  return new QRectF(
      self->globalSubRegion(
          p,
          *itemBounds,
          *filterBounds,
          primitiveUnits,
          filterUnits));
}

//  void QSvgFeFilterPrimitive::clipToTransformedBounds(QImage *buffer,
//      QPainter *p, const QRectF &localRect) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QSvgFeFilterPrimitive23clipToTransformedBoundsEP6QImageP8QPainterRK6QRectF(
    const QSvgFeFilterPrimitive *self,
    QImage *buffer,
    QPainter *p,
    const QRectF *localRect) {
  self->clipToTransformedBounds(buffer, p, *localRect);
}

//  QImage QSvgFeFilterPrimitive::apply(const QMap<QString, QImage> &sources,
//      QPainter *p, const QRectF &itemBounds, const QRectF &filterBounds,
//      QtSvg::UnitTypes primitiveUnits, QtSvg::UnitTypes filterUnits) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK21QSvgFeFilterPrimitive5applyERK4QMapI7QString6QImageEP8QPainterRK6QRectFSA_N5QtSvg9UnitTypesESC_(
    const QSvgFeFilterPrimitive *self,
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

//  bool QSvgFeFilterPrimitive::requiresSourceAlpha() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSvgFeFilterPrimitive19requiresSourceAlphaEv(
    const QSvgFeFilterPrimitive *self) {
  return self->requiresSourceAlpha();
}

//  QString QSvgFeFilterPrimitive::input() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QSvgFeFilterPrimitive5inputEv(
    const QSvgFeFilterPrimitive *self) {
  return new QString(self->input());
}

//  QString QSvgFeFilterPrimitive::result() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QSvgFeFilterPrimitive6resultEv(
    const QSvgFeFilterPrimitive *self) {
  return new QString(self->result());
}

//  QSvgRectF QSvgFeFilterPrimitive::rect() const
extern "C" Q_DECL_EXPORT
QSvgRectF *ritual_ZNK21QSvgFeFilterPrimitive4rectEv(
    const QSvgFeFilterPrimitive *self) {
  return new QSvgRectF(self->rect());
}

//  const QSvgFeFilterPrimitive
//      *QSvgFeFilterPrimitive::castToFilterPrimitive(const QSvgNode *node)
extern "C" Q_DECL_EXPORT
const QSvgFeFilterPrimitive *ritual_ZN21QSvgFeFilterPrimitive21castToFilterPrimitiveEPK8QSvgNode(
    const QSvgNode *node) {
  return QSvgFeFilterPrimitive::castToFilterPrimitive(node);
}

//  a Python function taken by a CuteQSvgFeFilterPrimitive, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgFeFilterPrimitive(
    QSvgFeFilterPrimitive *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgFeFilterPrimitive *>(self)->take(key, call);
}

//  bool QSvgFeFilterPrimitive::requiresSourceAlpha() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QSvgFeFilterPrimitive19requiresSourceAlphaEv(
    const QSvgFeFilterPrimitive *self) {
  return self->QSvgFeFilterPrimitive::requiresSourceAlpha();
}
