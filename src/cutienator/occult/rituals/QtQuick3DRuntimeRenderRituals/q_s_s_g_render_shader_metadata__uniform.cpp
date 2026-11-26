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

//  from ../qtquick3d/src/runtimerender/qssgrendershadermetadata.cpp, line 36, as _ZN24QSSGRenderShaderMetadata7Uniform19conditionFromStringERK7QString
namespace QSSGRenderShaderMetadata {
inline Uniform::Condition Uniform::conditionFromString(const QString &condition)
{
    if (condition.isEmpty())
        return Uniform::Condition::None;

    if (condition.at(0) == QChar::fromLatin1('!'))
        return Uniform::Negated;

    return Uniform::Regular;
}
}  // namespace QSSGRenderShaderMetadata
//  -----------------------------------------------------------------------

//  Condition QSSGRenderShaderMetadata::Uniform::conditionFromString(const
//      QString &condition)
extern "C" Q_DECL_EXPORT
QSSGRenderShaderMetadata::Uniform::Condition ritual_ZN24QSSGRenderShaderMetadata7Uniform19conditionFromStringERK7QString(
    const QString *condition) {
  return QSSGRenderShaderMetadata::Uniform::conditionFromString(*condition);
}

//  QSSGRenderShaderMetadata::Uniform::~Uniform()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGRenderShaderMetadata7UniformD1Ev(
    QSSGRenderShaderMetadata::Uniform *self) {
  delete self;
}
