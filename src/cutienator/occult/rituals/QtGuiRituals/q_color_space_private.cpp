//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcolorspace_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcolorspace_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qcolorspace.h>
#include <QtGui/qcolortransform.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qcolortransform.h"
#include "qcolortransform_p.h"
#include "qcmyk_p.h"
#include "qcolorclut_p.h"
#include "qcolormatrix_p.h"
#include "qcolorspace_p.h"
#include "qcolortrc_p.h"
#include "qcolortrclut_p.h"
#include <QtCore/qatomic.h>
#include <QtCore/qmath.h>
#include <QtGui/qcolor.h>
#include <QtGui/qimage.h>
#include <QtGui/qtransform.h>
#include <QtCore/private/qsimd_p.h>
#include <qdebug.h>
#include "qcolorspace.h"
#include "qcolorspace_p.h"
#include "qcolortransform.h"
#include "qcolorclut_p.h"
#include "qcolormatrix_p.h"
#include "qcolortransferfunction_p.h"
#include "qcolortransform_p.h"
#include "qicc_p.h"
#include <qatomic.h>
#include <qmath.h>
#include <qtransform.h>
#include <qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/painting/qcolortransform.cpp, line 2051, as _ZNK22QColorTransformPrivate10isIdentityEv
inline bool QColorTransformPrivate::isIdentity() const
{
    if (colorSpaceIn == colorSpaceOut)
        return true;
    if (!colorMatrix.isIdentity())
        return false;
    if (colorSpaceIn && colorSpaceOut) {
        if (colorSpaceIn->equals(colorSpaceOut.constData()))
            return true;
        if (!colorSpaceIn->isThreeComponentMatrix() || !colorSpaceOut->isThreeComponentMatrix())
            return false;
        if (colorSpaceIn->transferFunction != colorSpaceOut->transferFunction)
            return false;
        if (colorSpaceIn->transferFunction == QColorSpace::TransferFunction::Custom) {
            return colorSpaceIn->trc[0] == colorSpaceOut->trc[0]
                && colorSpaceIn->trc[1] == colorSpaceOut->trc[1]
                && colorSpaceIn->trc[2] == colorSpaceOut->trc[2];
        }
    } else {
        if (colorSpaceIn && !colorSpaceIn->isThreeComponentMatrix())
            return false;
        if (colorSpaceOut && !colorSpaceOut->isThreeComponentMatrix())
            return false;
        if (colorSpaceIn && colorSpaceIn->transferFunction != QColorSpace::TransferFunction::Linear)
            return false;
        if (colorSpaceOut && colorSpaceOut->transferFunction != QColorSpace::TransferFunction::Linear)
            return false;
    }
    return true;
}

//  from src/gui/painting/qcolorspace.cpp, line 111, as _ZN18QColorSpacePrivateC1Ev
inline QColorSpacePrivate::QColorSpacePrivate()
{
}

//  from src/gui/painting/qcolorspace.cpp, line 195, as _ZN18QColorSpacePrivateC1E7QPointFN11QColorSpace16TransferFunctionEf
inline QColorSpacePrivate::QColorSpacePrivate(QPointF whitePoint,
                                       QColorSpace::TransferFunction transferFunction,
                                       float gamma)
        : primaries(QColorSpace::Primaries::Custom)
        , transferFunction(transferFunction)
        , colorModel(QColorSpace::ColorModel::Gray)
        , gamma(gamma)
        , whitePoint(QColorVector::fromXYChromaticity(whitePoint))
{
    chad = QColorMatrix::chromaticAdaptation(this->whitePoint);
    toXyz = chad;
    setTransferFunction();
}

//  from src/gui/painting/qcolorspace.cpp, line 1251, as _ZNK18QColorSpacePrivate7isValidEv
inline bool QColorSpacePrivate::isValid() const noexcept
{
    if (!isThreeComponentMatrix())
        return !mAB.isEmpty();
    if (!toXyz.isValid())
        return false;
    if (colorModel == QColorSpace::ColorModel::Gray) {
        if (!trc[0].isValid())
            return false;
    } else if (colorModel == QColorSpace::ColorModel::Rgb){
        if (!trc[0].isValid() || !trc[1].isValid() || !trc[2].isValid())
            return false;
    } else {
        return false;
    }
    return true;
}

//  from src/gui/painting/qcolorspace.cpp, line 435, as _ZN18QColorSpacePrivate19setTransferFunctionEv
inline void QColorSpacePrivate::setTransferFunction()
{
    switch (transferFunction) {
    case QColorSpace::TransferFunction::Linear:
        trc[0] = QColorTransferFunction();
        if (qFuzzyIsNull(gamma))
            gamma = 1.0f;
        break;
    case QColorSpace::TransferFunction::Gamma:
        trc[0] = QColorTransferFunction::fromGamma(gamma);
        break;
    case QColorSpace::TransferFunction::SRgb:
        trc[0] = QColorTransferFunction::fromSRgb();
        if (qFuzzyIsNull(gamma))
            gamma = 2.31f;
        break;
    case QColorSpace::TransferFunction::ProPhotoRgb:
        trc[0] = QColorTransferFunction::fromProPhotoRgb();
        if (qFuzzyIsNull(gamma))
            gamma = 1.8f;
        break;
    case QColorSpace::TransferFunction::Bt2020:
        trc[0] = QColorTransferFunction::fromBt2020();
        if (qFuzzyIsNull(gamma))
            gamma = 2.1f;
        break;
    case QColorSpace::TransferFunction::St2084:
        trc[0] = QColorTransferGenericFunction::pq();
        break;
    case QColorSpace::TransferFunction::Hlg:
        trc[0] = QColorTransferGenericFunction::hlg();
        break;
    case QColorSpace::TransferFunction::Custom:
        break;
    default:
        Q_UNREACHABLE();
        break;
    }
    trc[1] = trc[0];
    trc[2] = trc[0];
    lut.generated.storeRelease(0);
}

//  from src/gui/painting/qcolorspace.cpp, line 269, as _ZN18QColorSpacePrivate18identifyColorSpaceEv
inline void QColorSpacePrivate::identifyColorSpace()
{
    switch (primaries) {
    case QColorSpace::Primaries::SRgb:
        if (transferFunction == QColorSpace::TransferFunction::SRgb) {
            namedColorSpace = QColorSpace::SRgb;
            if (description.isEmpty())
                description = QStringLiteral("sRGB");
            return;
        }
        if (transferFunction == QColorSpace::TransferFunction::Linear) {
            namedColorSpace = QColorSpace::SRgbLinear;
            if (description.isEmpty())
                description = QStringLiteral("Linear sRGB");
            return;
        }
        break;
    case QColorSpace::Primaries::AdobeRgb:
        if (transferFunction == QColorSpace::TransferFunction::Gamma) {
            if (qAbs(gamma - 2.19921875f) < (1/1024.0f)) {
                namedColorSpace = QColorSpace::AdobeRgb;
                if (description.isEmpty())
                    description = QStringLiteral("Adobe RGB");
                return;
            }
        }
        break;
    case QColorSpace::Primaries::DciP3D65:
        if (transferFunction == QColorSpace::TransferFunction::SRgb) {
            namedColorSpace = QColorSpace::DisplayP3;
            if (description.isEmpty())
                description = QStringLiteral("Display P3");
            return;
        }
        break;
    case QColorSpace::Primaries::ProPhotoRgb:
        if (transferFunction == QColorSpace::TransferFunction::ProPhotoRgb) {
            namedColorSpace = QColorSpace::ProPhotoRgb;
            if (description.isEmpty())
                description = QStringLiteral("ProPhoto RGB");
            return;
        }
        if (transferFunction == QColorSpace::TransferFunction::Gamma) {
            // ProPhoto RGB's curve is effectively gamma 1.8 for 8bit precision.
            if (qAbs(gamma - 1.8f) < (1/1024.0f)) {
                namedColorSpace = QColorSpace::ProPhotoRgb;
                if (description.isEmpty())
                    description = QStringLiteral("ProPhoto RGB");
                return;
            }
        }
        break;
    case QColorSpace::Primaries::Bt2020:
        if (transferFunction == QColorSpace::TransferFunction::Bt2020) {
            namedColorSpace = QColorSpace::Bt2020;
            if (description.isEmpty())
                description = QStringLiteral("BT.2020");
            return;
        }
        if (transferFunction == QColorSpace::TransferFunction::St2084) {
            namedColorSpace = QColorSpace::Bt2100Pq;
            if (description.isEmpty())
                description = QStringLiteral("BT.2100(PQ)");
            return;
        }
        if (transferFunction == QColorSpace::TransferFunction::Hlg) {
            namedColorSpace = QColorSpace::Bt2100Hlg;
            if (description.isEmpty())
                description = QStringLiteral("BT.2100(HLG)");
            return;
        }
        break;
    default:
        break;
    }

    namedColorSpace = Unknown;
}

//  from src/gui/painting/qcolorspace.cpp, line 497, as _ZNK18QColorSpacePrivate19transformationToXYZEv
inline QColorTransform QColorSpacePrivate::transformationToXYZ() const
{
    QColorTransform transform;
    auto ptr = new QColorTransformPrivate;
    transform.d = ptr;
    ptr->colorSpaceIn = this;
    ptr->colorSpaceOut = this;
    if (isThreeComponentMatrix())
        ptr->colorMatrix = toXyz;
    else
        ptr->colorMatrix = QColorMatrix::identity();
    // Convert to XYZ relative to our white point, not the regular D50 white point.
    if (!chad.isNull())
        ptr->colorMatrix = chad.inverted() * ptr->colorMatrix;
    return transform;
}

//  from src/gui/painting/qcolorspace.cpp, line 514, as _ZNK18QColorSpacePrivate22isThreeComponentMatrixEv
inline bool QColorSpacePrivate::isThreeComponentMatrix() const
{
    return transformModel == QColorSpace::TransformModel::ThreeComponentMatrix;
}

//  from src/gui/painting/qcolorspace.cpp, line 519, as _ZN18QColorSpacePrivate33clearElementListProcessingForEditEv
inline void QColorSpacePrivate::clearElementListProcessingForEdit()
{
    Q_ASSERT(transformModel == QColorSpace::TransformModel::ElementListProcessing);
    Q_ASSERT(primaries == QColorSpace::Primaries::Custom);
    Q_ASSERT(transferFunction == QColorSpace::TransferFunction::Custom);

    transformModel = QColorSpace::TransformModel::ThreeComponentMatrix;
    colorModel = QColorSpace::ColorModel::Rgb;
    isPcsLab = false;
    mAB.clear();
    mBA.clear();
}
//  -----------------------------------------------------------------------

//  QColorSpacePrivate::QColorSpacePrivate()
extern "C" Q_DECL_EXPORT
QColorSpacePrivate *ritual_ZN18QColorSpacePrivateC1Ev() {
  return new QColorSpacePrivate();
}

//  QColorSpacePrivate::QColorSpacePrivate(QPointF whitePoint,
//      QColorSpace::TransferFunction transferFunction, float gamma)
extern "C" Q_DECL_EXPORT
QColorSpacePrivate *ritual_ZN18QColorSpacePrivateC1E7QPointFN11QColorSpace16TransferFunctionEf(
    const QPointF *whitePoint,
    QColorSpace::TransferFunction transferFunction,
    float gamma) {
  return new QColorSpacePrivate(*whitePoint, transferFunction, gamma);
}

//  QColorSpacePrivate::QColorSpacePrivate(const QColorSpacePrivate &other)
extern "C" Q_DECL_EXPORT
QColorSpacePrivate *ritual_ZN18QColorSpacePrivateC1ERKS_(
    const QColorSpacePrivate *other) {
  return new QColorSpacePrivate(*other);
}

//  const QColorSpacePrivate *QColorSpacePrivate::get(const QColorSpace
//      &colorSpace)
extern "C" Q_DECL_EXPORT
const QColorSpacePrivate *ritual_ZN18QColorSpacePrivate3getERK11QColorSpace(
    const QColorSpace *colorSpace) {
  return QColorSpacePrivate::get(*colorSpace);
}

//  bool QColorSpacePrivate::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QColorSpacePrivate7isValidEv(
    const QColorSpacePrivate *self) {
  return self->isValid();
}

//  void QColorSpacePrivate::setTransferFunction()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QColorSpacePrivate19setTransferFunctionEv(
    QColorSpacePrivate *self) {
  self->setTransferFunction();
}

//  void QColorSpacePrivate::identifyColorSpace()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QColorSpacePrivate18identifyColorSpaceEv(
    QColorSpacePrivate *self) {
  self->identifyColorSpace();
}

//  QColorTransform QColorSpacePrivate::transformationToXYZ() const
extern "C" Q_DECL_EXPORT
QColorTransform *ritual_ZNK18QColorSpacePrivate19transformationToXYZEv(
    const QColorSpacePrivate *self) {
  return new QColorTransform(self->transformationToXYZ());
}

//  bool QColorSpacePrivate::isThreeComponentMatrix() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QColorSpacePrivate22isThreeComponentMatrixEv(
    const QColorSpacePrivate *self) {
  return self->isThreeComponentMatrix();
}

//  void QColorSpacePrivate::clearElementListProcessingForEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QColorSpacePrivate33clearElementListProcessingForEditEv(
    QColorSpacePrivate *self) {
  self->clearElementListProcessingForEdit();
}

//  QColorSpacePrivate::~QColorSpacePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QColorSpacePrivateD1Ev(QColorSpacePrivate *self) {
  delete self;
}
