//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlvme_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlvme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqmlvme_p.h"
#include <private/qmetaobjectbuilder_p.h>
#include "qqmlengine.h"
#include <QtQml/private/qqmlcomponent_p.h>
#include <QStack>
#include <QPointF>
#include <QSizeF>
#include <QRectF>
#include <QtCore/qdebug.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qvarlengtharray.h>
#include <QtQml/qjsvalue.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlvme.cpp, line 41, as _ZN12QQmlVMEGuardC1Ev
inline QQmlVMEGuard::QQmlVMEGuard()
: m_objectCount(0), m_objects(nullptr), m_contextCount(0), m_contexts(nullptr)
{
}

//  from ../qtdeclarative/src/qml/qml/qqmlvme.cpp, line 46, as _ZN12QQmlVMEGuardD1Ev
inline QQmlVMEGuard::~QQmlVMEGuard()
{
    clear();
}

//  from ../qtdeclarative/src/qml/qml/qqmlvme.cpp, line 51, as _ZN12QQmlVMEGuard5guardEP17QQmlObjectCreator
inline void QQmlVMEGuard::guard(QQmlObjectCreator *creator)
{
    clear();

    std::vector<QQmlGuard<QObject>> &objects = creator->allCreatedObjects();
    m_objectCount = objects.size();
    m_objects = new QQmlGuard<QObject>[m_objectCount];
    for (size_t ii = 0; ii < m_objectCount; ++ii)
        m_objects[ii] = objects[ii];

    m_contextCount = 1;
    m_contexts = new QQmlGuardedContextData[m_contextCount];
    m_contexts[0] = creator->parentContextData();
}

//  from ../qtdeclarative/src/qml/qml/qqmlvme.cpp, line 66, as _ZN12QQmlVMEGuard5clearEv
inline void QQmlVMEGuard::clear()
{
    delete [] m_objects;
    delete [] m_contexts;

    m_objectCount = 0;
    m_objects = nullptr;
    m_contextCount = 0;
    m_contexts = nullptr;
}

//  from ../qtdeclarative/src/qml/qml/qqmlvme.cpp, line 77, as _ZNK12QQmlVMEGuard4isOKEv
inline bool QQmlVMEGuard::isOK() const
{
    for (size_t ii = 0; ii < m_objectCount; ++ii)
        if (m_objects[ii].isNull())
            return false;

    for (int ii = 0; ii < m_contextCount; ++ii)
        if (m_contexts[ii].isNull() || !m_contexts[ii]->engine())
            return false;

    return true;
}
//  -----------------------------------------------------------------------

//  QQmlVMEGuard::QQmlVMEGuard()
extern "C" Q_DECL_EXPORT
QQmlVMEGuard *ritual_ZN12QQmlVMEGuardC1Ev() {
  return new QQmlVMEGuard();
}

//  QQmlVMEGuard::~QQmlVMEGuard()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlVMEGuardD1Ev(QQmlVMEGuard *self) {
  delete self;
}

//  void QQmlVMEGuard::guard(QQmlObjectCreator *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlVMEGuard5guardEP17QQmlObjectCreator(
    QQmlVMEGuard *self,
    QQmlObjectCreator *a0) {
  self->guard(a0);
}

//  void QQmlVMEGuard::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlVMEGuard5clearEv(QQmlVMEGuard *self) {
  self->clear();
}

//  bool QQmlVMEGuard::isOK() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlVMEGuard4isOKEv(const QQmlVMEGuard *self) {
  return self->isOK();
}
