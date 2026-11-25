//  Written by hand on 2026-11-25 from
//  QtQuick/6.12.0/QtQuick/private/qsgcurvestrokenode_p.h, Qt 6.12.0, the same
//  text on every system. Kept as it is when the generator runs
//  again. Its inline code compiles only with
//  'QT_USE_QSTRINGBUILDER' defined, which 'Summon' tells the
//  compiler.
//  Not written: the two 'appendTriangle', 'defaultExtrusions' and
//  'curveABC', which take or give a 'std::array', and
//  'uncookedIndexes', which gives a list of numbers.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgcurvestrokenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsggradientcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/qsggeometry.h>

//  QSGCurveStrokeNode::QSGCurveStrokeNode()
extern "C" Q_DECL_EXPORT
QSGCurveStrokeNode *ritual_ZN18QSGCurveStrokeNodeC1Ev() {
  return new QSGCurveStrokeNode();
}

//  void QSGCurveStrokeNode::setColor(QColor col)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGCurveStrokeNode8setColorE6QColor(
    QSGCurveStrokeNode *self,
    const QColor *col) {
  self->setColor(*col);
}

//  QColor QSGCurveStrokeNode::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK18QSGCurveStrokeNode5colorEv(
    const QSGCurveStrokeNode *self) {
  return new QColor(self->color());
}

//  void QSGCurveStrokeNode::setCosmeticStroke(bool c)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGCurveStrokeNode17setCosmeticStrokeEb(
    QSGCurveStrokeNode *self,
    bool c) {
  self->setCosmeticStroke(c);
}

//  void QSGCurveStrokeNode::setStrokeWidth(float width)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGCurveStrokeNode14setStrokeWidthEf(
    QSGCurveStrokeNode *self,
    float width) {
  self->setStrokeWidth(width);
}

//  QGradient::Type QSGCurveStrokeNode::gradientType() const
extern "C" Q_DECL_EXPORT
QGradient::Type ritual_ZNK18QSGCurveStrokeNode12gradientTypeEv(
    const QSGCurveStrokeNode *self) {
  return self->gradientType();
}

//  void QSGCurveStrokeNode::setGradientType(QGradient::Type type)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGCurveStrokeNode15setGradientTypeEN9QGradient4TypeE(
    QSGCurveStrokeNode *self,
    QGradient::Type type) {
  self->setGradientType(type);
}

//  const QSGGradientCache::GradientDesc *
//      QSGCurveStrokeNode::strokeGradient() const
extern "C" Q_DECL_EXPORT
const QSGGradientCache::GradientDesc *ritual_ZNK18QSGCurveStrokeNode14strokeGradientEv(
    const QSGCurveStrokeNode *self) {
  return self->strokeGradient();
}

//  void QSGCurveStrokeNode::setStrokeGradient(const
//      QSGGradientCache::GradientDesc &strokeGradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGCurveStrokeNode17setStrokeGradientERKN16QSGGradientCache12GradientDescE(
    QSGCurveStrokeNode *self,
    const QSGGradientCache::GradientDesc *strokeGradient) {
  self->setStrokeGradient(*strokeGradient);
}

//  float QSGCurveStrokeNode::strokeWidth() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK18QSGCurveStrokeNode11strokeWidthEv(
    const QSGCurveStrokeNode *self) {
  return self->strokeWidth();
}

//  void QSGCurveStrokeNode::cookGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGCurveStrokeNode12cookGeometryEv(
    QSGCurveStrokeNode *self) {
  self->cookGeometry();
}

//  const QSGGeometry::AttributeSet &QSGCurveStrokeNode::attributes()
extern "C" Q_DECL_EXPORT
QSGGeometry::AttributeSet *ritual_ZN18QSGCurveStrokeNode10attributesEv() {
  return new QSGGeometry::AttributeSet(QSGCurveStrokeNode::attributes());
}

//  bool QSGCurveStrokeNode::expandingStrokeEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSGCurveStrokeNode22expandingStrokeEnabledEv() {
  return QSGCurveStrokeNode::expandingStrokeEnabled();
}

//  float QSGCurveStrokeNode::debug() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK18QSGCurveStrokeNode5debugEv(
    const QSGCurveStrokeNode *self) {
  return self->debug();
}

//  void QSGCurveStrokeNode::setDebug(float newDebug)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGCurveStrokeNode8setDebugEf(
    QSGCurveStrokeNode *self,
    float newDebug) {
  self->setDebug(newDebug);
}

//  void QSGCurveStrokeNode::setLocalScale(float scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGCurveStrokeNode13setLocalScaleEf(
    QSGCurveStrokeNode *self,
    float scale) {
  self->setLocalScale(scale);
}

//  float QSGCurveStrokeNode::localScale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK18QSGCurveStrokeNode10localScaleEv(
    const QSGCurveStrokeNode *self) {
  return self->localScale();
}

//  bool QSGCurveStrokeNode::useStandardDerivatives() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QSGCurveStrokeNode22useStandardDerivativesEv(
    const QSGCurveStrokeNode *self) {
  return self->useStandardDerivatives();
}

//  void QSGCurveStrokeNode::setUseStandardDerivatives(bool
//      useStandardDerivatives)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGCurveStrokeNode25setUseStandardDerivativesEb(
    QSGCurveStrokeNode *self,
    bool useStandardDerivatives) {
  self->setUseStandardDerivatives(useStandardDerivatives);
}

//  void QSGCurveStrokeNode::updateMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGCurveStrokeNode14updateMaterialEv(
    QSGCurveStrokeNode *self) {
  self->updateMaterial();
}

//  QSGCurveStrokeNode as the QSGCurveAbstractNode it is built on
extern "C" Q_DECL_EXPORT
QSGCurveAbstractNode *ritual_cast_QSGCurveStrokeNode_QSGCurveAbstractNode(
    QSGCurveStrokeNode *self) {
  return static_cast<QSGCurveAbstractNode *>(self);
}

//  void QSGCurveStrokeNode::setColor(QColor col)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QSGCurveStrokeNode8setColorE6QColor(
    QSGCurveStrokeNode *self,
    const QColor *col) {
  self->QSGCurveStrokeNode::setColor(*col);
}

//  void QSGCurveStrokeNode::cookGeometry()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QSGCurveStrokeNode12cookGeometryEv(
    QSGCurveStrokeNode *self) {
  self->QSGCurveStrokeNode::cookGeometry();
}

//  void QSGCurveStrokeNode::setUseStandardDerivatives(bool
//      useStandardDerivatives)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QSGCurveStrokeNode25setUseStandardDerivativesEb(
    QSGCurveStrokeNode *self,
    bool useStandardDerivatives) {
  self->QSGCurveStrokeNode::setUseStandardDerivatives(useStandardDerivatives);
}
