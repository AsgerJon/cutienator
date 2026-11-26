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

//  A QSvgFeColorMatrix that Python can take functions over in. Every QSvgFeColorMatrix
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgFeColorMatrixCall0)(const void *, int *);
typedef bool (*CuteQSvgFeColorMatrixCall1)(const void *, int *);
typedef bool (*CuteQSvgFeColorMatrixCall2)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgFeColorMatrixCall3)(const void *, int *);
class CuteQSvgFeColorMatrix : public QSvgFeColorMatrix {
public:
  using QSvgFeColorMatrix::QSvgFeColorMatrix;
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

  //  Type QSvgFeColorMatrix::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgFeColorMatrixCall0 call = reinterpret_cast<CuteQSvgFeColorMatrixCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgFeColorMatrix::type();
  }

  //  bool QSvgFeFilterPrimitive::requiresSourceAlpha() const
  bool requiresSourceAlpha() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgFeColorMatrixCall1 call = reinterpret_cast<CuteQSvgFeColorMatrixCall1>(taken[1]);
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
      CuteQSvgFeColorMatrixCall2 call = reinterpret_cast<CuteQSvgFeColorMatrixCall2>(taken[2]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSvgFeColorMatrixCall3 call = reinterpret_cast<CuteQSvgFeColorMatrixCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgFeColorMatrix::QSvgFeColorMatrix(QSvgNode *parent, const QString
//      &input, const QString &result, const QSvgRectF &rect, ColorShiftType
//      type, const Matrix &matrix)
extern "C" Q_DECL_EXPORT
QSvgFeColorMatrix *ritual_ZN17QSvgFeColorMatrixC1EP8QSvgNodeRK7QStringS4_RK9QSvgRectFNS_14ColorShiftTypeERK14QGenericMatrixILi5ELi5EdE(
    QSvgNode *parent,
    const QString *input,
    const QString *result,
    const QSvgRectF *rect,
    QSvgFeColorMatrix::ColorShiftType type,
    const QSvgFeColorMatrix::Matrix *matrix) {
  return new CuteQSvgFeColorMatrix(
      parent,
      *input,
      *result,
      *rect,
      type,
      *matrix);
}

//  QSvgFeColorMatrix::~QSvgFeColorMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSvgFeColorMatrixD1Ev(QSvgFeColorMatrix *self) {
  delete self;
}

//  Type QSvgFeColorMatrix::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK17QSvgFeColorMatrix4typeEv(
    const QSvgFeColorMatrix *self) {
  return self->type();
}

//  QImage QSvgFeColorMatrix::apply(const QMap<QString, QImage> &sources,
//      QPainter *p, const QRectF &itemBounds, const QRectF &filterBounds,
//      QtSvg::UnitTypes primitiveUnits, QtSvg::UnitTypes filterUnits) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK17QSvgFeColorMatrix5applyERK4QMapI7QString6QImageEP8QPainterRK6QRectFSA_N5QtSvg9UnitTypesESC_(
    const QSvgFeColorMatrix *self,
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

//  Matrix QSvgFeColorMatrix::matrix() const
extern "C" Q_DECL_EXPORT
QSvgFeColorMatrix::Matrix *ritual_ZNK17QSvgFeColorMatrix6matrixEv(
    const QSvgFeColorMatrix *self) {
  return new QSvgFeColorMatrix::Matrix(self->matrix());
}

//  a Python function taken by a CuteQSvgFeColorMatrix, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgFeColorMatrix(
    QSvgFeColorMatrix *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgFeColorMatrix *>(self)->take(key, call);
}

//  Type QSvgFeColorMatrix::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK17QSvgFeColorMatrix4typeEv(
    const QSvgFeColorMatrix *self) {
  return self->QSvgFeColorMatrix::type();
}

//  a QSvgFeColorMatrix::Matrix a ritual of QSvgFeColorMatrix gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSvgFeColorMatrix__QSvgFeColorMatrix_Matrix(
    QSvgFeColorMatrix::Matrix *self) {
  delete self;
}
