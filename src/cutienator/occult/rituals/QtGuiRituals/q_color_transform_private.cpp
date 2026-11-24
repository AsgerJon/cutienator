//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcolortransform_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcolortransform_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolortransform.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/painting/qcolorspace.cpp, line 514, as _ZNK18QColorSpacePrivate22isThreeComponentMatrixEv
inline bool QColorSpacePrivate::isThreeComponentMatrix() const
{
    return transformModel == QColorSpace::TransformModel::ThreeComponentMatrix;
}

//  from src/gui/painting/qcolortransform.cpp, line 1950, as _ZNK22QColorTransformPrivate8pcsAdaptEP12QColorVectorx
inline void QColorTransformPrivate::pcsAdapt(QColorVector *buffer, qsizetype count) const
{
    // Match Profile Connection Spaces (PCS):
    if (colorSpaceOut->isPcsLab && !colorSpaceIn->isPcsLab) {
        for (qsizetype j = 0; j < count; ++j)
            buffer[j] = buffer[j].xyzToLab();
    } else if (colorSpaceIn->isPcsLab && !colorSpaceOut->isPcsLab) {
        for (qsizetype j = 0; j < count; ++j)
            buffer[j] = buffer[j].labToXyz();
    }
}
//  -----------------------------------------------------------------------

//  QColorTransformPrivate *QColorTransformPrivate::get(const QColorTransform
//      &q)
extern "C" Q_DECL_EXPORT
QColorTransformPrivate *ritual_ZN22QColorTransformPrivate3getERK15QColorTransform(
    const QColorTransform *q) {
  return QColorTransformPrivate::get(*q);
}

//  void QColorTransformPrivate::prepare()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QColorTransformPrivate7prepareEv(
    QColorTransformPrivate *self) {
  self->prepare();
}

//  void QColorTransformPrivate::pcsAdapt(QColorVector *buffer, qsizetype
//      len) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK22QColorTransformPrivate8pcsAdaptEP12QColorVectorx(
    const QColorTransformPrivate *self,
    QColorVector *buffer,
    qsizetype len) {
  self->pcsAdapt(buffer, len);
}

//  QColorTransformPrivate::~QColorTransformPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QColorTransformPrivateD1Ev(QColorTransformPrivate *self) {
  delete self;
}
