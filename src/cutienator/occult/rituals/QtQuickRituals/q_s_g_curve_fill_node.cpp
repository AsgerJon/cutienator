//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgcurvefillnode_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgcurvefillnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsggradientcache_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qsgtransform_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtQuick/qsggeometry.h>
#include <functional>
#include <QtGui/QVector3D>
#include <QtGui/QVector2D>
#include <QtCore/QList>

//  const QMetaObject *QSGCurveFillNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QSGCurveFillNode10metaObjectEv(
    const QSGCurveFillNode *self) {
  return self->metaObject();
}

//  void *QSGCurveFillNode::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QSGCurveFillNode11qt_metacastEPKc(
    QSGCurveFillNode *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGCurveFillNode::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QSGCurveFillNode11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGCurveFillNode *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSGCurveFillNode::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QSGCurveFillNode2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSGCurveFillNode::tr(s, c, n));
}

//  QSGCurveFillNode::QSGCurveFillNode()
extern "C" Q_DECL_EXPORT
QSGCurveFillNode *ritual_ZN16QSGCurveFillNodeC1Ev() {
  return new QSGCurveFillNode();
}

//  void QSGCurveFillNode::setColor(QColor col)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGCurveFillNode8setColorE6QColor(
    QSGCurveFillNode *self,
    const QColor *col) {
  self->setColor(*col);
}

//  QColor QSGCurveFillNode::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QSGCurveFillNode5colorEv(const QSGCurveFillNode *self) {
  return new QColor(self->color());
}

//  void QSGCurveFillNode::setFillTextureProvider(QSGTextureProvider
//      *provider)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGCurveFillNode22setFillTextureProviderEP18QSGTextureProvider(
    QSGCurveFillNode *self,
    QSGTextureProvider *provider) {
  self->setFillTextureProvider(provider);
}

//  QSGTextureProvider *QSGCurveFillNode::fillTextureProvider() const
extern "C" Q_DECL_EXPORT
QSGTextureProvider *ritual_ZNK16QSGCurveFillNode19fillTextureProviderEv(
    const QSGCurveFillNode *self) {
  return self->fillTextureProvider();
}

//  void QSGCurveFillNode::setFillGradient(const
//      QSGGradientCache::GradientDesc &fillGradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGCurveFillNode15setFillGradientERKN16QSGGradientCache12GradientDescE(
    QSGCurveFillNode *self,
    const QSGGradientCache::GradientDesc *fillGradient) {
  self->setFillGradient(*fillGradient);
}

//  const QSGGradientCache::GradientDesc *QSGCurveFillNode::fillGradient()
//      const
extern "C" Q_DECL_EXPORT
const QSGGradientCache::GradientDesc *ritual_ZNK16QSGCurveFillNode12fillGradientEv(
    const QSGCurveFillNode *self) {
  return self->fillGradient();
}

//  void QSGCurveFillNode::setGradientType(QGradient::Type type)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGCurveFillNode15setGradientTypeEN9QGradient4TypeE(
    QSGCurveFillNode *self,
    QGradient::Type type) {
  self->setGradientType(type);
}

//  QGradient::Type QSGCurveFillNode::gradientType() const
extern "C" Q_DECL_EXPORT
QGradient::Type ritual_ZNK16QSGCurveFillNode12gradientTypeEv(
    const QSGCurveFillNode *self) {
  return self->gradientType();
}

//  void QSGCurveFillNode::setFillTransform(const QSGTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGCurveFillNode16setFillTransformERK12QSGTransform(
    QSGCurveFillNode *self,
    const QSGTransform *transform) {
  self->setFillTransform(*transform);
}

//  const QSGTransform *QSGCurveFillNode::fillTransform() const
extern "C" Q_DECL_EXPORT
const QSGTransform *ritual_ZNK16QSGCurveFillNode13fillTransformEv(
    const QSGCurveFillNode *self) {
  return self->fillTransform();
}

//  float QSGCurveFillNode::debug() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QSGCurveFillNode5debugEv(const QSGCurveFillNode *self) {
  return self->debug();
}

//  void QSGCurveFillNode::setDebug(float newDebug)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGCurveFillNode8setDebugEf(
    QSGCurveFillNode *self,
    float newDebug) {
  self->setDebug(newDebug);
}

//  void QSGCurveFillNode::appendTriangle(const std::array<QVector2D, 3> &v,
//      const std::array<QVector2D, 3> &n, std::function<QVector3D
//      (QVector2D)> uvForPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGCurveFillNode14appendTriangleERKSt5arrayI9QVector2DLm3EES4_St8functionIF9QVector3DS1_EE(
    QSGCurveFillNode *self,
    const std::array<QVector2D, 3> *v,
    const std::array<QVector2D, 3> *n,
    const std::function<QVector3D (QVector2D)> *uvForPoint) {
  self->appendTriangle(*v, *n, *uvForPoint);
}

//  void QSGCurveFillNode::appendTriangle(const QVector2D &v1, const
//      QVector2D &v2, const QVector2D &v3, const QVector3D &uv1, const
//      QVector3D &uv2, const QVector3D &uv3, const QVector2D &n1, const
//      QVector2D &n2, const QVector2D &n3, const QVector2D &duvdx, const
//      QVector2D &duvdy)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGCurveFillNode14appendTriangleERK9QVector2DS2_S2_RK9QVector3DS5_S5_S2_S2_S2_S2_S2_(
    QSGCurveFillNode *self,
    const QVector2D *v1,
    const QVector2D *v2,
    const QVector2D *v3,
    const QVector3D *uv1,
    const QVector3D *uv2,
    const QVector3D *uv3,
    const QVector2D *n1,
    const QVector2D *n2,
    const QVector2D *n3,
    const QVector2D *duvdx,
    const QVector2D *duvdy) {
  self->appendTriangle(
      *v1,
      *v2,
      *v3,
      *uv1,
      *uv2,
      *uv3,
      *n1,
      *n2,
      *n3,
      *duvdx,
      *duvdy);
}

//  void QSGCurveFillNode::appendTriangle(const QVector2D &v1, const
//      QVector2D &v2, const QVector2D &v3, std::function<QVector3D
//      (QVector2D)> uvForPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGCurveFillNode14appendTriangleERK9QVector2DS2_S2_St8functionIF9QVector3DS0_EE(
    QSGCurveFillNode *self,
    const QVector2D *v1,
    const QVector2D *v2,
    const QVector2D *v3,
    const std::function<QVector3D (QVector2D)> *uvForPoint) {
  self->appendTriangle(*v1, *v2, *v3, *uvForPoint);
}

//  QList<quint32> QSGCurveFillNode::uncookedIndexes() const
extern "C" Q_DECL_EXPORT
QList<quint32> *ritual_ZNK16QSGCurveFillNode15uncookedIndexesEv(
    const QSGCurveFillNode *self) {
  return new QList<quint32>(self->uncookedIndexes());
}

//  void QSGCurveFillNode::cookGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGCurveFillNode12cookGeometryEv(QSGCurveFillNode *self) {
  self->cookGeometry();
}

//  void QSGCurveFillNode::reserve(qsizetype size)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGCurveFillNode7reserveEx(
    QSGCurveFillNode *self,
    qsizetype size) {
  self->reserve(size);
}

//  void QSGCurveFillNode::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGCurveFillNode10preprocessEv(QSGCurveFillNode *self) {
  self->preprocess();
}

//  QVector2D QSGCurveFillNode::boundsSize() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK16QSGCurveFillNode10boundsSizeEv(
    const QSGCurveFillNode *self) {
  return new QVector2D(self->boundsSize());
}

//  void QSGCurveFillNode::setBoundsSize(const QVector2D &boundsSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGCurveFillNode13setBoundsSizeERK9QVector2D(
    QSGCurveFillNode *self,
    const QVector2D *boundsSize) {
  self->setBoundsSize(*boundsSize);
}

//  bool QSGCurveFillNode::useStandardDerivatives() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSGCurveFillNode22useStandardDerivativesEv(
    const QSGCurveFillNode *self) {
  return self->useStandardDerivatives();
}

//  void QSGCurveFillNode::setUseStandardDerivatives(bool
//      useStandardDerivatives)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGCurveFillNode25setUseStandardDerivativesEb(
    QSGCurveFillNode *self,
    bool useStandardDerivatives) {
  self->setUseStandardDerivatives(useStandardDerivatives);
}

//  void QSGCurveFillNode::handleTextureChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGCurveFillNode20handleTextureChangedEv(
    QSGCurveFillNode *self) {
  self->handleTextureChanged();
}

//  void QSGCurveFillNode::handleTextureProviderDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGCurveFillNode30handleTextureProviderDestroyedEv(
    QSGCurveFillNode *self) {
  self->handleTextureProviderDestroyed();
}

//  void QSGCurveFillNode::updateMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGCurveFillNode14updateMaterialEv(QSGCurveFillNode *self) {
  self->updateMaterial();
}

//  const QSGGeometry::AttributeSet &QSGCurveFillNode::attributes()
extern "C" Q_DECL_EXPORT
QSGGeometry::AttributeSet *ritual_ZN16QSGCurveFillNode10attributesEv() {
  return new QSGGeometry::AttributeSet(QSGCurveFillNode::attributes());
}

//  QSGCurveFillNode as the QSGCurveAbstractNode it is built on
extern "C" Q_DECL_EXPORT
QSGCurveAbstractNode *ritual_cast_QSGCurveFillNode_QSGCurveAbstractNode(
    QSGCurveFillNode *self) {
  return static_cast<QSGCurveAbstractNode *>(self);
}

//  void QSGCurveFillNode::setColor(QColor col)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGCurveFillNode8setColorE6QColor(
    QSGCurveFillNode *self,
    const QColor *col) {
  self->QSGCurveFillNode::setColor(*col);
}

//  void QSGCurveFillNode::cookGeometry()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGCurveFillNode12cookGeometryEv(
    QSGCurveFillNode *self) {
  self->QSGCurveFillNode::cookGeometry();
}

//  void QSGCurveFillNode::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGCurveFillNode10preprocessEv(QSGCurveFillNode *self) {
  self->QSGCurveFillNode::preprocess();
}

//  void QSGCurveFillNode::setUseStandardDerivatives(bool
//      useStandardDerivatives)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGCurveFillNode25setUseStandardDerivativesEb(
    QSGCurveFillNode *self,
    bool useStandardDerivatives) {
  self->QSGCurveFillNode::setUseStandardDerivatives(useStandardDerivatives);
}

//  a QList<quint32> a ritual of QSGCurveFillNode gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSGCurveFillNode__QList_quint32(QList<quint32> *self) {
  delete self;
}
