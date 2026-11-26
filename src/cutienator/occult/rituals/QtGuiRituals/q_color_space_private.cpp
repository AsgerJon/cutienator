//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcolorspace_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcolorspace_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolorspace.h>
#include <QtCore/qpoint.h>
#include <QtGui/qcolortransform.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolorspace.h>
#include <QtGui/private/qcolorspace_p.h>
#include <QtGui/qcolortransform.h>
#include <QtGui/private/qcolorclut_p.h>
#include <QtGui/private/qcolormatrix_p.h>
#include <QtGui/private/qcolortransferfunction_p.h>
#include <QtGui/private/qcolortransform_p.h>
#include <QtGui/private/qicc_p.h>
#include <QtCore/qatomic.h>
#include <QtCore/qmath.h>
#include <QtGui/qtransform.h>
#include <QtCore/qdebug.h>
#include <QtGui/qcolortransform.h>
#include <QtGui/private/qcolortransform_p.h>
#include <QtGui/private/qcmyk_p.h>
#include <QtGui/private/qcolorclut_p.h>
#include <QtGui/private/qcolormatrix_p.h>
#include <QtGui/private/qcolorspace_p.h>
#include <QtGui/private/qcolortrc_p.h>
#include <QtGui/private/qcolortrclut_p.h>
#include <QtCore/qatomic.h>
#include <QtCore/qmath.h>
#include <QtGui/qcolor.h>
#include <QtGui/qimage.h>
#include <QtGui/qtransform.h>
#include <QtCore/private/qsimd_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/painting/qcolorspace.cpp, line 90, as local:qcolorspace.cpp:qColorSpacePrimaryPointsToXyzMatrix
inline QColorMatrix qColorSpacePrimaryPointsToXyzMatrix(const QColorSpace::PrimaryPoints &primaries)
{
    // This converts to XYZ in some undefined scale.
    QColorMatrix toXyz = {
        QColorVector::fromXYChromaticity(primaries.redPoint),
        QColorVector::fromXYChromaticity(primaries.greenPoint),
        QColorVector::fromXYChromaticity(primaries.bluePoint)
    };

    // Since the white point should be (1.0, 1.0, 1.0) in the
    // input, we can figure out the scale by using the
    // inverse conversion on the white point.
    const auto wXyz = QColorVector::fromXYChromaticity(primaries.whitePoint);
    QColorVector whiteScale = toXyz.inverted().map(wXyz);

    // Now we have scaled conversion to XYZ relative to the given whitepoint
    toXyz = toXyz * QColorMatrix::fromScale(whiteScale);

    return toXyz;
}

//  from src/gui/painting/qcolorspace.cpp, line 1283, as local:qcolorspace.cpp:compareElement
static bool compareElement(const QColorSpacePrivate::TransferElement &element,
                           const QColorSpacePrivate::TransferElement &other)
{
    return element.trc[0] == other.trc[0]
        && element.trc[1] == other.trc[1]
        && element.trc[2] == other.trc[2]
        && element.trc[3] == other.trc[3];
}

//  from src/gui/painting/qcolorspace.cpp, line 354, as _ZN18QColorSpacePrivate14setToXyzMatrixEv
inline void QColorSpacePrivate::setToXyzMatrix()
{
    if (primaries == QColorSpace::Primaries::Custom) {
        toXyz = QColorMatrix();
        whitePoint = QColorVector::D50();
        return;
    }
    auto colorSpacePrimaries = QColorSpace::PrimaryPoints::fromPrimaries(primaries);
    toXyz = qColorSpacePrimaryPointsToXyzMatrix(colorSpacePrimaries);
    whitePoint = QColorVector::fromXYChromaticity(colorSpacePrimaries.whitePoint);
    chad = QColorMatrix::chromaticAdaptation(whitePoint);
    toXyz = chad * toXyz;
}

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

//  from src/gui/painting/qcolorspace.cpp, line 115, as _ZN18QColorSpacePrivateC1EN11QColorSpace15NamedColorSpaceE
inline QColorSpacePrivate::QColorSpacePrivate(QColorSpace::NamedColorSpace namedColorSpace)
        : namedColorSpace(namedColorSpace)
        , colorModel(QColorSpace::ColorModel::Rgb)
{
    switch (namedColorSpace) {
    case QColorSpace::SRgb:
        primaries = QColorSpace::Primaries::SRgb;
        transferFunction = QColorSpace::TransferFunction::SRgb;
        description = QStringLiteral("sRGB");
        break;
    case QColorSpace::SRgbLinear:
        primaries = QColorSpace::Primaries::SRgb;
        transferFunction = QColorSpace::TransferFunction::Linear;
        description = QStringLiteral("Linear sRGB");
        break;
    case QColorSpace::AdobeRgb:
        primaries = QColorSpace::Primaries::AdobeRgb;
        transferFunction = QColorSpace::TransferFunction::Gamma;
        gamma = 2.19921875f; // Not quite 2.2, see https://www.adobe.com/digitalimag/pdfs/AdobeRGB1998.pdf
        description = QStringLiteral("Adobe RGB");
        break;
    case QColorSpace::DisplayP3:
        primaries = QColorSpace::Primaries::DciP3D65;
        transferFunction = QColorSpace::TransferFunction::SRgb;
        description = QStringLiteral("Display P3");
        break;
    case QColorSpace::ProPhotoRgb:
        primaries = QColorSpace::Primaries::ProPhotoRgb;
        transferFunction = QColorSpace::TransferFunction::ProPhotoRgb;
        description = QStringLiteral("ProPhoto RGB");
        break;
    case QColorSpace::Bt2020:
        primaries = QColorSpace::Primaries::Bt2020;
        transferFunction = QColorSpace::TransferFunction::Bt2020;
        description = QStringLiteral("BT.2020");
        break;
    case QColorSpace::Bt2100Pq:
        primaries = QColorSpace::Primaries::Bt2020;
        transferFunction = QColorSpace::TransferFunction::St2084;
        description = QStringLiteral("BT.2100(PQ)");
        break;
    case QColorSpace::Bt2100Hlg:
        primaries = QColorSpace::Primaries::Bt2020;
        transferFunction = QColorSpace::TransferFunction::Hlg;
        description = QStringLiteral("BT.2100(HLG)");
        break;
    default:
        Q_UNREACHABLE();
    }
    initialize();
}

//  from src/gui/painting/qcolorspace.cpp, line 167, as _ZN18QColorSpacePrivateC1EN11QColorSpace9PrimariesENS0_16TransferFunctionEf
inline QColorSpacePrivate::QColorSpacePrivate(QColorSpace::Primaries primaries, QColorSpace::TransferFunction transferFunction, float gamma)
        : primaries(primaries)
        , transferFunction(transferFunction)
        , colorModel(QColorSpace::ColorModel::Rgb)
        , gamma(gamma)
{
    identifyColorSpace();
    initialize();
}

//  from src/gui/painting/qcolorspace.cpp, line 222, as _ZN18QColorSpacePrivateC1EN11QColorSpace9PrimariesERK5QListItE
inline QColorSpacePrivate::QColorSpacePrivate(QColorSpace::Primaries primaries, const QList<uint16_t> &transferFunctionTable)
        : primaries(primaries)
        , transferFunction(QColorSpace::TransferFunction::Custom)
        , colorModel(QColorSpace::ColorModel::Rgb)
        , gamma(0)
{
    setTransferFunctionTable(transferFunctionTable);
    identifyColorSpace();
    initialize();
}

//  from src/gui/painting/qcolorspace.cpp, line 177, as _ZN18QColorSpacePrivateC1ERKN11QColorSpace13PrimaryPointsENS0_16TransferFunctionEf
inline QColorSpacePrivate::QColorSpacePrivate(const QColorSpace::PrimaryPoints &primaries,
                                       QColorSpace::TransferFunction transferFunction,
                                       float gamma)
        : primaries(QColorSpace::Primaries::Custom)
        , transferFunction(transferFunction)
        , colorModel(QColorSpace::ColorModel::Rgb)
        , gamma(gamma)
        , whitePoint(QColorVector::fromXYChromaticity(primaries.whitePoint))
{
    Q_ASSERT(primaries.isValid());
    toXyz = qColorSpacePrimaryPointsToXyzMatrix(primaries);
    chad = QColorMatrix::chromaticAdaptation(whitePoint);
    toXyz = chad * toXyz;

    identifyColorSpace();
    setTransferFunction();
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

//  from src/gui/painting/qcolorspace.cpp, line 209, as _ZN18QColorSpacePrivateC1E7QPointFRK5QListItE
inline QColorSpacePrivate::QColorSpacePrivate(QPointF whitePoint, const QList<uint16_t> &transferFunctionTable)
      : primaries(QColorSpace::Primaries::Custom)
      , transferFunction(QColorSpace::TransferFunction::Custom)
      , colorModel(QColorSpace::ColorModel::Gray)
      , gamma(0)
      , whitePoint(QColorVector::fromXYChromaticity(whitePoint))
{
    chad = QColorMatrix::chromaticAdaptation(this->whitePoint);
    toXyz = chad;
    setTransferFunctionTable(transferFunctionTable);
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

//  from src/gui/painting/qcolorspace.cpp, line 348, as _ZN18QColorSpacePrivate10initializeEv
inline void QColorSpacePrivate::initialize()
{
    setToXyzMatrix();
    setTransferFunction();
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

//  from src/gui/painting/qcolorspace.cpp, line 368, as _ZN18QColorSpacePrivate24setTransferFunctionTableERK5QListItE
inline void QColorSpacePrivate::setTransferFunctionTable(const QList<uint16_t> &transferFunctionTable)
{
    QColorTransferTable table(transferFunctionTable.size(), transferFunctionTable);
    if (!table.isEmpty() && !table.checkValidity()) {
        qWarning() << "Invalid transfer function table given to QColorSpace";
        trc[0].m_type = QColorTrc::Type::Uninitialized;
        return;
    }
    transferFunction = QColorSpace::TransferFunction::Custom;
    QColorTransferFunction curve;
    if (table.asColorTransferFunction(&curve)) {
        // Table recognized as a specific curve
        if (curve.isIdentity()) {
            transferFunction = QColorSpace::TransferFunction::Linear;
            gamma = 1.0f;
        } else if (curve.isSRgb()) {
            transferFunction = QColorSpace::TransferFunction::SRgb;
        }
        trc[0].m_type = QColorTrc::Type::ParameterizedFunction;
        trc[0].m_fun = curve;
    } else {
        trc[0].m_type = QColorTrc::Type::Table;
        trc[0].m_table = table;
    }
}

//  from src/gui/painting/qcolorspace.cpp, line 394, as _ZN18QColorSpacePrivate25setTransferFunctionTablesERK5QListItES3_S3_
inline void QColorSpacePrivate::setTransferFunctionTables(const QList<uint16_t> &redTransferFunctionTable,
                                                   const QList<uint16_t> &greenTransferFunctionTable,
                                                   const QList<uint16_t> &blueTransferFunctionTable)
{
    QColorTransferTable redTable(redTransferFunctionTable.size(), redTransferFunctionTable);
    QColorTransferTable greenTable(greenTransferFunctionTable.size(), greenTransferFunctionTable);
    QColorTransferTable blueTable(blueTransferFunctionTable.size(), blueTransferFunctionTable);
    if (!redTable.isEmpty() && !greenTable.isEmpty() && !blueTable.isEmpty() &&
        !redTable.checkValidity() && !greenTable.checkValidity() && !blueTable.checkValidity()) {
        qWarning() << "Invalid transfer function table given to QColorSpace";
        trc[0].m_type = QColorTrc::Type::Uninitialized;
        trc[1].m_type = QColorTrc::Type::Uninitialized;
        trc[2].m_type = QColorTrc::Type::Uninitialized;
        return;
    }
    transferFunction = QColorSpace::TransferFunction::Custom;
    QColorTransferFunction curve;
    if (redTable.asColorTransferFunction(&curve)) {
        trc[0].m_type = QColorTrc::Type::ParameterizedFunction;
        trc[0].m_fun = curve;
    } else {
        trc[0].m_type = QColorTrc::Type::Table;
        trc[0].m_table = redTable;
    }
    if (greenTable.asColorTransferFunction(&curve)) {
        trc[1].m_type = QColorTrc::Type::ParameterizedFunction;
        trc[1].m_fun = curve;
    } else {
        trc[1].m_type = QColorTrc::Type::Table;
        trc[1].m_table = greenTable;
    }
    if (blueTable.asColorTransferFunction(&curve)) {
        trc[2].m_type = QColorTrc::Type::ParameterizedFunction;
        trc[2].m_fun = curve;
    } else {
        trc[2].m_type = QColorTrc::Type::Table;
        trc[2].m_table = blueTable;
    }
    lut.generated.storeRelease(0);
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

//  QColorSpacePrivate::QColorSpacePrivate(QColorSpace::NamedColorSpace
//      namedColorSpace)
extern "C" Q_DECL_EXPORT
QColorSpacePrivate *ritual_ZN18QColorSpacePrivateC1EN11QColorSpace15NamedColorSpaceE(
    QColorSpace::NamedColorSpace namedColorSpace) {
  return new QColorSpacePrivate(namedColorSpace);
}

//  QColorSpacePrivate::QColorSpacePrivate(QColorSpace::Primaries primaries,
//      QColorSpace::TransferFunction transferFunction, float gamma)
extern "C" Q_DECL_EXPORT
QColorSpacePrivate *ritual_ZN18QColorSpacePrivateC1EN11QColorSpace9PrimariesENS0_16TransferFunctionEf(
    QColorSpace::Primaries primaries,
    QColorSpace::TransferFunction transferFunction,
    float gamma) {
  return new QColorSpacePrivate(primaries, transferFunction, gamma);
}

//  QColorSpacePrivate::QColorSpacePrivate(QColorSpace::Primaries primaries,
//      const QList<uint16_t> &transferFunctionTable)
extern "C" Q_DECL_EXPORT
QColorSpacePrivate *ritual_ZN18QColorSpacePrivateC1EN11QColorSpace9PrimariesERK5QListItE(
    QColorSpace::Primaries primaries,
    const QList<uint16_t> *transferFunctionTable) {
  return new QColorSpacePrivate(primaries, *transferFunctionTable);
}

//  QColorSpacePrivate::QColorSpacePrivate(const QColorSpace::PrimaryPoints
//      &primaries, QColorSpace::TransferFunction transferFunction, float
//      gamma)
extern "C" Q_DECL_EXPORT
QColorSpacePrivate *ritual_ZN18QColorSpacePrivateC1ERKN11QColorSpace13PrimaryPointsENS0_16TransferFunctionEf(
    const QColorSpace::PrimaryPoints *primaries,
    QColorSpace::TransferFunction transferFunction,
    float gamma) {
  return new QColorSpacePrivate(*primaries, transferFunction, gamma);
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

//  QColorSpacePrivate::QColorSpacePrivate(QPointF whitePoint, const
//      QList<uint16_t> &transferFunctionTable)
extern "C" Q_DECL_EXPORT
QColorSpacePrivate *ritual_ZN18QColorSpacePrivateC1E7QPointFRK5QListItE(
    const QPointF *whitePoint,
    const QList<uint16_t> *transferFunctionTable) {
  return new QColorSpacePrivate(*whitePoint, *transferFunctionTable);
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

//  QColorSpacePrivate *QColorSpacePrivate::get(QColorSpace &colorSpace)
extern "C" Q_DECL_EXPORT
QColorSpacePrivate *ritual_ZN18QColorSpacePrivate3getER11QColorSpace(
    QColorSpace *colorSpace) {
  return QColorSpacePrivate::get(*colorSpace);
}

//  bool QColorSpacePrivate::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QColorSpacePrivate7isValidEv(
    const QColorSpacePrivate *self) {
  return self->isValid();
}

//  void QColorSpacePrivate::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QColorSpacePrivate10initializeEv(QColorSpacePrivate *self) {
  self->initialize();
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

//  void QColorSpacePrivate::setTransferFunctionTable(const QList<uint16_t>
//      &transferFunctionTable)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QColorSpacePrivate24setTransferFunctionTableERK5QListItE(
    QColorSpacePrivate *self,
    const QList<uint16_t> *transferFunctionTable) {
  self->setTransferFunctionTable(*transferFunctionTable);
}

//  void QColorSpacePrivate::setTransferFunctionTables(const QList<uint16_t>
//      &redTransferFunctionTable, const QList<uint16_t>
//      &greenTransferFunctionTable, const QList<uint16_t>
//      &blueTransferFunctionTable)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QColorSpacePrivate25setTransferFunctionTablesERK5QListItES3_S3_(
    QColorSpacePrivate *self,
    const QList<uint16_t> *redTransferFunctionTable,
    const QList<uint16_t> *greenTransferFunctionTable,
    const QList<uint16_t> *blueTransferFunctionTable) {
  self->setTransferFunctionTables(
      *redTransferFunctionTable,
      *greenTransferFunctionTable,
      *blueTransferFunctionTable);
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
