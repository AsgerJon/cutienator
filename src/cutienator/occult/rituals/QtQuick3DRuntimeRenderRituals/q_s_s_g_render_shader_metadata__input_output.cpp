//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadermetadata_p
//  .h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadermetadata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/private/qssgrendershadermetadata_p.h>
#include <QtCore/QPair>
#include <QtCore/QJsonDocument>
#include <QtCore/QJsonArray>
#include <QtCore/QJsonObject>
#include <QtCore/QJsonValue>
#include <QtCore/QtDebug>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/runtimerender/qssgrendershadermetadata.cpp, line 47, as _ZN24QSSGRenderShaderMetadata11InputOutput15stageFromStringERK7QString
namespace QSSGRenderShaderMetadata {
inline QSSGShaderGeneratorStage InputOutput::stageFromString(const QString &stage)
{
    if (stage == QLatin1String("vertex")) {
        return QSSGShaderGeneratorStage::Vertex;
    } else if (stage == QLatin1String("fragment"))
        return QSSGShaderGeneratorStage::Fragment;
    else {
        qWarning("Unknown stage in shader metadata: %s, assuming vertex", qPrintable(stage));
        return QSSGShaderGeneratorStage::Vertex;
    }
}
}  // namespace QSSGRenderShaderMetadata
//  -----------------------------------------------------------------------

//  QSSGShaderGeneratorStage
//      QSSGRenderShaderMetadata::InputOutput::stageFromString(const QString
//      &stage)
extern "C" Q_DECL_EXPORT
QSSGShaderGeneratorStage ritual_ZN24QSSGRenderShaderMetadata11InputOutput15stageFromStringERK7QString(
    const QString *stage) {
  return QSSGRenderShaderMetadata::InputOutput::stageFromString(*stage);
}

//  QSSGRenderShaderMetadata::InputOutput::~InputOutput()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGRenderShaderMetadata11InputOutputD1Ev(
    QSSGRenderShaderMetadata::InputOutput *self) {
  delete self;
}
