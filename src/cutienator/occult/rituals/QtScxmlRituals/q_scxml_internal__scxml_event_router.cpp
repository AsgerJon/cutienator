//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/qscxmlevent.h>
#include <QtCore/qmetaobject.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/private/qscxmlstatemachine_p.h>
#include <QtScxml/private/qscxmlexecutablecontent_p.h>
#include <QtScxml/private/qscxmlevent_p.h>
#include <QtScxml/qscxmlinvokableservice.h>
#include <QtScxml/private/qscxmldatamodel_p.h>
#include <QtCore/qfile.h>
#include <QtCore/qhash.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qstring.h>
#include <QtCore/qtimer.h>
#include <QtCore/qthread.h>
#include <functional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtscxml/src/scxml/qscxmlstatemachine.cpp, line 253, as local:qscxmlstatemachine.cpp:nextSegment
namespace QScxmlInternal {
static QString nextSegment(const QStringList &segments)
{
    if (segments.isEmpty())
        return QString();

    const QString &segment = segments.first();
    return segment == QLatin1String("*") ? QString() : segment;
}
}  // namespace QScxmlInternal

//  from ../qtscxml/src/scxml/qscxmlstatemachine.cpp, line 270, as _ZN14QScxmlInternal16ScxmlEventRouter16disconnectNotifyERK11QMetaMethod
namespace QScxmlInternal {
inline void ScxmlEventRouter::disconnectNotify(const QMetaMethod &signal)
{
    Q_UNUSED(signal);

    // Defer the actual work, as this may be called from a destructor, or the signal may not
    // actually be disconnected, yet.
    QTimer::singleShot(0, this, [this] {
        if (!children.isEmpty() || receivers(SIGNAL(eventOccurred(QScxmlEvent))) > 0)
            return;

        ScxmlEventRouter *parentRouter = qobject_cast<ScxmlEventRouter *>(parent());
        if (!parentRouter) // root node
            return;

        QHash<QString, ScxmlEventRouter *>::Iterator it = parentRouter->children.begin(),
                end = parentRouter->children.end();
        for (; it != end; ++it) {
            if (it.value() == this) {
                parentRouter->children.erase(it);
                parentRouter->disconnectNotify(QMetaMethod());
                break;
            }
        }

        deleteLater(); // The parent might delete itself, triggering QObject delete cascades.
    });
}
}  // namespace QScxmlInternal
//  -----------------------------------------------------------------------

//  const QMetaObject *QScxmlInternal::ScxmlEventRouter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QScxmlInternal16ScxmlEventRouter10metaObjectEv(
    const QScxmlInternal::ScxmlEventRouter *self) {
  return self->metaObject();
}

//  void *QScxmlInternal::ScxmlEventRouter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QScxmlInternal16ScxmlEventRouter11qt_metacastEPKc(
    QScxmlInternal::ScxmlEventRouter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QScxmlInternal::ScxmlEventRouter::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QScxmlInternal16ScxmlEventRouter11qt_metacallEN11QMetaObject4CallEiPPv(
    QScxmlInternal::ScxmlEventRouter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QScxmlInternal::ScxmlEventRouter::eventOccurred(const QScxmlEvent
//      &event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScxmlInternal16ScxmlEventRouter13eventOccurredERK11QScxmlEvent(
    QScxmlInternal::ScxmlEventRouter *self,
    const QScxmlEvent *event) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QScxmlInternal::ScxmlEventRouter")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "eventOccurred(const QScxmlEvent &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "eventOccurred(const QScxmlEvent &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(event)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QScxmlInternal::ScxmlEventRouter::disconnectNotify(const QMetaMethod
//      &signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScxmlInternal16ScxmlEventRouter16disconnectNotifyERK11QMetaMethod(
    QScxmlInternal::ScxmlEventRouter *self,
    const QMetaMethod *signal) {
  self->disconnectNotify(*signal);
}
