//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qclipperutils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qclipperutils_p.h>
#include <QtPositioning/6.12.0/QtPositioning/private/qdoublevector2d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <QtCore/QList>

//  QClipperUtils::QClipperUtils()
extern "C" Q_DECL_EXPORT
QClipperUtils *ritual_ZN13QClipperUtilsC1Ev() {
  return new QClipperUtils();
}

//  QClipperUtils::QClipperUtils(const QClipperUtils &other)
extern "C" Q_DECL_EXPORT
QClipperUtils *ritual_ZN13QClipperUtilsC1ERKS_(const QClipperUtils *other) {
  return new QClipperUtils(*other);
}

//  QClipperUtils::~QClipperUtils()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QClipperUtilsD1Ev(QClipperUtils *self) {
  delete self;
}

//  double QClipperUtils::clipperScaleFactor()
extern "C" Q_DECL_EXPORT
double ritual_ZN13QClipperUtils18clipperScaleFactorEv() {
  return QClipperUtils::clipperScaleFactor();
}

//  int QClipperUtils::pointInPolygon(const QDoubleVector2D &point, const
//      QList<QDoubleVector2D> &polygon)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QClipperUtils14pointInPolygonERK15QDoubleVector2DRK5QListIS0_E(
    const QDoubleVector2D *point,
    const QList<QDoubleVector2D> *polygon) {
  return QClipperUtils::pointInPolygon(*point, *polygon);
}

//  void QClipperUtils::clearClipper()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QClipperUtils12clearClipperEv(QClipperUtils *self) {
  self->clearClipper();
}

//  void QClipperUtils::addSubjectPath(const QList<QDoubleVector2D> &path,
//      bool closed)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QClipperUtils14addSubjectPathERK5QListI15QDoubleVector2DEb(
    QClipperUtils *self,
    const QList<QDoubleVector2D> *path,
    bool closed) {
  self->addSubjectPath(*path, closed);
}

//  void QClipperUtils::addClipPolygon(const QList<QDoubleVector2D> &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QClipperUtils14addClipPolygonERK5QListI15QDoubleVector2DE(
    QClipperUtils *self,
    const QList<QDoubleVector2D> *path) {
  self->addClipPolygon(*path);
}

//  QList<QList<QDoubleVector2D>> QClipperUtils::execute(Operation op,
//      PolyFillType subjFillType, PolyFillType clipFillType)
extern "C" Q_DECL_EXPORT
QList<QList<QDoubleVector2D>> *ritual_ZN13QClipperUtils7executeENS_9OperationENS_12PolyFillTypeES1_(
    QClipperUtils *self,
    QClipperUtils::Operation op,
    QClipperUtils::PolyFillType subjFillType,
    QClipperUtils::PolyFillType clipFillType) {
  return new QList<QList<QDoubleVector2D>>(
      self->execute(
          op,
          subjFillType,
          clipFillType));
}

//  void QClipperUtils::setPolygon(const QList<QDoubleVector2D> &polygon)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QClipperUtils10setPolygonERK5QListI15QDoubleVector2DE(
    QClipperUtils *self,
    const QList<QDoubleVector2D> *polygon) {
  self->setPolygon(*polygon);
}

//  int QClipperUtils::pointInPolygon(const QDoubleVector2D &point) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QClipperUtils14pointInPolygonERK15QDoubleVector2D(
    const QClipperUtils *self,
    const QDoubleVector2D *point) {
  return self->pointInPolygon(*point);
}

//  a QList<QList<QDoubleVector2D>> a ritual of QClipperUtils gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QClipperUtils__QList_QList_QDoubleVector2D(
    QList<QList<QDoubleVector2D>> *self) {
  delete self;
}
