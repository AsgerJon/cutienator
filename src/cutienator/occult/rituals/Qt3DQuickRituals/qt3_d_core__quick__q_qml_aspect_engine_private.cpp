//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuick/6.12.0/Qt3DQuick/private/qqmlaspectengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquick_global_p.h>
#include <Qt3DQuick/Qt3DQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/qqmlaspectengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuick/private/qqmlaspectengine_p.h>
#include <Qt3DCore/qentity.h>
#include <QtCore/QDebug>
#include <QtQml/QQmlComponent>
#include <QtQml/QQmlContext>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/quick3d/quick3d/qqmlaspectengine.cpp, line 25, as _ZN8Qt3DCore5Quick23QQmlAspectEnginePrivateC1Ev
namespace Qt3DCore::Quick {
inline QQmlAspectEnginePrivate::QQmlAspectEnginePrivate()
    : QObjectPrivate()
    , m_qmlEngine(new QQmlEngine())
    , m_aspectEngine(new QAspectEngine())
    , m_component(nullptr)
{
}
}  // namespace Qt3DCore::Quick

//  from ../qt3d/src/quick3d/quick3d/qqmlaspectengine.cpp, line 135, as _ZN8Qt3DCore5Quick23QQmlAspectEnginePrivate18_q_continueExecuteEv
namespace Qt3DCore::Quick {
inline void QQmlAspectEnginePrivate::_q_continueExecute()
{
    Q_Q(QQmlAspectEngine);

    QObject::disconnect(m_component, SIGNAL(statusChanged(QQmlComponent::Status)),
                        q, SLOT(_q_continueExecute()));

    if (m_component->isError()) {
        const auto errors = m_component->errors();
        for (const QQmlError &error : errors) {
            QMessageLogger(error.url().toString().toLatin1().constData(), error.line(), 0).warning()
                << error;
        }
        emit q->statusChanged(q->status());
        return;
    }

    QObject* obj = m_component->create();

    if (m_component->isError()) {
        const auto errors = m_component->errors();
        for (const QQmlError &error : errors) {
            QMessageLogger(error.url().toString().toLatin1().constData(), error.line(), 0).warning()
                << error;
        }
        emit q->statusChanged(q->status());
        return;
    }

    // Let users know we have loaded the QML file, and the scene has been instantiated.
    // This gives a chance to manipulate the scene before passing it over to the
    // aspect engine. Useful for convenience window classes to set up cameras and surfaces
    // on the framegraph and event sources for the input aspect etc.
    emit q->sceneCreated(obj);
    m_aspectEngine->setRootEntity(QEntityPtr(qobject_cast<QEntity *>(obj)));
    emit q->statusChanged(q->status());
}
}  // namespace Qt3DCore::Quick
//  -----------------------------------------------------------------------

//  Qt3DCore::Quick::QQmlAspectEnginePrivate::QQmlAspectEnginePrivate()
extern "C" Q_DECL_EXPORT
Qt3DCore::Quick::QQmlAspectEnginePrivate *ritual_ZN8Qt3DCore5Quick23QQmlAspectEnginePrivateC1Ev() {
  return new Qt3DCore::Quick::QQmlAspectEnginePrivate();
}

//  QQmlAspectEngine *Qt3DCore::Quick::QQmlAspectEnginePrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::Quick::QQmlAspectEngine *ritual_ZN8Qt3DCore5Quick23QQmlAspectEnginePrivate6q_funcEv(
    Qt3DCore::Quick::QQmlAspectEnginePrivate *self) {
  return self->q_func();
}

//  const QQmlAspectEngine
//      *Qt3DCore::Quick::QQmlAspectEnginePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::Quick::QQmlAspectEngine *ritual_ZNK8Qt3DCore5Quick23QQmlAspectEnginePrivate6q_funcEv(
    const Qt3DCore::Quick::QQmlAspectEnginePrivate *self) {
  return self->q_func();
}

//  void Qt3DCore::Quick::QQmlAspectEnginePrivate::_q_continueExecute()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick23QQmlAspectEnginePrivate18_q_continueExecuteEv(
    Qt3DCore::Quick::QQmlAspectEnginePrivate *self) {
  self->_q_continueExecute();
}
