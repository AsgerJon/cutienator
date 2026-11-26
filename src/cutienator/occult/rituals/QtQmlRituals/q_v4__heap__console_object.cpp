//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlbuiltinfunctions_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlbuiltinfunctions_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlbuiltinfunctions_p.h>
#include <QtQml/private/qqmlcomponent_p.h>
#include <QtQml/private/qqmldebugconnector_p.h>
#include <QtQml/private/qqmldebugserviceinterfaces_p.h>
#include <QtQml/private/qqmldelayedcallqueue_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlloggingcategorybase_p.h>
#include <QtQml/private/qqmlplatform_p.h>
#include <QtQml/private/qqmlstringconverters_p.h>
#include <QtQml/private/qv4dateobject_p.h>
#include <QtQml/private/qv4domerrors_p.h>
#include <QtQml/private/qv4engine_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4include_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qv4sequenceobject_p.h>
#include <QtQml/private/qv4stackframe_p.h>
#include <QtQml/qqmlfile.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qcryptographichash.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qvarlengtharray.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlbuiltinfunctions.cpp, line 2037, as local:qqmlbuiltinfunctions.cpp:Log
enum ConsoleLogTypes {
    Log,
    Info,
    Warn,
    Error
};

//  from ../qtdeclarative/src/qml/qml/qqmlbuiltinfunctions.cpp, line 2233, as _ZN3QV413ConsoleObject11method_timeEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue ConsoleObject::method_time(const FunctionObject *b, const Value *, const Value *argv, int argc)
{
    QV4::Scope scope(b);
    if (argc != 1)
        THROW_GENERIC_ERROR("console.time(): Invalid arguments");

    QString name = argv[0].toQStringNoThrow();
    scope.engine->startTimer(name);
    return QV4::Encode::undefined();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/qml/qqmlbuiltinfunctions.cpp, line 2259, as _ZN3QV413ConsoleObject12method_countEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue ConsoleObject::method_count(const FunctionObject *b, const Value *, const Value *argv, int argc)
{
    // first argument: name to print. Ignore any additional arguments
    QString name;
    if (argc > 0)
        name = argv[0].toQStringNoThrow();

    Scope scope(b);
    QV4::ExecutionEngine *v4 = scope.engine;

    QV4::CppStackFrame *frame = v4->currentStackFrame;

    QString scriptName = frame->source();

    int value = v4->consoleCountHelper(scriptName, frame->lineNumber(), 0);
    QString message = name + QLatin1String(": ") + QString::number(value);

    QMessageLogger(qPrintable(scriptName), frame->lineNumber(),
                   qPrintable(frame->function()))
        .debug("%s", qPrintable(message));

    return QV4::Encode::undefined();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/qml/qqmlbuiltinfunctions.cpp, line 2192, as _ZN3QV413ConsoleObject14method_profileEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue ConsoleObject::method_profile(const FunctionObject *b, const Value *, const Value *, int)
{
    QV4::Scope scope(b);
    QV4::ExecutionEngine *v4 = scope.engine;

    QV4::CppStackFrame *frame = v4->currentStackFrame;
    const QByteArray baSource = frame->source().toUtf8();
    const QByteArray baFunction = frame->function().toUtf8();
    QMessageLogger logger(baSource.constData(), frame->lineNumber(), baFunction.constData());
    QQmlProfilerService *service = QQmlDebugConnector::service<QQmlProfilerService>();
    if (!service) {
        logger.warning("Cannot start profiling because debug service is disabled. Start with -qmljsdebugger=port:XXXXX.");
    } else {
        service->startProfiling(v4->jsEngine());
        logger.debug("Profiling started.");
    }

    return QV4::Encode::undefined();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/qml/qqmlbuiltinfunctions.cpp, line 2244, as _ZN3QV413ConsoleObject14method_timeEndEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue ConsoleObject::method_timeEnd(const FunctionObject *b, const Value *, const Value *argv, int argc)
{
    QV4::Scope scope(b);
    if (argc != 1)
        THROW_GENERIC_ERROR("console.timeEnd(): Invalid arguments");

    QString name = argv[0].toQStringNoThrow();
    bool wasRunning;
    qint64 elapsed = scope.engine->stopTimer(name, &wasRunning);
    if (wasRunning) {
        qDebug("%s: %llims", qPrintable(name), elapsed);
    }
    return QV4::Encode::undefined();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/qml/qqmlbuiltinfunctions.cpp, line 2212, as _ZN3QV413ConsoleObject17method_profileEndEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue ConsoleObject::method_profileEnd(const FunctionObject *b, const Value *, const Value *, int)
{
    QV4::Scope scope(b);
    QV4::ExecutionEngine *v4 = scope.engine;

    QV4::CppStackFrame *frame = v4->currentStackFrame;
    const QByteArray baSource = frame->source().toUtf8();
    const QByteArray baFunction = frame->function().toUtf8();
    QMessageLogger logger(baSource.constData(), frame->lineNumber(), baFunction.constData());

    QQmlProfilerService *service = QQmlDebugConnector::service<QQmlProfilerService>();
    if (!service) {
        logger.warning("Ignoring console.profileEnd(): the debug service is disabled.");
    } else {
        service->stopProfiling(v4->jsEngine());
        logger.debug("Profiling ended.");
    }

    return QV4::Encode::undefined();
}
}  // namespace QV4
//  -----------------------------------------------------------------------
