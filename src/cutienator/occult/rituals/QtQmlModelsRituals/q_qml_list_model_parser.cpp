//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_list_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqmllistmodel_p_p.h"
#include "qqmllistmodelworkeragent_p.h"
#include <private/qjsvalue_p.h>
#include <private/qqmlcustomparser_p.h>
#include <private/qqmlengine_p.h>
#include <private/qqmljsast_p.h>
#include <private/qqmljsengine_p.h>
#include <private/qqmllistwrapper_p.h>
#include <private/qqmlnotifier_p.h>
#include <private/qqmlopenmetaobject_p.h>
#include <private/qv4alloca_p.h>
#include <private/qv4dateobject_p.h>
#include <private/qv4lookup_p.h>
#include <private/qv4object_p.h>
#include <private/qv4objectiterator_p.h>
#include <private/qv4qmlcontext_p.h>
#include <private/qv4sequenceobject_p.h>
#include <private/qv4urlobject_p.h>
#include <qqmlcontext.h>
#include <qqmlinfo.h>
#include <QtCore/qdebug.h>
#include <QtCore/qstack.h>
#include <QXmlStreamReader>
#include <QtCore/qdatetime.h>
#include <QScopedValueRollback>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 3029, as _ZN19QQmlListModelParser16definesEmptyListE11QStringView
inline bool QQmlListModelParser::definesEmptyList(QStringView s)
{
    if (s.startsWith(QLatin1Char('[')) && s.endsWith(QLatin1Char(']'))) {
        for (auto c : s.sliced(1).chopped(1)) {
            if (!c.isSpace())
                return false;
        }
        return true;
    }
    return false;
}
//  -----------------------------------------------------------------------

//  bool QQmlListModelParser::definesEmptyList(QStringView s)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlListModelParser16definesEmptyListE11QStringView(
    const QString *s) {
  return QQmlListModelParser::definesEmptyList(QStringView(*s));
}

//  QQmlListModelParser::~QQmlListModelParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlListModelParserD1Ev(QQmlListModelParser *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_list_model)
