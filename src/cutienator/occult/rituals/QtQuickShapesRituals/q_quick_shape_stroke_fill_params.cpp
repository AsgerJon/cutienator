//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesglobal_p.h>
#include <QtQuickShapes/QtQuickShapes>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/private/qquickshape_p.h>
#include <QtQuickShapes/private/qquickshape_p_p.h>
#include <QtQuickShapes/private/qquickshapegenericrenderer_p.h>
#include <QtQuickShapes/private/qquickshapesoftwarerenderer_p.h>
#include <QtQuickShapes/private/qquickshapecurverenderer_p.h>
#include <private/qsgplaintexture_p.h>
#include <QtGui/private/qdrawhelper_p.h>
#include <QOpenGLFunctions>
#include <QtCore/QLoggingCategory>
#include <rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickshapes/qquickshape.cpp, line 84, as _ZN27QQuickShapeStrokeFillParamsC1Ev
inline QQuickShapeStrokeFillParams::QQuickShapeStrokeFillParams()
    : strokeColor(Qt::white),
      strokeWidth(1),
      fillColor(Qt::white),
      fillRule(QQuickShapePath::OddEvenFill),
      joinStyle(QQuickShapePath::BevelJoin),
      miterLimit(2),
      capStyle(QQuickShapePath::SquareCap),
      strokeStyle(QQuickShapePath::SolidLine),
      dashOffset(0),
      fillGradient(nullptr),
      strokeGradient(nullptr),
      fillItem(nullptr),
      trim(nullptr)
{
    dashPattern << 4 << 2; // 4 * strokeWidth dash followed by 2 * strokeWidth space
}
//  -----------------------------------------------------------------------

//  QQuickShapeStrokeFillParams::QQuickShapeStrokeFillParams()
extern "C" Q_DECL_EXPORT
QQuickShapeStrokeFillParams *ritual_ZN27QQuickShapeStrokeFillParamsC1Ev() {
  return new QQuickShapeStrokeFillParams();
}

//  QQuickShapeStrokeFillParams::~QQuickShapeStrokeFillParams()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickShapeStrokeFillParamsD1Ev(
    QQuickShapeStrokeFillParams *self) {
  delete self;
}
