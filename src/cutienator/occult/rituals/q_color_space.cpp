//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qcolorspace.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qcolorspace.h>
#include <QtCore/qpoint.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qcolortransform.h>
#include <QtCore/qvariant.h>

//  QColorSpace::QColorSpace()
extern "C" Q_DECL_EXPORT
QColorSpace *ritual_ZN11QColorSpaceC1Ev() {
  return new QColorSpace();
}

//  QColorSpace::QColorSpace(NamedColorSpace namedColorSpace)
extern "C" Q_DECL_EXPORT
QColorSpace *ritual_ZN11QColorSpaceC1ENS_15NamedColorSpaceE(
    QColorSpace::NamedColorSpace namedColorSpace) {
  return new QColorSpace(namedColorSpace);
}

//  QColorSpace::QColorSpace(QPointF whitePoint, TransferFunction
//      transferFunction, float gamma)
extern "C" Q_DECL_EXPORT
QColorSpace *ritual_ZN11QColorSpaceC1E7QPointFNS_16TransferFunctionEf(
    const QPointF *whitePoint,
    QColorSpace::TransferFunction transferFunction,
    float gamma) {
  return new QColorSpace(*whitePoint, transferFunction, gamma);
}

//  QColorSpace::QColorSpace(Primaries primaries, TransferFunction
//      transferFunction, float gamma)
extern "C" Q_DECL_EXPORT
QColorSpace *ritual_ZN11QColorSpaceC1ENS_9PrimariesENS_16TransferFunctionEf(
    QColorSpace::Primaries primaries,
    QColorSpace::TransferFunction transferFunction,
    float gamma) {
  return new QColorSpace(primaries, transferFunction, gamma);
}

//  QColorSpace::QColorSpace(Primaries primaries, float gamma)
extern "C" Q_DECL_EXPORT
QColorSpace *ritual_ZN11QColorSpaceC1ENS_9PrimariesEf(
    QColorSpace::Primaries primaries,
    float gamma) {
  return new QColorSpace(primaries, gamma);
}

//  QColorSpace::QColorSpace(const QPointF &whitePoint, const QPointF
//      &redPoint, const QPointF &greenPoint, const QPointF &bluePoint,
//      TransferFunction transferFunction, float gamma)
extern "C" Q_DECL_EXPORT
QColorSpace *ritual_ZN11QColorSpaceC1ERK7QPointFS2_S2_S2_NS_16TransferFunctionEf(
    const QPointF *whitePoint,
    const QPointF *redPoint,
    const QPointF *greenPoint,
    const QPointF *bluePoint,
    QColorSpace::TransferFunction transferFunction,
    float gamma) {
  return new QColorSpace(
      *whitePoint,
      *redPoint,
      *greenPoint,
      *bluePoint,
      transferFunction,
      gamma);
}

//  QColorSpace::QColorSpace(const PrimaryPoints &primaryPoints,
//      TransferFunction transferFunction, float gamma)
extern "C" Q_DECL_EXPORT
QColorSpace *ritual_ZN11QColorSpaceC1ERKNS_13PrimaryPointsENS_16TransferFunctionEf(
    const QColorSpace::PrimaryPoints *primaryPoints,
    QColorSpace::TransferFunction transferFunction,
    float gamma) {
  return new QColorSpace(*primaryPoints, transferFunction, gamma);
}

//  QColorSpace::~QColorSpace()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColorSpaceD1Ev(QColorSpace *self) {
  delete self;
}

//  QColorSpace::QColorSpace(const QColorSpace &colorSpace)
extern "C" Q_DECL_EXPORT
QColorSpace *ritual_ZN11QColorSpaceC1ERKS_(const QColorSpace *colorSpace) {
  return new QColorSpace(*colorSpace);
}

//  Primaries QColorSpace::primaries() const
extern "C" Q_DECL_EXPORT
QColorSpace::Primaries ritual_ZNK11QColorSpace9primariesEv(
    const QColorSpace *self) {
  return self->primaries();
}

//  TransferFunction QColorSpace::transferFunction() const
extern "C" Q_DECL_EXPORT
QColorSpace::TransferFunction ritual_ZNK11QColorSpace16transferFunctionEv(
    const QColorSpace *self) {
  return self->transferFunction();
}

//  float QColorSpace::gamma() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11QColorSpace5gammaEv(const QColorSpace *self) {
  return self->gamma();
}

//  QString QColorSpace::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QColorSpace11descriptionEv(const QColorSpace *self) {
  return new QString(self->description());
}

//  void QColorSpace::setDescription(const QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColorSpace14setDescriptionERK7QString(
    QColorSpace *self,
    const QString *description) {
  self->setDescription(*description);
}

//  void QColorSpace::setTransferFunction(TransferFunction transferFunction,
//      float gamma)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColorSpace19setTransferFunctionENS_16TransferFunctionEf(
    QColorSpace *self,
    QColorSpace::TransferFunction transferFunction,
    float gamma) {
  self->setTransferFunction(transferFunction, gamma);
}

//  QColorSpace QColorSpace::withTransferFunction(TransferFunction
//      transferFunction, float gamma) const
extern "C" Q_DECL_EXPORT
QColorSpace *ritual_ZNK11QColorSpace20withTransferFunctionENS_16TransferFunctionEf(
    const QColorSpace *self,
    QColorSpace::TransferFunction transferFunction,
    float gamma) {
  return new QColorSpace(
      self->withTransferFunction(
          transferFunction,
          gamma));
}

//  void QColorSpace::setPrimaries(Primaries primariesId)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColorSpace12setPrimariesENS_9PrimariesE(
    QColorSpace *self,
    QColorSpace::Primaries primariesId) {
  self->setPrimaries(primariesId);
}

//  void QColorSpace::setPrimaries(const QPointF &whitePoint, const QPointF
//      &redPoint, const QPointF &greenPoint, const QPointF &bluePoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColorSpace12setPrimariesERK7QPointFS2_S2_S2_(
    QColorSpace *self,
    const QPointF *whitePoint,
    const QPointF *redPoint,
    const QPointF *greenPoint,
    const QPointF *bluePoint) {
  self->setPrimaries(*whitePoint, *redPoint, *greenPoint, *bluePoint);
}

//  void QColorSpace::setWhitePoint(QPointF whitePoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColorSpace13setWhitePointE7QPointF(
    QColorSpace *self,
    const QPointF *whitePoint) {
  self->setWhitePoint(*whitePoint);
}

//  QPointF QColorSpace::whitePoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QColorSpace10whitePointEv(const QColorSpace *self) {
  return new QPointF(self->whitePoint());
}

//  void QColorSpace::setPrimaryPoints(const PrimaryPoints &primaryPoints)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColorSpace16setPrimaryPointsERKNS_13PrimaryPointsE(
    QColorSpace *self,
    const QColorSpace::PrimaryPoints *primaryPoints) {
  self->setPrimaryPoints(*primaryPoints);
}

//  PrimaryPoints QColorSpace::primaryPoints() const
extern "C" Q_DECL_EXPORT
QColorSpace::PrimaryPoints *ritual_ZNK11QColorSpace13primaryPointsEv(
    const QColorSpace *self) {
  return new QColorSpace::PrimaryPoints(self->primaryPoints());
}

//  TransformModel QColorSpace::transformModel() const
extern "C" Q_DECL_EXPORT
QColorSpace::TransformModel ritual_ZNK11QColorSpace14transformModelEv(
    const QColorSpace *self) {
  return self->transformModel();
}

//  ColorModel QColorSpace::colorModel() const
extern "C" Q_DECL_EXPORT
QColorSpace::ColorModel ritual_ZNK11QColorSpace10colorModelEv(
    const QColorSpace *self) {
  return self->colorModel();
}

//  void QColorSpace::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColorSpace6detachEv(QColorSpace *self) {
  self->detach();
}

//  bool QColorSpace::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QColorSpace7isValidEv(const QColorSpace *self) {
  return self->isValid();
}

//  bool QColorSpace::isValidTarget() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QColorSpace13isValidTargetEv(const QColorSpace *self) {
  return self->isValidTarget();
}

//  QColorSpace QColorSpace::fromIccProfile(const QByteArray &iccProfile)
extern "C" Q_DECL_EXPORT
QColorSpace *ritual_ZN11QColorSpace14fromIccProfileERK10QByteArray(
    const QByteArray *iccProfile) {
  return new QColorSpace(QColorSpace::fromIccProfile(*iccProfile));
}

//  QByteArray QColorSpace::iccProfile() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QColorSpace10iccProfileEv(const QColorSpace *self) {
  return new QByteArray(self->iccProfile());
}

//  QColorTransform QColorSpace::transformationToColorSpace(const QColorSpace
//      &colorspace) const
extern "C" Q_DECL_EXPORT
QColorTransform *ritual_ZNK11QColorSpace26transformationToColorSpaceERKS_(
    const QColorSpace *self,
    const QColorSpace *colorspace) {
  return new QColorTransform(self->transformationToColorSpace(*colorspace));
}

//  QVariant QColorSpace::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QColorSpacecv8QVariantEv(const QColorSpace *self) {
  return new QVariant(self->operator QVariant());
}
