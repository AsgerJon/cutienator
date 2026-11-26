//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljavascriptexpression_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljavascriptexpression_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qqmlerror.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlglobal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmljavascriptexpression_p.h>
#include <QtQml/private/qqmljavascriptexpression_p.h>
#include <QtQml/private/qqmlexpression_p.h>
#include <QtQml/private/qv4context_p.h>
#include <QtQml/private/qv4value_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4script_p.h>
#include <QtQml/private/qv4errorobject_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qqmlbuiltinfunctions_p.h>
#include <QtQml/private/qqmlsourcecoordinate_p.h>
#include <QtQml/private/qqmlabstractbinding_p.h>
#include <QtQml/private/qqmlpropertybinding_p.h>
#include <QtCore/private/qproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmljavascriptexpression.cpp, line 26, as _ZN16QQmlDelayedError8addErrorEP17QQmlEnginePrivate
inline bool QQmlDelayedError::addError(QQmlEnginePrivate *e)
{
    if (!e) return false;

    if (e->inProgressCreations == 0) return false; // Not in construction

    if (prevError) return true; // Already in error chain

    prevError = &e->erroredBindings;
    nextError = e->erroredBindings;
    e->erroredBindings = this;
    if (nextError) nextError->prevError = &nextError;

    return true;
}

//  from ../qtdeclarative/src/qml/qml/qqmljavascriptexpression.cpp, line 42, as _ZN16QQmlDelayedError16setErrorLocationERK18QQmlSourceLocation
inline void QQmlDelayedError::setErrorLocation(const QQmlSourceLocation &sourceLocation)
{
    m_error.setUrl(QUrl(sourceLocation.sourceFile));
    m_error.setLine(qmlConvertSourceCoordinate<quint16, int>(sourceLocation.line));
    m_error.setColumn(qmlConvertSourceCoordinate<quint16, int>(sourceLocation.column));
}

//  from ../qtdeclarative/src/qml/qml/qqmljavascriptexpression.cpp, line 49, as _ZN16QQmlDelayedError19setErrorDescriptionERK7QString
inline void QQmlDelayedError::setErrorDescription(const QString &description)
{
    m_error.setDescription(description);
}

//  from ../qtdeclarative/src/qml/qml/qqmljavascriptexpression.cpp, line 54, as _ZN16QQmlDelayedError14setErrorObjectEP7QObject
inline void QQmlDelayedError::setErrorObject(QObject *object)
{
    m_error.setObject(object);
}

//  from ../qtdeclarative/src/qml/qml/qqmljavascriptexpression.cpp, line 59, as _ZN16QQmlDelayedError24catchJavaScriptExceptionEPN3QV415ExecutionEngineE
inline void QQmlDelayedError::catchJavaScriptException(QV4::ExecutionEngine *engine)
{
    m_error = engine->catchExceptionAsQmlError();
}
//  -----------------------------------------------------------------------

//  QQmlDelayedError::QQmlDelayedError()
extern "C" Q_DECL_EXPORT
QQmlDelayedError *ritual_ZN16QQmlDelayedErrorC1Ev() {
  return new QQmlDelayedError();
}

//  QQmlDelayedError::~QQmlDelayedError()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlDelayedErrorD1Ev(QQmlDelayedError *self) {
  delete self;
}

//  bool QQmlDelayedError::addError(QQmlEnginePrivate *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQmlDelayedError8addErrorEP17QQmlEnginePrivate(
    QQmlDelayedError *self,
    QQmlEnginePrivate *a0) {
  return self->addError(a0);
}

//  QQmlError QQmlDelayedError::removeError()
extern "C" Q_DECL_EXPORT
QQmlError *ritual_ZN16QQmlDelayedError11removeErrorEv(
    QQmlDelayedError *self) {
  return new QQmlError(self->removeError());
}

//  bool QQmlDelayedError::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlDelayedError7isValidEv(const QQmlDelayedError *self) {
  return self->isValid();
}

//  const QQmlError &QQmlDelayedError::error() const
extern "C" Q_DECL_EXPORT
QQmlError *ritual_ZNK16QQmlDelayedError5errorEv(
    const QQmlDelayedError *self) {
  return new QQmlError(self->error());
}

//  void QQmlDelayedError::clearError()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlDelayedError10clearErrorEv(QQmlDelayedError *self) {
  self->clearError();
}

//  void QQmlDelayedError::setErrorLocation(const QQmlSourceLocation
//      &sourceLocation)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlDelayedError16setErrorLocationERK18QQmlSourceLocation(
    QQmlDelayedError *self,
    const QQmlSourceLocation *sourceLocation) {
  self->setErrorLocation(*sourceLocation);
}

//  void QQmlDelayedError::setErrorDescription(const QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlDelayedError19setErrorDescriptionERK7QString(
    QQmlDelayedError *self,
    const QString *description) {
  self->setErrorDescription(*description);
}

//  void QQmlDelayedError::setErrorObject(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlDelayedError14setErrorObjectEP7QObject(
    QQmlDelayedError *self,
    QObject *object) {
  self->setErrorObject(object);
}

//  void QQmlDelayedError::catchJavaScriptException(QV4::ExecutionEngine
//      *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlDelayedError24catchJavaScriptExceptionEPN3QV415ExecutionEngineE(
    QQmlDelayedError *self,
    QV4::ExecutionEngine *engine) {
  self->catchJavaScriptException(engine);
}
